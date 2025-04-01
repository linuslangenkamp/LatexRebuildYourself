# LaTeX Auto-Rebuild Tool

Automatically rebuilds LaTeX documents when source files change, based on modification time.

## Usage

### Set up alias (add to your shell config):
```shell
alias latex_rebuild='python3 /install/directory/rebuild.py'
```

### Use some custom shell script
```shell
latex_rebuild some_tex_file.tex -shell ./build_tex_file.sh
```

### Use standard latex compiler
```shell
latex_rebuild some_tex_file.tex -latex pdflatex
latex_rebuild some_tex_file.tex -latex lualatex
latex_rebuild some_tex_file.tex -latex xelatex
# ... and other LaTeX engines
```
