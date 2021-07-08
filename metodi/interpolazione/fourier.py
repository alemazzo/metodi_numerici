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
    d = 1 / fs
    n = t * fs
    delta = 1 / t

    x = np.linspace(0, t, n)
    y = f(x)

    frequenze = np.arange(-fs / 2, fs / 2, delta)
    polinomio = fftshift(fft(y))

    indici = filtro(frequenze)
    polinomio[indici] = 0

    return ifft(ifftshift(polinomio))
