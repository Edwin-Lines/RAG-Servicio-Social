text=""
fileDirectory ='main3.cpp' #Cambiar por el directorio en donde se encuentre el main.cpp
with open(fileDirectory, encoding="utf-8") as f:
    text+=f.readline()[:-1].replace('\\','\\\\').replace('"','\\"')
    for linea in f:
        text+='\\n'+linea[:-1].replace('\\','\\\\').replace('"','\\"')
with open('resultado.txt', "w") as f:
    f.write(text)
#print(text)