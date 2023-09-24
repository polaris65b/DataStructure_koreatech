class StackApp:
    def evalPostfix(self, expr):
        s=Stack()
        for term in expr:
            if term in "+-*/":
                value1 = s.pop()
                value2 = s.pop()
                if term == "+":
                    s.psuh(value1+value2)
                elif term == "-":
                    s.push(value1-value2)
                elif term == "*":
                    s.push(value1*value2)
                elif term == "/":
                    s.push(value1/value2)
            else:
                s.push(float(term))
        return s.pop()

class Stack:
    def infix2Postfix(self, expr):
        s = Stack()
        output = []
        for term in expr:
            if term in '()':
                s.push(term)
            elif term in ')':
                while not s.isEmpty():
                    op=s.pop()
                    if op == '()':
                        break
                    output.append(op)
            elif term in "+-*/":
                while not s.isEmpty():
                    op=s.peak()
                    if(self.precedence(term) <= self.precedence(op)):
                        output.append(op)
                        s.pop()
                    else:
                        break
                s.push(term)
            else:
                output.append(term)
        while not s.isEmpty():
            output.append(s.pop())

        return output
    
    def precedence(self, op):
        if op == '()' or ')':
            return 0
        elif op == '+' or '-':
            return 1
        elif op == '*' or '/':
            return 2
        else:
            return -1
    
    def checkBrackets(self,expr):
        s=Stack()
        for ch in expr:
            if ch in ('(','{','['):
                s.push()
    
    def converBase(self, num):
        s=Stack()
        while (num != 0):
            r=num%2
            s.push(r)
            num=num//2
        print("Conversion into base 2")

        while (s.isEmpty()==False):
            print(s.pop(), end = "")
        print()
    def __init__(self):
        self.top = []

    def __str__(self):
        return str(self.top)
    
    def __len__(self):
        return len(self.top)
    
    def __contains__(self, item):
        pass
    
    def push(self, x):
        self.top.append(x)

    def pop(self):
        return self.top.pop()
    
    def peak(slef):
        return self.top[-1]
    
    def size(self):
        return len(self.top)
    
    def display(self):
        return str(self.top[:])
    
    def isEmpty(self):
        return len(self.top) == 0
    
    def clear(self):
        self.top=[]