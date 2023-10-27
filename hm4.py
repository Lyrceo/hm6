import random

class NumberEncryptor:
    def __init__(self):
        self.value = None

    def encrypt(self, number):
        self.value = number
        operation = random.choice(["+", "-", "*", "/"])
        operand = random.randint(1, 10)
        
        if operation == "+":
            self.value += operand
        elif operation == "-":
            self.value -= operand
        elif operation == "*":
            self.value *= operand
        elif operation == "/":
            self.value /= operand

    def __str__(self):
        if self.value is not None:
            return f"Зашифроване число: {self.value}"
        else:
            return "Значення не зашифровано"


encryptor = NumberEncryptor()
number = 10
encryptor.encrypt(number)
print(encryptor)  

number = 5
encryptor.encrypt(number)
print(encryptor) 
