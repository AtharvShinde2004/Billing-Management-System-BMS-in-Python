class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Invoice:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(InvoiceItem(product, quantity))

    def calculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.items)
        return total

    def generate_invoice(self):
        print("Invoice for:", self.customer.name)
        print("Address:", self.customer.address)
        print("Email:", self.customer.email)
        print("\nInvoice Items:")
        for item in self.items:
            print(f"{item.product.name} - Quantity: {item.quantity} - Price: ${item.product.price}")
        total = self.calculate_total()
        print(f"Total: ${total}")

def main():
    customer = Customer("John Doe", "123 Main St, City, Country", "john.doe@example.com")

    product1 = Product("Product A", 10.99)
    product2 = Product("Product B", 5.99)

    invoice = Invoice(customer)

    invoice.add_item(product1, 3)
    invoice.add_item(product2, 2)

    invoice.generate_invoice()

if __name__ == "__main__":
    main()
