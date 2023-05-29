import numpy as np
from scipy import ifft
from scipy.fft import fft
from Handler import Handler


class Spectral(Handler):
	def __init__(self, shift, frame_length, fs):
		Handler.__init__(self, int(fs*frame_length - 2))
		self.shift = int(shift*2*frame_length)

	def process(self, x):
		yf = fft(x)

		size = len(yf)
		yf[self.shift:size//2] = yf[0:size//2-self.shift]
		yf[0:self.shift] = 0
		[left, right] = np.split(yf, 2)
		right[:] = np.flipud(left)

		sig = ifft(yf)
		sig = np.real(sig)
		return sig.astype(int)
