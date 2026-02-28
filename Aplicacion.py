#constructor
class Cliente:
    def __init__(self):
       self. __id = 0
       self.__nombre = None
       self.__apellido = None
       self.__sexo = None
       self.__direccion = None
       self.__telefono = 0
    #get
    def get_id(self)->int:
        return self.__id
    def get_nombres(self)->str:
        return self.__nombre()
    def get_apellidos(self)->str:
        return self.__apellido()
    def get_sexo(self)->str:
        return self.__sexo()
    def get_direccion(self)->str:
        return self.__direccion()
    def get_telefono(self):
        return self.__telefono
    #set
    def set_id(self,id):
        self.__id = id
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_id(self,apellido):
        self.__apellido = apellido
    def set_id(self,sexo):
        self.__sexo = sexo
    def set_id(self,direccion):
        self.__direccion = direccion
    def set_id(self,telefono):
        self.__telefono = telefono
    #proceso
    def esmujer(self)->bool:
        return self.__sexo == "f" or self.__sexo == "F"
    def leer (self):
        self.__nombre = input("nombre:")
        self.__apellido = input("apellido:")
        self.__sexo = input("sexo:")
        self.__direccion = input("direccion:")
        self.__telefono = input("telefono:")
    def mostrar(self):
        print("nombre:", self.__nombre, "apellido:", self.__apellido, "sexo", self.__sexo, "direcion", self.__direccion,"telefono:", self.__telefono)

#nodo
class NodoCliente:
    def __init__(self):
        self.__dato = Cliente()
        self.__dirsig = NodoCliente()
    #get
    def get_dato(self)->Cliente:
        return self.__dato
    def get_dirsig(self)->NodoCliente:
        return self.__dirsig
    #set 
    def set_dato(self,dato:Cliente):
        self.__dato = dato
    def set_dirsig(self,dirsig:NodoCliente):
        self.__dirsig = dirsig    