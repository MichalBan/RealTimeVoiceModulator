import os


class Logger:
	folder_name = 'logs'
	in_log_name = 'log_in.txt'
	out_log_name = 'log_out.txt'
	f_log_name = 'log_f.txt'
	in_log = None
	out_log = None
	f_log = None
	log_enabled = False

	@staticmethod
	def enable_logging():
		if not os.path.exists(Logger.folder_name):
			os.makedirs(Logger.folder_name)
		Logger.in_log = open(os.path.join(Logger.folder_name, Logger.in_log_name), 'w')
		Logger.out_log = open(os.path.join(Logger.folder_name, Logger.out_log_name), 'w')
		Logger.f_log = open(os.path.join(Logger.folder_name, Logger.f_log_name), 'w')
		Logger.log_enabled = True

	@staticmethod
	def log_audio(indata, outdata):
		if Logger.log_enabled:
			for i in range(len(indata)):
				Logger.in_log.write(str(indata[i][0]) + '\n')
				Logger.out_log.write(str(outdata[i][0]) + '\n')

	@staticmethod
	def log_frequency(f):
		if Logger.log_enabled:
			Logger.f_log.write(str(f) + '\n')

	@staticmethod
	def close():
		Logger.log_enabled = False
		Logger.in_log.close()
		Logger.out_log.close()
		Logger.f_log.close()

	@staticmethod
	def read_audio():
		Logger.close()
		filename = os.path.join(Logger.folder_name, Logger.in_log_name)
		signal_in = [int(x) for x in open(filename, 'r').readlines()]
		filename = os.path.join(Logger.folder_name, Logger.out_log_name)
		signal_out = [int(x) for x in open(filename, 'r').readlines()]
		Logger.close()
		return [signal_in, signal_out]

	@staticmethod
	def read_frequency():
		Logger.close()
		f = [int(x) for x in open(Logger.f_log_name, 'r').readlines()]
		Logger.close()
		return f
