"""Implementation of Linear Feedback Shift Register with n cells

    This program will generate a cipher sequence (Si) with a n-bit seed. Si will be 2^(n) - 1 bits
    This kind of cipher key is not secure nowadays, it is just for educational purposes, as it can be easily attacked with Berlemkamp-Massey attack.
    We are assuming that the primitive polynomial is x^4 + x + 1

    Usage:
        You have to pass the seed size as an argument
        python lfsr-n-bits.py -s 127
        You can also put '--verbose' argument so that the program will be printing what it's doing on each step.
"""
from random import randint
import sys

seed_lenght = 0
reg = []
si = []
verbose_mode = False

# Getting seed lenght
try:
    seed_lenght = sys.argv[sys.argv.index("-s") + 1]
except:
    print("You need to specify seed size with -s.\nExample: --seedSize 10\n")

# Getting verbose mode
try:
    if sys.argv[sys.argv.index("--verbose")]:
        verbose_mode = True
except:
    verbose_mode = False


for i in range(int(seed_lenght)):
    reg.append(randint(0, 1))

if verbose_mode:
    print("Random seed generated:")
    print(*reg, sep='')


def linear_feedback_shift_register():
    # Pop last item
    pop_el = reg.pop()
    # Append last item to cipher sequence
    si.append(pop_el)
    # XOR operation between popped element and first element
    if pop_el == reg[0]:
        xor_el = 0
    else:
        xor_el = 1
    # Insert in first pos XOR result
    reg.insert(0, xor_el)
    if verbose_mode:
        print("Reg: " + str(reg) + "\tOutput bit: " +
              str(pop_el) + "\tReplacement bit: " + str(xor_el))


for i in range(2 ** (len(reg)) - 1):
    linear_feedback_shift_register()

if verbose_mode:
    print("Output:")
print(*si, sep='')
