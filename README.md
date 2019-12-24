
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

# Table of contents
1. [Profiles](#profiles)
2. [Basic usage](#basic)
3. [Help](#help)
4. [Setting the profiles](#setprofiles)
5. [Changing the terminal](#terminal)
6. [Ignoring plotex parser](#ignore)
7. [Verbose](#verbose)
8. [Display selected options](#display)
9. [LaTeX post-process](#postprocess)
10. [Append the header](#append)
11. [Replace the header](#replace)

## Profiles <a name="profiles"></a> 

In `profiles` dir, user can save custom ploting profiles.
To add new profile (or to modify the existing one) create a `file.py` containg dictionary `terminalSettings` and list `plotSettings`.
Dictionary `terminalSettings` should have 3 keys and corresponding values:

 * `terminal` : name of gnuplot terminal
 * `terminalOptions` : gnuplot terminal options (e.g. `standalone`, `png`, ...)
 * `header` : list of TeX commands loaded in document preamble, i.e. before `\begin{document}`

List `plotSettings` contains gnuplot commands loaded with the profile, e.g.
 * `plotSettings = ['set grid']` will cause that every script run with the profile will have `set grid` gnuplot option by default. 

## Basic usage <a name="basic"></a> 

To run `plotex` type `plotex` in your terminal with name of the gnuplot script to interpret:

```
plotex test.plt
```

where `test.plt` is gnuplot script. 
Please, do not use `set terminal` inside gnuplot script. 
(**TODO** ignore set terminal in gnuplot script)

## Help <a name="help"></a> 


To see options avaliable in plotex use `-h` help flag

```
plotex -h
```

## Setting the profile <a name="setprofiles"></a> 


To change the profile use `-p` option

```
plotex test.plt -p cairolatex
```

which will change `default` profile into `cairolatex`.

## Changing the terminal <a name="terminal"></a> 


To change the termianl use `-t` option

```
plotex test.plt -t epslatex
```

which will change terminal set in `default` profilo into `epslatex` gnuplot terminal.

## Ignoring plotex parser <a name="ignore"></a> 


To ignore `plotex` script use `-i` option

```
plotex test.plt -i
```

Only gnuplot will run, without LaTeX compiler.
If one does not use any `set term` in gnuplot script, the default gnuplot terminal will be used (most probably `x11` terminal or `wxt` depends on distribution).

## Verbose <a name="verbose"></a> 


Option `-v` increases plotex output verbosity.
One can track what plotex is doing

```
plotex test.plt -v
```

## Display selected options <a name="display"></a> 


Flag `-d` shows selected options loaded from profile after parsing the args

 * terminal
 * terminalOptions
 * header
 * plot Settings

```
plotex test.plt -d
```

Option is very useful with `-a` and `-r` flags to check the result.

## LaTeX post-process <a name="postprocess"></a> 


After flag `-l` user can list the command which will be added after `\begin{document}` (see example below).

Example:
```
plotex test.plt -l '\tiny' '\bfseries'
```

This command will affect the font in the entire plot (to `\tiny`) and change text font to boldfold type.
Please note that `\bfseries` does not affect the mathfont!

## Append the header <a name="append"></a> 


Flag `-a` appends the header option loaded by the profile.
E.g. if one needs to change the font to `ebgaramond` and load `tikz` package in selected plot, just use the following commang

```
plotex test.plt -a '\usepackage{ebgaramond}' '\usepackage{tikz}'
```

## Replace the header <a name="replace"></a> 


Flag `-r` works similar as `-a` option, but it replaces all header options loaded from profile.

```
plotex test.plt -r '\usepackage{lmodern}'
