# ~ res:
hi = "[root ~]$ "
# ~ def test():
    # ~ import start_2
# ~ import start_2
# ~ test()
# проверить есть ли файл:
def check_file(address_file = "index.txt"):
    '''
    нужен для чтения файла.
    '''

    try:
        f = open(address_file, 'r') # если ошибка, то: файла нет или его нельзя читать.
        return True # ответ: файл есть.
    except:
        return False # ответ: файла нет.
    finally:
        f.close() # обьязательно нужно закрыть файл, если не закрылся(функция сама это сделает).
#file_null = not check_file("t.txt")

# проверить на возможность редактировать:
def can_i_edit_the_file(address_file = "index.txt"):
    '''
    нужен для создания файла и записи.
    '''
    if(check_file(address_file)):
        res = "w"
        f = open(address_file, "r")
        res = fff.read()
        f.close()

def read_file(address, res=""):
    tmp = ""
    if(check_file(address)):
        ff = open(address)
        tmp = ff.read()
        ff.close()
    return tmp


def main_start():
    while True:
        command = input(hi)
        if ".quit"    in command:
            break
        elif "read"   in command:
            pass
        # ~ elif "write"  in command:
            # ~ pass
        elif "format" in command:
            pass
        elif "open"   in command:
            pass
        elif "set"    in command:
            pass
        elif ".usr"   in command:
            pass
        break





main_start()
# ~ #~/projects/Terminal.beta   [user set new open del]
# ~ .user -name root -pasword !auto_pasword -lang EN -no_auto_pasword;-auto_pasword or -no_auto_pasword, -default
# ~ set -if_file_null_other; -if_file_null_creat or -if_file_null_check
# ~ set -if_no_write_file_rename; or -if_no_write_file_try_again or -if_no_write_file_other
# ~ format -must_not_be "";
# ~ format -have_not_be "";
# ~ format -if_must_be_change_value "";
# ~ format -if_have_be_change_value "";
# ~ read -address "t.txt" -var tmp1
# ~ open -read -write -; -r -w -rw...
# ~ ;set -set address ;де розшташована утилита. - сет не будет ибо он отдельно для каждого палгина разный....
# ~ .info user
# ~ .help
# ~ .quit
# ~ ;#/\это все коментарии
# ~ ;"" - кавычки не обьязательны но нужны для сохранения пустого текста а также текста с пробелами и некоторыми символами.
# ~ ;() - скобки не обьязательны, но нужны для сохранения масива, пока что это не разрешается, но будет в have_not_be и must_not_be. пример: format -must_not_be ("", ""); в других если такое и будет, то только для того чтобы сохранить последний переззапсывая предедущие.... насчот скобок их можно будет испоьзовать и в реад.
