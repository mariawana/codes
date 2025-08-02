import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Ikaw lang at ikaw ang sinisigaw", 0.10),
        ("Ng puso kong 'di mapakali", 0.095),
        ("Ikaw lang at ikaw ang sinisigaw", 0.12),
        ("Pag-ibig ko'y sana mapansin", 0.11),

    ]

    delays = [ 0.13, 0.15, 0.5, 
              2 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()






























