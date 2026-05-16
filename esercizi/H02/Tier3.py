import random
import matplotlib.pyplot as plt
from math import sqrt
import Tier2  # Importo il modulo precedente con le funzioni già pronte

# ======================================================================

random.seed(3)
N = [  # Lista con numero lanci
    10,
    50,
    100,
    300,
    500,
    700,
    800,
    1000,
    3000,
    5000,
    7000,
    10000,
    20000,
    50000,
]
K = 15  # Numero di simulazioni
stima = []  # Deviazione standard per ogni N
N_sqrt = []  # Valore di 1/srt(N) per ogni N
C = 1.5  # Cosatante moltiplicativa

for i in N:  # Calcola la deviazione standard per ogni N
    cicli = []  # Valori di pi greco per ogni j-esima simulazione

    for j in range(K):  # Esegue le K simulazioni
        cicli.append(Tier2.sim(i))  # Calcola il valore di pi greco

    stima.append(Tier2.stime(cicli)[1])  # Calcola la deviazione standard

for i in N:
    N_sqrt.append(
        C / sqrt(i)
    )  # Calcolo il valore di 1/sqrt(N) con costante moltiplicativa

# Formattazione del grafico
plt.title(r"$\sigma$ vs N")
plt.xlabel("N")
plt.ylabel(r"$\sigma$")
plt.scatter(N, stima, label="Simulazione")
plt.plot(N, N_sqrt, color="red", label=r"Andamento teorico $1/\sqrt{N}$")
plt.loglog()
plt.legend()
plt.show()
