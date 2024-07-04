import os

from playwright.sync_api import sync_playwright

INVOICE_TEMPLATE_PATH = "templates/invoice.html"

# Sample data to fill the template
invoice_data = {
    "invoice_number": "12345",
    "date": "2024-07-04",
    "client_name": "Sheldon Cooper",
    "client_address": "7 Elm Street, Any town, USA",
    "items": [
        {"description": "Apples", "quantity": 2, "price": "$10.00", "total": "$20.00"},
        {"description": "Mangoes", "quantity": 1, "price": "$15.00", "total": "$15.00"},
    ],
    "total": "$35.00"
}


def generate_pdf(pdf_path: str,
                 /) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Listen to console messages
        page.on("console", lambda msg: msg.text)

        # Navigate to the local HTML file
        page.goto(f'file://{os.path.abspath(INVOICE_TEMPLATE_PATH)}')

        # Inject script to send the invoice data to the page
        page.evaluate(f"""
            window.postMessage({{
                'type': 'generate_invoice',
                'config': {invoice_data}
            }}, '*');
        """)

        # Wait for the specific console message
        try:
            with page.expect_console_message(lambda msg: "invoice ready" in msg.text, timeout=10000):
                print("Waiting for the invoice to be ready...")

            # After the console message, generate the PDF
            print("Invoice is ready, generating PDF...")
            page.pdf(path=pdf_path)
            print(f"Invoice generated and saved as {pdf_path}")

        except TimeoutError:
            print("Unable to generate report within timeout")
        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            browser.close()


if __name__ == "__main__":
    output_pdf_path = "invoice.pdf"
    generate_pdf(output_pdf_path)
