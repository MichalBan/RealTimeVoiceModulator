from scipy import signal
from Handler import Handler


class Filter(Handler):
	def __init__(self, order, window, btype, fs):
		Handler.__init__(self, order+1)
		self.b = signal.firwin(order, cutoff=window, pass_zero=btype, fs=fs)

	def process(self, x):
		return signal.lfilter(self.b, [1], x)
