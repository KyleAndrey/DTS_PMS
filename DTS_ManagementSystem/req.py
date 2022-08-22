import subprocess, sys

def req1():
    command = [
        sys.executable, '-m', 'pip', 'freeze', '>', 'requirements.txt',
    ]
        
    subprocess.check_call(command, shell=True)

def req2():
    command = [
        sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt',
    ]

    subprocess.check_call(command, shell=True)

a = str(input())
if a=='1':
    req1()

elif a=='2':
    req2()

else:
    quit()