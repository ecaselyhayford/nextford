from datetime import datetime


class Payments:
    def __init__(self, amount=0, product=None):  # constructor
        self.amount = amount
        self.date = datetime.now()
        self.product = product

    def process_payment(self):  # process the payment
        print(f"Processing payment of ${self.amount} for {self.product.name}")

    def payment_reminder(self):  # remind the payment
        print("Reminder: Your payment is due.")

    def payment_penalty(self):  # apply penalty for late payment

        print(f"Applying penalty on payment of {self.amount}")
