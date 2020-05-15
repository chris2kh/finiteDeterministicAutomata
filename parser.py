#!/usr/bin/python
import re

myFile = open("example.txt", "r").readlines()

program = {
    "DESCRIPTION" : '',
    "STATES" : '',
    "TOKENS" : '',
    "TRANSITION" : '',
    "START_STATE" : '',
    "ACCEPT_STATES" : ''
}

# record in dictionary each line(s) where each automaton attribute appears 
for line in myFile:
    for attribute in program:    
        if line.startswith(attribute):
            program[attribute] = line
            lastParsedAttribute = attribute #for later use in case of multiline attribute definition
            break

    # ignore newlines and comments
    if line.startswith("\n") or line.startswith("//"):
        pass
    elif not line.startswith(lastParsedAttribute):
        # line is a continuation of last parsed attribute, so append it
        program[lastParsedAttribute] += line


# now we can parse corresponding line(s) for each attribute using regular expressions

states = []
for state in re.findall(r'"([^"]*)"',program["STATES"]):
  states.append(state)
program["STATES"] = states

tokens = []
for token in re.findall(r'"([^"]*)"',program["TOKENS"]):
  tokens.append(token)  
program["TOKENS"] = tokens

transition = []
for parsedRow in re.findall(r'\[([^\[]*)\]',program["TRANSITION"]):
  row = []
  for outcome in re.findall(r'"([^"]*)"',parsedRow):
    row.append(outcome)
  transition.append(row)
program["TRANSITION"] = transition

program["START_STATE"] = re.findall(r'"([^"]*)"', program["START_STATE"])[0]

acceptStates = []
for accepted in re.findall(r'"([^"]*)"', program["ACCEPT_STATES"]):
  acceptStates.append(accepted)      
program["ACCEPT_STATES"] = acceptStates
