from random import choice
from random import randint

class Example():
    """
    Generate math example depending on inserted parameters.
    """
    def __init__(self, numcount = 2, operator = [" + "," - "],
                 interval = [-1000,1000], decimal = 0):
        if type(numcount) != int:
            raise TypeError("Integer expected")
        if numcount < 2:
            raise ValueError("You need two or more numbers")
        self.numcount = numcount
        for i in operator:
            if i not in [" + "," - "," * "," / "]:
                raise ValueError("Defined operator expected")
        self.operator = operator
        if type(interval[0]) != int or type(interval[1]) != int:
            raise TypeError("Integer expexted")
        if interval[0] > interval[1]:
            raise ValueError("End of interval must be bigger than start")
        self.interval = interval
        if type(decimal) != int:
            raise TypeError("Integer expected")
        if decimal not in range(0,16):
            raise ValueError("Maximum is 15 decimal numbers")
        self.decimal = decimal
        self._numbers_ = []
        self._operators_ = []
        self.generate_problem()
        self._result_ = self.solve_it()
       
    def generate_problem(self):
        modifier = 10**self.decimal
        if self.decimal == 0:
            for i in range(self.numcount):
                self._numbers_.append(randint(self.interval[0],
                         self.interval[1]))
        else: 
            for i in range(self.numcount):
                 self._numbers_.append(randint(self.interval[0]*modifier,
                         self.interval[1]*modifier)/modifier)
        for j in range(self.numcount-1):
            self._operators_.append(choice(self.operator))

    def __str__(self) -> str:
        problemstr = ""
        for i in range(len(self._operators_)):
            problemstr = problemstr + \
                (str(self._numbers_[i]) if self._numbers_[i] >= 0
                else "("+str(self._numbers_[i])+")")+self._operators_[i]
        problemstr = problemstr+\
            (str(self._numbers_[-1]) if self._numbers_[-1] >= 0
            else "("+str(self._numbers_[-1])+")")+ " = "
        return problemstr
    
    def __len__(self):
        return len(self.__str__())
    
    def solve_it(self):
        div = False
        help_result = self._numbers_[0]
        for i in range(len(self._numbers_)-1):
            if self._operators_[i] == " + ":
                help_result += self._numbers_[i+1]
            elif self._operators_[i] == " - ":
                help_result -= self._numbers_[i+1]
            elif self._operators_[i] == " * ":
                help_result *= self._numbers_[i+1]
            elif self._operators_[i] == " / ":
                help_result /= self._numbers_[i+1]
                div = True
        return help_result if div else round(help_result,self.decimal)
    
    def whole_example(self):
        return self.__str__() + str(self.solve_it())

#p = Example(5,[" / ", " * "," + "],interval=[-50,50],decimal=0,divint=True)
#d = Example(2, [" + "])
#print(p)
#print(p.solve_it())
#print(p.whole_example())
#print(d)
#print(d.solve_it())
#print(len(d))




