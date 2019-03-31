import numpy as np
import random
import tkinter as tk
import math
import tkinter as tk
import time


probability_dict={1:0.1,2:0.3,3:0.7,4:0.9}

def buildmap():
    nmap=np.random.random((50,50))
    map=np.zeros((50,50))
    for i in range(50):
        for j in range(50):
            if nmap[i][j]<0.2:
                map[i][j]=1
            elif nmap[i][j]<0.5:
                map[i][j]=2
            elif nmap[i][j]<0.8:
                map[i][j]=3
            else: map[i][j]=4

    return map
def generate_target():
    x=random.randint(0,49)
    y=random.randint(0,49)
    return x,y

def drawCanvas(canvas,matrix,size):

    for (x,y) ,value in np.ndenumerate(matrix):
        if value == 1:
            rect(canvas,size,(x,y),(x+1,y+1),'white')
        if value == 2:
            rect(canvas, size, (x, y), (x + 1, y + 1), '#8e8484')
        if value == 3:
            rect(canvas, size, (x, y), (x + 1, y + 1), '#5e7f5d')
        if value == 4:
            rect(canvas, size, (x, y), (x + 1, y + 1), '#353835')



def rect(canvas,size,a,b,color='black'):
    (x1,y1)=a
    (x2,y2)=b
    x1*=size
    y1*=size
    x2 *= size
    y2 *= size
    canvas.create_rectangle((x1,y1,x2,y2),fill=color)
    canvas.update_idletasks()



class Agent(object):

    def __init__(self):
        self.belief_state = np.full((50,50),1/2500)

    def search_cell(self,x,y,targetx,targety,map):

        p = random.random()
        tp= map[x][y]
        if x==targetx and y== targety:
            if (tp==1 and p<0.9) or (tp==2 and p<0.7 )or(tp==3 and p<0.3)or(tp==4 and p<0.1):
                return (tp,True)
            else:
                return (tp,False)

    def rule1(self):
        point=np.where(self.belief_state == np.max(self.belief_state))
        x=point[0][0]
        y=point[1][0]
        return x,y   #return the most likely point by rule1
    def rule2(self):
        return x,y   #return the most likely point by rule2
    def update_state(self,x,y,tp):
        falseNeg = probability_dict[tp]
        prob=self.belief_state[x][y]
        for i in range(50):
            for j in range(50):
                if i==x and j==y:
                    self.belief_state[i][j]= falseNeg*prob/(1-prob+prob*falseNeg)

                else:
                    prob1 = self.belief_state[i][j]
                    self.belief_state[i][j]= prob1/(1-prob+prob*falseNeg)

    def record_state(self):
        pass
        # record search history
    def show_state(self):
        pass
        #visualization




def main():

    map = buildmap()
    (a,b)=generate_target()
    print(a,b)
    Ai= Agent()
    x = random.randint(0, 30)
    y = random.randint(0, 30)
    result = Ai.search_cell(x,y,a,b,map)
    print(result)
    num=1
    dim = 30
    grid = buildmap(dim)
    height, width = (dim, dim)
    cellsize = (int)(400 / dim)
    master = tk.Tk()
    master.title('map')
    canvasGenerate = tk.Canvas(master, width=width * cellsize, height=height * cellsize)
    canvasGenerate.grid(row=0, column=0)
    drawCanvas(canvasGenerate, np.transpose(grid), cellsize)
    tk.mainloop()
    while((not result) and (num)<2000):
        tp=map[x][y]
        Ai.update_state(x,y,tp)
        x,y=Ai.rule1()
        result = Ai.search_cell(x,y,a,b,map)
        num=num+1
        print(num)

    print(x,y)

    
main()









