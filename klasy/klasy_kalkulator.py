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
operation = 0
while(1):
    print("Welcome, this is you complex number calculator")
    print("Put your first complex number:")
    number1.putComplexNumber()
    print("Put your second complex number:")
    number2.putComplexNumber()
    print("Choose which mathematical operation you want:")
    print("1. Add")
    print("2. Subtract")
    operation = int(input())
    if(operation == 1):
        print("Sum of two complex numbers")
        result.add(number1, number2)
        result.show()
    elif(operation == 2):
        print("Subtracted two complex numbers")
        result.subtract(number1, number2)
        result.show()
