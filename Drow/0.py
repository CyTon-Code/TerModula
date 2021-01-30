from read.libs import lib
lib.main(["asdad", "sda"])
fff = open("read/libs/lib.py")
tmp = fff.read()
fff.close()
fff = open("read/libs/open.py")
tm = fff.read()
fff.close()
fff = open("read/libs/lib.py", 'w')
fff.write(tm)
fff.close()
from importlib import reload
lib = reload(lib)
from read.libs import lib
lib = reload(lib)
fff = open("read/libs/lib.py", 'w')
fff.write(tmp)
fff.close()
lib.main(["asdad", "sda"])
lib = reload(lib)
from read.libs import lib
lib = reload(lib)

lib.main(["asdad", "sda"])
