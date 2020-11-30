from Empty import *
from Obstacle import *
from Dirtiness import *
import random

class Children:
    def __init__(self):
        self.symbol = '&'
        
    def toDirty(self,i,j,environment,n,m): 
        c = 0
        resultList = []
        if (i-1) >= 0 and type(environment[i-1][j]) is Empty:
            resultList.append((i-1,j))
        elif (i-1) >= 0 and type(environment[i-1][j]) is Children:
            c += 1
        if (j-1) >= 0 and type(environment[i][j-1]) is Empty:
            resultList.append((i,j-1))
        elif (j-1) >= 0 and type(environment[i][j-1]) is Children:
            c += 1
        if (i+1) < n and type(environment[i+1][j]) is Empty:
            resultList.append((i+1,j))
        elif (i+1) < n and type(environment[i+1][j]) is Children:
            c += 1
        if (j+1) < m and type(environment[i][j+1]) is Empty:
            resultList.append((i,j+1))
        elif (j+1) < m and type(environment[i][j+1]) is Children:
            c += 1
        if (i+1) < n and (j+1) < m and type(environment[i+1][j+1]) is Empty:
            resultList.append((i+1,j+1))
        elif (i+1) < n and (j+1) < m and type(environment[i+1][j+1]) is Children:
            c += 1
        if (i+1) < n and (j-1) >= 0 and type(environment[i+1][j-1]) is Empty:
            resultList.append((i+1,j-1))
        elif (i+1) < n and (j-1) >= 0 and type(environment[i+1][j-1]) is Children:
            c += 1
        if (i-1) >= 0 and (j+1) < m and type(environment[i-1][j+1]) is Empty:
            resultList.append((i-1,j+1))
        elif (i-1) >= 0 and (j+1) < m and type(environment[i-1][j+1]) is Children:
            c += 1
        if (i-1) >= 0 and (j-1) >= 0 and type(environment[i-1][j-1]) is Empty:
            resultList.append((i-1,j-1))
        elif (i-1) >= 0 and (j-1) >= 0 and type(environment[i-1][j-1]) is Children:
            c += 1
        if c == 2:
            c = 3
        elif c >= 3:
            c = 6
        for y in range(0,c):
            if len(resultList) > 0:
                r = random.randint(0,len(resultList)-1)
                environment[resultList[r][0]][resultList[r][1]] = Dirtiness()
                resultList.remove(resultList[r])
        return environment

    def moving(self,environment,i,j,n,m):
        l = self.adyacentPossiblesCount(environment,i,j,n,m)
        r = random.randint(0,1)
        if len(l) > 0 and r > 0:
            r = random.randint(0,len(l) - 1)
            if type(environment[l[r][0]][l[r][1]]) is Empty:
                environment[i][j] = Empty()
                environment[l[r][0]][l[r][1]] = self
            else:
                environment = self.movObstacle(environment,i,j,l[r][0],l[r][1],n,m) 
        return environment

    def movObstacle(self,environment,i,j,x,y,n,m):
        tempi = x - i
        tempj = y - j
        while True:
            x += tempi
            y += tempj
            if x < 0 or y < 0 or x >= n or y >= m:
                break
            elif type(environment[x][y]) is Empty:
                environment[x][y] = Obstacle()
                environment[i][j] = Empty()
                environment[i+tempi][j+tempj] = self
                break
            elif type(environment[x][y]) is Obstacle:
                pass
            else:
                break
        return environment

    def adyacentPossiblesCount(self,environment,i,j,n,m):
        resultList = []
        if (i-1) >= 0 and (type(environment[i-1][j]) is Empty or type(environment[i-1][j]) is Obstacle):
            resultList.append((i-1,j))
        if (j-1) >= 0 and (type(environment[i][j-1]) is Empty or type(environment[i][j-1]) is Obstacle):
            resultList.append((i,j-1))
        if (i+1) < n and (type(environment[i+1][j]) is Empty or type(environment[i+1][j]) is Obstacle):
            resultList.append((i+1,j))
        if (j+1) < m and (type(environment[i][j+1]) is Empty or type(environment[i][j+1]) is Obstacle):
            resultList.append((i,j+1))
        if (i+1) < n and (j+1) < m and (type(environment[i+1][j+1]) is Empty or type(environment[i+1][j+1]) is Obstacle):
            resultList.append((i+1,j+1))
        if (i+1) < n and (j-1) >= 0 and (type(environment[i+1][j-1]) is Empty or type(environment[i+1][j-1]) is Obstacle):
            resultList.append((i+1,j-1))
        if (i-1) >= 0 and (j+1) < m and (type(environment[i-1][j+1]) is Empty or type(environment[i-1][j+1]) is Obstacle):
            resultList.append((i-1,j+1))
        if (i-1) >= 0 and (j-1) >= 0 and (type(environment[i-1][j-1]) is Empty or type(environment[i-1][j-1]) is Obstacle):
            resultList.append((i-1,j-1))
        return resultList