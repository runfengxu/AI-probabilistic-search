import numpy as np


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



class Agent(object):

    def __init__(self):
        self.belief_state = np.full((50,50),1/2500)

    def search_rule1(self):
        #search one spot with rule1
    def search_rule2(self):
        #search one spot with rule2
    def update_state(self):
        #update the belief state according to the search result
    def record_state(self):
        # record search history
    def show_state(self):
        #visualization




def main():










