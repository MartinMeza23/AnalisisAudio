import sys

sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave
import thinkplot

waveTelefono = read_wave("telefono.wav")
waveTelefono.plot()
decorate(xlabel="Tiempo (s)")
thinkplot.show()

#espectro = waveTelefono.make_spectrum()
#espectro.plot()
#decorate(xlabel="Frecuencia (Hz)")
#thinkplot.show()

wavePrimerDijito = waveTelefono.segment(start=0,duration=0.5)
#wavePrimerDijito.plot()
#decorate(xlabel="Tiempo (s)")
#thinkplot.show()

#
espectroPrimerDijito = wavePrimerDijito.make_spectrum()
espectroPrimerDijito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

waveSegundoDijito = waveTelefono.segment(start=0.5,duration=0.5)
espectroSegundoDijito = waveSegundoDijito.make_spectrum()
espectroSegundoDijito.plot()
decorate(xlabel="Frecuencia (Hz)")

waveTercerDijito = waveTelefono.segment(start=1, duration=0.5)
espectroTercerDijito = waveTercerDijito.make_spectrum()
espectroTercerDijito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

