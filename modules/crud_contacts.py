from modules.messages import CONTACTO_AGREGADO_EXITOSO
from modules.utils import cargar_datos, guardar_datos
    
def registrar_contacto(id, Nombres, Apellidos, Telefono, email, direccion, tipo, notas ):
    

    datos = cargar_datos()
    for contacto in datos["contactos"]:
        if contacto["id"] == id:
            return "El ID ya está registrado."
        
    nuevo_usuario = {
        "id": id,
        "Nombres": Nombres,
        "Apellidos": Apellidos,
        "Telefono": Telefono,
        "email": email,
        "direccion": direccion,
        "tipo": tipo,
        "notas": notas
            }
    
    datos["contactos"].append(nuevo_usuario)
    guardar_datos(datos)
    return CONTACTO_AGREGADO_EXITOSO

def listar_contactos():
    datos = cargar_datos()
    return datos["contactos"]

def buscar_contacto(termino):
    datos = cargar_datos()
    resultados = []
    termino = termino.lower().strip()
    for contacto in datos["contactos"]:
        completo_nombre = f"{contacto['Nombres']} {contacto['Apellidos']}".lower()
        if (termino == str(contacto["id"]) or termino in completo_nombre or termino in contacto["tipo"].lower()): resultados.append(contacto)
    return resultados



def actualizar_contacto (id, Nombres, Apellidos, Telefono, email, direccion, tipo, notas ):
    datos = cargar_datos()
    for contacto in datos["contactos"]:
        if contacto["id"] == id:
            contacto["Nombres"] = Nombres
            contacto["Apellidos"] = Apellidos
            contacto["Telefono"] = Telefono
            contacto["email"] = email
            contacto["direccion"] = direccion
            contacto["tipo"] = tipo
            contacto["notas"] = notas
            guardar_datos(datos)
            return "Contacto actualizado exitosamente."
    return "Contacto no encontrado."

def eliminar_contacto(id):
    datos = cargar_datos()
    for contacto in datos["contactos"]:
        if contacto["id"] == id:
            datos["contactos"].remove(contacto)
            guardar_datos(datos)
            return "Contacto eliminado exitosamente."
    return "Contacto no encontrado."


def buscar_contacto_por_id(id):
    datos = cargar_datos
    for contacto in datos["contactos"]:
        if contacto ["id"] == id:
            return contacto
    return None

