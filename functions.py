import numpy as np
import matplotlib.pyplot as plt


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
    
    alfabeto_ = {}
    
    for i in range(len(query)):

        new_tuple = (query[i],target[i])
        
        if new_tuple in alfabeto_:
            alfabeto_.update({new_tuple:alfabeto_[new_tuple]+1})
        
        else:
            alfabeto_.setdefault(new_tuple,1)
            
        
    index_count = np.array(list(alfabeto_.values()))
    intersect_entalphy = entalphy(index_count) 
    
    return entalphy_X+entalphy_Y-intersect_entalphy
    
    
def average(index_count,length):
    
    index_count = index_count/np.sum(index_count)
    index_count = index_count*np.array(length)
    print(np.sum(index_count))



            
    
    

    
    
    
        
    
    
    

