import subprocess, sys
from subprocess import run

venv = './env/Scripts/python.exe'
req = './req.py'

def choiceA():
    a = str(input('Create requirements.txt? [y/n]: ').lower())
    if a == 'y':
        run([venv, req], input='1', encoding='ascii')
        print("Requirements file has been created.")
        quit()

def choiceB():
    b = str(input('Create new virtual environment? [y/n]: ').lower())
    if b == 'y':
        command = [
            sys.executable, '-m', 'venv', 'env.', '--clear',
        ]

        subprocess.check_call(command, shell=True)
        print("New virtual environment created.")
        quit()

def choiceC():
    c = str(input('Install packages? [y/n]: ').lower())
    if c == 'y':
        run([venv, req], input='2', encoding='ascii')
        print("Dependencies installed.")
        quit()

def menu():
    y = str(input('\n[A] Create requirements.\n[B] Create environment.\n[C] Install requirements.\n[X] Exit.\n\nChoose one from the following: ').upper())
    if y == 'A':
        choiceA()

    elif y == 'B':
        choiceB()

    elif y == 'C':
        choiceC()

    elif y == 'X':
        quit()

    else:
        print("Invalid input!")
        menu()

x = str(input('Is virtual environment deactivated? [y/n]: ').lower())
if x == 'y':
    menu()

else:
    print("Exit virtual environment first!")
    quit()