import random
import sys
from math import sqrt

# ===========================================================


def sim(N):  # Funzione che esegue una simulazione
    i = 0  # Lanci dentro a cerchio
    o = 0  # Lanci fuori dal cerchio

    for n in range(N):  # Ciclo di simulazione

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # Blocco che controlla se il lancio è avvenuto dentro o fuori dal cerchio
        r = x**2 + y**2
        if r <= 1:
            i += 1
        else:
            o += 1

    pi = 4 * i / N  # Calcolo di π
    return pi


# Funzione che esegue media, deviazione standard e SDOM su una lista di dati
def stime(L):

    media = sum(L) / len(L)
    somma_scarti = sum((z - media) ** 2 for z in L)
    std = sqrt(1 / (len(L) - 1) * somma_scarti)
    sdom = std / sqrt(len(L))
    return media, std, sdom


# ===========================================================

if __name__ == "__main__":

    random.seed(67)
    N = int(sys.argv[1])  # Numero di lanci
    K = int(sys.argv[2])  # Numero di simulazioni
    L = []  # Lista con stime di π

    # Esegue le K simulazioni
    for m in range(K):
        L.append(sim(N))

    dati = stime(L)  # Salva i dati

    print(f"Stima di π: {dati[0]:.5f}")
    print(f"Deviazione standard: {dati[1]:.5f}")
    print(f"SDOM: {dati[2]:.5f}")
