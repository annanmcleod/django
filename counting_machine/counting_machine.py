

# function is initialized
class Count:
    def __init__ (self, inc, dec):
        self.inc = inc
        self.dec = dec

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1

class CountingMachine(Count):
    def __init__ (self):
        self.count = 0

    


