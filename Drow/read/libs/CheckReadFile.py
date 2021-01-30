if __name__ == "__main__":
    print("I am is Module!!!")
    print("Bye Bye!!!")
    # If not imported,i exit is the module.
    exit()
def info_m():
    __doc__ = """Pattern:
CheckReadFile -a terminal/""
terminal/ - неполный адресс неявно начинается в родительской папке.
"""
    print(__doc__)
    pass
pass
def help_m():
    __doc__ = """"""
    print(__doc__)
    pass
pass
def main_m(address_file):
    address_file = input("address file: ") # "read/terminals/index.terminal"
    # ~ address_file = tmp[1] # "read/terminals/index.terminal"
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
        print(".Module not defined. Modul:", address_file)
        return False # ответ: файла нет или его не прочитано.
    finally:
        try:
            f.close() # обьязательно нужно закрыть файл, если еще не.
        except:
            print(".File is Error. Error is not defined.") # если
            #попасть в это место, то файл нельзя закрыть.. Читая: файл
            #изчез или нельзя закрыть.
            return False
        # закрылся файл(функция сама это сделает).
    pass
pass
def error_m(tmp):
    pass
pass
