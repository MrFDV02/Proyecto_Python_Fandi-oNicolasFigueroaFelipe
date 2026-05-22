from modules.core import login, menu_principal
from modules.messages import MENSAJE_BIENVENIDA


print(MENSAJE_BIENVENIDA)
usuario = None
while not usuario:
    usuario = login()
menu_principal(usuario)