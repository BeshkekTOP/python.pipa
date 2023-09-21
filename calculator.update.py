import math 
o = (input("Введите операцию"))
if o == "+":
    a = float (input ("Введите первое число"))
    b = float (input ("Введите второе  число"))
    def sum (a,b):
        print (a + b)
        return a + b 
    sum (a, b )
elif o == "-":
    a = float (input ("Введите первое число"))
    b = float (input ("Введите второе  число"))
    def minus (a,b):
        print(a - b)
        return (a - b)

    minus (a, b)
elif o == "*":
    a = float (input ("Введите первое число"))
    b = float (input ("Введите второе число"))
    def umnoj (a,b):
        print (a * b)
        return a * b
    umnoj (a,b)
elif o == "/":
    a = float (input ("Введите первое число"))
    b = float (input ("Введите второе число"))
    def dele (a,b):
        print (a / b)
        return a / b
    dele (a,b)
elif o == "**":
    a = float (input ("Введите первое число"))
    b = float (input ("Введите второе число"))  
    def step (a,b):
        print (a ** b)
        return a ** b
    step (a,b)
elif o == "кор":
    a = float (input ("Введите первое число"))
    def cor (a):
        print (a ** 0.5)
        return a ** 0.5
    cor (a)
elif o == "син":
    a = float (input ("Введите первое число"))
    def sin (a):
        print (math.sin (a))
        return math.sin (a)
    sin (a)
elif o == "кос":
    a = float (input ("Введите первое число"))
    def cos (a):
        print (math.cos  (a))
        return math.cos (a)
    cos (a)
elif o == "таг":
    a = float (input ("Введите первое число"))
    def tag (a):
        print(math.tan (a))
        return math.tan (a)
    tag (a)
else:
    print ("Ошибка")