#4
#Main 
import Usuario
import Funciones
import Administrador

user_cliente = ""
pin_cliente = ""
rol_cliente = ""

print("    🍿 ¡BIENVENIDO A CINEMATIC! 🍿    ")

while True:
    print("1. Iniciar sesión")
    print("2. Crear cuenta nueva")
    print("3. Cerrar programa")
    print("-" * 40)
    
    opcion_inicio = input("Seleccione una opción para empezar: ").strip()
    print('')

    if opcion_inicio == "1":
        # Ejecuta el login
        
        exito, rol = Usuario.iniciar_sesion(user_cliente, pin_cliente, rol_cliente)
        if exito:
            if rol == "administrador":
                Administrador.menu_administrador()
            elif rol == "cliente":
                Funciones.menu_cliente(user_cliente)
                
    elif opcion_inicio == "2":

        user_cliente, pin_cliente, rol_cliente = Usuario.registrar_usuario()
        print("Ya puedes iniciar sesión.")
        print('')
        
    elif opcion_inicio == "3" or opcion_inicio.upper() == "SALIR":
        print("Apagando servidores de Cinematic...")
        print("¡Que pases una buena noche de películas! 🎬🍿 Bye!")
        break
    else:
        print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
        print("-" * 40)