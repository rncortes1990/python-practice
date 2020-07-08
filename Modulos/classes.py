from collections import Counter
l=[1,2,3,4,5,6,7,8,9,8,7,6,5,6,7,6,5,6,7,6,5,4,3,2,1,2,3,2,3,4,5]
nombres = Counter(["nico","josefa","josefa","Diego","josefa","nico"])
s = sum(l[1:])
print(s)
print(Counter(l))
c= Counter(l)
cc=Counter(" ".join(nombres).split())
#####################
print(c.items())
print(cc.items())
print(cc.most_common(1))
print(cc.most_common(2))
print(cc.most_common(3))
print(cc.keys())
print(cc.values())
###################
from collections import namedtuple
Persona = namedtuple('Persona','nombre apellido edad')
persona = Persona(nombre="nico",apellido="cortes",edad=29)
print(persona.nombre)
print(persona[0])