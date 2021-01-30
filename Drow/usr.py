user_data = [
    "root" # name
    ,"!auto_password" # password
    ,"" # список ошибок, если строка не пустая то выход с любого цикла или функции при начале... Error_list
    ,"[root ~]$ " # hi
]
def reflesh(tmp):
    user_data = tmp

def info():
    print("""
    user
    """, user_data)
# ~ dream(".usr", .user -name root -pasword !auto_pasword -lang EN -no_auto_pasword);-auto_pasword or -no_auto_pasword, -default
def dream(command):
    process = " "
    for i in command:
        if (".u" == (i[0] + i[1])):
            info()
        if (i == "-no_auto_pasword"):
            #if (i != "_"):
            #    pass
            #else:
            #    continue
            pass
        elif (i == "-auto_pasword"):
            if ("!" in i):
                pass
            else:
                user_data[1] += "!"
        elif (i == "-no_auto_pasword"):
            if(user_data[1][0] == "!"):
                process = user_data[1] # please enter you new pasword...
                while True:
                    process = input("Enter you new pasword: ")
                    if (process == user_data[1]):
                        print("the password remains the same")
                    elif (process[0] == "!"):
                        print("the password remains the same")
                    elif (process != ""  and process[0] != "."):
                        user_data[1] = process
                        break
            else:
                print("the password remains the same")
        # ~ else:#if: default
        elif (i == "-default"):
            user_data[0] = "root"
            user_data[1] = "!auto_password"
            user_data[2] = ""
            user_data[3] = "[root ~]$ "
        if (process == "-pasword"):
            if (i != "_"):
                if( "!" not in i):
                    user_data[1] = i
                else:
                    pass
            else:
                continue
        elif (process == "-lang"):
            if(i != "_"):
                pass
            else:
                continue
        elif (process == "-name"):
            if(i != "_"):
                user_data[0] = i
            else:
                continue
        # ~ elif (process == )
        if (i[0] == "-"):
            process = i
        else:
            process = " "
dream([".user", "-name", "admin", "-pasword", "auto_pasord", "-lang",
 "EN", "-auto_pasword"])
info()
