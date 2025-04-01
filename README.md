Auto rebuild of latex files based on last modification time

Possible configurations:

    Alias:
        latex_rebuild = python3 /install/directory/rebuild.py

    Shell build:
        latex_rebuild some_tex_file.tex -shell ./build_tex_file.sh 

    Latex builds:
        latex_rebuild some_tex_file.tex -latex pdflatex
        latex_rebuild some_tex_file.tex -latex lualatex
        latex_rebuild some_tex_file.tex -latex xelatex
                                                  .
                                                  .
                                                  .
