# Real Time Voice Modulator
This is a college project. it's system for real-time speech modulation with a few parametrised effects.
## Effects
There are 3 effects to choose from:
 - Constant: It's a simple constant passband FIR filter, which utilises Hamming widow.
 - Spectral: This effect uses FFT and IFFT to shift the whole spectres of signal.
 - Adaptive: It's a passband filter that magnifies the strongest frequencies by analizying spectre and creating appropriate filters on the fly.
## Dependencies
This project uses following libraries:
 - numpy
 - scipy
 - sounddevice
 - matplotlib
 - tkinter
## How to use
 - run main.py (mentioned above libraries are needed)
 - choose effect and parameters
 - click run
 - talk to your microphone

As a result the voice recorded by microphone should be played by the speakers with a small delay. The desired effect should be heard.
The modified sound recording is saved in "output" folder.
Logs of sound values are saved in "logs" folder.
## parameters
Common parametrs include:
 - Sampling frequency
 - Duration - the duration of voice recording
 - Frame length - the length of frames the sound is split to for real-time modulation
 - Order of filter

If constant filter is used Band min and Band max create the band the filter passes.
If spectral modulation is used Frequency shift parameter means how much is the spectre shifted right.
If adaptive modulation is used Band width means how wide should the passed band be around the strongest frequency.
