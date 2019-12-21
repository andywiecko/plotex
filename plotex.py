#!/bin/python3


class Plotex():
    pass


def Glue():
    pass

def PlotexParser():
    
    gnuplotHeaderSettings=\
r"""{shebang}
# terminal settings parsed by plotex
set term {terminal} standalone {terminalOptions} header {header}
set output 'test.tex' 
"""

    gnuplotScriptSettings="{settings}"
    gnuplotScriptSettings="# gnuplot script settings loaded from profile\n" + gnuplotScriptSettings.format(settings="set grid") + "\n"

    gnuplotScript="# gnuplot script loaded by plotex"+\
r"""
set grid
set yr[:1.1]
set xlabel '$x$'
set ylabel '$f(x)$'

p sin(x)/x w lp t '$f(x)=\frac{\sin x}{x\pi}$'

    """
    gnuplotHeaderSettings = gnuplotHeaderSettings.format(
            shebang="#!/bin/gnuplot",
            terminal="cairolatex",
            terminalOptions="",
            header=r"'\usepackage{mathptmx}'")
    

    print(gnuplotHeaderSettings)
    print(gnuplotScriptSettings)
    print(gnuplotScript)

def main():
    PlotexParser()


if __name__=="__main__":
    main()
