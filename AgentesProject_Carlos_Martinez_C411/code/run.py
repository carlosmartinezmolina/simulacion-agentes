from Environment import *
from Children import *
from Robot import *
import time





def main():
    # n = (int)input('Escribe la cantidad de filas: ')
    # m = (int)input('Escribe la cantidad de columnas: ')
    # dirtyP = (int)input('Escribe el porciento de basura: ')
    # obstacleP = (int)input('Escribe el porciento de obstaculos: ')
    # childrenCount = (int)input('Escribe la cantidad de niños: ')
    # t = (int)input('Escribe cada cuantas unidades de tiempo cambia el ambiente: ')
    # e = Environment(n,m,dirtyP,obstacleP,childrenCount)
    r = mySimulation()
    print()
    print('Promedio de todas las simulaciones')
    print('Porciento de casillas sucias medio: ' + str(r[0]))
    print('Veces que el robot fue despedido : ' + str(r[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(r[2]))
    #simulation()
    


def mySimulation():
    finalResult = (0,0,0)
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(6,6,15,20,1,6,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(6,6,15,20,1,6,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 6x6,15 por ciento de basura ,20 por ciento de obstáculos, 1 niños y 6t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(7,8,10,10,3,5,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(7,8,10,10,3,5,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 7x8,10 por ciento de basura ,10 por ciento de obstáculos, 3 niños y 5t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(10,10,15,20,2,5,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(10,10,15,20,2,5,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 10x10,15 por ciento de basura ,20 por ciento de obstáculos, 2 niños y 5t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(7,8,10,10,5,10,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(7,8,10,10,5,10,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 7x8,10 por ciento de basura ,10 por ciento de obstáculos, 5 niños y 10t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(12,8,40,10,5,10,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(12,8,40,10,5,10,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 12x8,40 por ciento de basura ,10 por ciento de obstáculos, 5 niños y 10t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(15,15,5,5,2,10,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(15,15,5,5,2,10,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 15x15,5 por ciento de basura ,5 por ciento de obstáculos, 2 niños y 10t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(20,15,20,10,10,15,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(20,15,20,10,10,15,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 20x15,20 por ciento de basura ,10 por ciento de obstáculos, 10 niños y 15t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(5,5,50,50,3,5,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(5,5,50,50,3,5,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 5x5,50 por ciento de basura ,50 por ciento de obstáculos, 3 niños y 5t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(10,5,10,5,1,50,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(10,5,10,5,1,50,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 10x5,10 por ciento de basura ,5 por ciento de obstáculos, 1 niños y 50t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    print()
    finalResultR = (0,0,0)
    finalResultP = (0,0,0)
    for i in range(0,30):
        result = simulation(15,15,25,20,15,12,False,True)
        finalResultR = ((finalResultR[0]+result[0])/2,finalResultR[1]+result[1],finalResultR[2]+result[2])
        finalResult = ((finalResult[0]+result[0])/2,finalResult[1]+result[1],finalResult[2]+result[2])
        result = simulation(15,15,25,20,15,12,False,False)
        finalResultP = ((finalResultP[0]+result[0])/2,finalResultP[1]+result[1],finalResultP[2]+result[2])
        finalResult = ((result[0]+finalResult[0])/2,result[1]+finalResult[1],finalResult[2]+result[2])
    print('Ambiente 15x15,25 por ciento de basura ,20 por ciento de obstáculos, 15 niños y 12t')
    print('Reactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultR[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultR[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultR[2]))
    print()
    print('Proactivo')
    print('Porciento de casillas sucias medio: ' + str(finalResultP[0]))
    print('Veces que el robot fue despedido : ' + str(finalResultP[1]))
    print('Veces que el robot ubicó a todos los niños en el corral : ' + str(finalResultP[2]))
    return finalResult

def simulation(n=7,m=8,dirtyP=10,obstacleP=10,childrenCount=3,t = 5,boolean= True,robot = True):
    e = Environment(n,m,dirtyP,obstacleP,childrenCount)
    if boolean:
        e.printE()
    c = 1
    robotDespedido = 0
    limpioTodaLaCasa = 0
    while True: 
        if robot:
            r = Robot().movPolicy1(e.environment)
        else:
            r = Robot().movPolicy2(e.environment)
        if boolean:
            e.printE()
        if r == 'exit':
            #print('yes')
            limpioTodaLaCasa = 1
            break
        e.EnvironmentTurn()
        if boolean:
            e.printE()
        d = e.checkDirtiness()
        if d >= 60:
            #print('la casa esta un ' + str(d) + ' porciento sucia')
            r = 'exit'
            robotDespedido = 1
            #print('Game Over')
        if c >= 100:
            r = 'exit'
            robotDespedido = 1
            #print('Game Over 100 steps')
        if r == 'exit':
            break
        if c % t == 0:
            e.redistribucionRandom()
            if boolean:
                #print('redistribucion')
                e.printE()
        c += 1
    d = e.checkDirtiness()
    return (d,robotDespedido,limpioTodaLaCasa)

    

main()