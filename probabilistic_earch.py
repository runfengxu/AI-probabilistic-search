import numpy as np
import random
import tkinter as tk
import math
import tkinter as tk
import time


probability_dict={1:0.1,2:0.3,3:0.7,4:0.9}

def buildmap(dim):
    nmap=np.random.random((dim,dim))
    map=np.zeros((dim,dim))
    for i in range(dim):
        for j in range(dim):
            if nmap[i][j]<0.2:
                map[i][j]=1
            elif nmap[i][j]<0.5:
                map[i][j]=2
            elif nmap[i][j]<0.8:
                map[i][j]=3
            else: map[i][j]=4

    return map
def generate_target(dim):
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    return x,y

def remove_target(dim):
    x1,y1 = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
    x = a+x1
    y = b+y1
    while((x<0)or(x>dim-1)or(y<0)or(y>dim-1)):
        x1,y1= random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        x = a + x1
        y = b + y1
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

def update_cell(canvas,size,result,y,x):
    time.sleep(0.5)
    canvas.create_text((size*(2*x+1)/2,size*(2*y+1)/2),text='X',fill='red',font = 'Helevetica 10 bold')
    canvas.update()
    time.sleep(0.5)

def manhattan(x,y,a,b):
    return abs(x-a)+abs(y-b)


class Agent(object):

    def __init__(self,dim):
        self.belief_state = np.full((dim,dim),1/(dim*dim))
        self.dim=dim



    def search_cell(self,x,y,targetx,targety,map):

        p = random.random()
        tp= map[x][y]
        if x==targetx and y== targety:
            if (tp==1 and p<0.9) or (tp==2 and p<0.7 )or(tp==3 and p<0.3)or(tp==4 and p<0.1):
                return True
        else:
                return False

    def rule1(self):
        point=np.where(self.belief_state == np.max(self.belief_state))
        i=random.randint(0,len(point[0])-1)
        x=point[0][i]
        y=point[1][i]
        return x,y
    def rule2(self,map):
        matrix=np.zeros((self.dim,self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                p = self.belief_state[i][j]
                tp=map[i][j]
                if tp==1:
                    matrix[i][j]=0.9*p
                elif tp==2:
                    matrix[i][j]=0.7*p
                elif tp==3:
                    matrix[i][j] = 0.3 * p
                elif tp==4:
                    matrix[i][j] = 0.1 * p

        point=np.where(matrix==np.max(matrix))
        x=point[0][0]
        y=point[1][0]
        return x,y


    def rule1_sec4(self,a,b):
        matrix = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                p = self.belief_state[i][j]
                matrix[i][j] = p/manhattan(i,j,a,b)

        point = np.where(matrix == np.max(matrix))
        x = point[0][0]
        y = point[1][0]
        return x, y

    def rule2_sec4(self,a,b):
        matrix = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                p = self.belief_state[i][j]
                tp = map[i][j]
                if tp == 1:
                    matrix[i][j] = 0.9 * p/manhattan(i,j,a,b)
                elif tp == 2:
                    matrix[i][j] = 0.7 * p/manhattan(i,j,a,b)
                elif tp == 3:
                    matrix[i][j] = 0.3 * p/manhattan(i,j,a,b)
                elif tp == 4:
                    matrix[i][j] = 0.1 * p/manhattan(i,j,a,b)

        point = np.where(matrix == np.max(matrix))
        x = point[0][0]
        y = point[1][0]
        return x, y

    def update_state(self,x,y,tp):
        falseNeg = probability_dict[tp]
        prob=self.belief_state[x][y]
        for i in range(self.dim):
            for j in range(self.dim):
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
    dim = 50
    l = 1
    s = 0
    map = buildmap(dim)
    while (l < 50):
        point1 = np.where(map==1)
        i = random.randint(0,len(point1[0]-1))
        (a,b)=(point1[0][i],point1[1][i])
        # print(a,b)
        # print(map[a][b])
        Ai= Agent(dim)
        x = random.randint(0, 49)
        y = random.randint(0, 49)
        result = Ai.search_cell(x,y,a,b,map)
        num=1

        while ((not result) and (num<10000)):
            tp=map[x][y]
            Ai.update_state(x,y,tp)
            x,y=Ai.rule1()
            result = Ai.search_cell(x,y,a,b,map)
            num=num+1

        print(l)
        l=l+1
        s=s+num
    print('rule1',s/(l-1))

    l=1
    while (l < 50):
        point1 = np.where(map==1)
        i = random.randint(0,len(point1[0]-1))
        (a,b)=(point1[0][i],point1[1][i])
        # print(a,b)
        # print(map[a][b])
        Ai= Agent(dim)
        x = random.randint(0, 49)
        y = random.randint(0, 49)
        result = Ai.search_cell(x,y,a,b,map)
        num=1

        while ((not result) and (num<10000)):
            tp=map[x][y]
            Ai.update_state(x,y,tp)
            x,y=Ai.rule2(map)
            result = Ai.search_cell(x,y,a,b,map)
            num=num+1

        print(l)
        l=l+1
        s=s+num
    print('rule2',s/(l-1))
main()









