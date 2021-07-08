import numpy as np
from scipy.fft import fft, ifft
from scipy.fftpack import fftshift, ifftshift


def fourier(f, t, fs, filtro):
    """
    Filtraggio di un segnale che presenta un rumore basandosi su un filtro
    sulle sequenze specificato.

    :param f: la funzione composta dalla funzione esatta sommata alla funzione rumore
    :param t: durata del segnale
    :param fs: frequenza di campionamento
    :param filtro: il filtro da applicare alle frequenze (lambda in funzione dell'array delle frequenze
                   [lambda freq: np.abs(freq) > 10])
    :return: i valori della funzione filtrata nel linespace da 0 a t con t * fs punti
    """
    n = t * fs  # numero di campioni
    delta = 1 / t  # passo di campionamento nel dominio di Fourier

    x = np.linspace(0, t, n)  # dominio temporale
    y = f(x)  # campionamento del segnale rumoroso nel dominio temporale

    frequenze = np.arange(-fs / 2, fs / 2, delta)  # range delle frequenze del segnale
    polinomio = fftshift(fft(y))  # coefficenti del polinomio di Fourier

    indici = filtro(frequenze)  # filtro le frequenze
    polinomio[indici] = 0  # applico i filtri ai coefficenti del polinomio di Fourier

    return ifft(ifftshift(polinomio))  # ricalcolo il valore della funzione filtrata usando l'inversa di Fourier
