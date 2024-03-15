import tkinter as tk
from tkinter import simpledialog
import numpy as np

# Funções para os cálculos
def calcular_saida_por_entrada_em(em):
    bm = em / c
    i = (em * bm) / (2 * mu_0)
    return bm, i

def calcular_saida_por_entrada_i(i):
    bm = np.sqrt(2 * i * mu_0)
    em = bm * c
    return em, bm

def calcular_saida_por_entrada_bm(bm):
    em = bm * c
    i = (em * bm) / (2 * mu_0)
    return em, i

def calcular_saida_por_entrada_f(f):
    lam = c / f
    k = 2 * np.pi / lam
    w = 2 * np.pi * f
    return lam, k, w

def calcular_saida_por_entrada_lam(lam):
    f = c / lam
    k = 2 * np.pi / lam
    w = 2 * np.pi * f
    return f, k, w

def calcular_saida_por_entrada_k(k):
    lam = 2 * np.pi / k
    f = c / lam
    w = 2 * np.pi * f
    return f, lam, w

def calcular_saida_por_entrada_w(w):
    f = w / (2 * np.pi)
    lam = c / f
    k = 2 * np.pi / lam
    return f, lam, k

def converter_unidades(valor, de_unidade, para_unidade):
    if de_unidade == "m":
        if para_unidade == "km":
            return valor / 1000, "km"
        elif para_unidade == "cm":
            return valor * 100, "cm"
        elif para_unidade == "mm":
            return valor * 1000, "mm"
    elif de_unidade == "T" and para_unidade == "G":
        return valor * 10000, "G"  
    return None, None

def menu_conversao():
    print("\nMenu de Conversão de Unidades:")
    print("1 - Metro para Quilômetro")
    print("2 - Metro para Centímetro")
    print("3 - Metro para Milímetro")
    print("4 - Tesla para Gauss")
    print("0 - Voltar")
    escolha = int(input("Escolha uma opção: "))
    if escolha != 0:
        valor = float(input("Digite o valor para conversão: "))
        unidades = ["", "km", "cm", "mm", "G"]
        conversoes = [(valor, "m", "km"), (valor, "m", "cm"), (valor, "m", "mm"), (valor, "T", "G")]
        if 1 <= escolha <= 4:
            valor_convertido, unidade = converter_unidades(*conversoes[escolha-1])
            print(f"Valor convertido: {valor_convertido:.3f} {unidade}")
        else:
            print("Opção inválida!")

# Constantes
c = 3.00e8  # Velocidade da luz em m/s
mu_0 = 4 * np.pi * 1e-7  # Permeabilidade magnética no vácuo

# Menu principal
def menu_principal():
    print("\nMenu de Opções:")
    print("1 - Calcular Bm (Amplitude do campo magnético) e I (Intensidade da onda) a partir de Em (Amplitude do campo elétrico)")
    print("2 - Calcular Em (Amplitude do campo elétrico) e Bm (Amplitude do campo magnético) a partir de I (Intensidade da onda)")
    print("3 - Calcular Em (Amplitude do campo elétrico) e I (Intensidade da onda) a partir de Bm (Amplitude do campo magnético)")
    print("4 - Calcular λ (Comprimento de onda), k (Número de onda) e ω (Frequência angular) a partir de f (Frequência)")
    print("5 - Calcular f (Frequência), k (Número de onda) e ω (Frequência angular) a partir de λ (Comprimento de onda)")
    print("6 - Calcular f (Frequência), λ (Comprimento de onda) e ω (Frequência angular) a partir de k (Número de onda)")
    print("7 - Calcular f (Frequência), λ (Comprimento de onda) e k (Número de onda) a partir de ω (Frequência angular)")
    print("8 - Conversão de Unidades")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

def main():
    print("Integrantes do Grupo: \n Matheus Ferreira de Freitas 241230804 \n Henrique Hodel Babler 241230796")
    print("\nDescrição do Programa: Este programa é destinado ao estudo das ondas eletromagnéticas, explorando conceitos como amplitude do campo elétrico e magnético, intensidade da onda, frequência, comprimento de onda, número de onda e frequência angular. O objetivo é aplicar esses conceitos em cálculos práticos, facilitando a compreensão da física das ondas eletromagnéticas.")

    while True:
        escolha = menu_principal()
        if escolha == 0:
            print("Saindo do programa...")
            break
        elif escolha == 1:
            em = float(input("Digite o valor da amplitude do campo elétrico (Em) em volts por metro (V/m): "))
            bm, i = calcular_saida_por_entrada_em(em)
            print(f"Bm (Amplitude do campo magnético): {bm:.3e} T")
            print(f"I (Intensidade da onda): {i:.3e} W/m^2")
        elif escolha == 2:
            i = float(input("Digite o valor da intensidade da onda (I) em watts por metro quadrado (W/m^2): "))
            em, bm = calcular_saida_por_entrada_i(i)
            print(f"Em (Amplitude do campo elétrico): {em:.3e} V/m")
            print(f"Bm (Amplitude do campo magnético): {bm:.3e} T")
        elif escolha == 3:
            bm = float(input("Digite o valor da amplitude do campo magnético (Bm) em tesla (T): "))
            em, i = calcular_saida_por_entrada_bm(bm)
            print(f"Em (Amplitude do campo elétrico): {em:.3e} V/m")
            print(f"I (Intensidade da onda): {i:.3e} W/m^2")
        elif escolha == 4:
            f = float(input("Digite o valor da frequência (f) em hertz (Hz): "))
            lam, k, w = calcular_saida_por_entrada_f(f)
            print(f"Comprimento de onda (λ): {lam:.3e} m")
            print(f"Número de onda (k): {k:.3e} m^-1")
            print(f"Frequência angular (ω): {w:.3e} rad/s")
        elif escolha == 5:
            lam = float(input("Digite o valor do comprimento de onda (λ) em metros (m): "))
            f, k, w = calcular_saida_por_entrada_lam(lam)
            print(f"Frequência (f): {f:.3e} Hz")
            print(f"Número de onda (k): {k:.3e} m^-1")
            print(f"Frequência angular (ω): {w:.3e} rad/s")
        elif escolha == 6:
            k = float(input("Digite o valor do número de onda (k) em metros^-1 (m^-1): "))
            f, lam, w = calcular_saida_por_entrada_k(k)
            print(f"Frequência (f): {f:.3e} Hz")
            print(f"Comprimento de onda (λ): {lam:.3e} m")
            print(f"Frequência angular (ω): {w:.3e} rad/s")
        elif escolha == 7:
            w = float(input("Digite o valor da frequência angular (ω) em radianos por segundo (rad/s): "))
            f, lam, k = calcular_saida_por_entrada_w(w)
            print(f"Frequência (f): {f:.3e} Hz")
            print(f"Comprimento de onda (λ): {lam:.3e} m")
            print(f"Número de onda (k): {k:.3e} m^-1")
        elif escolha == 8:
            menu_conversao()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
