### Código Python con Menú Desplegable:

```python
import tkinter as tk
from tkinter import ttk
import os

def ejecutar_script(script):
    script_path = os.path.join("scripts", script)
    os.system("python {}".format(script_path))

def ejecutar_seleccion():
    script_seleccionado = combo_scripts.get()
    if script_seleccionado:
        ejecutar_script(script_seleccionado)

def main():
    root = tk.Tk()
    root.title("Ejecutar Scripts")

    # Lista de nombres de scripts
    scripts = os.listdir("scripts")

    # Crear combo box para seleccionar script
    combo_scripts = ttk.Combobox(root, values=scripts, state="readonly")
    combo_scripts.pack(pady=10)

    # Botón para ejecutar el script seleccionado
    btn_ejecutar = tk.Button(root, text="Ejecutar", command=ejecutar_seleccion)
    btn_ejecutar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
```

### README:

#### Ejecutar Scripts con Interfaz Gráfica

Este repositorio contiene dos archivos importantes:

1. **main.py**: Este archivo contiene el código Python para una interfaz gráfica simple que te permite seleccionar y ejecutar scripts ubicados en la carpeta `scripts`.

2. **scripts/**: Esta carpeta contiene los scripts que pueden ser ejecutados desde la interfaz gráfica. Cada script debe seguir el formato de nombre `codeX.py`, donde `X` es un número que identifica al script.

### Uso:

1. **Instalación de Dependencias:**

   Asegúrate de tener instalado Python en tu sistema. Para ejecutar la interfaz gráfica, necesitarás tener instalada la biblioteca `tkinter` de Python. Si no la tienes instalada, puedes instalarla utilizando pip:

   ```
   pip install tk
   ```

2. **Ejecutar la Interfaz Gráfica:**

   Para ejecutar la interfaz gráfica, simplemente ejecuta el archivo `main.py` desde la línea de comandos:

   ```
   python main.py
   ```

3. **Seleccionar y Ejecutar un Script:**

   Una vez que la interfaz gráfica se haya abierto, verás un menú desplegable con los nombres de los scripts disponibles en la carpeta `scripts`. Selecciona el script que deseas ejecutar y haz clic en el botón "Ejecutar".

   El script seleccionado se ejecutará y podrás ver la salida en la consola.

### Estructura de Carpetas y Archivos:

```
mi_programa/
│   main.py
│
└── scripts/
    │   code1.py
    │   code2.py
    │   code3.py
    │   ...
```

En la carpeta `scripts`, puedes colocar todos los scripts que deseas ejecutar desde la interfaz gráfica. Asegúrate de seguir el formato de nombres `codeX.py`, donde `X` es un número que identifica al script.

### Notas:

- Este código proporciona una forma sencilla de ejecutar scripts desde una interfaz gráfica en lugar de ejecutarlos directamente desde la línea de comandos.
  
- Si necesitas agregar más scripts, simplemente colócalos en la carpeta `scripts` con el formato de nombre adecuado, y la interfaz gráfica los reconocerá automáticamente en la lista desplegable.

- Puedes personalizar y extender este código según tus necesidades. Por ejemplo, podrías agregar funcionalidades adicionales a los scripts o mejorar la interfaz gráfica con más elementos como botones, etiquetas, etc.

Espero que esto te sea útil. Si tienes alguna pregunta o necesitas más ayuda, no dudes en contactarme. ¡Gracias por utilizar este código!
