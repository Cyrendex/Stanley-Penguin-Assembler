"""
spasm.py - Stanley/Penguin Processor Assembler

Description:
    This Python script serves as an assembler for the Stanley/Penguin processor, converting assembly code
    into machine code that can be executed on the corresponding hardware.

Usage:
    NOT YET IMPLEMENTED

Version:
    1.0

For more information, refer to the README.md file or visit https://github.com/Cyrendex/Stanley-Penguin-Assembler.
"""
import os

machine_code = str()
opcodes = {
    'LOAD': '0',
    'STORE': '1',
    'READ': '2',
    'WRITE': '3',
    'ADD': '4',
    'SUB': '5',
    'MUL': '6',
    'DIV': '7',
    'MOD': '8',
    'AND': '9',
    'OR': 'A',
    'XOR': 'B',
    'JMP': 'C',
    'JZ': 'D',
    'JLZ': 'E',
    'JGZ': 'F'
}
label_addresses = dict()

if __name__ == '__main__':
    pass

def get_labels(filename):
    index_counter = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip(): # Skip empty lines.
                    continue
                tokens = line.split() # Split line into tokens
                first_element = tokens[0] # Get the first token
                if first_element.startswith('.'): # Is the first element a label?
                    label_addresses.update({first_element[:-1], index_counter})
                index_counter += 1 
            file.close()
    except IOError:
        print(IOError)





