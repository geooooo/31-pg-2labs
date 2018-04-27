"""
    1. Вводим многочлен
    2. Ввдим отрезок на котором определяем корни
    3. Точность на которой определяем
    4. Вычислить значение в этой точке
    5. Выяснить на каких промежутках есть корни
"""


import re


def find_root_div_mid(x0, x1, accur, f):
    def mid(x0, x1):
        return (x0 + x1) / 2

    while True:
        x2 = mid(x0, x1)
        fx2 = f(x2)
        if abs(fx2) < accur:
            break
        if f(x0) * fx2 < 0:
            x1 = x2
        else:
            x0 = x2
    return x2


def find_root_hord(x0, x1, accur, f):
    la = x0
    lb = x1
    fa = f(la)
    while True:
        fb = f(lb)
        lc = (la * fb - lb * fa) / (fb - fa)
        fc = f(lc)
        lb = lc
        if abs(fc) < accur:
            break
    return lc


def find_root_newton(x0, x1, accur, f, df, df2):
    if f(x0) * df2(x1) > 0:
        lc = x0
    else:
        lc = x1
    while True:
        fc = f(lc)
        try:
            lc = lc - f(lc) / df(lc)
        except:
            lc = lc - f(lc)
        if abs(fc) < accur:
            break
    return lc


def find_root_newton_mod(x0, x1, accur, f, df, df2):
    if f(x0) * df2(x1) > 0:
        lc = x0
    else:
        lc = x1
    fb = df(lc)
    while True:
        fc = f(lc)
        try:
            lc = lc - f(lc) / fb
        except:
            lc = lc - f(lc)
        # print(abs(fc))
        if abs(fc) < accur:
            break
    return lc


def get_df(f_str):
    # x**3 - 4.5*x**2 + 2*x + 0.77

    # замена степеней
    df = f_str + " "
    expr_list = []
    while True:
        pow_expr =re.search(r"[A-z](\*\*\d)?", df)
        if (not pow_expr):
            break
        l, r = pow_expr.span()
        pow_expr = pow_expr.group()
        if len(pow_expr) > 1:
            var, num = pow_expr.split("**")
            new_expr = f"{num}*{var}**{int(num)-1}"
        else:
            new_expr = "1"
        expr_list.append(new_expr)
        df = df[:l] + "{}" + df[r:]
    # Удаление констант
    df = df.format(*expr_list)
    expr_list = []
    while True:
        pow_expr =re.search(r" \d+(\.\d+)? ", df)
        if (not pow_expr):
            break
        l, r = pow_expr.span()
        expr_list.append(new_expr)
        df = df[:l-2] + df[r:]
    return df, eval(f"lambda x: {df}")


# отладка
# find_root_newton_mod.__code__ = find_root_newton.__code__
import sys
sys.stdin = open("in.txt", "rt")


def main():
    # Вводим многочлен
    print("Введите многочлен: ", end="")
    f_str = input()
    # Определяем функцию от заданного многочлена
    f = eval("lambda x: {}".format(f_str))
    df_str, df = get_df(f_str)
    _, df2 = get_df(df_str)
    # Ввод диапазона
    print("Введите интервал a..b: ", end="")
    a, b = [float(num) for num in input().split("..")]
    # Ввод шага
    print("Введите шаг: ", end="")
    step = float(input())
    # Ввод точности
    print("Введите точность: ", end="")
    accur = float(input())
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
                print("(Деление пополам) Есть корень: {2:0.{3}f} на отрезке [{0:2}..{1:2}]".format(
                    x - step,
                    x,
                    find_root_div_mid(x - step, x, accur, f),
                    len(str(accur)) - 2
                ))
                print("(Хорды) Есть корень: {2:0.{3}f} на отрезке [{0:2}..{1:2}]".format(
                    x - step,
                    x,
                    find_root_hord(x - step, x, accur, f),
                    len(str(accur)) - 2
                ))
                print("(Ньютон) Есть корень: {2:0.{3}f} на отрезке [{0:2}..{1:2}]".format(
                    x - step,
                    x,
                    find_root_newton(x - step, x, accur, f, df, df2),
                    len(str(accur)) - 2
                ))
                print("(Ньютон мод) Есть корень: {2:0.{3}f} на отрезке [{0:2}..{1:2}]".format(
                    x - step,
                    x,
                    find_root_newton_mod(x - step, x, accur, f, df, df2),
                    len(str(accur)) - 2
                ))
                print()
        sign_prev = sign_cur


if __name__ == "__main__":
    main()
