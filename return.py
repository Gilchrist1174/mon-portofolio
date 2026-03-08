import tkinter as tk
from tkinter import messagebox

# Fonction de conversion
def c_to_f():
    try:
        celsius = float(entry_c.get())  # Récupère la valeur entrée
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{celsius}°C = {fahrenheit}°F")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur Celsius → Fahrenheit")
root.geometry("300x150")

# Label et champ pour entrer la température
label_c = tk.Label(root, text="Température en Celsius :")
label_c.pack(pady=5)

entry_c = tk.Entry(root)
entry_c.pack(pady=5)

# Bouton pour lancer la conversion
btn_convert = tk.Button(root, text="Convertir", command=c_to_f)
btn_convert.pack(pady=5)

# Label pour afficher le résultat
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# Boucle principale de Tkinter
root.mainloop()
