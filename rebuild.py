"""
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
"""

import os
import subprocess
import argparse
import time
import glob


def get_modification_time(file):
    return os.path.getmtime(file)

def run_pdflatex(latex_file, command):
    latex_dir = os.path.dirname(os.path.abspath(latex_file))
    os.chdir(latex_dir)
    
    # Run the LaTeX command (pdflatex, lualatex, etc.)
    process = subprocess.Popen([command, os.path.basename(latex_file)], 
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Simulate pressing Enter for Errors
    stdout, stderr = process.communicate(input=b"\n" * 500)
    try:
        print(stdout.decode())
        print(stderr.decode())
    except:
        pass

def run_make(latex_file):
    latex_dir = os.path.dirname(os.path.abspath(latex_file))
    os.chdir(latex_dir)

    # Run make command (no need to manually invoke bibtex or latexmk)
    process = subprocess.Popen(['make', '-B'],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Simulate pressing Enter for Errors
    stdout, stderr = process.communicate(input=b"\n" * 500)

    try:
        print(stdout.decode())
        print(stderr.decode())
    except:
        pass

def run_shell_script(latex_file, script):
    latex_dir = os.path.dirname(os.path.abspath(latex_file))
    os.chdir(latex_dir)

    # Run Shell script
    process = subprocess.Popen([script, os.path.basename(latex_file)],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Simulate pressing Enter for Errors
    stdout, stderr = process.communicate(input=b"\n" * 500)

    try:
        print(stdout.decode())
        print(stderr.decode())
    except:
        pass

def get_latest_modification_time(directory):
    tex_files = glob.glob(os.path.join(directory, "*.tex"))
    if not tex_files:
        return 0
    return max(get_modification_time(f) for f in tex_files)

def check_and_compile(last_mod_time, latex_file, command, script, make, alltex, finit):
    if alltex:
        current_mod_time = get_latest_modification_time(os.path.dirname(latex_file))
    else:
        current_mod_time = get_modification_time(latex_file)

    if last_mod_time == 0 and not finit:
        last_mod_time = current_mod_time

    if current_mod_time > last_mod_time:
        action = command or script or ("make -B" if make else None)
        print(f"Source files have been modified. Running {action}...")
        
        if script:
            run_shell_script(latex_file, script)
        elif make:
            run_make(latex_file)
        else:
            run_pdflatex(latex_file, command)

        last_mod_time = current_mod_time
    return last_mod_time

def main():
    parser = argparse.ArgumentParser(description="Automatically compile LaTeX file if modified.")
    parser.add_argument("latex_file", help="Path to the LaTeX file to be compiled")
    parser.add_argument("-latex", choices=["pdflatex", "lualatex", "xelatex", "tectonic"],
                        help="The LaTeX engine to use for compilation (pdflatex, lualatex, xelatex, tectonic).")
    parser.add_argument("-shell", help="Path to the shell script for compilation.")
    parser.add_argument("-make", action="store_true", help="Trigger make for compilation.")
    parser.add_argument("-alltex", action="store_true", help="Check all .tex files in directory for modifications.")
    parser.add_argument("-finit", action="store_true", help="Forces an initial build.")

    args = parser.parse_args()
    last_mod_time = 0

    print("Latex Rebuild Yourself running...")

    while True:
        last_mod_time = check_and_compile(last_mod_time, args.latex_file, args.latex, args.shell, args.make, args.alltex, args.finit)
        time.sleep(1)

if __name__ == "__main__":
    main()
