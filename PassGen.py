import random
import string
import argparse
from typing import List

class GeneradorContraseñas:
    def __init__(self):
        self.caracteres_ambiguos = 'l1I0O|'  # Caracteres que pueden confundirse
        self.caracteres_seguros = self._filtrar_caracteres()
    
    def _filtrar_caracteres(self) -> str:
        """Filtra caracteres ambiguos para evitar confusiones"""
        todos_caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(c for c in todos_caracteres if c not in self.caracteres_ambiguos)
    
    def generar_contraseña(self, longitud: int = 20) -> str:
        """Genera una contraseña segura con composición mínima garantizada"""
        if longitud < 8:
            raise ValueError("La longitud mínima debe ser de 8 caracteres")
        
        # Componentes obligatorios
        componentes = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Resto de caracteres
        componentes.extend(random.choice(self.caracteres_seguros) for _ in range(longitud - 4))
        
        # Mezclar y unir
        random.shuffle(componentes)
        return ''.join(componentes)
    
    def generar_varias(self, cantidad: int = 5, longitud: int = 20) -> List[str]:
        """Genera múltiples contraseñas seguras"""
        return [self.generar_contraseña(longitud) for _ in range(cantidad)]
    
    def calcular_fortaleza(self, contraseña: str) -> float:
        """Calcula un puntaje de fortaleza (0-1)"""
        puntaje = 0.0
        
        # Longitud
        puntaje += min(len(contraseña) / 40, 0.3)  # Máximo 30% por longitud
        
        # Diversidad de caracteres
        categorias = 0
        if any(c.isupper() for c in contraseña): categorias += 1
        if any(c.islower() for c in contraseña): categorias += 1
        if any(c.isdigit() for c in contraseña): categorias += 1
        if any(c in string.punctuation for c in contraseña): categorias += 1
        puntaje += categorias * 0.15  # Máximo 60% por diversidad
        
        # Entropía aproximada
        caracteres_unicos = len(set(contraseña))
        puntaje += min(caracteres_unicos / len(contraseña), 0.1)  # Máximo 10%
        
        return min(puntaje, 1.0)
    
    def mostrar_fortaleza(self, contraseña: str) -> str:
        """Muestra una representación visual de la fortaleza"""
        puntaje = self.calcular_fortaleza(contraseña)
        barras = int(puntaje * 10)
        return f"Fortaleza: [{'█' * barras}{'░' * (10 - barras)}] {int(puntaje * 100)}%"

def interfaz_linea_comandos():
    """Maneja la interfaz por línea de comandos"""
    parser = argparse.ArgumentParser(description='Generador de Contraseñas Seguras')
    parser.add_argument('-l', '--longitud', type=int, default=20, help='Longitud de la contraseña')
    parser.add_argument('-n', '--numero', type=int, default=1, help='Número de contraseñas a generar')
    parser.add_argument('-f', '--fortaleza', action='store_true', help='Mostrar fortaleza de la contraseña')
    args = parser.parse_args()
    
    generador = GeneradorContraseñas()
    
    if args.numero > 1:
        contraseñas = generador.generar_varias(args.numero, args.longitud)
        print("\n".join(contraseñas))
    else:
        contraseña = generador.generar_contraseña(args.longitud)
        print(f"\nContraseña generada: {contraseña}")
        
        if args.fortaleza:
            print(generador.mostrar_fortaleza(contraseña))

def interfaz_interactiva():
    """Interfaz interactiva simple para usuarios"""
    generador = GeneradorContraseñas()
    
    print("\n=== Generador Interactivo de Contraseñas ===")
    longitud = int(input("Longitud deseada (8-50, default 20): ") or 20)
    cantidad = int(input("Número de contraseñas a generar (default 1): ") or 1)
    
    if cantidad > 1:
        print("\nGenerando contraseñas...\n")
        contraseñas = generador.generar_varias(cantidad, longitud)
        for i, pwd in enumerate(contraseñas, 1):
            print(f"{i}. {pwd} - {generador.mostrar_fortaleza(pwd)}")
    else:
        contraseña = generador.generar_contraseña(longitud)
        print(f"\nContraseña generada: {contraseña}")
        print(generador.mostrar_fortaleza(contraseña))
    
    print("\n¡Listo! Recuerda guardar tus contraseñas de forma segura.")

def main():
    try:
        # Si se pasan argumentos, usar CLI, sino interfaz interactiva
        if len(sys.argv) > 1:
            interfaz_linea_comandos()
        else:
            interfaz_interactiva()
    except Exception as e:
        print(f"\n⚠️ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()
