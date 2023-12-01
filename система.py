import os
import subprocess

while True:
    # Выводим приглашение для ввода команды
    command = input("Введите команду (exit для выхода): ")

    # Проверяем введенную команду
    if command.lower() == 'exit':
        # Выходим из цикла, если введена команда exit
        break
    elif command.lower() == 'dir':
        # Имитируем команду dir для вывода списка файлов и каталогов
        file_list = os.listdir()
        print("\n".join(file_list))
    elif command.lower() == 'cd':
        # Имитируем команду cd для смены текущего рабочего каталога
        new_directory = input("Введите новый каталог: ")
        try:
            os.chdir(new_directory)
            print(f"Текущий каталог: {os.getcwd()}")
        except FileNotFoundError:
            print("Каталог не найден.")
    elif command.lower() == 'runcmd':
        # Имитируем выполнение произвольной команды через командную строку
        cmd_to_run = input("Введите команду для выполнения: ")
        try:
            subprocess.run(cmd_to_run, shell=True)
        except Exception as e:
            print(f"Ошибка при выполнении команды: {e}")
    elif command.lower() == 'start':
        # Имитируем команду start для запуска приложения
        app_to_start = input("Введите имя приложения для запуска: ")
        try:
            subprocess.Popen(app_to_start)
        except Exception as e:
            print(f"Ошибка при запуске приложения: {e}")
    elif command.lower() == 'help':
        # Добавляем команду help для вывода списка доступных команд
        print("Доступные команды:")
        print("dir - Вывести список файлов и каталогов")
        print("cd - Сменить текущий рабочий каталог")
        print("runcmd - Выполнить произвольную команду")
        print("start - Запустить приложение")
        print("print - Вывести сообщение в консоль")
        print("help - Вывести список доступных команд")
        # Дополнительные команды (добавьте свои собственные команды)
        print("example_command - Пример новой команды")
    elif command.lower() == 'print':
        # Добавляем команду print для вывода сообщения в консоль
        message = input("Введите сообщение для вывода: ")
        print(message)
    else:
        # Выводим сообщение об ошибке для неизвестных команд
        print("Неизвестная команда. Попробуйте снова.")