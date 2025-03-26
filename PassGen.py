import random
import string

def generar_contraseña(longitud_minima=10):
    # Caracteres que se pueden usar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Asegurarse de que la contraseña tenga al menos la longitud mínima
    longitud = max(longitud_minima, 20)
    
    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

def guardar_contraseña(contraseña, titulo):
    # Crear un archivo txt con la contraseña
    with open(f"{titulo}.txt", "w") as archivo:
        archivo.write(contraseña)
    print(f"Contraseña guardada en '{titulo}.txt'.")

def main():
    # Generar una contraseña segura
    contraseña = generar_contraseña()
    print(f"Contraseña generada: {contraseña}")
    
    # Preguntar al usuario si desea guardar la contraseña
    guardar = input("¿Deseas guardar esta contraseña? (s/n): ").strip().lower()
    
    if guardar == 's':
        # Pedir un título para el archivo
        titulo = input("Ingresa un título para el archivo (sin extensión): ").strip()
        guardar_contraseña(contraseña, titulo)
    else:
        print("Contraseña no guardada.")

if __name__ == "__main__":
    main()