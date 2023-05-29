import tkinter as tk
from tkinter import ttk
from scipy.io.wavfile import write
import numpy as np
import os
from Adaptive import Adaptive
from Filter import Filter
from Handler import Handler
from Logger import Logger
from Plotter import Plotter
from Device import Device
from Spectral import Spectral


class Main:
    label_row = 0
    element_height = 2
    element_width = 40

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("voice modulator")
        self.window.geometry('700x500')

        self.handler_var = tk.StringVar()
        self.fs_var = tk.IntVar()
        self.duration_var = tk.IntVar()
        self.frame_var = tk.DoubleVar()
        self.order_var = tk.IntVar()
        self.band_min_var = tk.IntVar()
        self.band_max_var = tk.IntVar()
        self.band_width_var = tk.IntVar()
        self.shift_var = tk.IntVar()

        self.create_visual_elements()

    def create_visual_elements(self):
        self.create_label("Effect type")
        self.create_combo(self.handler_var, ('none', 'constant', 'spectral', 'adaptive'))

        self.create_label("Sampling frequency [Hz]")
        self.create_combo(self.fs_var, (48000, 44100))

        self.create_label("Duration [s]")
        self.create_combo(self.duration_var, (1, 2, 5, 10))

        self.create_label("Frame length [s]")
        self.create_combo(self.frame_var, (0.02, 0.05, 0.1, 1))

        self.create_label("Order of filter")
        self.create_combo(self.order_var, (2, 10, 30, 100))

        self.create_label("Band min [Hz]")
        self.create_combo(self.band_min_var, (100, 200, 400, 800))

        self.create_label("Band max [Hz]")
        self.create_combo(self.band_max_var, (200, 1000, 2000, 5000))

        self.create_label("Band width [Hz]")
        self.create_combo(self.band_width_var, (50, 100, 150))

        self.create_label("Frequency shift [Hz]")
        self.create_combo(self.shift_var, (50, 150, 500))

        self.create_button()

    def create_button(self):
        button = tk.Button(self.window, text="run", width=Main.element_width, height=Main.element_height,
                           command=self.run)
        button.grid(column=1, row=Main.label_row + 1)

    def create_combo(self, varlable, values):
        combo = ttk.Combobox(self.window, state="readonly", width=Main.element_width, textvariable=varlable)
        combo['values'] = values
        combo.grid(column=1, row=Main.label_row)
        combo.current(0)

    def create_label(self, text):
        Main.label_row = Main.label_row + 1
        tk.Label(self.window, text=text, width=Main.element_width, height=Main.element_height) \
            .grid(column=0, row=Main.label_row)

    def run(self):
        Logger.enable_logging()
        plot = Plotter(self.fs_var.get())

        audio = Device(self.fs_var.get(), self.frame_var.get())
        digital_filter = self.create_digital_filter()
        audio.set_stream_handler(digital_filter)

        audio.stream(self.duration_var.get())
        signals = Logger.read_audio()

        handler = self.handler_var.get()
        folder_name = 'output'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        with open(os.path.join(folder_name, (handler + '_example.wav')), 'w') as file:
            write(file.name, self.fs_var.get(),  np.array(signals[1]).astype(np.int32))
        plot.spectrum(signals)

        if self.handler_var.get() == 'adaptive':
            f = Logger.read_frequency()
            plot.draw(f)

    def create_digital_filter(self):
        digital_filter = None
        handler = self.handler_var.get()
        if handler == 'none':
            digital_filter = Handler()
        elif handler == 'constant':
            digital_filter = Filter(self.order_var.get(), [self.band_min_var.get(), self.band_max_var.get()],
                                    'bandpass', self.fs_var.get())
        elif handler == 'spectral':
            digital_filter = Spectral(self.shift_var.get(), self.frame_var.get(), self.fs_var.get())
        elif handler == 'adaptive':
            digital_filter = Adaptive(self.order_var.get(), self.band_width_var.get(),
                                      [self.band_min_var.get(), self.band_max_var.get()], self.fs_var.get())
        return digital_filter

    def main(self):
        self.window.mainloop()


if __name__ == '__main__':
    Main().main()
