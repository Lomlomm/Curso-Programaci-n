import os 
import random 
from main_space import game_loop
def inicio_sesion(): 
    rol = ''
    email = input("Email: ")
    # str 
    password = input("Contraseña: ")
    # int(input("lo que le queramos pedir: "))
    lista_usuarios = crear_lista_usuarios()
    for usuario in lista_usuarios: 
        # usuario = {id:,email:,contraseña:,rol:,}
        if usuario['email'] == email and usuario['password'] == password: 
            rol = usuario['rol'].upper()
            return True, rol
    '''if existe == True:
        print("Bienvenido")
    else: 
        print("Las credenciales son incorrectas") 
    '''
    return False, rol


def crear_lista_usuarios(): 
    # w -> write - sobreescribe sobre todo el archivo 
    # r -> read 
    # a -> append - agrega lo que le mandes al final del archivo 
    archivo = open("usuarios.txt", "r")
    dict_usuario = {}
    lista_usuario = []
    for linea in archivo.readlines(): 
        usuario = linea.split(",") # regresa una lista de los elementos sin el separador 
        dict_usuario['id'] = usuario[0]
        dict_usuario['email'] = usuario[1]
        dict_usuario['password'] = usuario[2]
        dict_usuario['rol'] = usuario[3]
        # {id:,email:,contraseña:,rol:,}
        lista_usuario.append(dict_usuario)
        dict_usuario = {}
    
    return lista_usuario
def registrar_usuario():
    elegir_rol = random.randint(-2, 2)
    if elegir_rol > 0: 
        rol = 'admin'
    else: 
        rol = 'user'
    verificar = False 
    email = input("Email: ")
    while verificar == False: 
        password = input("Password: ")
        ver_password = input("Repite password: ")
        if password == ver_password: 
            verificar = True
        else: 
            print("Las contraseñas no coinciden")
    lista_usuarios = crear_lista_usuarios()
    id_usuario = sacar_id(lista_usuarios)
    texto = f"{id_usuario},{email},{password},{rol}"
    archivo = open("usuarios.txt", 'a')
    archivo.write("\n")
    archivo.write(texto)
    print("USUARIO AÑADIDO")



def sacar_id(lista_usuarios): 
    usuario_anterior = lista_usuarios[-1]
    id_usuario_anterior = int(usuario_anterior['id'])
    id_actual = id_usuario_anterior + 1
    return id_actual

def sobreescribir_archivo(lista_usuarios): 
    nueva_lista = []
    for usuario in lista_usuarios: 
        linea = f"{usuario['id']},{usuario['email']},{usuario['password']},{usuario['rol']}"
        nueva_lista.append(linea)
    archivo = open("usuarios.txt", "w")
    archivo.writelines(nueva_lista)

def eliminar_usuario_menu(): 
    lista_usuarios = crear_lista_usuarios()
    repite = True
    while repite == True:
        print("Selecciona una opción del menú: ")
        print("1.- Eliminar por ID")
        print("2.- Eliminar por Email")
        print("3.- Salir")
        opcion = input("Opcion: ")
        if opcion == '1' or opcion.upper() == 'ELIMINAR POR ID': 
            id_usuario = input("ID del usuario a eliminar: ")
            lista_usuarios = eliminar_por_id(id_usuario, lista_usuarios)
            sobreescribir_archivo(lista_usuarios)
        elif opcion == '2' or opcion.upper() == 'ELIMINAR POR EMAIL': 
            email_usuario = input("Email del usuario a eliminar: ")
            lista_usuarios = eliminar_por_email(email_usuario, lista_usuarios)
            sobreescribir_archivo(lista_usuarios)
        elif opcion == '3' or opcion.upper() == 'SALIR': 
            repite = False
        else: 
            print("Elige una opción válida")


def eliminar_por_id(id_usuario, lista_usuarios): 
    for i in range(len(lista_usuarios)): 
        if lista_usuarios[i]['id'] == id_usuario: 
            lista_usuarios.pop(i)
            break
    return lista_usuarios

def eliminar_por_email(email_usuario, lista_usuarios): 
    for i in range(len(lista_usuarios)): 
        if lista_usuarios[i]['email'] == email_usuario: 
            lista_usuarios.pop(i)
            break
    return lista_usuarios

def menu_admin(): 
    repite = True
    while repite: 
        print("Elige una opción del menú")
        print("1. Eliminar usuario")
        print("2. Jugar")
        print("3. Cambiar contrasenia")
        print("4. Salir")
        opcion = input("Opcion: ")
        opcion = opcion.upper()
        if opcion == '1' or opcion == 'ELIMINAR USUARIO': 
            eliminar_usuario_menu()
        elif opcion == '2' or opcion =='JUGAR': 
            game_loop()
        elif opcion == '3' or opcion =='CAMBIAR CONTRASENIA': 
            cambiar_contrasenia()
        elif opcion == '4' or opcion == 'SALIR': 
            break
        else: 
            print("Elige una opción válida")

def menu_usuario(): 
    repite = True
    while repite: 
        print("Elige una opción del menú")
        print("1. Cambiar contraseña")
        print("2. Jugar")
        print("3. Salir")
        opcion = input("Opcion: ")
        opcion = opcion.upper()
        if opcion == '1' or opcion == 'CAMBIAR CONTRASEÑA': 
            cambiar_contrasenia()
        elif opcion == '2' or opcion =='JUGAR': 
            game_loop()
        elif opcion == '3' or opcion == 'SALIR': 
            break
        else: 
            print("Elige una opción válida")

def checar_correo(): 
    existe = False
    lista_usuarios = crear_lista_usuarios()
    email = input("Introduce tu correo electrónico: ")
    for i, usuario in enumerate(lista_usuarios): 
        # Pensar en los posibles baches que puede tener esta condición (may, min)
        if usuario['email'] == email: 
            existe = True
            break
    return existe, lista_usuarios, i

def cambiar_contrasenia(): 
    existe, lista_usuarios, indice = checar_correo()
    verificar = False
    #Recordar qué hace esta condición
    if existe: 
        while verificar == False: 
            password = input("New password: ")
            ver_password = input("Repite password: ")
            if password == ver_password: 
                verificar = True
            else: 
                print("Las contraseñas no coinciden")
            lista_usuarios[indice]['password'] = password
            sobreescribir_archivo(lista_usuarios)
    else: 
        print("Correo electrónico introducido no es un usuario")

def main(): 
    # 1. inicio sesion, 2. registrarte, 3. eliminar usuario 
    # Que se repita el menu hasta que el usuario ingrese una opción válida
    repite = True
    while repite == True: 
        print("ELIGE UNA OPCIÓN DEL MENÚ")
        print("1. Iniciar sesion")
        print("2. Registrarte")
        print("3. Salir")
        opcion = input("opcion: ")

        opcion = opcion.upper() #lo pone en mayúsculas 

        if opcion == 'INICIAR SESION' or opcion == '1':
            existe_usuario, rol = inicio_sesion()
            if existe_usuario: 
                print("bienvenido")
                print(rol)
                if rol == 'ADMIN\n': 
                    menu_admin()
            else: print("Credenciales inválidas")

        elif opcion == 'REGISTRARTE' or opcion == '2': 
            registrar_usuario()
        elif opcion == 'SALIR' or opcion == '3': 
            repite = False
        else: 
            print("Opción inválida")

main()