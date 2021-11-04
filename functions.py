import numpy as np
import matplotlib.pyplot as plt
import math as m

def create_src():
    alfabeto=np.arange(10)
    src=np.random.randint(0,10,20)
    return [src,alfabeto]

def count(src,alfabeto):
    index_count=[]
    for i in alfabeto:
        index_count.append(np.count_nonzero(src==i))

    return np.array(index_count)


def show_graphic(index_count,alfabeto_):
    
    plt.bar(alfabeto_,index_count)
    plt.xlabel("Alfabeto")
    plt.ylabel("Frequência Absoluta")
    plt.title("Histograma")
    plt.locator_params(axis='y', integer=True)
    plt.show()
"""
def entalphy(index_count):
    _entalphy=[]
    total_cases=np.sum(index_count)
    for i in index_count:
        if i!=0:
            probability=i/total_cases
            _entalphy.append((probability)*(m.log2(probability)))
    
    print((-1)*np.sum(_entalphy))

"""
def entalphy(index_count):

    
    index_count_prob = index_count/np.sum(index_count)
    index_count_prob = np.delete(index_count_prob,np.where(index_count_prob==0))
    
    index_count = index_count/np.sum(index_count)
    index_count = np.delete(index_count,np.where(index_count==0))
    index_count = np.log2(index_count)
    index_count = index_count*index_count_prob
    entalphy_= -1*np.sum(index_count)
    

    return entalphy_
    

def entalphy_X_Y(X,Y,alfabeto):
    Y = np.array(Y)
    X = np.array(X)

    index_count_Y = count(Y,alfabeto)
    
    entalphy_Y = entalphy(index_count_Y)
    y_x = np.setdiff1d(Y,X)
    index_count_y_x = count(Y,y_x)
    entalphy_y_x = entalphy(index_count_y_x)

    final_entaphy = entalphy_Y - entalphy_y_x
    print(final_entaphy)

    


def average(index_count,length):

    index_count = index_count/np.sum(index_count)
    
    index_count = index_count*np.array(length)

    print(np.sum(index_count))
    

entalphy_X_Y([6,8,9,7,2,4,9,9,4,9],[2,6,4,10,5,9,5,8,0,8],[0,1,2,3,4,5,6,7,8,9,10])
    
    
    
    

