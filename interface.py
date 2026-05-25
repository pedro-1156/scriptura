from tkinter import filedialog

import customtkinter as ctk

caminho = None


def achar_arquivo():
    global caminho
    caminho = filedialog.askopenfilename(
        title="Escolha um arquivo Word", filetypes=[("Arqivos Word", "*.docx")]
    )
    return caminho if caminho and caminho.endswith(".pdf") else None


def main():
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app.geometry("500x500")
    app.iconbitmap("scriptura.ico")
    app.title("Scriptura")
    button = ctk.CTkButton(app, text="Escolha arquivo", command=achar_arquivo)
    text = ctk.CTkLabel(
        app, text="Clique no botão abaixo para escolher um arquivo e saia da janela."
    )
    text.place(relx=0.5, rely=0.25, anchor="center")
    button.place(relx=0.5, rely=0.5, anchor="center")
    app.mainloop()
    return caminho


if __name__ == "__main__":
    main()
