import numpy as np
from scipy.fft import fft, ifft
from scipy.fftpack import fftshift, ifftshift


def fourier(f, t, fs, filtro):
    """

    :param f:
    :param t:
    :param fs:
    :param filtro:
    :return:
    """
    d = 1 / fs
    n = t * fs
    delta = 1 / t

    x = np.linspace(0, t, n)
    y = f(x)

    frequenze = np.arange(-fs/2, fs/2, delta)
    polinomio = fftshift(fft(y))

    indici = filtro(frequenze)
    polinomio[indici] = 0

    return ifft(ifftshift(polinomio))

