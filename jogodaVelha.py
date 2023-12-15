import tkinter as tk
from tkinter import messagebox
import random

class JogoDaVelhaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha (Henrique)")
        self.root.geometry("400x400")
        self.root.configure(bg="#2C3E50")

        self.frame = tk.Frame(root, bg="#2C3E50")
        self.frame.pack(expand=True)

        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogadores = ["X", "O"]
        self.vez_do_jogador = 0

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.frame, text="", font=("Helvetica", 24), width=3, height=1, command=lambda i=i, j=j: self.fazer_jogada(i, j))
                self.botoes[i][j].grid(row=i, column=j, padx=5, pady=5)
                self.botoes[i][j].configure(bg="#34495E", fg="#ECF0F1")

        self.logo_label = tk.Label(root, text="Jogo da Velha (Henrique)", font=("Helvetica", 16), bg="#2C3E50", fg="#ECF0F1")
        self.logo_label.pack(pady=10)

    def exibir_tabuleiro(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=self.tabuleiro[i][j])

    def verificar_vitoria(self, jogador):
        for i in range(3):
            if all(self.tabuleiro[i][j] == jogador for j in range(3)) or all(self.tabuleiro[j][i] == jogador for j in range(3)):
                return True

        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True

        return False

    def verificar_empate(self):
        return all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3))

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " " and not self.verificar_vitoria("X") and not self.verificar_vitoria("O") and not self.verificar_empate():
            self.tabuleiro[linha][coluna] = "X"
            self.exibir_tabuleiro()

            if self.verificar_vitoria("X"):
                messagebox.showinfo("Fim do Jogo", "Parabéns! Você venceu!")
                self.resetar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim do Jogo", "O jogo terminou em empate!")
                self.resetar_jogo()
            else:
                self.vez_do_jogador = 1
                self.jogada_ia()

    def jogada_ia(self):
        disponiveis = [(i, j) for i in range(3) for j in range(3) if self.tabuleiro[i][j] == " "]
        if disponiveis:
            
            for linha, coluna in disponiveis:
                self.tabuleiro[linha][coluna] = "O"
                if self.verificar_vitoria("O"):
                    self.exibir_tabuleiro()
                    messagebox.showinfo("Fim do Jogo", "O Pc venceu!")
                    self.resetar_jogo()
                    return
                self.tabuleiro[linha][coluna] = " "

            
            for linha, coluna in disponiveis:
                self.tabuleiro[linha][coluna] = "X"
                if self.verificar_vitoria("X"):
                    self.tabuleiro[linha][coluna] = "O"
                    self.exibir_tabuleiro()
                    self.vez_do_jogador = 0
                    return
                self.tabuleiro[linha][coluna] = " "

            linha, coluna = random.choice(disponiveis)
            self.tabuleiro[linha][coluna] = "O"
            self.exibir_tabuleiro()

            if self.verificar_vitoria("O"):
                messagebox.showinfo("Fim do Jogo", "O Pc venceu!")
                self.resetar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim do Jogo", "O jogo terminou em empate!")
                self.resetar_jogo()
            else:
                self.vez_do_jogador = 0

    def resetar_jogo(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.vez_do_jogador = 0
        self.exibir_tabuleiro()
        if self.vez_do_jogador == 1:
            self.jogada_ia()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#2C3E50")
    escolha_inicial = messagebox.askquestion("Escolher Primeiro Jogador", "Você quer começar com 'X'?")

    jogo_da_velha_gui = JogoDaVelhaGUI(root)
    if escolha_inicial =="no":
        jogo_da_velha_gui.vez_do_jogador = 1
        jogo_da_velha_gui.resetar_jogo()

    

    root.mainloop()
