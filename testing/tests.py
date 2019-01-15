import pyxample as pyx

pyx.set("test", "testval1") #Insertamos string
print(pyx.get("test"))

pyx.set("testNum", 23) #Insertamos numero
print(pyx.get("testNum"))
pyx.increment("testNum") #Incrementamos el valor
print(pyx.get("testNum"))
pyx.decrement("testNum") #Decrementamos el valor
print(pyx.get("testNum"))
