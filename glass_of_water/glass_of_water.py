class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        self.amount += amount
        if self.amount > self.capacity:
            self.amount = self.capacity

    def pour_out(self, amount):
        self.amount -= amount
        if self.amount <= 0:
            self.amount = 0

# glass1 amount does not change for pour in
# glass2 amount does change until it reaches an amount of 5
# glass3 amount continues changing till it reaches 123

# glass1 amount starts at 2 and doesn't go below 0
# glass2 amount starts at 5 and doesn't go below 5
# glass3 amount starts at 123 and continues to go down.