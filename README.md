
# Requirements

* `GNUplot` (v. 5.2+)
* `pdflatex` (`texlive-full` is recommended)
* `python3` (v. 3.6+)

# Install

To install plotex run `INSTALL.sh` script (with `sudo`).
Python `setup.py` file is still WIP.

# Usage

```
usage: plotex.py [-h] [-p PROFILE] [-a APPEND [APPEND ...] | -r
                 [REPLACE [REPLACE ...]]] [-t TERMINAL] [-d] [-i] [-v]
                 [-l POSTPROCESS]
                 filename

positional arguments:
  filename              gnuplot script filename to parse via plotex

optional arguments:
  -h, --help            show this help message and exit
  -p PROFILE, --profile PROFILE
                        select profile module
  -a APPEND [APPEND ...], --append APPEND [APPEND ...]
                        append terminal header options
  -r [REPLACE [REPLACE ...]], --replace [REPLACE [REPLACE ...]]
                        replace terminal header options
  -t TERMINAL, --terminal TERMINAL
                        set terminal
  -d, --display         display profile settings
  -i, --ignore          use default gnuplot terminal provided by gnuplot
                        settings instead of terminal set by plotex
  -v, --verbose         increase output verbosity
  -l POSTPROCESS, --postprocess POSTPROCESS
                        add commands after \begin{document}
```

# Examples

## Profiles

In `profiles` dir, user can save custom ploting profiles.
To add new profile (or to modify the existing one) create a `file.py` containg dictionary `terminalSettings` and list `plotSettings`.
Dictionary `terminalSettings` should have 3 keys and corresponding values:

 * `terminal` : name of gnuplot terminal
 * `terminalOptions` : gnuplot terminal options (e.g. `standalone`, `png`, ...)
 * `header` : list of TeX commands loaded in document preamble, i.e. before `\begin{document}`

## Basic usage
To run `plotex` type `plotex` in your terminal with name of the gnuplot script to interpret:

```
plotex test.plt
```

where `test.plt` is gnuplot script. 
Please, do not use `set terminal` inside gnuplot script. 
(**TODO** ignore set terminal in gnuplot script)

## Help

To see options avaliable in plotex use `-h` help flag

```
plotex -h
```

## Setting the profile

To change the profile use `-p` option

```
plotex test.plt -p cairolatex
```

which will change `default` profile into `cairolatex`.

## Changing the terminal

To change the termianl use `-t` option

```
plotex test.plt -t epslatex
```

which will change terminal set in `default` profilo into `epslatex` gnuplot terminal.

## Ignoring plotex parser

To ignore `plotex` script use `-i` option

```
plotex test.plt -i
```

Only gnuplot will run, without LaTeX compiler.
If one does not use any `set term` in gnuplot script, the default gnuplot terminal will be used (most probably `x11` terminal or `wxt` depends on distribution).

## Verbose

Option `-v` increases plotex output verbosity.
One can track what plotex is doing

```
plotex test.plt -v
```

## LaTeX post-process

