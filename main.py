from numpy.core.fromnumeric import size
import functions as f
from PIL import Image
from scipy.io import wavfile
import numpy as np
import string
import huffmancodec as huf
import matplotlib.pyplot as plt
import math as m

def ex_1(src,alfabeto):
    index_count=f.count(src,alfabeto)
    f.show_graphic(index_count,alfabeto)

def ex_2():
    src_and_alfabeto=f.create_src()
    src=src_and_alfabeto[0]
    alfabeto=src_and_alfabeto[1]
    index_count=f.count(src,alfabeto)
    print(f.entalphy(index_count))

def ex_3_and_ex_4(file_name,ex_4):
    
    file_dir = "./data/"+file_name
    file_extension=file_name.split(".")[-1]

    if file_extension=="bmp":

        _alfabeto=np.arange(256)
        src=np.array(Image.open(file_dir)).flatten()
        counted_=f.count(src,_alfabeto)
        
        if ex_4==0:
            entropia = f.entalphy(counted_)
            hmax = np.log2(len(_alfabeto))
            taxa = ((hmax-entropia)/hmax)*100
            print("Entropia:",entropia)
            print("Taxa",taxa)
            f.show_graphic(counted_,_alfabeto)

        else:
            counted_ = np.array(list(filter(lambda a : a!=0 ,counted_ )))
            Codec = huf.HuffmanCodec.from_data(src)
            symbols,lengths = Codec.get_code_len()
            
            e_x = f.average(counted_,lengths)
            e_x_2 = f.average(counted_,np.power(lengths,2))
            var = e_x_2-(e_x**2)
            
            print("Huffman :" ,e_x)
            print("Variância",var)
            
    elif file_extension=="wav":

        samplerate, src = wavfile.read(file_dir)
        alfabeto=np.arange(256)
        counted_=f.count(src,alfabeto)

        if ex_4==0:
            entropia = f.entalphy(counted_)
            hmax = np.log2(len(alfabeto))
            taxa = ((hmax-entropia)/hmax)*100
            print("Entropia:",entropia)
            print("Taxa",taxa)
            f.show_graphic(counted_,alfabeto)
        
        else:
            counted_ = np.array(list(filter(lambda a: a!=0,counted_)))
            src=np.array(src)
            codec = huf.HuffmanCodec.from_data(src)
            symbols,lengths = codec.get_code_len()
            
            e_x = f.average(counted_,lengths)
            e_x_2 = f.average(counted_,np.power(lengths,2))
            var = e_x_2-(e_x**2)
            
            print("Huffman :",e_x)
            print("Variância:",var)
            
    
    elif file_extension=="txt":

        alfabeto=np.concatenate([np.arange(65,91),np.arange(97,123)])
        alfabeto_letras=list(map(chr,list(alfabeto)))
        
        file=open(file_dir,"r")
        src=file.read()
        src= list(map(ord,list(src))) #para aplicar a função ord em todos os elementos da lista,depois converto para lista pois é me devolvido um ponteiro para a lista
        src= list(filter(lambda a: (91>a>=65) or (123>a>=91) , src))
        src=np.array(src)
        
        counted_=f.count(src,alfabeto)

        if ex_4==0:
            entropia = f.entalphy(counted_)
            hmax = np.log2(len(alfabeto))
            taxa = ((hmax-entropia)/hmax)*100
            print("Entropia:",entropia)
            print("Taxa",taxa)
            f.show_graphic(counted_,alfabeto_letras)
        
        else:
            counted_= np.array(list(filter(lambda a: a!=0 , counted_)))
            codec = huf.HuffmanCodec.from_data(src)
            symbols,lengths = codec.get_code_len()
            
            e_x = f.average(counted_,lengths)
            e_x_2 = f.average(counted_,np.power(lengths,2))
            var = e_x_2-(e_x**2)
            
            print("Huffman :" ,e_x)
            print("Variância:",var)
            
            
            
            
            
            
            
def ex_5(file_name):
    inicial=0
    final=1 
    file_dir = "./data/"+file_name
    file_extension=file_name.split(".")[-1]

    if file_extension =="txt":
    
        file=open(file_dir,"r")
        src=file.read()
        src= list(map(ord,list(src))) 
        src= list(filter(lambda a: (91>a>=65) or (123>a>=91) , src))
        src= list(map(chr,list(src)))
        
        
        dict_count = {}
        
        while final < len(src):
            newTuple = (src[inicial],src[final])
            
            if  newTuple  in dict_count:
                dict_count.update({newTuple:dict_count[newTuple]+1})
                
            else:
                dict_count.setdefault(newTuple,1)
                
            final+=1
            inicial = final-1
        
        print(f.entalphy(list(dict_count.values()))/2)
    
    if file_extension == "bmp":

        src = list(np.array(Image.open(file_dir)).flatten())
        src = list(map(str,src))

        dict_count = {}
        
        while final < len(src):
            
            newTuple = (src[inicial],src[final])
            
            if  newTuple  in dict_count:
                dict_count.update({newTuple:dict_count[newTuple]+1})
                
            else:
                dict_count.setdefault(newTuple,1)
                
            final+=1
            inicial = final-1

        print(f.entalphy(list(dict_count.values()))/2)
        

    if file_extension == "wav":

        samplerate, src = wavfile.read(file_dir)
        src = list(map(str,src))

        dict_count ={}

        while final < len(src):
            
            newTuple = (src[inicial],src[final])
            
            if  newTuple  in dict_count:
                dict_count.update({newTuple:dict_count[newTuple]+1})
                
            else:
                dict_count.setdefault(newTuple,1)
                
            final+=1
            inicial = final-1

        print(f.entalphy(list(dict_count.values()))/2)

