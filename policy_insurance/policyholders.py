
class PolicyHolder():
    def __init__(self, policy_holder_id, name, email):  # constructor
        self.active = True
        self.name = name
        self.email = email
        self.products = []
        self.payments = []
        self.policy_holder_id = policy_holder_id

    def register_policy_holder(self):  # register a new policyholder
        print(f"Policyholder {self.name} is registered successfully.")

    def suspend_policy_holder(self):  # suspend a policyholder
        if not self.active:
            print(f"Policyholder {self.name} is already suspended.")
            return
        self.active = False
        print(f"Policyholder {self.name} is suspended.")

    def reactivate_policy_holder(self):  # reactivate a policyholder
        if not self.active:
            print(f"Policyholder {self.name} is reactivated successfully.")
            self.active = True
        print(f"Policyholder {self.name} is already active.")

    def register_product(self, product):
        self.products.append(product)

    def make_payment(self, payment):
        self.payments.append(payment)
