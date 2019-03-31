import numpy as np
import random
import sys
def buildmap():
    nmap=np.random.random((50,50))
    map=[]
    for i in range(50):
        map[i]=[]
        for j in range(50):
            if nmap[i][j]<0.2:
                map[i][j]='flat'
            elif nmap[i][j]<0.5:
                map[i][j]='hilly'
            elif nmap[i][j]<0.8:
                map[i][j]='forested'
            else map[i][j]='caves'

    return map
def generate_target:
    x=random.randint(0,49)
    y=random.randint(0,49)
    return x,y

class Agent(object):

    def __init__(self):
        self.belief_state = np.full((50,50),1/2500)

    def search_cell(self,a,b,targetx,targety,map):

        p = random.random()
        tp= map[a][b]
        if a==targetx and b== targety:
            if (tp='flat' && p<0.9) || (tp='hilly'&& p<0.7 )||(tp='forested'&&p<0.3)||(tp='caves'&& p<0.1):
                return True
            else:
                return False

    def rule1(self):
        return x,y   #return the most likely point by rule1
    def rule2(self):
        return x,y   #return the most likely point by rule2
    def update_state(self):
        #update the belief state according to the search result
    def record_state(self):
        # record search history
    def show_state(self):
        #visualization




def main():
    map = buildmap()
    (x,y)=generate_target()
    Ai= Agent()
    a = random.randint(0, 49)
    b = random.randint(0, 49)
    Ai.search_cell(a,b,x,y,map)











