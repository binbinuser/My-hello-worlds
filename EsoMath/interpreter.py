import math

variables = {}
functions = {}

data = ""
vars = "x y z n a b c d e f g h i j k l m o p q r s t u v w".split(" ")



with open('program.lang') as f:
	data = f.read()

#def sentence(a):
	#return "".join([chr(math.floor(variables[a]/i%1*10000)) for i in [10^floor((len(str(a))-1)/j) for j in range(len(str(a))-1)]])
	#b = ""
	#for i in range(len(variables[a])/5):
	#	b+=chr(math.floor(i/100000))
	#return 



data = data.replace(chr(13),chr(10))
data2 = data.split(chr(10))

for i in data2:
	if '//' in i:
		functions[i[:i.find("//")]] = i[i.find("//")+2:]
	elif '=' in i:
		variables[i[:i.find("=")]] = i[i.find("=")+1:]
	elif '~' in i:
		fun = functions[i[:i.find(" ")]]
		for j in i[i.find(" ")+1:i.find("~")].split(","):
			e = j.split(":")
			fun = fun.replace(e[0],variables[e[1]])
		variables[i[i.find("~")+1:]] = eval(fun)
	elif '@' in i:
		#print(sentence(i[1:]))
		n = ""
		for j in i.replace('@','').split(","):
			n += chr(int(variables[j]))
		print(n)
	elif '|' in i:
		fun = i[i.find('|')+1:]
		for j in variables:
			fun = fun.replace(j,str(variables[j]))
		variables[i[:i.find("|")]] = eval(fun)
	elif len(i) > 0:
		print(f"{variables[i]:,}")
