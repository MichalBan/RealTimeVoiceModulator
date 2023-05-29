import numpy as np
from scipy import signal
from scipy.fft import fft, fftfreq
from Handler import Handler
from Logger import Logger


class Adaptive(Handler):
	def __init__(self, order, band_width, band, fs):
		Handler.__init__(self, order+1)
		self.fs = fs
		self.deadband = band
		self.order = order
		self.band_width = band_width
		self.period = 1/fs

	def process(self, x):
		f_max = self.find_strongest_frequency(x)
		f_top = np.min([f_max + self.band_width // 2, self.fs // 2 - 1])
		f_bot = np.max([f_max - self.band_width // 2, 1])
		b = signal.firwin(self.order, [f_bot, f_top], pass_zero='bandpass', fs=self.fs)
		return signal.lfilter(b, [1], x)

	def find_strongest_frequency(self, x):
		n = len(x)
		t = self.period
		yf = fft(x)
		xf = fftfreq(n, t)

		index_end = int(self.deadband[1]*len(yf)//self.fs)
		index_start = int(self.deadband[0]*len(yf)//self.fs)
		index_max = np.argmax(yf[index_start:index_end])
		f_max = int(xf[index_start + index_max])
		Logger.log_frequency(f_max)
		return f_max
