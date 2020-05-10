#!/usr/bin/python

class Automaton():
    def __init__(self,program):
        self.program = program
        self.program["currentState"] = program["START_STATE"]

    def run(self, tape):
        if tape.isOver():
            return self.decision()
        else:
            self.makeTransition(tape)
            return self.run(tape.shift())

    def makeTransition(self, tape):
        s = self.program["STATES"].index(self.program["currentState"])
        t = self.program["TOKENS"].index(tape.currentToken())
        self.program["currentState"] = self.program["TRANSITION"][s][t]

    def decision(self):
        return self.program["currentState"] in self.program["ACCEPT_STATES"] 


class Tape():
    def __init__(self,message):
        self.message = message

    def isOver(self):
        return self.message == ""

    def currentToken(self):
        return self.message[0]

    def shift(self):
        self.message = self.message[1:]
        return self