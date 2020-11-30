from Children import *
from Dirtiness import *
from Obstacle import *
from Robot import *
from Yard import *
from Empty import *
import random



class Environment:
    def __init__(self,n,m,dirtyP,obstacleP,childrenCount):
        self.environment = [ [ Empty() for j in range(0,m) ] for i in range(0,n) ]
        self.filas = n
        self.columnas = m
        self.childrenCount = childrenCount
        self.initalEnv(n,m,dirtyP,obstacleP,childrenCount)
        #self.environmentTest = [ [ Empty() for j in range(0,m) ] for i in range(0,n) ]
        # self.environmentTest[3][3] = Dirtiness()
        # self.environmentTest[2][2] = Dirtiness()
        #self.environmentTest[3][2] = Yard()
        #self.environmentTest[3][4] = (Yard(),Robot())
        #self.environmentTest[3][3] = (Yard(),Children())
        #self.environmentTest[3][5] = Yard()
        # self.environmentTest[1][1] = (Robot(),Children())

    def redistribucionRandom(self):
        l = []
        l1 = []
        for item in self.environment:
            for j in item:
                if (not (type(j) is Empty)) and not (type(j) is Yard or (type(j) is tuple and type(j[0]) is Yard)):
                    l.append(j)
                elif type(j) is Yard or (type(j) is tuple and type(j[0]) is Yard):
                    l1.append(j)
        temp = [ [ Empty() for j in range(0,self.columnas) ] for i in range(0,self.filas) ]
        self.environment = temp
        while len(l1) > 0:
            while True:
                rpos = (random.randint(0,self.filas-1),random.randint(0,self.columnas-1))
                if type(self.environment[rpos[0]][rpos[1]]) is Empty:
                    self.environment[rpos[0]][rpos[1]] = l1[0]
                    mt = l1[0]
                    l1.pop(0)
                    y = self.puttingYardRandom(self.filas,self.columnas,l1)
                    if len(y) == len(l1):
                        l1 = []
                        break
                    else:
                        l1.append(mt)
                        self.environment[rpos[0]][rpos[1]] = Empty()
        while len(l) > 0:
            c = 0
            while True:
                c += 1
                if c >= 100:
                    self.fix(l[0],temp)
                    l.pop(0)
                    break
                rpos = (random.randint(0,self.filas-1),random.randint(0,self.columnas-1))
                if type(temp[rpos[0]][rpos[1]]) is Empty:
                    temp[rpos[0]][rpos[1]] = l[0]
                    l.pop(0)
                    break
        self.environment = temp

    def checkDirtiness(self):
        c = 0
        for i in self.environment:
            for j in i:
                if type(j) is Dirtiness:
                    c += 1
        return (c*100) / (self.filas * self.columnas)

    def initalEnv(self,n,m,dirtyP,obstacleP,childrenCount):
        while True:
            rpos = (random.randint(0,n-1),random.randint(0,m-1))
            if type(self.environment[rpos[0]][rpos[1]]) is Empty:
                self.environment[rpos[0]][rpos[1]] = Yard()
                l1 = []
                for i in range(0,childrenCount-1):
                    l1.append(Yard())
                y = self.puttingYardRandom(n,m,l1)
                if len(y) == childrenCount - 1:
                    break
                else:
                    self.environment[rpos[0]][rpos[1]] = Empty()
        p = (dirtyP*(n*m)) // 100
        if p >= (n*m - childrenCount*2 - 1):
            p = n*m // 10
        boolean = True
        for i in range(0,p):
            c = 0
            if not boolean:
                x = 0
                for item in self.environment:
                    y = 0
                    for j in item:
                        if type(j) is Empty:
                            self.environment[x][y] = Dirtiness()
                        y += 1
                    x += 1
            while True and boolean:
                c += 1
                if c >= 100:
                    boolean = False
                    break
                rpos = (random.randint(0,n-1),random.randint(0,m-1))
                if type(self.environment[rpos[0]][rpos[1]]) is Empty:
                    self.environment[rpos[0]][rpos[1]] = Dirtiness()
                    break
        tmp = p
        p = (obstacleP*(n*m)) // 100
        if p >= (n*m - childrenCount*2 - 1 - tmp):
            p = n*m // 10
        boolean = True
        for i in range(0,p):
            c = 0
            if not boolean:
                x = 0
                for item in self.environment:
                    y = 0
                    for j in item:
                        if type(j) is Empty:
                            self.environment[x][y] = Dirtiness()
                        y += 1
                    x += 1
            while True and boolean:
                c += 1
                if c >= 100:
                    boolean = False
                    break
                rpos = (random.randint(0,n-1),random.randint(0,m-1))
                if type(self.environment[rpos[0]][rpos[1]]) is Empty:
                    self.environment[rpos[0]][rpos[1]] = Obstacle()
                    break
        for i in range(0,childrenCount):
            c = 0
            while True:
                c += 1
                if c >= 100:
                    self.fix(Children(),self.environment)
                    break
                rpos = (random.randint(0,n-1),random.randint(0,m-1))
                if type(self.environment[rpos[0]][rpos[1]]) is Empty:
                    self.environment[rpos[0]][rpos[1]] = Children()
                    break
        c = 0
        while True:
            c += 1
            if c >= 100:
                self.fix(Robot(),self.environment)
                break
            rpos = (random.randint(0,n-1),random.randint(0,m-1))
            if type(self.environment[rpos[0]][rpos[1]]) is Empty:
                self.environment[rpos[0]][rpos[1]] = Robot()
                break
    
    def fix(self,value,environment):
        x = 0
        for item in environment:
            y = 0
            for jtem in environment:
                if type(environment[x][y]) is Empty:
                    environment[x][y] = value
                y += 1
            x += 1

    def getYardPosition(self):
        result = []
        x = 0
        for i in self.environment:
            y = 0
            for j in i:
                if type(j) is Yard or (type(j) is tuple and type(j[0]) is Yard):
                    result.append((x,y))
                y += 1
            x += 1
        return result

    def puttingYardRandom(self,n,m,listYard):
        result = []
        pos  = 0
        boolean = True
        while boolean and not (len(result) == len(listYard)):
            l = self.getYardPosition()
            boolean = False
            for i in l:
                l1 = self.adyacentEmptyCount(i[0],i[1],n,m)
                if len(l1) > 0 and pos < len(listYard):
                    boolean = True
                    r = random.randint(0,len(l1)-1)
                    result.append(l1[r])
                    posi = l1[r][0]
                    posj = l1[r][1]
                    self.environment[posi][posj] = listYard[pos]
                    pos += 1
        if not (len(result) == len(listYard)):
            #print('ohoh ' + str(len(result)) + ' ' + str(temp))
            for i in result:
                self.environment[i[0]][i[1]] = Empty()
        return result

    def adyacentEmptyCount(self,i,j,n,m):
        resultList = []
        if (i-1) >= 0 and type(self.environment[i-1][j]) is Empty:
            resultList.append((i-1,j))
        if (j-1) >= 0 and type(self.environment[i][j-1]) is Empty:
            resultList.append((i,j-1))
        if (i+1) < n and type(self.environment[i+1][j]) is Empty:
            resultList.append((i+1,j))
        if (j+1) < m and type(self.environment[i][j+1]) is Empty:
            resultList.append((i,j+1))
        if (i+1) < n and (j+1) < m and type(self.environment[i+1][j+1]) is Empty:
            resultList.append((i+1,j+1))
        if (i+1) < n and (j-1) >= 0 and type(self.environment[i+1][j-1]) is Empty:
            resultList.append((i+1,j-1))
        if (i-1) >= 0 and (j+1) < m and type(self.environment[i-1][j+1]) is Empty:
            resultList.append((i-1,j+1))
        if (i-1) >= 0 and (j-1) >= 0 and type(self.environment[i-1][j-1]) is Empty:
            resultList.append((i-1,j-1))
        return resultList

    def getChildrenPosition(self):
        i = 0
        j = 0
        l = []
        for item in self.environment:
            j = 0
            for x in item:
                if type(x) is Children:
                    l.append((x,i,j))
                j += 1
            i += 1
        return l

    def EnvironmentTurn(self):
        l = self.getChildrenPosition()
        for i in l:
            self.environment = i[0].moving(self.environment,i[1],i[2],self.filas,self.columnas)
            if type(self.environment[i[1]][i[2]]) is Empty:
                self.environment = i[0].toDirty(i[1],i[2],self.environment,self.filas,self.columnas)
                
    def printE(self):
        for i in self.environment:
            for j in i:
                if type(j) is Yard:
                    print(Yard().symbol,end=" ")
                elif type(j) is Empty:
                    print(Empty().symbol,end=" ")
                elif type(j) is Robot:
                    print(Robot().symbol,end=" ")
                elif type(j) is Dirtiness:
                    print(Dirtiness().symbol,end=" ")
                elif type(j) is Obstacle:
                    print(Obstacle().symbol,end=" ")
                elif type(j) is Children:
                    print(Children().symbol,end=" ")
                elif type(j) is tuple and type(j[0]) is Yard and len(j) == 2:
                    if type(j[1]) is Children:
                        print(Yard().childrenSymbol,end=" ")
                    else:
                        print(Yard().robotSymbol,end=" ")
                elif type(j) is tuple and type(j[0]) is Yard and len(j) > 2:
                    print(Yard().childrenSymbol,end=" ")
                elif type(j) is tuple and type(j[0]) is Robot:
                    print(Robot().childrenSymbol,end=" ")
                elif type(j) is tuple and type(j[0]) is Dirtiness:
                    print(Robot().dirtinessSymbol,end=" ")
                else:
                    print('!')
            print()
        print('next turn')