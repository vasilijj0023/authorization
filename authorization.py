from main import load_key
from cryptography.fernet import Fernet


def authorization(login,password,fernet):
    with open("password.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.rstrip()
            lgn,pwd = line.split("|")
            if login == lgn and password == fernet.decrypt(pwd.encode()).decode():
                return True
    return False


def main():
    key = load_key()
    fernet = Fernet(key)
    while True:
        login = input("Введете логин: ")
        password = input("Введите пароль: ")
        if authorization(login,password,fernet):
            print("Вы авторизованы.")
            break
        else:
            print("Пользователь не найден.")


if __name__ == '__main__':
    main()