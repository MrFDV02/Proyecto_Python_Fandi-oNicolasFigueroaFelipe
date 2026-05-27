import os
import json
import time

from modules.utils import cargar_datos, guardar_datos, borrar_pantalla, pausar_pantalla
from modules.messages import *
from modules.crud_users import buscar_usuario, registrar_usuario, eliminar_usuario, actualizar_usuario, buscar_usuario_por_id
from modules.crud_contacts import registrar_contacto, listar_contactos, buscar_contacto, actualizar_contacto, eliminar_contacto, buscar_contacto_por_id
from modules.auditoria import auditar_datos


borrar_pantalla()
def login():
    print(LOGIN_SESION)
    
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    usuario = buscar_usuario(email, contraseña)
    if usuario:
        borrar_pantalla()
        return usuario
    else:
        borrar_pantalla()
        print(ERROR_LOGIN)
        pausar_pantalla()
        borrar_pantalla()
        return None

def menu_principal(usuario):
    while True:
        opcion = input(MENU_PRINCIPAL)
        borrar_pantalla()
        if opcion == "1":
            print(LETRERO_AGREGAR)
            try:
                id = str(int(input("Ingrese el ID del contacto a actualizar: ")))
            except ValueError:
                borrar_pantalla()
                print(LETRERO_AGREGAR)
                print("El ID debe ser un número. Por favor, ingrese un ID válido.")
                pausar_pantalla()
                borrar_pantalla()
                continue
            crear_contacto = cargar_datos()
            ids_existentes = [c["id"] for c in crear_contacto["contactos"]]
            if id in ids_existentes:
                print("El ID ya está registrado.")
                pausar_pantalla()
                borrar_pantalla()
            else:
                Nombres = input("Ingrese los nombres: ")
                Apellidos = input("Ingrese los apellidos: ")
                Telefono = input("Ingrese el teléfono: ")
                email = input("Ingrese el email: ")
                direccion = input("Ingrese la dirección: ")
                tipo = input("Ingrese el tipo de contacto: ")
                notas = input("Ingrese las notas: ")
                resultado = registrar_contacto(id, Nombres, Apellidos, Telefono, email, direccion, tipo, notas)
                borrar_pantalla()
                print(resultado)
                pausar_pantalla()
                borrar_pantalla()

        elif opcion == "2":
            borrar_pantalla()
            print(MENSAJE_CONTATOS)
            contactos = listar_contactos()
            if contactos:
                print(f"{'ID':<10} {'Nombres':<15} {'Apellidos':<15} {'Telefono':<15} {'Email':<20} {'Tipo':<10} {'Notas':<5}")
                print("-" * 105)
                for contacto in contactos:
                    print(f"{contacto['id']:<10} {contacto['Nombres']:<15} {contacto['Apellidos']:<15} {contacto['Telefono']:<15} {contacto['email']:<20} {contacto['tipo']:<10} {contacto['notas']:<5}")
            else:
                print("No hay contactos registrados.")
            pausar_pantalla()
            borrar_pantalla()

        elif opcion == "3":
            borrar_pantalla()
            print (MENSAJE_BUSCADOR)
            contacto = input("Ingrese el ID, nombre, apellido o tipo del contacto a buscar: ")
            if not contacto: 
                print("ERROR: Debe escribir algo para buscar.")
                pausar_pantalla()
                borrar_pantalla()  
            else:
                print(MENSAJE_BUSCADOR)
                resultados = buscar_contacto(contacto)
                borrar_pantalla()

                if resultados:
                    print(MENSAJE_BUSCADOR)
                    print(f"{'ID':<10} {'Nombres':<15} {'Apellidos':<15} {'Telefono':<15} {'Email':<20} {'Tipo':<10} {'Notas':<20}")
                    print("-" * 105)
                    for contacto in resultados: 
                        print(f"{contacto['id']:<10} {contacto['Nombres']:<15} {contacto['Apellidos']:<15} {contacto['Telefono']:<15} {contacto['email']:<20} {contacto['tipo']:<10} {contacto['notas']:<20}")
                        pausar_pantalla()

                else:
                    print(MENSAJE_BUSCADOR)
                    print("No se encontraron contactos que coincidan con la búsqueda.")
                    pausar_pantalla()
                    borrar_pantalla()

        elif opcion == "4":
            print(LETRERO_ACTUALIZAR)
            try:
                id = str(int(input("Ingrese el ID del contacto a actualizar: ")))
            except ValueError:
                borrar_pantalla()
                print(LETRERO_ACTUALIZAR)
                print("El ID debe ser un número. Por favor, ingrese un ID válido.")
                pausar_pantalla()
                borrar_pantalla()
                continue
            contacto_encontrado = buscar_contacto_por_id(id)
            if contacto_encontrado:
                borrar_pantalla()
                print(f"Contacto encontrado: {contacto_encontrado['Nombres']} {contacto_encontrado['Apellidos']}")
                print("-" * 40)
                Nombres = input("Ingrese los nuevos nombres: ")
                Apellidos = input("Ingrese los nuevos apellidos: ")
                Telefono = input("Ingrese el nuevo teléfono: ")
                email = input("Ingrese el nuevo email: ")
                direccion = input("Ingrese la nueva dirección: ")
                tipo = input("Ingrese el nuevo tipo de contacto: ")
                notas = input("Ingrese las nuevas notas: ")
                resultado = actualizar_contacto(id, Nombres, Apellidos, Telefono, email, direccion, tipo, notas)
                borrar_pantalla()
                print(resultado)
                pausar_pantalla()
                borrar_pantalla()
            else:
                borrar_pantalla()
                print(LETRERO_ACTUALIZAR)
                print("Contacto no encontrado.")
                pausar_pantalla()
                borrar_pantalla()

        elif opcion == "5":
            print(LETRERO_BORRAR)
            id = input("Ingrese el ID del contacto a eliminar: ")
            confirmar = input(ELIMINACION_CONFIRMAR)
            if confirmar == "s":
                borrar_pantalla()
                resultado = eliminar_contacto(id) 
                borrar_pantalla()
                print(CONTACTO_ELIMINADO)
                print(resultado)  
                pausar_pantalla()
                borrar_pantalla()   
            else:
                borrar_pantalla()
                print(ADVERTENCIA)
                pausar_pantalla()
                borrar_pantalla()

        elif opcion == "6":
            if usuario["rol"] == "administrador":
                while True:
                    subopcion = input(MENU_USUARIOS)
                    borrar_pantalla()
                    if subopcion == "1":
                        borrar_pantalla()
                        try:
                            id = str(int(input("Ingrese el ID del usuario a registrar: ")))
                        except ValueError:
                            print("El ID debe ser un número. Por favor, ingrese un ID válido.")
                            continue
                        usuario_encontrado = buscar_usuario_por_id(id)
                        if usuario_encontrado:
                            borrar_pantalla()
                            print("|| El ID ya está registrado. ||")
                            pausar_pantalla()
                            borrar_pantalla()
                        else:
                            nombres = input("Ingrese los nombres: ")
                            apellidos = input("Ingrese los apellidos: ")
                            telefono = input("Ingrese el teléfono: ")
                            email = input("Ingrese el email: ")
                            direccion = input("Ingrese la dirección: ")
                            rol = input("Ingrese el rol (admin/operario): ")
                            while rol not in ["admin", "operario"]:
                                print("El rol debe ser 'admin' u 'operario'.")
                                rol = input("Ingrese el rol (admin/operario): ")
                            contraseña = input("Ingrese la contraseña: ")
                            resultado = registrar_usuario(id, nombres, apellidos, telefono, email, direccion, contraseña, rol)
                            borrar_pantalla()
                            print(resultado)
                            pausar_pantalla()
                            borrar_pantalla()
                    elif subopcion == "2":
                        borrar_pantalla()
                        try:
                            id = str(int(input("Ingrese el ID del usuario a actualizar: ")))
                        except ValueError:
                            print("El ID debe ser un número. Por favor, ingrese un ID válido.")
                            continue
                        usuario_encontrado = buscar_usuario_por_id(id)
                        if usuario_encontrado:
                            borrar_pantalla()
                            print(f"Usuario encontrado: {usuario_encontrado['Nombres']} {usuario_encontrado['Apellidos']}")
                            print("-" * 40)
                            nombres = input("Ingrese los nuevos nombres: ")
                            apellidos = input("Ingrese los nuevos apellidos: ")
                            telefono = input("Ingrese el nuevo teléfono: ")
                            email = input("Ingrese el nuevo email: ")
                            direccion = input("Ingrese la nueva dirección: ")
                            contraseña = input("Ingrese la nueva contraseña: ")
                            rol = input("Ingrese el nuevo rol: ")
                            while rol not in ["admin", "operario"]:
                                print("El rol debe ser 'admin' u 'operario'.")
                                rol = input("Ingrese el nuevo rol: ")
                            resultado = actualizar_usuario(id, nombres, apellidos, telefono, email, direccion, contraseña, rol)
                            borrar_pantalla()
                            print(resultado)
                            pausar_pantalla()
                            borrar_pantalla()
                        else:
                            print("Usuario no encontrado.")
                            pausar_pantalla()
                            borrar_pantalla()
                    elif subopcion == "3":
                        borrar_pantalla()
                        id = input("Ingrese el ID del usuario a eliminar: ")
                        confirmar = input(ELIMINACION_CONFIRMAR)
                        if confirmar == "s":
                            resultado = eliminar_usuario(id)
                            borrar_pantalla()
                            print(resultado)
                            pausar_pantalla()
                            borrar_pantalla()
                        else:
                            print("|| Eliminación cancelada. ||")
                            pausar_pantalla()
                            borrar_pantalla()
                    elif subopcion == "0":
                        borrar_pantalla()
                        print("Regresando al menú principal...")
                        pausar_pantalla()
                        borrar_pantalla()
                        break
                    else:
                        borrar_pantalla()
                        print(MENU_USUARIOS)
                        print("Opción no válida.")
                        pausar_pantalla()
                        borrar_pantalla()
            else:
                borrar_pantalla()
                print(ACCESO_DENEGADO)
                pausar_pantalla()
                borrar_pantalla()

        elif opcion == "0":          
            print(CERRAR_SESION)
            print("      [WAIT] Desconectando núcleo...")
            time.sleep(1)
            print("      [ OK ] Contactos guardados.")
            time.sleep(0.5)
            print("      [OFF] Sistema fuera de línea.")
            time.sleep(1)
            exit() 

        elif opcion == "7":
            print(LETRERO_AUDITORIA)
            auditar_datos()
            pausar_pantalla()
            borrar_pantalla()

        else:
            borrar_pantalla()                      
            print("Opción no válida. Por favor, ingrese una opción del menú.")
            pausar_pantalla()
            borrar_pantalla()