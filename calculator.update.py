import math
def run():
    try:
        num1 = int(input('Укажите первое число: '))
    except ValueError:
        num1 = int(input('Вы ввели некорректные данные.'))
    try:
        num2 = int(input('Укажите второе число: '))
    except ValueError:
        num2 = int(input('Вы ввели некорректные данные.'))
    op = operation()
    result = calc(num1, num2, op)
    print(f'Результат: {result}')

def summa (num1, num2):
    return num1 + num2
def sub (num1, num2):
    return num1 - num2
def mult (num1, num2):
    return num1 * num2
def div (num1, num2):
    return num1 / num2
def calc(num1, num2, oper):
    result = None
    if oper == '+':
        result = summa(num1, num2)
    elif oper == '-':
        result = sub(num1, num2)
    elif oper == '*':
        result = mult(num1, num2)
    elif oper == '/':
        if (num2 == 0):
            print('Деление на ноль запрещено!')
            return
        result = div(num1, num2)
    elif oper == 'sqrt':
        if (num2 < 0):
            print('Ошибка')
            return
        result = num1 ** 0.5
    elif oper == '**':
        result = num1 ** num2
    elif oper == 'sin':
        result = math.sin(num1)
    elif oper == "cos":
        result = math.cos(num1)
    elif oper == "tan":
        result = math.tan(num1)
    elif oper == "fac":
        if (num2 < 0):
            print('Ошибка')
            return
        result = math.factorial(num1)
    else:
        print('Некорректная операция!')
    return result
def operation():
    mes = input('Выберите операцию \n ')
    if mes == '+':
        print('Вы выбрали сумму')
    elif mes == '-':
        print('Вы выбрали разность')
    elif mes == '*':
        print('Вы выбрали умножение')
    elif mes == '/':
        print('Вы выбрали деление')
    elif mes == 'sqrt':
        print('Вы выбрали нахождение процента первого числа от второго')
    elif mes == '**':
        print('Вы выбрали возведение в степень')
    elif mes == 'sin':
        print('Вы выбрали синус')
    elif mes == 'cos':
        print('Вы выбрали косинус')
    elif mes == 'tan':
        print('Вы выбрали тангенс')
    elif mes == 'fac':
        print('Вы выбрали факториал')

    correct_operations = ['+', '-', '*', '/', 'sqrt', '**', 'sin', 'cos', 'tan', 'fac']

    while mes not in correct_operations:
        print('Такой операции нет в списке. Попробуйте ещё!')

        mes = input()
    return mes
progam_is_running = True
while(progam_is_running):
    run()
    answer = input('Желаете продолжить?\n'
      ' Введите + если да и прочий символ, если нет: ')
    if answer != '+':
        progam_is_running = False
