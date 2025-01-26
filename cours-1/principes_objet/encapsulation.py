class BankAccount:
    def __init__(self, owner, balance, credit_limit):
        self.owner = owner
        self.__balance = balance  # Attribut privé
        self.__credit_limit = credit_limit  # Attribut privé

    # Getter pour accéder au solde
    def get_balance(self):
        return self.__balance

    # Méthode pour savoir si l'utilisateur peut payer une certaine somme
    def can_pay(self, amount):
        return amount <= self.__balance + self.__credit_limit

    # Dépôt d'argent
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Le montant doit être positif.")

    # Retrait d'argent (avec vérification de la possibilité de paiement)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        elif amount <= self.__balance + self.__credit_limit:
            # Utilisation du crédit autorisé si le solde est insuffisant
            self.__credit_limit -= (amount - self.__balance)
            self.__balance = 0
        else:
            raise ValueError("Solde insuffisant et limite de crédit atteinte.")

# Utilisation
account = BankAccount("Alice", 1000, 500)  # Alice a un solde de 1000 et une limite de crédit de 500

# Vérifier si Alice peut payer
print(account.can_pay(1200))  # True, car 1000 (solde) + 500 (crédit) = 1500, suffisant pour 1200
print(account.can_pay(1700))  # False, car 1000 + 500 = 1500, insuffisant pour 1700

# Retrait
account.withdraw(1200)  # Utilisation du crédit de 200, il reste 100 dans le solde
print(account.can_pay(100))  # True, car 0 (solde) + 500 (crédit) suffisant pour 100
`