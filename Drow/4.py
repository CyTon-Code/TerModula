import os
from importlib import reload
iterabl = 0

# ~ print(["/", "\\"[0][0]])
# ~ address_file = "index.terminal"
# ~ if "/" not in address_file and "\\" not in address_file:
    # ~ print(1)
# ~ else:
    # ~ print(2)
# ~ address_file = "read/terminals/index.terminal"
# ~ if "/" not in address_file and "\\" not in address_file:
    # ~ print(3)
# ~ else:
    # ~ print(4)

#TODO:
"""
не удалять этот коменнтарий. На будущие, нельзя создавать lib, так как
мы используем перемещение фалов, а не их редактирование и можем
случайно повредить чужую библиотеку."""
"try:\tfrom work import lib\nexcept:\tpass\n" # иморт если файл есть.
def whats_file_name(address_file):# "read/terminals/index.terminal"
    if "/" not in address_file and "\\" not in address_file:
        return address_file
    i_one = 0 # search index file after / (before)
    n_end = len(address_file)
    b_list = ["/", "\\"[0][0]]
    j_str = -1
    if address_file=="" or address_file==" " or address_file=="\n" or (
    address_file=="\t"):
        return None
    while i < n:
        if address_file[i_one] in b_list:
            j_str = i
        i_one += 1
    if j_str == -1:
        return
    # ~ while
    pass
def can_i_edit_the_file(address_file = "write.txt"):
    __doc__ = '''var: Checking the possibility of editing a module...
    Нужен для создания файла и записи файла или модуля.
    '''
    print(__doc__)
    # проверить на возможность редактировать:
    if(not check_file(address_file)):
        return False #?
    else:
        print("file is it reality...")
        res = input("Edited file now? Y?N")
        if (res[0].upper() != "N"):
            # ~ return True # - еще нужно проверить на возможность
            #редактировать.
            pass
        else:
            return False
    res = "w"
    try:
        f = open(address_file, "w")
        f.write(res)
        print("The file not is blocking editing.I can keep working. :D")
        return True
    except:
        print("The file is blocking editing.I can't keep working. :C")
        return False
    finally:
        f.close()
    pass
def can_i_creat_the_file(address_file = "write.txt"):
    __doc__ = '''var: Checking the possibility of editing a module...
    Нужен для создания файла и записи файла или модуля.
    '''
    print(__doc__)
    # проверить на возможность редактировать:
    if(not check_file(address_file)):
        return True #?
    else:
        pass
        print("file is it reality...")
        res = input("Writed file now? Y/N? ")
        if (res[0].upper() != "N"):
            # ~ return True # - еще нужно проверить на возможность
            #записи.
            pass
        else:
            return True
    res = "w"
    try:
        f = open(address_file, "w")
        f.write(res)
        print("The file not is blocking editing.I can keep working. :D")
        return True
    except:
        print("The file is blocking editing.I can't keep working. :C")
        return False
    finally:
        f.close()
    pass
def check_file(address_file = "read/terminals/index.terminal"):
    __doc__ = '''var: Checking module readability...
    Нужен для чтения файла и проверки на сущестование файла или модуля.
    '''
    # ~ print(__doc__)
    # проверить есть ли файл:
    try:
        f = open(address_file, 'r') # если ошибка, то: файла нет или
        # его нельзя читать.
        return True # ответ: файл есть и его прочитано.
    except:
        print("Module not defined. modul:", address_file)
        return False # ответ: файла нет или его не прочитано.
    finally:
        try:
            f.close() # обьязательно нужно закрыть файл, если еще не.
        except:
            pass # если попасть в это место, то файл нельзя закрыть
            #читая: файл изчез или нельзя закрыть.
        # закрылся (функция сама это сделает).
    pass
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
    # TODO: Нужно доработать проверку разности имен, а также проверку
    #на сущестование файла перед перемещением.
    if(address == two_address):
        pass # Также сюда нужно попасть когда имена в адресах не
        #совпадают нельзя перемещать переименовывая файл.
        pass # адресса совпадают: перемещать не нужно.
    else:
        # Перемещаем и переменовываем файл:
        if(os.path.exists(address)):
            os.replace(address, two_address) # cut.
    # вернуть адресс первого располоения:
    return (address, two_address)
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
def start_modul_cut(tmp):
    global iterabl
    __doc__ = '''var: I am trying to run a module...
    Нужен для запуска модуля.
    '''
    print(__doc__)
    address = "read/libs/{0}.py".format(tmp[0])
    print(address)
    if(not check_file("work/lib.py")):
        old_address = cuting(address)[0]
    else:
        while(check_file("drow/" + str(iterabl) + ".py")):
            iterabl += 1
        cuting(address, "drow/" + str(iterabl) + ".py")
        old_address = address
        if(not check_file("work/lib.py")):
            old_address = cuting(address)[0]
        else:
            # ~ exit()
            pass
    try:
        from work import lib
        lib = reload(lib)
        lib.main_m(tmp)
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
        old_address = cuting(address)[0]
    else:
        while(check_file("drow/" + str(iterabl) + ".py")):
            iterabl += 1
        cuting(address, "drow/" + str(iterabl) + ".py")
        old_address = address
        if(not check_file("work/lib.py")):
            old_address = cuting(address)[0]
        else:
            # ~ exit()
            pass
    try:
        from work import lib
        lib = reload(lib)
        lib.info_m()
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
    finally:
        if(check_file("work/lib.py")):
            cuting("work/lib.py", old_address)
    pass
def help_modul_cut(tmp):
    address ="read/libs/{0}.py".format(tmp[1])
    print(address)


    if(not check_file("work/lib.py")):
        old_address = cuting(address)[0]
    else:
        while(check_file("drow/" + str(iterabl) + ".py")):
            iterabl += 1

        cuting(address, "drow/" + str(iterabl) + ".py")

        old_address = address

        if(not check_file("work/lib.py")):
            old_address = cuting(address)[0]
        else:
            # ~ exit()
            pass
    try:
        from work import lib
        print(1)
        lib = reload(lib)
        print(1)
        lib.help_m()
        print(1)
        print("The attempt to start the module was successful! :D")
    except:
        print("Error when importing a module or launching it.. :C")
    finally:
        if(check_file("work/lib.py")):
            cuting("work/lib.py", old_address)
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
                help_modul_cut(tmp)
        my_list = [".info", ".i"] # print info to me
        if (tmp[0] in my_list):
            if (len(tmp) <= 1):
                print(__doc__)
            else:
                info_modul_cut(tmp)
        my_list = [".sys", ".s"]
        if (tmp[0] in my_list):
            pass
    else:
        start_modul_cut(tmp)
    pass
def start_file(address = "read/libs/index.terminal", c=""):
    print(end=c)
    if(not check_file(address)):
        pass
    else:
        f = open(address, "r")
        for l in f:
            if(l !="\n" and l !=" " and l !=""):
                started(l)
        f.close()
def start_me():
    while True:
        c = input("[root ~]$ ")
        if(c !="\n" and c !=" " and c !=""):
            started(c)
    pass

#import and start modul-file:
start_file()

#start console:
start_me()
