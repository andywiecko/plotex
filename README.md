
# Requirements

* `GNUplot`
* `pdflatex`
* `python3`

# Usage

```bash
usage: plotex.py [-h] [-p PROFILE] [-a APPEND [APPEND ...] | -r
                 [REPLACE [REPLACE ...]]] [-t TERMINAL] [-d] [-i]
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
```

# Examples

```bash
python3 plotex.py test.plt -d -a '\\usepackage{times}' '\\usepackage[utf8]{inputenc}'
```

