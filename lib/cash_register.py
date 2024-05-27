#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.item = []
    self.total = 0
    self.transactions = []

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    self.item.extend([item]*quantity)
    self.transactions.append((item, price, quantity))

  def apply_discount(self):
    if self.discount >0:
      discount_amount = (self.discount / 100) * self.total
      self.total -=discount_amount
      return f"After the discount, the total comes to ${self.total:.2f}."
    else: 
      return "There is no discount to apply"

  def void_last_transaction(self):
    if self.transactions:
      last_item, last_price, last_quantity = self.transactions.pop()
      self.total -= last_price * last_quantity
      for _ in range(last_quantity):
        self.items.remove(last_item)
    else:
      return "There are no transactions to void."



