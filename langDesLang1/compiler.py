data = ""
#data2= data.split(chr(10))
#data2 = ["".join(i.split(chr(13))) for i in data2]
codepy =""

keywords = {'Def': 'procedure', 'If': 'granted', 'Else': 'unless', 'ElIf': 'stipulation', 'Try': 'attempt', 'Except': 'capture', 'Finally': 'eventually', 'Class': 'family', 'Import': 'accommodate', 'Not': 'opposite', 'While': 'during'}

kws = "<>==!+-%*^"
y = False
idntlvl = 0

def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key
    return "key doesn't exist"

with open("program.lang") as f:
  data = f.read().replace("    ","").replace(chr(13),chr(10))

data2= data.split(chr(10))
extrafun = []

def canbefloat(str):
  try:
    if float(str) == float(str):
      return True
  except:
    return False



for i,d in enumerate(data2):
  o = d.split(" ")
  s = False
  cmnt = False
  for j,b in enumerate(o):
    l = True
    m = b.replace('"',"")
    if b.count('"')>1:
      codepy += f'"<STREND><THING1>{b.replace("<THING1>","")}"'
      #print("stwing without that uwu")
      s = not s
      l = False
    elif '"' in b:
      s = not s
      #if not s:
      #codepy += "<THING1>"
      codepy += '"'
      if s:
        codepy = codepy.replace("<STREND>","")
        codepy += "<STREND>"
        #codepy = codepy.replace("<THING1>","")
        #codepy += "<THING1>"
    if not s:
      #if "joined" == b:
      #  if o[j+1] == "with":
      #    codepy+="+"
      #elif "plus" == b:
      #  #if o[j+1] == "with":
      #  codepy+="+"
      if "parsed" == b:
        if o[j+1] == "as":
          if o[j+2] == "a" or o[j+2] == "an":
            #if o[j+3] == "string":
            #codepy += ')'
            if o[j+3] == "equation":
              codepy = f'{codepy[:codepy.find("<STREND>")-1]}eval({codepy[codepy.find("<STREND>")-1:].replace("<STREND>","")})'
            elif o[j+3]=="variable":
              codepy =codepy[:codepy.find("<STREND>")-1]+codepy[codepy.find("<STREND>")-1:].replace("<STREND>","").replace("<THING1>","").replace('"',"")
            else:
              codepy = f'{codepy[:codepy.find("<STREND>")-1]}{o[j+3].replace("ing","").replace("eger","")}({codepy[codepy.find("<STREND>")-1:].replace("<STREND>","")})'
      #elif "print" == b:
      #  codepy+="print("
      #elif "ask" == b:
      #  codepy+="<METHOD>input("
      #elif "saving" == b:
      #  if "it" == o[j+1]:
      #    if "as" == o[j+2]:
      #      codepy = codepy.replace("<METHOD>",f'{o[j+3]} = ')
      #elif "" == b:
      #  
      elif "=" == b:
        #if "to" == o[j+2]:
        #if "<METHOD>" in d or "<STREND>" in d:
        #    codepy += d.replace("<STREND>",f'{o[j-1]} = ').replace("<METHOD>",f'{o[j+1]} = ')
        #else:
        #    codepy += f"{o[j-1].replace('$','')[:round(len(o[j-1])/2)]} = {d.replace('=','').replace(o[j-1],'')}"
        codepy+=" = "
      elif "==>" == b:
        if "<==" in o:
          codepy = f'{codepy[:codepy.find("<STREND>")-1]}exec({codepy[codepy.find("<STREND>")-1:].replace("<==","").replace("==>","").replace("<STREND>","")})'
      elif b in ["then","do"]:
        idntlvl+=1
        codepy+=":"
      elif b == "end":
        idntlvl-=1
      elif "$" in b:
        codepy+=b[1:]
      elif b in kws:
        codepy+=b
      elif b == keywords["If"]:
        codepy+="if "#+d.replace(keywords["If"],"").[:d.find("do")]#.replace("")
        y = True
      elif b == keywords["While"]:
        codepy+="while "#+d.replace(keywords["While"],"")[:d.find("do")]#.replace("")
        y = True
      elif b == keywords["Def"]:
        codepy+="def "#+d.replace(keywords["Def"],"")[:d.find("do")]#.replace("")
        extrafun.append(d[:d.find("(")])
        y = True
      elif b == keywords["Class"]:
        codepy+="class "#+d.replace(keywords["Class"],"")[:d.find("do")]#.replace("")
        y = True
      elif b == keywords["Import"]:
        codepy +="import "
        y = True
      elif canbefloat(b):
        codepy+=b
      elif "'" in b:
        s = True
        cmnt = True
      else:
        if b in keywords.values():#try:
          #random = keywords["e"]
          #r = {p for p in keywords if keywords  [p]==b}
          r = get_key(b, keywords)
          #codepy+= keywords.keys()[keywords.values().index(b)].lower()+" "
          codepy+= r.lower()+" "
        else:
          #abcs = ['abs','all','any','ascii','bin','bool','bytearray','bytes','callable','chr','classmethod','compile','complex','delatrr','dir','divmod','enumerate','eval','exec','filter','filter','float','format','getattr','globals','hasattr','hash','help','hex','id','isinstance','issubclass','iter','len','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','type','vars','_import_','print','input']
          for c in ['abs','all','any','ascii','bin','bool','bytearray','bytes','callable','chr','classmethod','compile','complex','delatrr','dir','divmod','enumerate','eval','exec','filter','filter','float','format','getattr','globals','hasattr','hash','help','hex','id','isinstance','issubclass','iter','len','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','type','vars','_import_','print','input']:
            if b[:b.find("(")] == c:
              codepy+=b+""
          for c in extrafun:
            if b[:b.find("(")] == c:
              codepy+=b
          if y:
            codepy+=b
            y = not y
       
    elif not cmnt:
      codepy += " "+b.replace("\"","")
      print("* == IN STR == *")
    print(codepy)
    if not l:
      s = not s
    #if cnd:
    #  codepy += replace("then",":")
  codepy += chr(10)+"".join(["  " for i in range(idntlvl)])
  #cmnt = False

with open("program.py","w") as f:
  f.write("""

#Type your extra code here.

#e.g., (remove string to add)

'''

from time import time

def binorpraan():
  return "binbinuser" if time()%2 < 1 else "praanpraanuser"

'''



"""+codepy.replace("<STREND>","").replace("<METHOD>","").replace("<THING1>","\\\"")+f"main()")
  print("Success!")

#BINPILER v1.2 ------ DO NOT REMOVE
#MADE USING BINBINUSER PROGRAMMING LANG DES - DON'T REMOVE
