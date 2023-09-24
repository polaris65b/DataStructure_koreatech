class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)

    def subtract(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return Complex(real_diff, imag_diff)

    def multiply(self, other):
        real_product = self.real * other.real - self.imag * other.imag
        imag_product = self.real * other.imag + self.imag * other.real
        return Complex(real_product, imag_product)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
