class ComplexNumbers:
    def putComplexNumber(self):
        self.re = float(input("Put real part: "))
        self.im = float(input("Put imaginary part: "))
    def add(self, number1, number2):
        self.re = number1.re + number2.re
        self.im = number1.im + number2.im
    def subtract(self, number1, number2):
        self.re = number1.re - number2.re
        self.im = number1.im - number2.im
    def show(self):
        if self.im < 0:
            print(self.re, " - ", abs(self.im), "i", sep="")
        else:
            print(self.re, " + ", self.im, "i", sep="")

number1 = ComplexNumbers()
number2 = ComplexNumbers()
result = ComplexNumbers()
number1.putComplexNumber()
number2.putComplexNumber()
number1.show()
number2.show()
print("Sum of two complex numbers")
result.add(number1,number2)
result.show()
print("Subtracted two complex numbers")
result.subtract(number1,number2)
result.show()