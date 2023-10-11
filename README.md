# Stanley-Penguin-Assembler
An **assembler** for the CPU named "Stanley/Penguin" with an *infamously* fluid syntax.

Stanley/Penguin is a humble processor with not-so-staggering specs. 

### Specifications

- The **Accumulator**, abbreviated 'A' which is a 32-bit register that stores our values; this is basically a 32-bit register, and every operation that the machine does will involve this part.
    
- The **Instruction Pointer**, abbreviated 'IP' which is another 32-bit register, which is specially used to hold the address of the next instruction that is to be executed.
    
- **256 MiB words of memory**, each of which is 32-bits wide, which is abbreviated 'M'; remember one MiB or Mebibyte is different than a Megabyte. A Megabyte is 1 million bytes but a Mebibyte is 1024 * 1024 or 220 bytes, which is actually 1,048,576 bytes.
    
- The **ports** to which we can write information, and from which we can also read input; these are abbreviated 'P' Note that ports are randomly selected from the memory space and are used for input and output as if from external devices like keyboards, screens, printers, etc. The selection of the port address is made so that it won't conflict with other memory locations which the program may need to use for storage.
   
[Source](https://bjohnson.lmu.build/cmsi2210web/week06.html) for the specifications.
    
In order to start, we need a solid **instruction set**. I will take the liberty of yanking this table from a website that neatly lays out the instruction set for the processor "Stanley/Penguin":

<pre>
opcode |        Action         |  Mnemonic  |               Meaning
  0    |       A := M[x]       |    LOAD    |   Load the Accumulator from memory address [x]
  1    |       M[x] := A       |    STORE   |   Store accumulator to memory 
  2    |       A :=P[x]	       |    READ    |   Read from a port into the accumulator
  3    |       P[x] := A       |    WRITE   |   Write accumulator out to a port
  4    |     A := A + M[x]     |    ADD	    |   Add into accumulator
  5    |     A := A - M[x]     |    SUB	    |   Subtract from accumulator  
  6    |     A := A × M[x]     |    MUL	    |   Multiply into accumulator  
  7    |     A := A ÷ M[x]     |    DIV	    |   Divide accumulator  
  8    |    A := A mod M[x]    |    MOD	    |   Modulo  
  9    |     A := A & M[x]     |    AND	    |   Bitwise AND  
  A    |     A := A | M[x]     |    OR	    |   Bitwise OR  
  B    |     A := A ^ M[x]     |    XOR	    |   Bitwise XOR  
  C    |       IP := x         |    JMP	    |   Set IP to jump to new address for next instruction  
  D    | if A = 0 then IP := x |    JZ	    |   Jump if accumulator is zero  
  E    | if A < 0 then IP := x |    JLZ	    |   Jump if accumulator is less than zero  
  F    | if A > 0 then IP := x |    JGZ	    |   Jump if accumulator is greater than zero
  </pre>
[Source](https://bjohnson.lmu.build/cmsi2210web/week06.html) for the table.

This program will take in a text file containing properly written Stanley/Penguin code, which is ***very arbitrary*** as I am starting this project, and convert it to machine code following the instruction set. I plan on using python to handle file reading/writing.