def ex_6_a(query,target,alfabeto,passo):
    
    index_final = len(query)
    index_inicial = 0
    infmut = []
    
    while index_final <= len(target):
        compare=target[index_inicial:index_final]
        index_final+=passo
        index_inicial+=passo
        infmut.append(round(f.entalphy_X_Y(compare,query,alfabeto),4))
        
    
    return np.array(infmut)

def ex_6_b():
    
    samplerate, guitarSolo = wavfile.read("data\\guitarSolo.wav")
    
    samplerate, target01_repeat = list(wavfile.read("data\\target01 - repeat.wav"))
    samplerate, target02_repeatNoise = list(wavfile.read("data\\target02 - repeatNoise.wav"))
    
    f_01 = ex_6_a(guitarSolo,target01_repeat,np.arange(256),round(len(guitarSolo)/4))
    f_02 = ex_6_a(guitarSolo,target02_repeatNoise,np.arange(256),round(len(guitarSolo)/4))
    
    
    plt.plot(f_01,label = "Target01 - repeat")
    plt.plot(f_02,label= "target02 - repeatNoise")
    plt.legend()
    plt.show()
    
    

def ex_6_c():
    samplerate, guitarSolo = wavfile.read("data\\guitarSolo.wav")
    inf_mut_max_values=[]
    
    for i in range(1,8):
        samplerate, song__ = wavfile.read("data\\Song0"+str(i)+".wav")
    
        infMut_array = ex_6_a(guitarSolo,song__,np.arange(256),round(len(guitarSolo)/4))
        print(infMut_array)
        f.create_simple_plot(infMut_array,"Song0"+str(i)+".wav")

        
        inf_mut_max_values.append(np.amax(infMut_array))
    
    inf_mut_max_values_sorted = np.sort(inf_mut_max_values)
    
        
    for i in range(1,8):
        maxValue = inf_mut_max_values_sorted[-i] 
        print("Valor máximo da informação mútua no fihcheiro Song0"+str(i+1)+".wav é : "+str(maxValue))
        

def menu():
    
    opcao=100
    
    while opcao!=0:
        
        print("---------MENU---------")
        print("1 - Exercício 1")
        print("2 - Exercício 2")
        print("3 - Exercício 3")
        print("4 - Exercício 4")
        print("5 - Exercício 5")
        print("6 - Exercício 6")
        print("0 - Exit")
        opcao = int(input("Qual a alinea que deseja correr??"))
    
        if opcao==0:
            quit()
        if opcao == 1: 
            src_and_alfabeto=f.create_src()
            src=src_and_alfabeto[0]
            alfabeto=src_and_alfabeto[1]
            ex_1(src,alfabeto)
        elif opcao == 2:
            ex_2()
        elif opcao == 3:
            file_name = input("Qual o nome do ficheiro??")
            ex_3_and_ex_4(file_name,0)
        elif opcao == 4:
            file_name = input("Qual o nome do ficheiro??")
            ex_3_and_ex_4(file_name,1)
        elif opcao == 5:
            file_name = input("Qual o nome do ficheiro??")
            ex_5(file_name)
        
        elif opcao == 6:
            seis_alinea = input("Qual alinea deseja fazer??(a/b/c)").lower()
            
            if seis_alinea.lower() == "a":
                passo = int(input("Qual o passo??:"))
                query = np.array([2,6,4,10,5,9,5,8,0,8])
                target = np.array([6,8,9,7,2,4,9,9,4,9,1,4,8,0,1,2,2,6,3,2,0,7,4,9,5,4,8,5,2,7,8,0,7,4,8,5,7,4,3,2,2,7,3,5,2,7,4,9,9,6])
                alfabeto = np.arange(11)
                print(ex_6_a(query,target,alfabeto,passo)) 
                
            elif seis_alinea == "b":
                ex_6_b()
            elif seis_alinea == "c":
                ex_6_c()
 
if __name__ == "__main__":
    # ex_1()
    # ex_2()
    #ex_3_and_ex_4("data\\english.txt",0)
    #ex_3_and_ex_4("english.txt",1)

    #ex_5("english.txt") 

    
    #print(ex_6_a(query,target,alfabeto,1))
    #ex_6_b()
    #ex_6_c()
    menu()
    