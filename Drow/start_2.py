"""
Данная программа понятна всем!
Программа поможет избежать большинство ошибок в работе с файлами!:-)
Также в коде вы найдете полезные функции:
  -редактирование файла.
  -удаление файла.
  -очистка файла.
  -запись в файл если он пустой.
  
"""
#packages = [] # масив с документациями функции иди всеъ функци	... или программы..
# name user:
name = "root"
pasword = "!auto_pasword" #несмотря на то какой бы нибыл пароль заходит
# автоматом. нельзя вводить пароль начиная с ! .
# defalult name:
hi = "[" + name + " ~]$ "   # приветствие перед каждой командой.

# ввод пароля:
def pasword_read():
    fff.open("pasword.txt")
    tmp = fff.read()
    fff.close()
    return tmp

# Настройки - случаи:

if_file_null_to_creat = True # Если файла нет, создать новый?

# Особые Значения:
must_not_be = "" # содержимое которому содержимое файла не должно быть
# равно.
if_must_be_change_value = "Hello, World!" # если must_not_be равен
# значению от содержимого файла, то изменить значение
# на if_must_be_change_value.

# Значения:
file_null = False # файла нет?
no_write_file = False # файл нельзя редактировать?

# проверить есть ли файл:
def check_file(address_file = "index.txt"):
    try:
        fff = open(address_file, 'r') # если ошибка, то: файла нет или его нельзя читать.
        return True # ответ: файл есть.
    except:
        return False # ответ: файла нет.
    finally:
        fff.close() # обьязательно нужно закрыть файл, если не закрылся(функция сама это сделает).
#file_null = not check_file("t.txt")


# проверить на возможность редактировать:
def can_i_edit_the_file(address_file = "index.txt"):
    if(check_file(address_file)):
        res = "w"
        fff = open(address_file, "r")
        res = fff.read()
        fff.close()




# вывод на екран:
#print(
#    "файл есть? -", check_file("t.txt"),
#    "\nфайла нет? -", file_null)


# res:
cmd_list = [".quit", ".usr", ".set", ".clr"]
cmd_list_usr = [".back", "name", "pasw", ".quit"]
cmd_list_set = [".back", "name", "pasw", ".quit"]
# usr: name, (no pasword)
# quit - выход
# set - изминение всех настроек
# clr - очичтить проводник - терминал.

# def Hello(List):
#     print(List)

# приветствие в начале команды:
def print_list(list_cmd):
    hello_world = "top command:"
    for i in list_cmd:
        hello_world += " " + i
    print(hello_world)
    return hello_world


def May_I_get_out(auto_cmd):
    auto_cmd = "click_auto: " + auto_cmd + "\ndefalult: Y\nY/N? "
    exit = input(auto_cmd).upper()
    if (exit[0] == "N"):
        return False
    return True
i = 0
print_list(cmd_list)
command = "start"
while True:
    if (command != cmd_list[0]):
        command = input(hi).lower()
    #command = input(hi).lower()
    if (i >= 5):
        if (May_I_get_out(cmd_list[0])):
            command = cmd_list[0]
        else:
            pass
        i = 0
    if (command == cmd_list[0]):
        break
    elif (command == cmd_list[1]):
        j = 0
        print_list(cmd_list_usr)
        command= ""
        while True:
            if (command != cmd_list_usr[0]):
                command = input(hi).lower()
            if (j >= 5):
                if (May_I_get_out(cmd_list_usr[0])):
                    command = cmd_list_usr[0]
                else:
                    pass
                j = 0
            if (command == cmd_list[0]):
                #command = cmd_list[0]
                break
            elif (command == cmd_list_usr[0]):
                print_list(cmd_list)
                break
            elif (command == cmd_list_usr[1]):
                command = name + " rename: "
                command = input(command)
                if (command != "" and command[0] != "."):
                    #new_hi(command)
                    name = command
                    hi = "[" + name + " ~]$ "
                command = cmd_list_usr[0]
            elif (command == cmd_list_usr[2]):
                while True:
                    if (pasword[0] != '!'):
                        command = input("Enter your pasword: ")
                        if (command == pasword):
                            break
                    else:
                        break
                command = input("Enter you new pasword: ")
                if (command == pasword):
                    print("the password remains the same")
                elif (command[0] == "!"):
                    print("the password remains the same")
                elif (command != ""  and command[0] != "."):
                    pasword = command
                command = cmd_list_usr[0]
            else:
                print(command)
            # cmd_list_usr = command

            # print(cmd_list_usr[1], "rename to", command)
            # hi = "[" + cmd_list_usr[1] + " ~]$ "   # приветствие перед каждой командой.
            # elif (command == cmd_list_usr[1]):
            #     while i

            # print("command:")
            j += 1
        pass
    else:
        print("not difinet to", command)
        i += 1 # потом придумать: добавлять если предедущий и эот были равны
print("\n[Terminat Exited]")






exit()

def f_read_creat (sources, tmp = ""):
     try:
          f = open(sources, "r")
          tmp = f.read()
     except:
          f = open(sources, "w")
          f.write(tmp)
     finally:
          f.close()
     return tmp
#  start_2.py
#  
#  Copyright 2020 CyTon Code <cytoncode@localhost.localdomain>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 


#f_read("in.txt")
