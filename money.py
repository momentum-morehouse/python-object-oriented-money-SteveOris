# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    pass


class Currency:
  

    def __init__(self, name, code, symbol=None, digits=2):
      
      self.name = name
      self.code = code
      self.symbol = symbol
      self.digits = digits
      
      
        
        

    def __str__(self):
      if self.symbol:
        return f"{self.code} ({self.symbol})"
      else: 
        return f" {self.code}"
      

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and self.code == other.code and self.symbol == other.symbol and self.digits == other.digits)


class Money:
    

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

       

        

    def __str__(self):
      
      if self.currency.symbol:
        return f"{self.currency.symbol}{self.amount:.{self.currency.digits}f}"
      else:
        return f"{self.currency.code} {self.amount:.{self.currency.digits}f}"


    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
          add = self.amount + other.amount
          testrun = Money(add,self.currency)
          return testrun
        else:
          raise DifferentCurrencyError

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
          sub = self.amount - other.amount
          testrun = Money(sub,self.currency)
          return testrun
        else:
          raise DifferentCurrencyError


    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        mul = self.amount * multiplier
        testrun = Money(mul,self.currency)
        return testrun
        


    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        div = self.amount / divisor
        testrun = Money(div,self.currency)
        return testrun
