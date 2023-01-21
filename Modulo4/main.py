import os
import main_space
def crear_usuario():
    pass
def iniciar_sesion():
    email = input("Email: ")
    password = input("Contraseña: ")
    lista_usuarios = guardar_usuarios()
    for usuario in lista_usuarios: 
        if usuario['email'] == email and usuario['contraseña'] == password: 
            return True
    return False
def cerrar_sesion(): 
    pass
def baja_usuario(): 
    pass
def guardar_usuarios():
    file = open('usuarios.txt', 'r')
    dict_usuario = {}
    lista_usuarios = []
    for line in file.readlines(): 
        dict_usuario = {}
        # Me regresa una lista con los valores sin las comas
        usuario = line.split(',')
        dict_usuario['id'] = usuario[0]
        dict_usuario['email'] = usuario[1]
        dict_usuario['contraseña'] = usuario[2]
        dict_usuario['rol'] = usuario[3]
        lista_usuarios.append(dict_usuario)
    return lista_usuarios
def menu_admin(): 
    print("Elige una opción del menú")
    print("1. Eliminar usuario")
    print("2. Jugar")
    opcion = input("Opcion: ")
    opcion = opcion.upper()
    if opcion == '1' or 'ELIMINAR USUARIO': 
        baja_usuario()
def main(): 
    repite = True
    while repite == True:
        print("Elige una opción del menú")
        print("1. Iniciar sesion")
        print("2. Registrarte")
        print("3. Salir")
        opcion = input("Opcion: ")
        opcion = opcion.upper()
        inicio_sesion = False
        if opcion == '1' or 'INICIAR SESION': 
            inicio_sesion = iniciar_sesion()
            if inicio_sesion == True: 
                main_space.game_loop()
            else: 
                print("USUARIO INCORRECTO")
        if opcion == '2' or 'REGISTRARTE': 
            crear_usuario()
        if opcion == '3' or 'SALIR': 
            repite = False

