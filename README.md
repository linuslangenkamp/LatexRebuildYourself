```console
usage: rebuild.py [-h] [-latex {pdflatex,lualatex,xelatex,tectonic}] [-shell SHELL] [-make] [-alltex] latex_file

Automatically compile LaTeX file if modified.

positional arguments:
  latex_file            Path to the LaTeX file to be compiled

options:
  -h, --help            show this help message and exit
  -latex {pdflatex,lualatex,xelatex,tectonic}
                        The LaTeX engine to use for compilation (pdflatex, lualatex, xelatex, tectonic).
  -shell SHELL          Path to the shell script for compilation.
  -make                 Trigger make -B for compilation.
  -alltex               Check all .tex files in directory for modifications.
```
