data = ""
with open("program.txt") as f:
	data = f.read()

data2 = data.split(chr(10))
codepy = ""

for i,d in enumerate(data2):
	o = d.split(" ")
	s = False
	for j,b in enumerate(o):
		l = True
		if f'"{b}"' == b:
			codepy += f'"<STREND><THING1>{b.replace("<THING1>","")}"'
			print("stwing without that uwu")
			s = not s
			l = False
		elif '"' in b:
			s = not s
			if not s:
				codepy += "<THING1>"
			codepy += '"'
			if s:
				codepy = codepy.replace("<STREND>","")
				codepy += "<STREND>"
				codepy = codepy.replace("<THING1>","")
				codepy += "<THING1>"
		if not s:
			if "joined" == b:
				if o[j+1] == "with":
					codepy+="+"
			elif "plus" == b:
				#if o[j+1] == "with":
				codepy+="+"
			elif "parsed" == b:
				if o[j+1] == "as":
					if o[j+2] == "a" or o[j+2] == "an":
						#if o[j+3] == "string":
						#codepy += ')'
						if o[j+3] == "equation":
							codepy = f'{codepy[:codepy.find("<STREND>")-1]}eval({codepy[codepy.find("<STREND>")-1:].replace("<STREND>","")})'
						elif o[j+3]=="variable":
							codepy = codepy[:codepy.find("<STREND>")-1]+codepy[codepy.find("<STREND>")-1:].replace("<STREND>","").replace("<THING1>","").replace('"',"")
						else:
							codepy = f'{codepy[:codepy.find("<STREND>")-1]}{o[j+3].replace("ing","").replace("eger","")}({codepy[codepy.find("<STREND>")-1:].replace("<STREND>","")})'
			elif "(without" == b:
				if o[j+1] == "quotes)":
					codepy = codepy.replace('<THING1>',"")
			elif "Display" == b:
				if "console" in o:
					codepy+="print("
			elif "." in b:
				codepy += ")"
			elif "Ask" == b:
				codepy+="<METHOD>input("
			elif "saving" == b:
				if "it" == o[j+1]:
					if "as" == o[j+2]:
						codepy = codepy.replace("<METHOD>",f'{o[j+3]} = ')
			#elif "" == b:
			#	
			elif "set" == b:
				if "to" == o[j+2]:
					codepy = codepy.replace("<STREND>",f'{o[j+1]} = ').replace("<METHOD>",f'{o[j+1]} = ')
			elif "==>" == b:
				if "<==" in o:
					codepy = f'{codepy[:codepy.find("<STREND>")-1]}exec({codepy[codepy.find("<STREND>")-1:].replace("<==","").replace("==>","").replace("<STREND>","")})'
		else:
			codepy += " "+b.replace("\"","")
		print(codepy)
		if not l:
			s = not s
	codepy += chr(10)

with open("program.py","w") as f:
	f.write(codepy.replace("<STREND>","").replace("<METHOD>","").replace("<THING1>","\\\""))
