if __name__ == "__main__":
    print("I am is Module!!!")
    print("Bye Bye!!!")
    # Exited elce not importing-выход если не импорт.
    exit()
def info_m():
    print("""""")
def help_m():
    print("""""")
def main_m(address):
    if type(address) != str:
        raise ErrorTypeParam
    print("Check file:", address)
    try:
        fff = open(address, "r")
        print(end=address+" существует!")
        try:
            fff.read()
            print(" И читабелен!")
            return True  # File defined, bud and reading.
        except:
            print(" И не читабелен!")
            # ~ print("-a:", address)
            return False # File defined, bud not reading.
    except:
        print(address, "не существует или не открывается!")
        # ~ print("-a:", address)
        return False # file is not defined.
    finally:
        try:
            fff.close()
        except:
            pass
    pass
def error_m(tmp):
    print("""modul: check is errored!""")
pass
