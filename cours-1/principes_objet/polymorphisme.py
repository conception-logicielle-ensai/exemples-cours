class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of {amount} made using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of {amount} made using PayPal.")

class Bitcoin(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of {amount} made using Bitcoin.")

# Polymorphisme : utilisation de différentes méthodes de paiement
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Utilisation
credit_card = CreditCard()
paypal = PayPal()
bitcoin = Bitcoin()

process_payment(credit_card, 100)  # Payment of 100 made using Credit Card.
process_payment(paypal, 200)       # Payment of 200 made using PayPal.
process_payment(bitcoin, 300)      # Payment of 300 made using Bitcoin.
