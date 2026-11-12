import math
import tkinter as tk
from tkinter import ttk


def calcular_imc(altura_cm, peso_kg):
    altura = float(altura_cm.strip().replace(",", ".")) / 100
    peso = float(peso_kg.strip().replace(",", "."))
    if not all(math.isfinite(v) and v > 0 for v in (altura, peso)):
        raise ValueError("Informe altura e peso positivos.")
    imc = peso / altura ** 2
    if not math.isfinite(imc):
        raise ValueError("Valores fora do intervalo de cálculo.")
    return imc


def classificar_imc(imc):
    for limite, faixa in (
        (18.5, "Abaixo do peso"),
        (25, "Peso normal"),
        (30, "Sobrepeso"),
        (35, "Obesidade grau I"),
        (40, "Obesidade grau II"),
    ):
        if imc < limite:
            return faixa
    return "Obesidade grau III"


def criar_janela():
    janela = tk.Tk()
    janela.title("Cálculo do IMC - Índice de Massa Corporal")
    janela.minsize(540, 240)
    painel = ttk.Frame(janela, padding=16)
    painel.pack(fill="both", expand=True)
    painel.columnconfigure(2, weight=1)

    campos = []
    rotulos = ("Nome do paciente:", "Endereço completo:", "Altura (cm):", "Peso (kg):")
    for linha, rotulo in enumerate(rotulos):
        ttk.Label(painel, text=rotulo).grid(row=linha, column=0, sticky="w", pady=5)
        campo = ttk.Entry(painel, width=18)
        campo.grid(row=linha, column=1, columnspan=2 if linha < 2 else 1,
                   sticky="ew", padx=(10, 0), pady=5)
        campos.append(campo)

    resultado = tk.StringVar(value="Resultado")
    caixa = ttk.LabelFrame(painel, text="IMC")
    caixa.grid(row=2, column=2, rowspan=2, sticky="nsew", padx=(12, 0), pady=5)
    ttk.Label(caixa, textvariable=resultado, anchor="center", justify="center",
              wraplength=210).pack(fill="both", expand=True, padx=8, pady=8)

    def calcular():
        try:
            imc = calcular_imc(campos[2].get(), campos[3].get())
        except (ValueError, ArithmeticError):
            resultado.set("Informe altura e peso válidos e positivos.")
            return
        valor = f"{imc:.2f}".replace(".", ",")
        resultado.set(f"IMC: {valor} kg/m²\n{classificar_imc(imc)}")

    def reiniciar():
        for campo in campos:
            campo.delete(0, tk.END)
        resultado.set("Resultado")
        campos[0].focus_set()

    botoes = ttk.Frame(painel)
    botoes.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(14, 0))
    ttk.Button(botoes, text="Calcular", command=calcular).pack(side="left")
    ttk.Button(botoes, text="Reiniciar", command=reiniciar).pack(side="left", padx=8)
    ttk.Button(botoes, text="Sair", command=janela.destroy).pack(side="right")
    campos[0].focus_set()
    return janela


if __name__ == "__main__":
    criar_janela().mainloop()
