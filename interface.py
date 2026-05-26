from tkinter import filedialog

import customtkinter as ctk

import sys, os

caminho = None


def achar_arquivo():
    global caminho
    caminho = filedialog.askopenfilename(
        title="Escolha um arquivo Word", filetypes=[("Arqivos Word", "*.docx")]
    )
    return caminho if caminho and caminho.endswith(".docx") else None


prompt = None
def set_prompt(textbox):
    global prompt
    prompt = textbox.get("1.0", "end")

def main():
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app.geometry("1920x1080")
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
    icon_path = os.path.join(base_path, "scriptura.ico")
    app.iconbitmap(icon_path)
    app.title("Scriptura")

    text = ctk.CTkLabel(
        app, text="Clique no botão abaixo para escolher um arquivo, escolha o prompt, clique no botão e saia da janela."
    )
    button = ctk.CTkButton(app, text="Escolha arquivo", command=achar_arquivo)
    textbox = ctk.CTkTextbox(app, width=300, height=160)
    submit_button = ctk.CTkButton(app, text="Enviar prompt", command=lambda: set_prompt(textbox))

    text.place(relx=0.5, rely=0.125, anchor="center")
    button.place(relx=0.5, rely=0.25, anchor="center")
    textbox.place(relx=0.5, rely=0.5, anchor="center")
    submit_button.place(relx=0.5, rely=0.75, anchor="center")

    app.mainloop()
    return [caminho, prompt]


if __name__ == "__main__":
    main()
