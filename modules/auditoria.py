import re
import json

from modules.utils import cargar_datos

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def auditar_datos():
    datos = cargar_datos()
    
    campos_obligatorios_usuarios = ["id", "Nombres", "Apellidos", "Telefono", "email", "direccion", "contraseña", "rol"]
    
    usuarios_con_errores = []
    contactos_con_errores = []
    
    ids_usuarios_con_errores = set()
    ids_contactos_con_errores = set()

    for usuario in datos["usuarios"]:
        u_id = usuario.get("id")
        for campo in campos_obligatorios_usuarios:
            if campo not in usuario:
                usuarios_con_errores.append(f"El usuario {u_id} falta el campo {campo}")
                ids_usuarios_con_errores.add(u_id)
        
        if "Telefono" in usuario:
            try:
                int(usuario["Telefono"])    
            except ValueError:
                usuarios_con_errores.append(f"El telefono del usuario {u_id} no es un numero valido")
                ids_usuarios_con_errores.add(u_id)
        
        if "email" in usuario and not validar_email(usuario["email"]):
            usuarios_con_errores.append(f"El email del usuario {u_id} no es válido: {usuario['email']}")
            ids_usuarios_con_errores.add(u_id)

        roles_validos = ["admin", "operario"]
        if "rol" in usuario and usuario["rol"] not in roles_validos:
            usuarios_con_errores.append(f"El rol del usuario {u_id} no es valido: {usuario['rol']}")
            ids_usuarios_con_errores.add(u_id)

    campos_obligatorios_contactos = ["id", "Nombres", "Apellidos", "Telefono", "email"]
    tipos_validos = ["cliente", "proveedor", "contacto", "colaborador", "aliado", "personal", "otro"]

    for contacto in datos["contactos"]:
        c_id = contacto.get("id")
        c_email = contacto.get("email")
        for campo in campos_obligatorios_contactos:
            if campo not in contacto:
                contactos_con_errores.append(f"El contacto {c_id} con el email {c_email} falta el campo {campo}")
                ids_contactos_con_errores.add(c_id)
        
        if "Telefono" in contacto:
            try:
                int(contacto["Telefono"])
            except ValueError:
                contactos_con_errores.append(f"El telefono del contacto {c_id} con el email {c_email} no es valido")
                ids_contactos_con_errores.add(c_id)
        
        if "email" in contacto and not validar_email(contacto["email"]):
            contactos_con_errores.append(f"El email del contacto {c_id}  no es valido: {contacto['email']}")
            ids_contactos_con_errores.add(c_id)
            
        if "tipo" in contacto and contacto["tipo"] not in tipos_validos:
            contactos_con_errores.append(f"El tipo de contacto {c_id} con email {c_email} no es valido: {contacto['tipo']}")
            ids_contactos_con_errores.add(c_id)

    reporte_final = {
        "lista_usuarios_usuarios_con_errores": usuarios_con_errores,
        "lista_contactos_contactos_con_errores": contactos_con_errores,
        "resumen_auditoria": {
            "total_usuarios": len(datos.get("usuarios", [])),   
            "total_contactos": len(datos.get("contactos", [])),
            "usuarios_con_errores": len(ids_usuarios_con_errores),
            "contactos_con_errores": len(ids_contactos_con_errores),
            "usuarios_con_email_duplicado": 0,
            "contacto_con_id_duplicado": 0
        }
    }

    with open("reporte_auditoria_datos.json", "w", encoding="utf-8") as reporte:
        json.dump(reporte_final, reporte, indent=4) 

    if len(usuarios_con_errores) == 0 and len(contactos_con_errores) == 0:
        print("Auditoria finalizada: No se encontraron errores")
    else:
        print("Auditoria finalizada: Se encontraron errores. Revisa el archivo reporte_auditoria_datos.json")