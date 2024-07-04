# Invoice Generator

This project is an invoice generator that uses Playwright to generate a PDF from an HTML template. The HTML template receives configuration data through JavaScript and updates the invoice content dynamically. The Playwright script injects this data into the HTML template and waits for a console log indicating that the invoice is ready before generating the PDF.

## Prerequisites

- Python 3.7 or higher
- Playwright

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install Playwright browsers (chromium, firefox, etc..):
    ```bash
    playwright install chromium
    ```

## Usage

1. Ensure the `invoice.html` file is in the templates directory alongside `generate_invoice.py`.

2. Run the Python script to generate the invoice PDF:
    ```bash
    python3 generate_invoice.py
    ```

## Project Structure

- `invoice.html`: The HTML template for the invoice.
- `generate_invoice.py`: The Python script that injects data into the HTML template and generates the PDF.
- `requirements.txt`: The file containing the list of required Python packages.

## HTML Template

The HTML template uses JavaScript to receive configuration data and update the invoice content dynamically. It listens for a message event and updates the DOM accordingly.

## Python Script

The Python script uses Playwright to:
- Launch a browser and open the HTML template.
- Inject the invoice data into the HTML template.
- Wait for a console log indicating that the invoice is ready.
- Generate the PDF and save it to the specified path.

## Console Output

The script listens to console messages from the HTML page to determine when the invoice is ready to be printed as a PDF.

## Example

### Sample Data

The sample data used in the script (`generate_invoice.py`):
```python
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
