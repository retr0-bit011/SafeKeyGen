# SafeKeyGen
SafeKeyGen es una herramienta desarrollada en python que genera contraseñas seguras de una longitud mínima de 20 caracteres.
## Instalación
1.  Clona este repositorio:
   ```bash
   git clone https://github.com/retr0-bit011/SafeKeyGen.git
```
2. Navega hasta el directorio
   ````bash
   cd SafeKeyGen
   ````
3. Corre el script
   ````bash
   python3 SafeKeyGen.py
   ````
## Modo de Uso
1. Para modo interativo
   ````bash
   python3 SafeKeyGen.py
   ````
   Sigue las intrucciones.
2. Para argumentos por línea de comando
   Ejemplo de uso: 
   ````bash
   python SafeKeyGen.py -l 25 -n 3 -f
   ````
   -l : longitud de contraseña (por defecto 20)
   -n : numeros de contraseñas a generar
   -f : mostrar fortaleza de la contraseña
## Requisitos
 -Python 3.6 o superior
- Módulos estándar de Python (no se requieren instalaciones adicionales)
  
