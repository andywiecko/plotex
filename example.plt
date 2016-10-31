#!/bin/gnuplot

set grid
set yr[:1.1]
set xlabel '$x$'
set ylabel '$f(x)$'

p sin(x)/x w lp t '$f(x)=\frac{\sin x}{x\pi}$'
