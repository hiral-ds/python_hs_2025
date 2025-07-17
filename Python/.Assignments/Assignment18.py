#abstraction

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

credit = CreditCard()
upi = UPI()

credit.pay(1500)
upi.pay(750)