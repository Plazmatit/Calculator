name = input("Ведеите свое имя")
print("Здравствуйте," ,name )

def main():
    print("Это простой калькулятор на Python")                 # Выводим сообщение
    while True:                                                # Выводим сообщение какие действия есть
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input("Действие: ")                            # Переменная для хранения действия
        if action == "q":                                       # Если action равен q то
            print("Выход из программы")                         # Выводим сообщение
            break                                               # Выходим из цикла
        if action in ('+', '-', '*', '/'):                      # Если action равен +, -, *, /, то
            x = float(input("x = "))                            # Присваиваем значение переменной x
            y = float(input("y = "))                            # Присваиваем значение переменной y
            if action == '+':                                   # Если action равен + то
                print('%.2f + %.2f = %.2f' % (x, y, x+y))       # Выводим сумму x и y
            elif action == '-':                                 # Если action равен - то
                print('%.2f - %.2f = %.2f' % (x, y, x-y))       # Выводим разность x и y
            elif action == '*':                                 # Если action равен * то
                print('%.2f * %.2f = %.2f' % (x, y, x*y))       # Выводим результат умножения x на y
            elif action == '/':                                 # Если action равен / то
                if y != 0:                                      # Если y не равен нулю то
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))   # Выводим результат деления x на y
                else:                                           # Иначе
                    print("Деление на ноль!")                   # Выводим сообщение, что на ноль делить нельзя


if __name__ == '__main__':
    main()


