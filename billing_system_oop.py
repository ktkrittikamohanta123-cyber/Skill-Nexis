# Mini Project (W3): Billing System using OOP
# Product class stores product details.
# Bill class calculates subtotal, tax, and final amount.
# The final bill is displayed in a tabular format.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=5):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        if not self.products:
            print("\nNo products added. Bill cannot be generated.")
            return

        print("\n" + "=" * 72)
        print("                         CUSTOMER BILL")
        print("=" * 72)
        print(f"{'Product':<22}{'Price (Rs.)':>14}{'Quantity':>12}{'Amount (Rs.)':>18}")
        print("-" * 72)

        for product in self.products:
            print(
                f"{product.name:<22}"
                f"{product.price:>14.2f}"
                f"{product.quantity:>12}"
                f"{product.get_total():>18.2f}"
            )

        print("-" * 72)
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal:':>48} Rs. {subtotal:>12.2f}")
        print(f"{f'Tax ({self.tax_rate}%):':>48} Rs. {tax:>12.2f}")
        print("=" * 72)
        print(f"{'FINAL AMOUNT:':>48} Rs. {total:>12.2f}")
        print("=" * 72)
        print("                 Thank you for shopping!")


# Main program
bill = Bill(tax_rate=5)  # Tax rate is 5%; change it if required.

print("===== BILLING SYSTEM =====")

while True:
    try:
        count = int(input("How many different products do you want to add? "))
        if count <= 0:
            print("Please enter at least one product.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

for i in range(count):
    print(f"\nEnter details for product {i + 1}:")

    while True:
        name = input("Product name: ").strip()
        if name:
            break
        print("Product name cannot be empty.")

    while True:
        try:
            price = float(input("Price per item (Rs.): "))
            if price < 0:
                print("Price cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()
