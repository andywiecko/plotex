#!/bin/sh


gnuplot   -e "set term epslatex color solid  font ',8' header '\\tiny'; set output 'src/fig1.tex'" $1
jobname="${1%.*}"

pdflatex  --output-directory=out --jobname=$jobname plot.tex
evince out/${jobname}.pdf &
