from random import choice, randint

class Problem:
    instances = []

    def __init__(self, numcount=2, operator=[" + ", " - "],
                 interval=[-1000, 1000], decimal=0):
        self.numcount = numcount
        self.operator = operator
        self.interval = interval
        self.decimal = decimal
        if not hasattr(self, 'problemx'):
            self.generate_problem()
        Problem.instances.append(self)

    def generate_problem(self):
        numbers = []
        number = int
        problemstr = ""
        for i in range(self.numcount):
            modifier = 10 ** self.decimal
            number = randint(self.interval[0] * modifier,
                             self.interval[1] * modifier) / modifier
            # modifier is for getting decimal numbers
            numbers.append(str(number) if number >= 0 else "(" + str(number) + ")")
        for j in numbers:
            operator = choice(self.operator)
            problemstr = problemstr + str(j) + operator
            self.problemx = problemstr[:-3] + " = "  # [:-3]-because last redundant operator

    def __str__(self) -> str:
        return self.problemx

p = Problem(5, [" / ", " * "], interval=[0, 50], decimal=3)
p = Problem(5,[" / ", " * "],interval=[0,50],decimal=3)
d = Problem(2)
print(p)
print(p)
print(d)
print(d)




