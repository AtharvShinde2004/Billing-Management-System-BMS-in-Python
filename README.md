# Python Billing Management System

This is a simple Billing Management System (BMS) implemented in Python. The system consists of classes representing customers, products, invoice items, and invoices. It provides basic functionalities for creating customers, adding products to invoices, calculating totals, and generating detailed invoices.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with the Billing Management System, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

## Usage

The core classes in the system include:

`Customer:` Represents a customer with attributes like name, address, and email.
`Product:` Represents a product with attributes like name and price.
`InvoiceItem:` Represents an item in the invoice, associating a product with a quantity.
`Invoice:` Represents an invoice for a specific customer, with a list of invoice items.
To use the system, create instances of these classes and interact with them as demonstrated in the example below.

## Example
```python 
from billing_system import Customer, Product, Invoice

# Create a customer
customer = Customer("John Doe", "123 Main St, City, Country", "john.doe@example.com")

# Create products
product1 = Product("Product A", 10.99)
product2 = Product("Product B", 5.99)

# Create an invoice for the customer
invoice = Invoice(customer)

# Add items to the invoice
invoice.add_item(product1, 3)
invoice.add_item(product2, 2)

# Generate and print the invoice
invoice.generate_invoice()
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License.
