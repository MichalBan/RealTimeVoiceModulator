import matplotlib.pyplot as plt


class Plotter:
	fignum = 1

	def __init__(self, fs):
		self.fs = fs

	def single_plot(self, signal):
		plt.figure(Plotter.fignum)
		Plotter.increment_fignum()
		plt.plot(signal)

	def draw(self, signals):
		if isinstance(signals[0], int):
			self.single_plot(signals)
		else:
			for sig in signals:
				self.single_plot(sig)
		plt.show()

	def spectrum(self, signals):
		plt.figure(Plotter.fignum)
		Plotter.increment_fignum()
		plt.magnitude_spectrum(signals[0], Fs=self.fs, scale='dB', color='blue')
		plt.title("before")
		plt.figure(Plotter.fignum)
		Plotter.increment_fignum()
		plt.magnitude_spectrum(signals[1], Fs=self.fs, scale='dB', color='red')
		plt.title("after")
		plt.show()

	@staticmethod
	def increment_fignum():
		Plotter.fignum = Plotter.fignum + 1
