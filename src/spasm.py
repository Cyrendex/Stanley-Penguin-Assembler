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

def parse_sp_code(filename):
    global machine_code
    line_counter = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                print("For this line, we have: " + line)
                line_counter += 1
                if not line.strip() or line.lstrip().startswith(';'): # Skip empty lines or comments.
                    continue
                tokens = line.split() # Split line into tokens
                print("Tokens for this line are: ")
                print(tokens)
                if not 1 < len(tokens) < 4:
                    raise TypeError("Line {0}: 2 or 3 arguments expected ({1} given)".format(line_counter, len(tokens)))

                token_pointer = 0 # Which token we're currently looking at
                if tokens[0].endswith(':'): # This line has a label
                    token_pointer += 1
                
                # SPECIAL CASE: label + value, no opcode.
                value_at_pointer = tokens[token_pointer]
                hex_or_decimal = (value_at_pointer.startswith('0x') or not value_at_pointer.upper().isupper()) # It's a number, not an address or an opcode mnemonic.
                if tokens[0] not in label_addresses and tokens[1] not in label_addresses and hex_or_decimal:
                    print("SPECIAL CASE!!!!!")
                    machine_code += '0' # This action is guaranteed to be LOAD by the rules of Stanley/Penguin
                    if not value_at_pointer.startswith('0x'): # Value is given in decimal format
                        value_at_pointer = hex(int(value_at_pointer))
                    
                    value_at_pointer = value_at_pointer.replace('0x', '') # Remove the '0x' to prepare for string concatination.
                    value_at_pointer = pad_values(value_at_pointer, line_counter)
                    if not 0 < len(value_at_pointer) < 8:
                        raise ValueError("Line {0}: Input length must be between 0 and 8 (len(\'{1}\') -> {2})".format(line_counter, value_at_pointer, len(value_at_pointer)))
                    machine_code += value_at_pointer
                    machine_code += '\n'
                    continue # We immediately skip to the next line.
                # Trying to add opcode to the most significant bit of the current line.
                if tokens[token_pointer] in opcodes:
                    machine_code += opcodes[tokens[token_pointer].upper()]
                else:
                    raise ValueError("Line {0}: The opcode \'{1}\' is not recognized.".format(line_counter, tokens[token_pointer]))
                
                token_pointer += 1
                # Adding the value to machine code. Case 1: it's an address. Case 2: it's an integer in some form.
                value_at_pointer = tokens[token_pointer]
                if value_at_pointer in label_addresses: # Case 1                    
                    value_at_address = str(label_addresses[value_at_pointer])
                    value_at_address = value_at_address.replace('0x', '')
                    value_at_pointer = pad_values(value_at_address, line_counter) # We have 28 bits left after the opcode, therefore, we need to pad the rest of the bits (7x4 = 28)
                elif value_at_pointer.upper().isupper() and value_at_pointer not in label_addresses and not value_at_pointer.startswith('0x'): # Non hexadecimal value with letters that's not in our label addresses. Error! 
                    raise ValueError ("Line {0}: The address \'{1}\' does not exist in label_addresses.".format(line_counter, value_at_pointer))
                else: # Case 2
                    if value_at_pointer.startswith('0x') is False: # Value is given in decimal format
                        value_at_pointer = hex(int(value_at_pointer))
                    value_at_pointer = value_at_pointer.replace('0x', '') # Remove the '0x' to prepare for string concatination.
                    value_at_pointer = pad_values(value_at_pointer, line_counter) # Same logic as the if block               

                if not 0 < len(value_at_pointer) < 8:
                    raise ValueError("Line {0}: Input length must be between 0 and 8 (len(\'{1}\') -> {2})".format(line_counter, value_at_pointer, len(value_at_pointer)))
                machine_code += value_at_pointer
                machine_code += "\n" # Go to next line   
    except FileNotFoundError as e:
        print("Error: {0}".format(e))

def get_labels(filename):
    index_counter = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip() or line.startswith(';'): # Skip empty lines and comments.
                    continue
                tokens = line.split() # Split line into tokens
                first_element = tokens[0] # Get the first token
                if first_element.endswith(':'): # Is the first element a label?
                    label_addresses[first_element[:-1]] = hex(index_counter).replace('0x','').upper()
                index_counter += 1 
    except IOError:
        print(IOError)

def pad_values(value, current_line, pad_length=7, pad_value='0'):
    if not isinstance(value, str):
        raise TypeError("Line {0}: pad_values expected 'str', but received '{1}')".format(current_line, type(value)))
    val_length = len(value)
    if pad_length <= val_length:
        return value
    else:
        for _ in range(val_length,pad_length):
            value = pad_value + value
    return value

if __name__ == '__main__':
    get_labels('test.txt')
    parse_sp_code('test.txt')
    print(machine_code)



