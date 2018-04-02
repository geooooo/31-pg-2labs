"""
    1. Вводим многочлен
    2. Ввдим отрезок на котором определяем корни
    3. Точность на которой определяем
    4. Вычислить значение в этой точке
    5. Выяснить на каких промежутках есть корни
"""

def main():
    # Вводим многочлен
    print("Введите многочлен: ", end="")
    expr = input()
    # Определяем функцию от заданного многочлена
    f = eval("lambda x: {}".format(expr))
    # Ввод диапазона
    print("Введите интервал a..b: ", end="")
    a, b = [int(num) for num in input().split("..")]
    # Ввод точности
    print("Введите точность: ", end="")
    accur = int(input())
    # Вычисление значений на интервале
    vals = {}
    for x in range(a, b + 1):
        vals[x] = f(x)
    # Вывод промежуточных результатов
    for x, fx in vals.items():
        print("При x = {:2}, f(x) = {}".format(x, fx))
    # Поиск промежутков с корнями
    sign_prev = None
    for x, fx in vals.items():
        sign_cur = "-" if fx < 0 else "+"
        if sign_prev and (sign_prev != sign_cur):
            print("Есть корень: [{0:2}..{1:2}] f(x) = {2:.{3}f}".format(x-1, x, fx, accur))
        sign_prev = "-" if fx < 0 else "+"

if __name__ == "__main__":
    main()
