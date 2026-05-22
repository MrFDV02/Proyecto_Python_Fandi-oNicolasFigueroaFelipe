from modules.utils import cargar_datos, guardar_datos
    
def buscar_usuario(email, contraseña):
    datos = cargar_datos()
    for usuario in datos["usuarios"]:
        if usuario ["email"] == email and usuario["contraseña"] == contraseña:
            return usuario
    return None

def registrar_usuario(id, Nombres, Apellidos, Telefono, email, direccion, contraseña, rol):
    datos = cargar_datos()
    for usuario in datos["usuarios"]:
        if usuario["id"] == id:          
            return "El ID ya está registrado."
        if usuario["email"] == email:
            return "El email ya está registrado."
        
    nuevo_usuario = {
        "id": id,
        "Nombres": Nombres,

        
        "Apellidos": Apellidos,
        "Telefono": Telefono,
        "email": email,
        "direccion": direccion,
        "contraseña": contraseña,
        "rol": rol
    }
    
    datos["usuarios"].append(nuevo_usuario)  
    guardar_datos(datos)                      
    return "Usuario registrado exitosamente." 


def eliminar_usuario(id):
    datos = cargar_datos()
    for usuario in datos["usuarios"]:
        if usuario["id"] == id:
            datos["usuarios"].remove(usuario)
            guardar_datos(datos)
            return "Usuario eliminado exitosamente."
    return "Usuario no encontrado."
    

def actualizar_usuario(id, Nombres, Apellidos, Telefono, email, direccion, contraseña, rol):
    datos = cargar_datos()
    for usuario in datos["usuarios"]:
        if usuario["id"] == id:
            usuario["Nombres"] = Nombres
            usuario["Apellidos"] = Apellidos
            usuario["Telefono"] = Telefono
            usuario["email"] = email
            usuario["direccion"] = direccion
            usuario["contraseña"] = contraseña
            usuario["rol"] = rol
            guardar_datos(datos)
            return "Usuario actualizado exitosamente."
    return "Usuario no encontrado."