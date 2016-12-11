#!/bin/sh


gnuplot   -e "set term epslatex color solid  font ',8' header '\\tiny'; set output '${PLOTEXDIR}src/fig1.tex'" $1
jobname="${1%.*}"

#pdflatex  --output-directory=out --jobname=$jobname src/plot.tex
pdflatex  -shell-escape --jobname=$jobname ${PLOTEXDIR}src/plot.tex 
#rm ${jobname}.aux
#rm ${jobname}.log

evince ${jobname}.pdf &
