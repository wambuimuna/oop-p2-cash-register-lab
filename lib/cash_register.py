#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100

        # Normalize to int when there's no fractional cents
        if isinstance(self.total, float) and self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void.")
            return

        last = self.previous_transactions.pop()
        amount = last["price"] * last["quantity"]
        self.total -= amount

        # remove the item occurrences from items list
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
