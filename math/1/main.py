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
    a, b = [float(num) for num in input().split("..")]
    # Ввод шага
    print("Введите шаг: ", end="")
    step = float(input())
    # Вычисление значений на интервале
    vals = {}
    x = a
    while x <= b:
        vals[x] = f(x)
        x += step
    # Вывод промежуточных результатов
    for x, fx in vals.items():
        print("При x = {:2}, f(x) = {:4}".format(x, fx))
    # Поиск промежутков с корнями
    sign_prev = None
    for x, fx in vals.items():
        sign_cur = "-" if fx < 0 else "+"
        if sign_prev and (sign_prev != sign_cur):
            if f(x - step) == 0:
                print("Корень найден при x = {}".format(x - step))
            else:
                print("Есть корень: [{0:2}..{1:2}]".format(x-step, x))
        sign_prev = "-" if fx < 0 else "+"


if __name__ == "__main__":
    main()
