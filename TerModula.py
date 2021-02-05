class ErrorMain(Exception):
    pass


def cut_to_import(path):
    print(path)
    pass


def import_module_or_old():
    try:  # Импортирую с места где положено основную версию.
        from scripts.modul import main
        # Именно эта функция запускает модуль:
        main()  # RUN

        del main
    # except Er:
    #     pass

    except:  # попытка номер два: - тут запуск старой\запас стабильной версии:
        try:  # Импортирую с места где положено стабильную старую версию.
            from scripts.modul import old
            old()  # RUN

            del old

        except:  # Не удалось импортировать запасную функцию:
            pass  # Говорю что такой команды нет.

    finally:
        pass
    pass


def import_module():
    try:
        from scripts.modul import main
        main()
        # Импортирую с места где положено
    except:
        pass  # Говорю что такой команды нет.
    pass


def start_module(path, import_old):
    cut_to_import(path)
    # Переместить ссилку в место для импорта

    if import_old:
        import_module_or_old()
        pass
    else:
        pass
    pass
