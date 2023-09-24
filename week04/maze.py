from Lab03 import Stack

class Cell:
    def __init__(self, r, c):
        self.row = r
        self.col = c
    def __str__(self):
        return '(' + str(self.row) + ',' + str(self.col) + ')'

class Maze:
    MAZE_SIZE = 6
    def getMap(self):
        map = [['e', '1', '1', '1', '0', '1'],
               ['0', '1', '1', '1', '0', '1'],
               ['0', '0', '1', '1', '0', '0'],
               ['1', '0', '1', '1', '1', '0'],
               ['1', '0', '1', '0', '0', '0'],
               ['1', '0', '0', '0', '1', 'x']]
        
        return map
    
    def DEFStack(self):
        s =Stack()
        entry = Cell(0,0)
        s.push(entry)
        while (s.isEmpty() == False):
            here = s.pop()
            r=here.row
            c=here.col
            if (map[r][c]=='x'):
                return True
            else:
                map[r][c] = ','
                if self.isvalid(r,c-1):
                    s.push(Cell(r,c-1))
                elif self.isvalid(r, c+1):
                    s.push(Cell(r,c+1))
                elif self.isvalid(r-1,c):
                    s.push(Cell(r-1,c))
                elif self.isvalid(r+1,c):
                    s.push(Cell(r+1,c))
        return False