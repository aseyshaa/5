def analysis_text():
    text = "a1 b2 c1 d1 e1"
    print(text)


def hand_text():
    a = "abc"
    return a


def autotext():
    b = "deb"
    return b


def menu():
    text = ""
    while True:
        print("Главное меню:")
        print("1. Ввести текст вручную.")
        print("2. Ввести текст случайным образом.")
        print("3. Решение задачи.")
        print("4. Выход из программы ")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            text = hand_text()
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "2":
            text = auto_text()
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "3":
            result = analysis_text()
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    menu()
