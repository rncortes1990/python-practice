# Ejercicio 3
# Utilizando como base el ejercicio de los personajes que hicimos,
# en este ejercicio tendrás que crear un gestor de personajes gestor.py 
# para añadir y borrar la información de los siguientes personajes:

# Vida	Ataque	Defensa	Alcance
# Caballero	4	2	4	2
# Guerrero	2	4	2	4
# Arquero	2	4	1	8
# Deberás hacer uso del módulo pickle y todos los cambios que realices se irán 
# guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistirán.

# Crea dos clases, una Personaje y otra Gestor.
import pickle,copy
class Personaje:
    def __init__(self,nombre):
        self.nombre=nombre
class Gestor:
    def __init__(self):
        self.personajes=self.cargar_archivo()
    def validar_existencia(self,nombre):
        for personaje in self.personajes:
            if nombre == personaje['nombre'].upper():
                raise Exception("Ya existe un {}".format(nombre))
            else:
                pass
    def eliminar_personaje(self,nombre):
        try:
            fichero = open("personajes.pckl","rb")
            for idx,personaje in enumerate(self.personajes):
                if personaje["nombre"].upper() == nombre.upper():
                   self.personajes.remove(personaje)
        except Exception:
            pass
        else:
            pass
        finally:
            fichero.close()

    def guardar_personaje(self,personaje):
        try:
            fichero = open("personajes.pckl","wb")
            if(type(self.personajes) is not None):
                self.validar_existencia(personaje.nombre.upper())
            if(personaje.nombre.upper()=="arquero".upper()):
                el = {'nombre':personaje.nombre.upper(),'vida':2, 'ataque':4, 'defensa': 1 ,'alcance':8 }
            elif(personaje.nombre.upper()=="caballero".upper()):
                el = {'nombre':personaje.nombre.upper(),'vida':4, 'ataque':2, 'defensa': 4, 'alcance':2 }
            elif(personaje.nombre.upper()=="guerrero".upper()):
                el = {'nombre':personaje.nombre.upper(),'vida':2, 'ataque':4, 'defensa': 2, 'alcance':4 }
            else:
                raise Exception("Debe elegir entre [arquero,guerrero,caballero]")
        except Exception as err:
            print(err)
        else:
            self.personajes.append(el)
            pickle.dump(self.personajes,fichero)
            fichero.close()
    def cargar_archivo(self):
        try:
            fichero = open("personajes.pckl","ab+")
            fichero.seek(0)
            data = pickle.load(fichero)
            fichero.close()
            personajes = data.copy()
        except TypeError as err:
            print("Error tipo :{} ".format(err))
        except EOFError as err:
            print("Archivo vacio o inexistente")
            fichero = open("personajes.pckl","wb")
            pickle.dump([],fichero)
            fichero.close()
            return []
        except Exception as err:
            print("Error :{} ".format(type(err).__name__))
        else:
            return personajes


g = Gestor()
g.guardar_personaje(Personaje("futbolista"))
g.guardar_personaje(Personaje("caballEro"))
g.guardar_personaje(Personaje("arquero"))
g.guardar_personaje(Personaje("guerrero"))
g.eliminar_personaje("caballEro")
g.eliminar_personaje("arquero")
g.eliminar_personaje("guerrero")
g.guardar_personaje(Personaje("futbolista"))

print(g.personajes)

# La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase), 
# y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).
# Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, 
# mostrarlos y borrarlos (a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo), 
# además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente.
# En caso de que el personaje ya exista en el Gestor entonces no se creará.
# Una vez lo tengas listo realiza las siguientes prueba en tu código:

# Crea los tres personajes de la tabla anterior y añádelos al Gestor.
# Muestra los personajes del Gestor.
# Borra al Arquero.
# Muestra de nuevo el Gestor.