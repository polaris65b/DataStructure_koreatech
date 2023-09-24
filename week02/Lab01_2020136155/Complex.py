class Complex:
    def __init__(self, x = 0.0, y = 0.0):
        self.re = x
        self.im = y

    def re(self):
        return self.re
    def im(self):
        return self.im

    def __str__(self):
        return '({},{}i)'.format(self.re, self.im)

    def __repr__(self):
        return '({},{}i)'.format(self.re, self.im)
    
    def add(self, other):
        x = self.re + other.re
        y = self.im + other.im
        return Complex(x, y)

    def subtract(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return Complex(real_diff, imag_diff)

    def multiply(self, other):
        real_product = self.real * other.real - self.imag * other.imag
        imag_product = self.real * other.imag + self.imag * other.real
        return Complex(real_product, imag_product)