import math
from importlib import reload

math = reload(math)
def modul_os():
    import os
    # Работаем с модулем OS

    # Узнаем тип операционной системы
    # Если это винда то получим "nt"
    print("Ваша Операционная система - ", os.name)
    # ~ a = os.uname
    # ~ for i in a:
        # ~ print(i)
    # ~ a.sysname
    # ~ print("Ваша Операционная система - ", os.uname)

    # Узнаем пути до системных папок
    print("Список переменных окружения: \n")
    print(os.environ)

    # Получаем список файлов и папок в указанноой папке
    print(os.listdir("/"), "\n")

    # Создаем папку
    os.makedirs("/home/cytoncode/Документы/sese", exist_ok=True)

    # Удаляем папку:
    # https://defpython.ru/kak_v_Python_udalit_fail_ili_papku
    # ~ input()
    # Удаляем файл
    # ~ if(os.path.exists("/home/cytoncode/Документы/sese")):
        # ~ os.remove("/home/cytoncode/Документы/sese")

    # Перемеаем и переменовываем файл
    # ~ if(os.path.exists("E:/2.txt")):
        # ~ os.replace("E:/2.txt", "E:/test/3.txt")

    # Открываем файл в системе програмой по умолчанию
    # ~ if(os.path.exists("E:/test/3.txt")):
        # ~ os.startfile("E:test/3.txt")
    pass
# ~ modul_os()

def cuting(address, two_address="work/lib.py"):
    """
    функция которая перемещает модули между ворк и хранилием в реад...
    Cut:
    .переменстить файл
    .сохранить имя а точнее первый адресс.
    .переименоать в либ.
     .при переподключении к другому модулю:
      .переметстить назад и вернуть имя.
      .начать с нулевого пункта.
     .при подключении к тому же самому модулю:
      .ничего не менять.
    .подключить модуль.
    """
    import os
    # Перемеаем и переменовываем файл
    if(os.path.exists(address)):
        os.replace(address, two_address)

    # вернуть адресс первого располоения:
    return address
def to_list(param):
    ignore_list = " \n"
    tmp_slovo = ""
    param += ' '
    result = []
    for i in param:
        if i not in ignore_list:
            tmp_slovo += i
        else:
            if (tmp_slovo != '' and tmp_slovo not in ignore_list):
                result.append(tmp_slovo)
            tmp_slovo = ""
    return result
def check_file(address_file = "read/libs/modul.txt"):
    __doc__ = '''var: Checking module readability...
    Нужен для чтения файла и проверки на сущестование файла или модуля.
    '''
    print(__doc__)
    # проверить есть ли файл:
    try:
        f = open(address_file, 'r') # если ошибка, то: файла нет или
        # его нельзя читать.
        return True # ответ: файл есть.
    except:
        print("Module not defined. modul:", address_file)
        return False # ответ: файла нет.
    finally:
        try:
            f.close() # обьязательно нужно закрыть файл, если не
        except:
            pass
        # закрылся (функция сама это сделает).
        pass

iterabl = 0
def start_modul_cut(tmp):
    global iterabl
    __doc__ = '''var: I am trying to run a module...
    Нужен для запуска модуля.
    '''
    print(__doc__)
    address = "read/libs/{0}.py".format(tmp[0])
    print(address)
    if(not check_file("work/lib.py")):
        old_address = cuting(address)
    else:
        while(check_file("drow/" + str(iterabl) + ".py")):
            iterabl += 1
        cuting(address, "drow/" + str(iterabl) + ".py")
        old_address = address
        if(not check_file("work/lib.py")):
            old_address = cuting(address)
        else:
            # ~ exit()
            pass
    try:
        from work.lib import main
        main(tmp)
        main = reload(main)
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
    finally:
        if(check_file("work/lib.py")):
            cuting("work/lib.py", old_address)
    pass
def info_modul_cut(tmp):
    address ="read/libs/{0}.py".format(tmp[1])
    print(address)
    if(not check_file("work/lib.py")):
        old_address = cuting(address)
    else:
        while(check_file("drow/" + str(iterabl) + ".py")):
            iterabl += 1
        cuting(address, "drow/" + str(iterabl) + ".py")
        old_address = address
        if(not check_file("work/lib.py")):
            old_address = cuting(address)
        else:
            # ~ exit()
            pass
    try:
        from work.lib import info
        info()
        info = reload(info)
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
    finally:
        cuting("work/lib.py", old_address)
def help_modul_cut(tmp):
    address ="read/libs/{0}.py".format(tmp[1])
    print(address)
    if(not check_file("work/lib.py")):
        old_address = cuting(address)
    else:
        while(check_file("drow/" + str(iterabl) + ".py")):
            iterabl += 1
        cuting(address, "drow/" + str(iterabl) + ".py")
        old_address = address
        if(not check_file("work/lib.py")):
            old_address = cuting(address)
        else:
            # ~ exit()
            pass
    try:
        from work.lib import helps
        helps()
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
    finally:
        cuting("work/lib.py", old_address)

