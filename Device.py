import sounddevice as sd
from Handler import Handler


class Device:
	def __init__(self, fs, frame_length, stream_handler=None):
		sd.default.channels = 1
		sd.default.blocksize = int(fs * frame_length)
		sd.default.dtype = 'int32'
		sd.default.samplerate=fs
		self.stream_handler = stream_handler

	def set_stream_handler(self, stream_handler: Handler):
		self.stream_handler = stream_handler

	def stream(self, duration):
		with sd.Stream(callback=self.stream_handler.callback):
			sd.sleep(int(duration * 1000))
