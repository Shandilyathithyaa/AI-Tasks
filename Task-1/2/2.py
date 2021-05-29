
from os import read


with open("F1.txt",'r') as f1:
    with open("F2.txt",'r') as f2:
        with open("F3.txt",'w') as f3:
            f1c = f1.read()
            f2c = f2.read()
            #f1.seek(0)
            #f2.seek(0)
            i=j=0
            while i < len(f1c) or j < len(f2c):
                word1 = ""
                word2 = ""
                if i < len(f1c):
                    while f1c[i] != ' ' and f1c[i] != '':
                        word1 += f1c[i]
                        i+=1
                        if  i >= len(f1c):
                            break
                    f3.write(word1 + ' ')    
                if j < len(f2c):
                    while f2c[j] != ' ' and f2c[j] != '':
                        word2 += f2c[j]
                        j+=1
                        if  j >= len(f2c):
                            break
                    f3.write(word2 + ' ')
                i+=1
                j+=1
