import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Nexus")
        self.geometry("800x600")

        # Création d'un frame pour centrer le contenu
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Ajout d'une étiquette de bienvenue
        self.welcome_label = customtkinter.CTkLabel(self, text="Bienvenue dans Nexus !", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.welcome_label.grid(row=0, column=0, padx=20, pady=20)

