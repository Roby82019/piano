import tkinter as tk
import pygame

class Piano:
    def __init__(self, root):
        self.root = root
        self.root.title("Piano de 31 Teclas")
        
        # Inicializar pygame para reproducir sonido
        pygame.mixer.init()

        # Definir las notas musicales
        self.notas = [
            "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4",  # Octava 4
            "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5",  # Octava 5
            "C6", "C#6", "D6", "D#6", "E6"  # Parte de la octava 6
        ]

        # Crear el teclado de piano
        self.crear_teclado()

    def crear_teclado(self):
        # Colores de las teclas
        teclas_blancas = ["C", "D", "E", "F", "G", "A", "B"]
        teclas_negras = ["C#", "D#", "F#", "G#", "A#"]
        
        # Posiciones relativas de las teclas negras
        posicion_tecla_negra = {"C#": 1, "D#": 2, "F#": 4, "G#": 5, "A#": 6}

        # Crear botones para las teclas blancas y negras
        row = 0
        for i, nota in enumerate(self.notas):
            if any(nota.startswith(t) for t in teclas_blancas):
                boton = tk.Button(self.root, text=nota, width=5, height=10, bg="white", command=lambda n=nota: self.reproducir_nota(n))
                boton.grid(row=row, column=i, padx=1, pady=1)
            elif any(nota.startswith(t) for t in teclas_negras):
                pos = posicion_tecla_negra[nota.split("#")[0]]
                boton = tk.Button(self.root, text=nota, width=3, height=6, bg="black", fg="white", command=lambda n=nota: self.reproducir_nota(n))
                boton.grid(row=row, column=i - pos, padx=1, pady=1, sticky="n")

    def reproducir_nota(self, nota):
        archivo = f"notas/{nota}.mp3"  # Usar formato .mp3
        try:
            pygame.mixer.music.stop()  # Detener cualquier sonido anterior
            pygame.mixer.music.load(archivo)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error al reproducir {nota}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    piano = Piano(root)
    root.mainloop()
