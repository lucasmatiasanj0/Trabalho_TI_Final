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

def count_improved(src,alfabeto):
    index_count_dict = {}

    
    for i in src:
        if i not in index_count_dict:
            index_count_dict.setdefault(i,1)
            
        else:
            index_count_dict.update({i:index_count_dict[i]+1})
            
    return np.array(list(index_count_dict.values()))
    

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
    entalphy_= -1*np.sum(np.log2(index_count_prob)*index_count_prob)

    return entalphy_
    

def entalphy_X_Y(target,query,alfabeto):
    
    target = np.array(target)
    query = np.array(query)
    
    index_Y = count(query,alfabeto)
    index_X = count(target,alfabeto)
    entalphy_Y = entalphy(index_Y)
    entalphy_X = entalphy(index_X)
    
    # Info Mut = H(X)+H(Y)-H(X,Y)
    
    #intersect=[]
    alfabeto_ = {}
    
    for i in range(len(query)):

        new_tuple = (query[i],target[i])
        #intersect.append(new_tuple)
        
        if new_tuple in alfabeto_:
            alfabeto_.update({new_tuple:alfabeto_[new_tuple]+1})
        
        else:
            alfabeto_.setdefault(new_tuple,1)
            
        
    index_count = np.array(list(alfabeto_.values()))
    intersect_entalphy = entalphy(index_count) 
    
    return entalphy_X+entalphy_Y-intersect_entalphy
    #index_count = count_improved(intersect,alfabeto)
    #print(index_count)
    #intersect_entalphy = entalphy(index_count) 
    
    
    
    
    
    
        
    
def average(index_count,length):
    
    index_count = index_count/np.sum(index_count)
    index_count = index_count*np.array(length)
    print(np.sum(index_count))

#query = np.array([2,6,4,10,5,9,5,8,0,8])
#target = np.array([6,8,9,7,2,4,9,9,4,9,1,4,8,0,1,2,2,6,3,2,0,7,4,9,5,4,8,5,2,7,8,0,7,4,8,5,7,4,3,2,2,7,3,5,2,7,4,9,9,6])
#alfabeto = [0,1,2,3,4,5,6,7,8,9,10]

#print(entalphy_X_Y(target,query,))
#print(np.histogram([6,8,9,7,2,4,9,9,4,9],[2,6,4,10,5,9,5,8,0,8],bin))

    
    
    
    

