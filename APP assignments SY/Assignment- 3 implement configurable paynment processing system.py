class CreditCard:
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class PayPal:
    def pay(self, amount):
        print("Paid ₹", amount, "using PayPal")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)

    def change_method(self, payment_method):
        self.payment_method = payment_method


# Using UPI
processor = PaymentProcessor(UPI())
processor.process_payment(1000)

# Changing to Credit Card
processor.change_method(CreditCard())
processor.process_payment(2000)

# Changing to PayPal
processor.change_method(PayPal())
processor.process_payment(1500)