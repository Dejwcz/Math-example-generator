from random import choice
from random import randint

class problem():
    

    def __init__(self, numcount = 2, operator = [" + "," - "],
                 interval = [-1000,1000], decimal = 0):
        self.numcount = numcount
        self.operator = operator
        self.interval = interval
        self.decimal = decimal
        self.numbers = []
        self.operators = []
        self.generate_problem()
        
# def __str__(self) -> str:
#     numbers = []
#     number = int
#     problemstr = ""
#     for i in range(self.numcount):
#         modifier = 10**self.decimal
#         number = randint(self.interval[0]*modifier,
#                          self.interval[1]*modifier)/modifier
#         # modifier is for getting decimal numbers
#         numbers.append(str(number) if number>=0 else "("+str(number)+")") 
#     for j in numbers:
#         operator = choice(self.operator)
#         problemstr = problemstr + str(j) + operator
#         self.problemx = problemstr[:-3] + " = " #[:-3]-because last redundant operator
#     return self.problemx
    
    def generate_problem(self):
        modifier = 10**self.decimal
        for i in range(self.numcount):
            self.numbers.append(randint(self.interval[0]*modifier,
                         self.interval[1]*modifier)/modifier)
        for j in range(self.numcount-1):
            self.operators.append(choice(self.operator))

    def __str__(self) -> str:
        return (str(self.numbers) + str(self.operators))
        
p = problem(5,[" / ", " * "],interval=[0,50],decimal=3)
d = problem(2)
print(p)
print(p)
print(d)
print(d)


