import os
import random

def inicio_sesion():
    email = input("Email: ")
    password = input("Contraseña: ")
    usuarios = guardar_usuario()
    for usuario in usuarios: 
        print(usuario)
        if usuario['email'] == email and usuario['password'] == password:
            return True
    return False

def crear_usuario(): 

    elegir_rol = random.randint(-2,2)
    if elegir_rol > 0: 
        rol = 'user'
    else: 
        rol = 'admin'
    coinciden = False
    while coinciden == False: 
        email = input("Email: ")
        password = input("Password: ")
        ver_password = input("Repite el password: ")
        if password == ver_password: 
            coinciden = True
        elif password != ver_password: 
            print("Las contraseñas no coinciden")
    # w reescribe sobre todo el archivo (write)
    # a agrega al final del archivo el nuevo texto (append) 
    archivo = open("usuarios.txt", 'a')
    lista_usuarios = guardar_usuario()
    # checar el último usuario, tomar su id, convertirlo a entero para sumarle 1 
    # El resultado de este proceso es el id del nuevo usuario. 
    ultimo_usuario = lista_usuarios[-1] # regresa el último elemento de la lista 
    # {id:, email:, password:, rol:}
    id_anterior = int(ultimo_usuario['id'])
    id_actual = id_anterior + 1
    usuario_nuevo = f"{id_actual},{email},{password},{rol}"
    archivo.write('\n') # Salto de linea 
    archivo.write(usuario_nuevo)
    print("BIENVENIDO, ", email)

def eliminar_usuario():
    # abrir el archivo en modo w 
    # eliminar usuario por correo o id 
    # guardar usuarios para tomar lista de los usuarios, buscar al usuario deseado 
    # Pueden recorrer la lista de usuarios con for i in range(len(lista de usuarios)), la 'i' es el índice del elemento actual
    # de la lista
    # Borrar al usuario de la lista. 
    # Imprimir la nueva lista en el archivo de texto. 
    lista_usuarios = guardar_usuario()
    salir = False
    while salir == False:
        print("Elige una opción del menú")
        print("1. Eliminar por id")
        print("2. Eliminar por correo")
        print("3. Salir")
        opcion = input("opcion: ")
        opcion = opcion.upper()
        if opcion == '3' or opcion == 'salir': 
            salir = True
        elif opcion == '2' or opcion == 'ELIMINAR POR CORREO': 
                eliminar_por_email(lista_usuarios)
        elif opcion == '1' or opcion == 'ELIMINAR POR ID': 
                eliminar_por_id(lista_usuarios)
        else: 
            print("Introduzca una opción válida")
    pass
def eliminar_por_id(lista_usuarios):
    existe_usuario = False
    id_usuario = input("Id del usuario a eliminar: ")
    for i in range(len(lista_usuarios)): 
        if lista_usuarios[i]['id'] == id_usuario: 
            existe_usuario = True
            lista_usuarios.pop(i)
            break
    if existe_usuario == False: 
        print("No se encontró al usuario")
    else: 
        print("Usuario eliminado")
    
    print(lista_usuarios)

def eliminar_por_email(lista_usuarios): 
    existe_usuario = False
    email_usuario = input("Email del usuario a eliminar: ")
    for i in range(len(lista_usuarios)): 
        if lista_usuarios[i]['email'] == email_usuario: 
            existe_usuario = True
            lista_usuarios.pop(i)
            break
    if existe_usuario == False: 
        print("No se encontró al usuario")
    else: 
        print("Usuario eliminado")
    print(lista_usuarios)

def guardar_usuario(): 
    archivo = open("usuarios.txt", 'r')
    dict_usuario = {}
    lista_usuarios = []
    for linea in archivo.readlines():
        dict_usuario = {}
        usuario = linea.split(',') #Regresa una lista
        dict_usuario['id'] = usuario[0]
        dict_usuario['email'] = usuario[1]
        dict_usuario['password'] = usuario[2]
        dict_usuario['rol'] = usuario[3]
        lista_usuarios.append(dict_usuario)
    archivo.close()
    return(lista_usuarios)

def main(): 
    elegir = True
    while elegir==True:
        print("Elige una opción del menú: ")
        print("1. Iniciar sesion")
        print("2. Registrarte")
        print("3. Salir")
        
        opcion = input("opción: ")
        opcion = opcion.upper()

        if opcion == '1' or opcion == 'INCIAR SESION': 
            existe = inicio_sesion()
            if existe == True: 
                pass #abrir juego
        elif opcion == '2' or opcion == 'REGISTRARTE': 
            crear_usuario()
        elif opcion == '3' or opcion == 'SALIR': 
            print("ADIOS!")
            elegir = False
        else: 
            print("POR FAVOR ELIGE UNA OPCIÓN VÁLIDA")

main()