def can_i_edit_the_file(address_file = "read/libs/lib.py"):
    __doc__ = '''var: Checking the possibility of editing a module...
    Нужен для создания файла и записи файла или модуля.
    '''
    print(__doc__)
    # проверить на возможность редактировать:
    # ~ if(check_file(address_file)):
    res = "w"
    try:
        f = open(address_file, "w")
        f.write(res)
        return True
    except:
        print("The file is blocking editing.I can't keep working.")
        return False
    finally:
        f.close()
    # ~ else:
    #    # ~ return False
    pass
def start_modul(tmp):
    __doc__ = '''var: I am trying to run a module...
    Нужен для запуска модуля.
    '''
    print(__doc__)
    address = "read/libs/{0}.py".format(tmp[0])
    tm = ""
    if (check_file(address)):
        fff = open(address, "r")
        tm = fff.read()
        fff.close()
    address = "read/libs/lib.py"
    # ~ if (can_i_edit_the_file(address)):
    fff = open(address, "w")
    fff.write(tm)
    fff.close()
    try:
        from libs.lib import main
        main(tmp)
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
    # ~ else:
    #    # ~ print("error3")
    pass
def info_modul(tmp):
    address ="read/libs/{0}.py".format(tmp[1])
    tm = ""
    if(check_file(address)):
        fff = open(address, "r")
        tm = fff.read()
        fff.close()
    address = "read/libs/lib.py"
    fff = open(address, "w")
    fff.write(tm)
    fff.close()
    try:
        from libs.lib import info
        info()
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
def help_modul(tmp):
    address ="read/libs/{0}.py".format(tmp[1])
    tm = ""
    if(check_file(address)):
        fff = open(address, "r")
        tm = fff.read()
        fff.close()
    address = "read/libs/lib.py"
    fff = open(address, "w")
    fff.write(tm)
    fff.close()
    try:
        from libs.lib import help
        help()
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
def start():
    __doc__ = """ command:
    .quit  .help  .info  .sys   checkf  cutf  delf  clearf"""
    __info__ = """
    Консольний проводник Я.
    Обработаю файлы для тебя.
    Разрабатывают еще Меня.
    Оцени балами же меня.
    На питоне писан был Я.
    А на С++ будет реализация.

    Спасибо за использование :D
    O1.01.2021 00:04:50

    Могу удалить старые файлы!
    Но и создать новые могу.
    О еще и перемещать могу.
    Юзаю есть ли файлы.
    """
    # 38  37|78 символов.
    print(__doc__) # info_me

    while True:
        c = input("[root ~]$ ")
        tmp = to_list(c)
        print(tmp)
        if (c[0] == "."):
            # ~ flag = False
            my_list = [".quit", ".q", ".exit", ".e"]
            if (tmp[0] in my_list):
                exit()
            my_list = [".help", ".h"] # print name to all or help name
            if (tmp[0] in my_list):
                if (len(tmp) <= 1):
                    print(__info__)
                else:
                    info_modul_cut(tmp)
            my_list = [".info", ".i"] # print info to me
            if (tmp[0] in my_list):
                if (len(tmp) <= 1):
                    print(__doc__)
                else:
                    pass
            my_list = [".sys", ".s"]
            if (tmp[0] in my_list):
                pass
        else:
            start_modul_cut(tmp)
        # ~ elif (c[0] == '-'):
        # ~ pass # блока парных команд или флажков.
        # ~ flag = False # нету предедущих слов
        # ~ if(tmp):
        # ~ flag = True
        # ~ elif (flag):
        pass
def started(c):
    __doc__ = """ command:
    .quit  .help  .info  .sys   checkf  cutf  delf  clearf"""
    __info__ = """
    Консольний проводник Я.
    Обработаю файлы для тебя.
    Разрабатывают еще Меня.
    Оцени балами же меня.
    На питоне писан был Я.
    А на С++ будет реализация.

    Спасибо за использование :D
    O1.01.2021 00:04:50

    Могу удалить старые файлы!
    Но и создать новые могу.
    О еще и перемещать могу.
    Юзаю есть ли файлы.
    """
    # 38  37|78 символов.
    print(__doc__) # info_me
    tmp = to_list(c)
    print(tmp)
    if (c[0] == "."):
        # ~ flag = False
        my_list = [".quit", ".q", ".exit", ".e"]
        if (tmp[0] in my_list):
            exit()
        my_list = [".help", ".h"] # print name to all or help name
        if (tmp[0] in my_list):
            if (len(tmp) <= 1):
                print(__info__)
            else:
                info_modul_cut(tmp)
        my_list = [".info", ".i"] # print info to me
        if (tmp[0] in my_list):
            if (len(tmp) <= 1):
                print(__doc__)
            else:
                pass
        my_list = [".sys", ".s"]
        if (tmp[0] in my_list):
            pass
    else:
        start_modul_cut(tmp)
    pass
def start_file():
    address = "read/libs/index.terminal"
    if(check_file(address)):
        f = open(address, "r")
        for l in f:
            started(l)
        f.close()
def start_me():
    #download module:
    start_file()

    while True:
        c = input("[root ~]$ ")
        if(c !="\n" and c !=" " and c !=""):
            started(c)
    pass

start_me()

# ~ cuting("work/liv.py", "work/lib.py")
