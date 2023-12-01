from random import choice
from random import randint

class Problem():
    
    def __init__(self, numcount = 2, operator = [" + "," - "],
                 interval = [-1000,1000], decimal = 0):
        self.numcount = numcount
        self.operator = operator
        self.interval = interval
        self.decimal = decimal
        self.numbers = []
        self.operators = []
        self.generate_problem()
        self.result = self.solve_it()
       
    def generate_problem(self):
        modifier = 10**self.decimal
        for i in range(self.numcount):
            self.numbers.append(randint(self.interval[0]*modifier,
                         self.interval[1]*modifier)/modifier)
        for j in range(self.numcount-1):
            self.operators.append(choice(self.operator))

    def __str__(self) -> str:
        problemstr = ""
        for i in range(len(self.operators)):
            problemstr = problemstr + \
                (str(self.numbers[i]) if self.numbers[i] >= 0
                else "("+str(self.numbers[i])+")")+self.operators[i]
        problemstr = problemstr+\
            (str(self.numbers[-1]) if self.numbers[-1] >= 0
            else "("+str(self.numbers[-1])+")")+ " = "
        return problemstr
    
    def __len__(self):
        return len(self.__str__())
    
    def solve_it(self):
        help_result = self.numbers[0]
        for i in range(len(self.numbers)-1):
            if self.operators[i] == " + ":
                help_result += self.numbers[i+1]
            elif self.operators[i] == " - ":
                help_result -= self.numbers[i+1]
            elif self.operators[i] == " * ":
                help_result *= self.numbers[i+1]
            elif self.operators[i] == " / ":
                help_result /= self.numbers[i+1]
        return round(help_result,self.decimal)
    
    def whole_example(self):
        return self.__str__() + str(self.solve_it())




        
#p = Problem(5,[" / ", " * "," + "],interval=[-50,50],decimal=3)
#d = Problem(2, [" + "])
#print(p)
#print(p.solve_it())
#print(p.whole_example())
#print(d)
#print(d.solve_it())
#print(len(d))




