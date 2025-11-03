import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Instituto de Formación Docente y Técnica N° 28 Anexo 328 - Norberto De La Riestra")
        self.root.geometry("1024x600")
        self.root.resizable(False, False)
        
        # Centrar la ventana
        self.center_window()
        
        # Configurar el estilo
        self.root.configure(bg='#2c3e50')
        
        # Crear el título principal
        title_label = tk.Label(
            self.root,
            text="EXPO 328",
            font=("Arial", 24, "bold"),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=30)
        
        # Crear el subtítulo
        subtitle_label = tk.Label(
            self.root,
            text="Selecciona un juego para jugar:",
            font=("Arial", 14),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        subtitle_label.pack(pady=10)
        
        # Crear el frame para los botones
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=30)
        
        # Botón para Snake Game
        snake_button = tk.Button(
            button_frame,
            text="SNAKE",
            font=("Arial", 16, "bold"),
            bg='#27ae60',
            fg='white',
            width=15,
            height=2,
            command=self.launch_snake,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        snake_button.pack(pady=10)
        
        # Botón para Tetris Game
        tetris_button = tk.Button(
            button_frame,
            text="TETRIS",
            font=("Arial", 16, "bold"),
            bg='#e74c3c',
            fg='white',
            width=15,
            height=2,
            command=self.launch_tetris,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        tetris_button.pack(pady=10)
        
        
        pong_button = tk.Button(
            button_frame,
            text="PONG 1 VS 1",
            font=("Arial", 16, "bold"),
            bg="#e4e73c",
            fg='white',
            width=15,
            height=2,
            command=self.launch_pong,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        pong_button.pack(pady=10)
        
        brick_button = tk.Button(
            button_frame,
            text="BRICK BREAKER",
            font=("Arial", 16, "bold"),
            bg="#5b65ec",
            fg='white',
            width=15,
            height=2,
            command=self.launch_brick,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        brick_button.pack(pady=10)
        
        # Botón para salir
        exit_button = tk.Button(
            button_frame,
            text="SALIR",
            font=("Arial", 12),
            bg='#95a5a6',
            fg='white',
            width=10,
            height=1,
            command=self.exit_app,
            relief='raised',
            bd=2,
            cursor='hand2'
        )
        exit_button.pack(pady=20)
        
        # Información sobre controles
        controls_label = tk.Label(
            self.root,
            font=("Arial", 10),
            fg='#7f8c8d',
            bg='#2c3e50',
            justify='center'
        )
        controls_label.pack(side='bottom', pady=10)
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 5) - (height // 5)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def launch_snake(self):
        """Ejecuta el juego Snake"""
        try:
            # Ocultar la ventana principal temporalmente
            self.root.withdraw()
            
            # Ejecutar el juego Snake
            subprocess.run([sys.executable, "snake_game.py"], check=True)
            
            # Mostrar la ventana principal nuevamente
            self.root.deiconify()
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "No se pudo ejecutar el juego Snake")
            self.root.deiconify()
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo snake_game.py")
            self.root.deiconify()
    
    def launch_tetris(self):
        """Ejecuta el juego Tetris"""
        try:
            # Ocultar la ventana principal temporalmente
            self.root.withdraw()
            
            # Ejecutar el juego Tetris
            subprocess.run([sys.executable, "tetris_game.py"], check=True)
            
            # Mostrar la ventana principal nuevamente
            self.root.deiconify()
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "No se pudo ejecutar el juego Tetris")
            self.root.deiconify()
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo tetris_game.py")
            self.root.deiconify()
    
    def launch_pong(self):
        """Ejecuta el juego Pong"""
        try:
            
            self.root.withdraw()
            
            
            subprocess.run([sys.executable, "pong_game.py"], check=True)
            
            
            self.root.deiconify()
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "No se pudo ejecutar el juego Pong")
            self.root.deiconify()
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo pong_game.py")
            self.root.deiconify()
    
    def launch_brick(self):
        """Ejecuta el juego Brick Breaker"""
        try:
            
            self.root.withdraw()
            
            
            subprocess.run([sys.executable, "brick_breaker_game.py"], check=True)
            
            
            self.root.deiconify()
            
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "No se pudo ejecutar el juego Brick Breaker")
            self.root.deiconify()
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo brick_breaker_game.py")
            self.root.deiconify()
    
    def exit_app(self):
        """Cierra la aplicación"""
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()

def main():
    """Función principal"""
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
