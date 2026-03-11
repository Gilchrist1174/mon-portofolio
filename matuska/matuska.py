import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice Simple")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Cadre d'affichage
        input_frame = tk.Frame(master, bd=0, relief="flat", bg="#ccc")
        input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                                    textvariable=self.input_text, width=30,
                                    bg="#eee", bd=0, justify="right")
        self.input_field.grid(row=0, column=0, ipady=10)
        self.input_field.pack(ipady=10) # Augmente la hauteur de la zone de texte

        # Cadre des boutons
        btns_frame = tk.Frame(master, bg="#ddd")
        btns_frame.pack()

        # Définition des boutons (texte, ligne, colonne)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Création et placement des boutons
        for btn_text, row, col in buttons:
            if btn_text == '=':
                button = tk.Button(btns_frame, text=btn_text, font=('arial', 15, 'bold'),
                                   fg="white", bg="#2e86de",
                                   width=7, height=2, bd=0, cursor="hand2",
                                   command=self.evaluate_expression)
            else:
                button = tk.Button(btns_frame, text=btn_text, font=('arial', 15, 'bold'),
                                   fg="black", bg="#eee",
                                   width=7, height=2, bd=0, cursor="hand2",
                                   command=lambda text=btn_text: self.button_click(text))
            button.grid(row=row, column=col, padx=2, pady=2)

        # Bouton Effacer (Clear)
        clear_button = tk.Button(btns_frame, text="C", font=('arial', 15, 'bold'),
                                 fg="white", bg="#c0392b",
                                 width=7, height=2, bd=0, cursor="hand2",
                                 command=self.clear_expression)
        clear_button.grid(row=5, column=0, columnspan=2, padx=2, pady=2) # Fusionne 2 colonnes

        # Bouton Supprimer dernier caractère (Backspace)
        back_button = tk.Button(btns_frame, text="DEL", font=('arial', 15, 'bold'),
                                 fg="white", bg="#f39c12",
                                 width=7, height=2, bd=0, cursor="hand2",
                                 command=self.backspace)
        back_button.grid(row=5, column=2, columnspan=2, padx=2, pady=2) # Fusionne 2 colonnes


    def button_click(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Erreur: Div par 0")
            self.expression = ""
        except Exception as e:
            self.input_text.set("Erreur")
            self.expression = ""

    def clear_expression(self):
        self.expression = ""
        self.input_text.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
