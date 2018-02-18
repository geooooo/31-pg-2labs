from myqueue import (
    ArrayQueue,
    ListQueue
)



def init():
    """
        Выбор реализации очереди и её инициализация
    """
    global q
    print(
        "Укажите способ реализации очереди:\n"
        "0 - через массив\n"
        "1 - через связанный список\n"
        ": ", end=""
    )
    number = int(input())
    print("Укажите размер очереди: ", end="")
    qsize = int(input())
    print("\n")
    if number == 0:
        q = ArrayQueue(qsize)
    elif number == 1:
        q = ListQueue(qsize)
    return q



def user_loop():
    """
        Цикл моделирования работы с технологической установкой
    """
    global q
    global cur_time
    while True:
        print(
            "Время: {} | Укажите операцию:\n"
            "Пробел - пройти единицу цикла обработки\n"
            "q - выйти\n"
            "0 - постановка детали на обработку\n"
            "1 - принудительное снятие детали\n"
            "2 - вывод списка деталей в очереди\n"
            "3 - перезапуск\n"
            ": ".format(cur_time)
        )
        cmd = input().strip().lower()
        print("\n")
        if cmd == "":
            print("ЦИКЛ РАБОТЫ УСТАНОВКИ ...")
            cmp_time()
            continue
        elif cmd == "q":
            print("Досвидания !")
            break
        elif cmd == "0":
            append()
        elif cmd == "1":
            force_delete()
        elif cmd == "2":
            out_list()
        elif cmd == "3":
            q = reset()



def cmp_time():
    """
        Контроль времени работы установки
        и снятие детали с очереди
    """
    global q
    global cur_time
    if q.is_empty():
        cur_time = 0
    else:
        cur_time += 1
        item = q.get()
        if item["time"] == cur_time:
            # Снятие детали
            print("Деталь: '{} {}' готова !\n".format(item["title"], item["time"]))
            q.delete()
            cur_time = 0



def append():
    global q
    if q.is_full():
        print("ОЧЕРЕДЬ ЗАПОЛНЕНА ПОЛНОСТЬЮ !\n")
        return
    print("Наименование и время работы детали: ", end="")
    title, time = input().split(" ")
    print("\n")
    q.insert({
        "title": title,
        "time":  int(time)
    })



def force_delete():
    global q
    global cur_time
    if q.is_empty():
        print("ОЧЕРЕДЬ ПУСТА !\n")
        return
    q.delete()
    cur_time = 0


def out_list():
    global q
    print(
        "Список деталей:\n"
        "№ Наименование Время_обработки"
    )
    for number, item in enumerate(q):
        print("{}\t{}\t{}".format(number, item["title"], item["time"]))
    print("\n")



def reset():
    return init()



def main():
    global q
    global cur_time
    q = reset()
    cur_time = 0
    user_loop()



if __name__ == '__main__':
    main()
