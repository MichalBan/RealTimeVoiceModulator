import numpy as np
from Logger import Logger


class Handler:
	def __init__(self, overlap=1):
		self.overlap = overlap
		self.old_data = np.zeros(overlap)

	def callback(self, indata, outdata, frames, time, status):
		long_indata = np.append(self.old_data, np.reshape(indata, len(indata)))
		long_outdata = self.process(long_indata)
		outdata[:] = np.reshape(long_outdata[self.overlap-1:-1], [len(indata), 1])
		self.old_data[:] = np.reshape(indata[-self.overlap-1:-1], self.overlap)
		Logger.log_audio(indata, outdata)

	def process(self, x):
		return x
