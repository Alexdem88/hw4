# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчёта заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

def pay():
    try:
        t= int(input('Выработка в часах'))
        s=int(input('Ставка в часах'))
        p=int(input('Премия фиксированная'))
        salary = (t*s)+p
        print(f'Ваш доход составит: {salary}')
    except ValueError:
        return print('Ошибка, необходимо ввести число')

pay() #через командую строку все работает!!!


