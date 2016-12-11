#!/bin/sh

ARGC=$#
fontsize='\\tiny'

if [ $ARGC -eq 0 ]
then
	echo 'filename of gnuplot script?'
fi

if [ $ARGC -gt 0 ]
then
	
	if [ $ARGC -gt 1 ]
	then
		fontsize=$2
		gnuplot   -e "set term epslatex color solid  font ',8' header '\\${fontsize}'; set output '${PLOTEXDIR}src/fig1.tex'" $1
	else
		gnuplot   -e "set term epslatex color solid  font ',8' header '\\tiny'; set output '${PLOTEXDIR}src/fig1.tex'" $1
	fi
		
	jobname="${1%.*}"
	pdflatex  -interaction=batchmode -shell-escape --jobname=$jobname ${PLOTEXDIR}src/plot.tex 
	rm ${jobname}.aux
	rm ${jobname}.log
	evince ${jobname}.pdf &

fi
