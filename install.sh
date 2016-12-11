#!/bin/sh

echo "# Copy these two lines into your's bashrc file"
echo export PLOTEXDIR=`pwd`/
PLOTEXDIR=`pwd`
echo alias plotex=`pwd`/plotex.sh

echo '\\documentclass{standalone}' > src/plot.tex
echo '\\usepackage{graphicx}' >> src/plot.tex
echo '\\begin{document}' >> src/plot.tex
echo '\\input{'${PLOTEXDIR}'/src/fig1.tex}' >> src/plot.tex
echo '\\end{document}' >> src/plot.tex
