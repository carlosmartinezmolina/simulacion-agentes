from Obstacle import *
from Children import *
from Dirtiness import *
from Yard import *
from Empty import *

class Robot:
    def __init__(self):
        self.symbol = '@'
        self.childrenSymbol = '+'
        self.dirtinessSymbol = '^'

    def movPolicy2(self,environment):
        l = self.getDirtinessPosition(environment)
        if len(l) == 0:
            #print('game completed')
            return 'exit'
        posRobot = (-1,-1)
        posRobotWithChildren = (-1,-1) 
        for i in range(0,len(environment)):
            for j in range(0,len(environment[i])):
                if type(environment[i][j]) is Robot or (type(environment[i][j]) is tuple and (type(environment[i][j][0]) is Dirtiness or (type(environment[i][j][1]) is Robot and type(environment[i][j][0]) is Yard) or (len(environment[i][j]) > 2 and not (type(environment[i][j][2]) is Dirtiness)))):
                    posRobot = (i,j)
                    break
                if type(environment[i][j]) is tuple and (type(environment[i][j][0]) is Robot or (len(environment[i][j]) > 2 and type(environment[i][j][2]) is Dirtiness)):
                    posRobotWithChildren = (i,j)
                    break
        if not (posRobot[0] == -1):
            self.movWithoutChildren2(environment,posRobot)
        elif not (posRobotWithChildren[0] == -1):
            for i in range(0,2):
                if not (type(environment[posRobotWithChildren[0]][posRobotWithChildren[1]]) is tuple):
                    break
                else:
                    temp = self.movWithChildren2(environment,posRobotWithChildren)
                    if not (temp[0][0] == 1000000):
                        posRobotWithChildren = temp[0]
                    if not temp[1]:
                        break
        else:
            self.printE(environment)
            print('no robot exist!')
        return ''

    def movPolicy1(self,environment):
        l = self.getDirtinessPosition(environment)
        if len(l) == 0:
            #print('game completed')
            return 'exit'
        posRobot = (-1,-1)
        posRobotWithChildren = (-1,-1) 
        for i in range(0,len(environment)):
            for j in range(0,len(environment[i])):
                if type(environment[i][j]) is Robot or (type(environment[i][j]) is tuple and (type(environment[i][j][0]) is Dirtiness or (type(environment[i][j][1]) is Robot and type(environment[i][j][0]) is Yard) or (len(environment[i][j]) > 2 and not (type(environment[i][j][2]) is Dirtiness)))):
                    posRobot = (i,j)
                    break
                if type(environment[i][j]) is tuple and (type(environment[i][j][0]) is Robot or (len(environment[i][j]) > 2 and type(environment[i][j][2]) is Dirtiness)):
                    posRobotWithChildren = (i,j)
                    break
        if not (posRobot[0] == -1):
            self.movWithoutChildren(environment,posRobot)
        elif not (posRobotWithChildren[0] == -1):
            for i in range(0,2):
                if not (type(environment[posRobotWithChildren[0]][posRobotWithChildren[1]]) is tuple):
                    break
                if len(environment[posRobotWithChildren[0]][posRobotWithChildren[1]]) > 2:
                    environment[posRobotWithChildren[0]][posRobotWithChildren[1]] = (self,Children())
                    break
                else:
                    temp = self.movWithChildren(environment,posRobotWithChildren)
                    if not (temp[0][0] == 1000000):
                        posRobotWithChildren = temp[0]
                    if not temp[1]:
                        break
        else:
            print('no robot exist!')
        return ''
    
    def movWithoutChildren(self,environment,posRobot):
        possibleMoves = self.getPossibleMoves(environment,posRobot[0],posRobot[1],len(environment),len(environment[0]))
        if len(possibleMoves) > 0:
            if type(environment[posRobot[0]][posRobot[1]]) is tuple and len(environment[posRobot[0]][posRobot[1]]) > 2 and type(environment[posRobot[0]][posRobot[1]][1]) is Robot:
                environment[posRobot[0]][posRobot[1]] = (Yard(),Children(),self)
            elif not (self.typeCheck(possibleMoves,Children,environment) == (-1,-1)):
                pos = self.typeCheck(possibleMoves,Children,environment)
                environment[pos[0]][pos[1]] = (self,environment[pos[0]][pos[1]])
                if type(environment[posRobot[0]][posRobot[1]]) is Robot:
                    environment[posRobot[0]][posRobot[1]] = Empty()
                elif type(environment[posRobot[0]][posRobot[1]]) is tuple:
                    if type(environment[posRobot[0]][posRobot[1]][0]) is Dirtiness:
                        environment[posRobot[0]][posRobot[1]] = Dirtiness()
                    elif len(environment[posRobot[0]][posRobot[1]]) > 2:
                        environment[posRobot[0]][posRobot[1]] = (Yard(),Children())
                    else:
                        environment[posRobot[0]][posRobot[1]] = Yard()
            elif not (self.typeCheck(possibleMoves,Dirtiness,environment) == (-1,-1)):
                if type(environment[posRobot[0]][posRobot[1]]) is tuple and type(environment[posRobot[0]][posRobot[1]][0]) is Dirtiness:
                    environment[posRobot[0]][posRobot[1]] = self
                else:
                    pos = self.typeCheck(possibleMoves,Dirtiness,environment)
                    environment[pos[0]][pos[1]] = (environment[pos[0]][pos[1]],self)
                    if type(environment[posRobot[0]][posRobot[1]]) is tuple:
                        if len(environment[posRobot[0]][posRobot[1]]) > 2:
                            environment[posRobot[0]][posRobot[1]] = (Yard(),Children())
                        else:
                            environment[posRobot[0]][posRobot[1]] = Yard()
                    else:
                        environment[posRobot[0]][posRobot[1]] = Empty()
            else:
                if type(environment[posRobot[0]][posRobot[1]]) is tuple and type(environment[posRobot[0]][posRobot[1]][0]) is Dirtiness:
                        environment[posRobot[0]][posRobot[1]] = self
                else:
                    pos = self.chosePosition(self.getChildrenPosition(environment),possibleMoves)
                    if pos[0] == 1000000:
                        pos = self.chosePosition(self.getDirtinessPosition(environment),possibleMoves)
                    if pos[0] == 1000000:
                        return
                    if type(environment[pos[0]][pos[1]]) is Empty:
                        environment[pos[0]][pos[1]] = self
                        if type(environment[posRobot[0]][posRobot[1]]) is tuple:
                            if len(environment[posRobot[0]][posRobot[1]]) > 2:
                                environment[posRobot[0]][posRobot[1]] = (Yard(),Children())
                            else:
                                environment[posRobot[0]][posRobot[1]] = Yard()
                        else:
                            environment[posRobot[0]][posRobot[1]] = Empty()
                    else:
                        environment[pos[0]][pos[1]] = (Yard(),self)
                        if type(environment[posRobot[0]][posRobot[1]]) is tuple:
                            if len(environment[posRobot[0]][posRobot[1]]) > 2:
                                environment[posRobot[0]][posRobot[1]] = (Yard(),Children())
                            else:
                                environment[posRobot[0]][posRobot[1]] = Yard()
                        else:
                            environment[posRobot[0]][posRobot[1]] = Empty()

    def movWithoutChildren2(self,environment,posRobot):
        possibleMoves = self.getPossibleMoves(environment,posRobot[0],posRobot[1],len(environment),len(environment[0]))
        if len(possibleMoves) > 0:
            l = self.getChildrenPosition(environment)
            r = self.chosePosition(l,possibleMoves)
            if r[1] == 1000000:
                temp = self.getDirtinessPosition(environment)
                r = self.chosePosition(temp,possibleMoves)
                if r[1] == 1000000:
                    return
                if type(environment[posRobot[0]][posRobot[1]]) is tuple and type(environment[posRobot[0]][posRobot[1]][0]) is Dirtiness:
                    environment[posRobot[0]][posRobot[1]] = self
                    return
            if type(environment[posRobot[0]][posRobot[1]]) is tuple and len(environment[posRobot[0]][posRobot[1]]) > 2 and type(environment[posRobot[0]][posRobot[1]][1]) is Robot:
                environment[posRobot[0]][posRobot[1]] = (Yard(),Children(),self)
            elif not (self.typeCheck(possibleMoves,Children,environment) == (-1,-1)):
                pos = self.typeCheck(possibleMoves,Children,environment)
                environment[pos[0]][pos[1]] = (self,environment[pos[0]][pos[1]])
                if type(environment[posRobot[0]][posRobot[1]]) is Robot:
                    environment[posRobot[0]][posRobot[1]] = Empty()
                elif type(environment[posRobot[0]][posRobot[1]]) is tuple:
                    if type(environment[posRobot[0]][posRobot[1]][0]) is Dirtiness:
                        environment[posRobot[0]][posRobot[1]] = Dirtiness()
                    elif len(environment[posRobot[0]][posRobot[1]]) > 2:
                        environment[posRobot[0]][posRobot[1]] = (Yard(),Children())
                    else:
                        environment[posRobot[0]][posRobot[1]] = Yard()
            else:
                if type(environment[r[0]][r[1]]) is Empty:
                    environment[r[0]][r[1]] = self
                    if type(environment[posRobot[0]][posRobot[1]]) is tuple:
                        if len(environment[posRobot[0]][posRobot[1]]) > 2:
                            environment[posRobot[0]][posRobot[1]] = (environment[posRobot[0]][posRobot[1]][0],environment[posRobot[0]][posRobot[1]][1])
                        else:
                            environment[posRobot[0]][posRobot[1]] = environment[posRobot[0]][posRobot[1]][0]
                    else:
                        environment[posRobot[0]][posRobot[1]] = Empty()
                else:
                    environment[r[0]][r[1]] = (environment[r[0]][r[1]],self)
                    if type(environment[posRobot[0]][posRobot[1]]) is tuple:
                        if len(environment[posRobot[0]][posRobot[1]]) > 2:
                            environment[posRobot[0]][posRobot[1]] = (environment[posRobot[0]][posRobot[1]][0],environment[posRobot[0]][posRobot[1]][1])
                        else:
                            environment[posRobot[0]][posRobot[1]] = environment[posRobot[0]][posRobot[1]][0]
                    else:
                        environment[posRobot[0]][posRobot[1]] = Empty()

    def movWithChildren(self,environment,posRobot):
        boolean = True
        possible = self.getPossibleMoves(environment,posRobot[0],posRobot[1],len(environment),len(environment[0]))
        possibleMoves = []
        for i in possible:
            if not (type(environment[i[0]][i[1]]) is Children):
                possibleMoves.append(i) 
        yardPosition = self.getYardPosition(environment)
        pos = self.chosePosition(yardPosition,possibleMoves)
        if pos[0] == 1000000:
            return (pos,False)
        if type(environment[pos[0]][pos[1]]) is Dirtiness:
            environment[pos[0]][pos[1]] = (self,Children(),Dirtiness())
            environment[posRobot[0]][posRobot[1]] = Empty()
        elif type(environment[pos[0]][pos[1]]) is Empty:
            environment[pos[0]][pos[1]] = environment[posRobot[0]][posRobot[1]]
            environment[posRobot[0]][posRobot[1]] = Empty()
        elif type(environment[pos[0]][pos[1]]) is Yard:
            environment[pos[0]][pos[1]] = (Yard(),self,Children)
            environment[posRobot[0]][posRobot[1]] = Empty()
            boolean = False
        return (pos,boolean)

    def movWithChildren2(self,environment,posRobot):
        boolean = True
        possible = self.getPossibleMoves(environment,posRobot[0],posRobot[1],len(environment),len(environment[0]))
        possibleMoves = []
        for i in possible:
            if not (type(environment[i[0]][i[1]]) is Children):
                possibleMoves.append(i)
        yardPosition = self.getYardPosition(environment)
        # print(posRobot)
        # print(environment[posRobot[0]][posRobot[1]])
        # print(possibleMoves)
        pos = self.chosePosition(yardPosition,possibleMoves)
        if pos[0] == 1000000:
            return (pos,False)
        # print(pos)
        # print(environment[pos[0]][pos[1]])
        if type(environment[pos[0]][pos[1]]) is Dirtiness:
            environment[pos[0]][pos[1]] = (self,Children(),Dirtiness())
        elif type(environment[pos[0]][pos[1]]) is Empty:
            environment[pos[0]][pos[1]] = (self,Children())
        elif type(environment[pos[0]][pos[1]]) is Yard:
            environment[pos[0]][pos[1]] = (Yard(),self,Children)
            boolean = False

        if len(environment[posRobot[0]][posRobot[1]]) == 2 and type(environment[posRobot[0]][posRobot[1]][0]) is Robot:
            environment[posRobot[0]][posRobot[1]] = Empty()
        else:
            environment[posRobot[0]][posRobot[1]] = Dirtiness()
        
        return (pos,boolean)

    def typeCheck(self,possibleMoves,_type,environment):
        for item in possibleMoves:
            if type(environment[item[0]][item[1]]) is _type:
                return item
        return (-1,-1)

    def getPossibleMoves(self,environment,i,j,n,m):
        resultList = []
        if (i-1) >= 0 and not (type(environment[i-1][j]) is Obstacle or type(environment[i-1][j]) is tuple):
            resultList.append((i-1,j))
        if (j-1) >= 0 and not (type(environment[i][j-1]) is Obstacle or type(environment[i][j-1]) is tuple):
            resultList.append((i,j-1))
        if (i+1) < n and not (type(environment[i+1][j]) is Obstacle or type(environment[i+1][j]) is tuple):
            resultList.append((i+1,j))
        if (j+1) < m and not (type(environment[i][j+1]) is Obstacle or type(environment[i][j+1]) is tuple):
            resultList.append((i,j+1))
        if (i+1) < n and (j+1) < m and not (type(environment[i+1][j+1]) is Obstacle or type(environment[i+1][j+1]) is tuple):
            resultList.append((i+1,j+1))
        if (i+1) < n and (j-1) >= 0 and not (type(environment[i+1][j-1]) is Obstacle or type(environment[i+1][j-1]) is tuple):
            resultList.append((i+1,j-1))
        if (i-1) >= 0 and (j+1) < m and not (type(environment[i-1][j+1]) is Obstacle or type(environment[i-1][j+1]) is tuple):
            resultList.append((i-1,j+1))
        if (i-1) >= 0 and (j-1) >= 0 and not (type(environment[i-1][j-1]) is Obstacle or type(environment[i-1][j-1]) is tuple):
            resultList.append((i-1,j-1))
        return resultList

    def getYardPosition(self,environment):
            i = 0
            j = 0
            l = []
            for item in environment:
                j = 0
                for x in item:
                    if type(x) is Yard:
                        l.append((i,j))
                    j += 1
                i += 1
            return l

    def getChildrenPosition(self,environment):
        i = 0
        j = 0
        l = []
        for item in environment:
            j = 0
            for x in item:
                if type(x) is Children:
                    l.append((i,j))
                j += 1
            i += 1
        return l

    def getDirtinessPosition(self,environment):
        i = 0
        l = []
        for item in environment:
            j = 0
            for x in item:
                if type(x) is Dirtiness:
                    l.append((i,j))
                j += 1
            i += 1
        if len(l) == 0:
            i = 0
            for item in environment:
                j = 0
                for x in item:
                    if type(x) is tuple and type(x[0]) is Dirtiness:
                        environment[i][j] = Robot()
                    j += 1
                i += 1
        return l

    def chosePosition(self,childrenPosition,possibleMoves):
        result = (1000000,1000000)
        for i in childrenPosition:
            for j in possibleMoves:
                distM = abs(i[0] - j[0]) + abs(i[1] - j[1])
                if distM < result[0]:
                    result = (distM,j)
        if result[1] == 1000000:
            return result
        return result[1]

    def printE(self,environment):
        for i in environment:
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
