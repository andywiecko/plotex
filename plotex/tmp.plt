#!/bin/gnuplot
# terminal settings parsed by plotex
set term cairolatex standalone  header '\usepackage{mathptmx}'
set output 'tmp.tex' 

# gnuplot script settings loaded from profile
set colorsequence classic
set key noautotitle

# gnuplot script loaded by plotex
set xlabel '$x$'
set ylabel '$y$'

plot x,x**2,sqrt(x)
