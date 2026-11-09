import os
import time

frames = [
    '\n  0 \n /|\ \n / \ ',
    '  0 \n /|\ \n / \ ',
    '\n  0 \n /|\ \n / \ ',
    '  0 \n \|/ \n / \ '
]

def animate():
    try:
        while True:
            for frame in frames:
                os.system('cls')
                print(frame)
                time.sleep(0.2)
    except KeyboardInterrupt:
        os.system('cls')
animate() 

white = '\u001b[47m'
red = '\u001b[41m'
blue = '\u001b[48;2;0;0;70m'
reset = '\u001b[0m'
height = 12
weight = 55
pixel = ' '

def flag():
    for i in range(height):
        if 0 <= i <= 1 or 10 <= i <= 11:
            print(red + pixel * weight + reset)
        if 2 <= i <= 3 or 8 <= i <= 9:
            print(white + pixel * weight + reset)
        if 4 <= i <= 7:
            print(blue + pixel * weight + reset)        
flag()


def single_uzor():
    return (
      "    ^    \n"
      "  ╭─┴─╮  \n"
      " ╱     ╲ \n"
      "╱       ╲"
)
def uzor_in_row(count):
    row = single_uzor()
    lines = row.split('\n')
    for line in lines:
        print(line * count)
uzor_in_row(10)


def sequence():
    cbol = []
    cmen = []
    m = []
    pixel = ' '
    with open('sequence.txt', 'r') as f:
        vals = [float(s.strip()) for s in f]
        for el in vals:
            if el >= 0 and el != 5:
                m.append(el)
    for el in m:
        if el > 5:
            cbol.append(el)
        else:
            cmen.append(el)
    protsbol = round(sum(cbol) / (sum(m) / 100), 2)
    protsmen = round(sum(cmen) / (sum(m) / 100), 2)
    print(f'{red + pixel * round(protsbol) + reset} {protsbol}%')
    print(f'{blue + pixel * round(protsmen) + reset} {protsmen}%')
sequence() 





    