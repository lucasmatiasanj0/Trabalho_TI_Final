import functions as f
from PIL import Image
from scipy.io import wavfile
import numpy as np
import string
import huffmancodec as huf

def ex_1():
    src_and_alfabeto=f.create_src()
    src=src_and_alfabeto[0]
    alfabeto=src_and_alfabeto[1]
    index_count=f.count(src,alfabeto)
    f.show_graphic(index_count,alfabeto)

def ex_2():
    src_and_alfabeto=f.create_src()
    src=src_and_alfabeto[0]
    alfabeto=src_and_alfabeto[1]
    index_count=f.count(src,alfabeto)
    f.entalphy(index_count)

def ex_3_and_ex_4(file_dir,ex_4):

    file_name=file_dir.split("\\")[-1]
    file_extension=file_name.split(".")[-1]

    if file_extension=="bmp":

        _alfabeto=np.arange(256)
        src=np.array(Image.open(file_dir)).flatten()
        counted_=f.count(src,_alfabeto)
        if ex_4==0:
            f.entalphy(counted_)
            f.show_graphic(counted_,_alfabeto)

        else:
            counted_ = np.array(list(filter(lambda a : a!=0 ,counted_ )))
            Codec = huf.HuffmanCodec.from_data(src)
            symbols,lengths = Codec.get_code_len()
        
            f.average(counted_,lengths)

    elif file_extension=="wav":

        samplerate, src = wavfile.read(file_dir)
        alfabeto=np.arange(256)
        counted_=f.count(src,alfabeto)

        if ex_4==0:
            f.entalphy(counted_)
            f.show_graphic(counted_,alfabeto)
        
        else:
            counted_ = np.array(list(filter(lambda a: a!=0,counted_)))
            src=np.array(src)
            codec = huf.HuffmanCodec.from_data(src)
            symbols,lengths = codec.get_code_len()
            
            f.average(counted_,lengths)
            
    
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
            f.entalphy(counted_)
            f.show_graphic(counted_,alfabeto_letras)
        
        else:
            counted_= np.array(list(filter(lambda a: a!=0 , counted_)))
            codec = huf.HuffmanCodec.from_data(src)
            symbols,lengths = codec.get_code_len()
            f.average(counted_,lengths)


def ex_6_a(query,target,alfabeto,passo):
    index_final = len(query)
    index_inicial = 0
    
    while index_final <= len(target):
        compare=target[index_inicial:index_final]
        index_final+=passo
        index_inicial+=passo
        
        
    

    

if __name__ == "__main__":
    # ex_1()
    # ex_2()
    ex_3_and_ex_4("data\\english.txt",0)

    
    #ex_6_a([2,6,4,10,5,9,5,8,0,8],[6,8,9,7,2,4,9,9,4,9,1,4,8,0,1,2,2,6,3,2,0,7,4,9,5,4,8,5,2,7,8,0,7,4,8,5,7,4,3,2,2,7,3,5,2,7,4,9,9,6],[0,1,2,3,4,5,6,7,8,9,10],3  )