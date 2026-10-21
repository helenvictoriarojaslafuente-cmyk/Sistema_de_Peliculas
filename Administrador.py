#3
#Administrador
import Funciones

def menu_administrador():
    while True: 
        print("    PANEL DE CONTROL - ADMINISTRADOR    ") 
        print("1. Ver catálogo de películas completo, 2. Agregar nuevo título o estreno, 3. Revisar el buzón de sugerencias, 4. Cerrar sesión")
        opcion = input("Seleccione una opción de gestión: ").strip()
        
        if opcion == "1":
            print("    CATÁLOGO EN SERVIDORES    ")
            for p in Funciones.peliculas:
                datos = Funciones.peliculas[p]
                if datos[1] <= 2026:
                    print(f" Peliculas {p} ({datos[1]}) - Género: {datos[0]} | Calificación: {datos[2]}Estrellas")
                else:
                    print(f" Peliculas [ESTRENO] {p} ({datos[1]}) - Género: {datos[0]}")
                
        elif opcion == "2":
            nueva = input("Nombre de la película: ").strip()
            cat = input("Género cinematográfico: ").strip().capitalize()
            try:
                año = int(input("Año de lanzamiento/estreno: "))
                
                if año <= 2026:
                    estrellas = 5 
                else:
                    estrellas = 0 
                
                if nueva and cat:
                    Funciones.peliculas[nueva] = [cat, año, estrellas]
                    print(f"¡La película '{nueva}' ({año}) fue dada de alta exitosamente!")
                else:
                    print("No se permiten campos vacíos.")
            except ValueError:
                print("El año debe ser un número entero válido.")
                
        elif opcion == "3":
            print("  PROPUESTAS RECIBIDAS DE CLIENTES  ")
            if len(Funciones.sugerencias_usuarios) == 0:
                print("El buzón se encuentra vacío por el momento.")
            else:
                contador = 1
                for sug in Funciones.sugerencias_usuarios: 
                    print(f"{contador}. {sug}")
                    contador = contador + 1
                    
        elif opcion == "4":
            print("Saliendo del módulo administrativo...")
            break
        else:
            print("Opción inválida.")