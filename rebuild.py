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

def get_modification_time(file):
    return os.path.getmtime(file)

def run_pdflatex(latex_file, command):
    latex_dir = os.path.dirname(os.path.abspath(latex_file))
    os.chdir(latex_dir)
    
    # Run the LaTeX command (pdflatex, lualatex, etc.)
    process = subprocess.Popen([command, os.path.basename(latex_file)], 
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Simulate pressing Enter for Errors
    stdout, stderr = process.communicate(input=b"\n")

    print(stdout.decode())
    print(stderr.decode())

def run_shell_script(latex_file, script):
    latex_dir = os.path.dirname(os.path.abspath(latex_file))
    os.chdir(latex_dir)

    # Run Shell script
    process = subprocess.Popen([script, os.path.basename(latex_file)],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Simulate pressing Enter for Errors
    stdout, stderr = process.communicate(input=b"\n")

    print(stdout.decode())
    print(stderr.decode())

def check_and_compile(latex_file, timestamp_file, command, script):
    if os.path.exists(timestamp_file):
        with open(timestamp_file, "r") as f:
            last_mod_time = float(f.read())
    else:
        last_mod_time = 0

    current_mod_time = get_modification_time(latex_file)

    if current_mod_time > last_mod_time:
        print(f"{latex_file} has been modified. Running {command or script}...")
        
        if script:
            run_shell_script(latex_file, script)
        else:
            run_pdflatex(latex_file, command)

        with open(timestamp_file, "w") as f:
            f.write(str(current_mod_time))
    else:
        return

def main():
    parser = argparse.ArgumentParser(description="Automatically compile LaTeX file if modified.")
    parser.add_argument("latex_file", help="Path to the LaTeX file to be compiled")
    parser.add_argument("-latex", choices=["pdflatex", "lualatex", "xelatex", "tectonic"],
                        help="The LaTeX engine to use for compilation (pdflatex, lualatex, xelatex, tectonic).")
    parser.add_argument("-shell", help="Path to the shell script for compilation.")

    args = parser.parse_args()
    timestamp_file = ".build_timestamp.txt"

    while True:
        check_and_compile(args.latex_file, timestamp_file, args.latex, args.shell)
        time.sleep(1)

if __name__ == "__main__":
    main()
