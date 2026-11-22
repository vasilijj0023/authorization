import os
from cryptography.fernet import Fernet


def write_key():
    with open("key.key", "wb") as f:
        f.write(Fernet.generate_key())


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
    return key


def add(fernet):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    with open("password.txt", "a", encoding="utf8") as f:
        f.write(f"{login}|{fernet.encrypt(password.encode()).decode()}\n")


def view(fernet):
    with open("password.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.rstrip()
            login,password = line.split("|")
            print(f"Логин: {login} | Пароль: {fernet.decrypt(password.encode()).decode()}")


def main():
    if not os.path.exists("key.key"):
        write_key()
    key = load_key()
    fernet = Fernet(key)
    while True:
        choice = int(input("Нажмите 1 что-бы добавить новый пароль, 2 что-бы посмотреть существующие и 3 что-бы выйти. "))
        if choice == 1:
            add(fernet)
        elif choice == 2:
            view(fernet)
        elif choice == 3:
            break
        else: 
            print("Проверьте ваш выбор.")


if __name__ == '__main__':
    main()