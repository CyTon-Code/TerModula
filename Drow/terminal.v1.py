user_data = [
"root" # name
,"!auto_password" # password
,"" # список ошибок, если строка не пустая то выход с любого цикла или функции
#при начале... Error_list
,"[root ~]$ " # hi
]
import os
os.system       (r"libs/usr.py")
import subprocess
subprocess.Popen(r"libs/usr.py", shell=True)
import subprocess
subprocess.call(r" libs/usr.py", shell=True)
import subprocess
cmd = 'python /home/cytoncode/projects/Terminal.beta/libs/usr.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = p.communicate()
result = out.split(' ')
for lin in result:
	   if not lin.startswith('#'):
		   print(lin)
# ~ lang_text = []
def user():
	from libs import usr

def lang(command):
	"""
	my flags: -en, -ru, -default / -def / -d, -ua / uk
	"""
	if (command == "-en"):
		pass
	elif (command == "-ru"):
		pass
	elif (command == "-default" or command == "-def" or command == "-d"):
		pass
	elif (command == "-ua" or command == "-uk"):
		pass
	print(command)
def start():
	from libs import lib

def slover(stringer):
	"""
	я Преобразовываю текст в слова. покачто отделяю по пробелам и по новым
	 строкам.
	"""
	result = []
	slovo = ""
	stringer += " "
	for i in stringer:
		if (i == " " or i == "\n"):
			if (slovo != "" and "\n" not in slovo and " " not in slovo):
				result.append(slovo)
			slovo = ""
		else:
			slovo += i
	return result


def rezak(command, n):
	slovo = ""
	i = 0
	for j in command:
		if (i >= n):
			break
		slovo += j
		i+=1
	return slovo



while True:
	command = input(user_data[3]).lower()
	# ~ print(slover(command))
	# ~ print(rezak(command, 5))

	try:
		slover(command)[1]
	except:
		command += " _"

	# ~ print(slover(command))
	if   (".lang" == rezak(command, 5) or ".l" == rezak(command, 2)):
		lang(slover(command)[1])
	elif (".user" == rezak(command, 5) or ".u" == rezak(command, 2)):
		usr(slover(command))
	elif (".help" == rezak(command, 5) or ".h" == rezak(command, 2)):
		#вызывает список модулей в наличии
		pass
	elif (".info" == rezak(command, 5) or ".i" == rezak(command, 2)):
		pass
		# вместо того чтобы вызвать main? вызывает его документацию.
	elif (".quit" == rezak(command, 5) or ".q" == rezak(command, 2)):
		exit()
	# ~ break
