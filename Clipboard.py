from subprocess import check_call
import os
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)
os.system('cls')
q = input('What is the input text?\n')
os.system('cls')
copy2clip(q)
