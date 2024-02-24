import tkinter as tk
import os

def ejecutar_script(script_folder):
    script_path = os.path.join(script_folder, "code{}.py".format(script_folder[-1]))
    os.system("python {}".format(script_path))

def main():
    root = tk.Tk()
    root.title("Ejecutar Scripts")

    # Funciones para llamar a los scripts
    def llamar_script_1():
        ejecutar_script("script_1")

    def llamar_script_2():
        ejecutar_script("script_2")

    def llamar_script_3():
        ejecutar_script("script_3")

    # Botones para llamar a los scripts
    btn_script_1 = tk.Button(root, text="Script 1", command=llamar_script_1)
    btn_script_1.pack()

    btn_script_2 = tk.Button(root, text="Script 2", command=llamar_script_2)
    btn_script_2.pack()

    btn_script_3 = tk.Button(root, text="Script 3", command=llamar_script_3)
    btn_script_3.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
