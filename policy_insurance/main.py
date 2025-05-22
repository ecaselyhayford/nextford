from policyholders import PolicyHolder
from products import Products
from payments import Payments


# Create products
product1 = Products("LI-101", "Life Insurance", 100)
product1.create_product()

product2 = Products("MO-101", "Motor Insurance", 200)
product2.create_product()

# Create and initialize policyholders
policyHolder1 = PolicyHolder(
    1, "Esther Casely Hayford", "ecaselyhayford@test.com")
policyHolder1.register_policy_holder()

policyHolder2 = PolicyHolder(2, "Judith Ketsi ", "judykay@test.com")
policyHolder2.register_policy_holder()

policyHolder3 = PolicyHolder(3, "Kofi Sampson ", "kofi@test.com")
policyHolder3.register_policy_holder()


# Register products to policyholders
policyHolder1.register_product(product1)
policyHolder2.register_product(product1)
policyHolder3.register_product(product2)

# Create and make payments
payment1 = Payments(100, product1)
payment1.process_payment()

payment2 = Payments(100, product1)
payment2.process_payment()

payment3 = Payments(200, product2)
payment3.process_payment()

policyHolder1.make_payment(payment1)
policyHolder2.make_payment(payment1)
policyHolder3.make_payment(payment3)


def display_policy_holder_details(polcyholders):
    for policyholder in polcyholders:
        print("*" * 50)
        print(f"Policyholder ID: {policyholder.policy_holder_id}")
        print(f"Name of Policyholder: {policyholder.name}")
        print(f"Email Address: {policyholder.email}")
        print(f"Status: {'Active' if policyholder.active else 'Suspended'}")
        if not policyholder.products:
            print("Insurance Product: None")
        else:
            print("Insurance Products:")
            for product in policyholder.products:
                print(f"- {product.name}({product.product_id}) ${product.price}")

        print("Payments:")
        if not policyholder.payments:
            print("No payments made yet.")
        else:

            for payment in policyholder.payments:
                print(
                    f"Payment of ${payment.amount} has been received for {payment.product.name} {payment.date.strftime('%Y-%m-%d')}"
                )


# Display policyholder details
display_policy_holder_details([policyHolder1, policyHolder2, policyHolder3])
