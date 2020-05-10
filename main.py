#!/usr/bin/python
from parser import program
from automata import Automaton, Tape

print("Welcome to this little DFA project\n")
print(program["DESCRIPTION"])	
message = raw_input("Please write the input you want to evaluate:  ")
tape = Tape(message)
automaton = Automaton(program)

success = automaton.run(tape)
if success:
    print("this input is valid for this automaton!! :)")
else: 
    print("this input is not valid for this automaton :(")