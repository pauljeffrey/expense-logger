# Expense/Receipts Logger

Expense/Receipts Logger is a simple web application built with Python and FastAPI. It exposes an endpoint for webhooks and receives emails, then appropriately logs them into a local storage. This project is designed to help individuals or teams easily keep track of their expenses and receipts by storing email receipts in a centralized location.

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
   - [Configuring Webhooks](#configuring-webhooks)
   - [Receiving and Logging Emails](#receiving-and-logging-emails)
4. [Roadmap](#roadmap)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- Expose an endpoint for webhook integration with email services.
- Receive emails sent to the webhook endpoint and extract relevant data from them.
- Log the extracted data, including expenses and receipts, into a local storage system.
- Provides a simple and convenient way to organize and manage expenses and receipts.
- Easily configurable to work with various email providers and storage solutions.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- A working email account (e.g., Gmail) for testing the webhook.

### Installation

Follow these steps to set up the Expense/Receipts Logger:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/daveokpare/expenses-logger.git
   ```
   
2. Change to the project directory:
   
   ```bash
   cd expenses-logger
   ```

3. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuring Webhooks

To configure the webhook for your email provider, follow these general steps:

1. Create a webhook endpoint on your server using FastAPI or use a service like ngrok to expose a local endpoint.
2. Configure your email provider or Zapier to send webhook notifications to the endpoint you created in step 1. You will typically need to provide the endpoint URL, HTTP method (e.g., POST), and any required authentication.
3. Update the application settings or configuration to use the same endpoint URL and authentication details.

### Receiving and Logging Emails

Once your webhook is configured, the Expense/Receipts Logger will receive emails and log them into local storage. Here's how to use it:

1. Start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```
2. Emails sent to the webhook endpoint will be processed and logged.
3. Access the logged expenses and receipts via the local storage system. You can implement additional features to search, categorize, or export this data as needed

## Roadmap

- [ ] Visualization using Streamlit

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or new features to propose, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

