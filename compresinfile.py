
"""
This program is used for compress the text file :
  #  compress :
  
     * its read the text file and compress and save in other file .
     
 # decompress :

      * In the compress file  its read and decompress and write in other file
      
"""
import re

def checking(string):
    str_1 = "0"
    found = 0
    while(not found) :
        found = 1
        for i in string :
           if(str_1 == i) :
               found = 0
               str_1 = chr(ord(str_1)+1)
               
               break
    return str_1




def pattern(string,x) :                                                 
    maxi = 0
    maxstr =""
    string_3 = checking(string)
    strlen = len(string)//4 + 1
    
    for j in range(1,len(string)+1,1) :
        string_1 = string[j-1:]
        check = 0
        str_1 = string_1[:x]
        count = 0
        while(check<x) :
            s = string_1[x+check :]
        
            for i in range(x,len(s)+1,x) :
                str_2 = s[i-x:i]
                if(str_1 == str_2) :
                    count = count+1
                    
            check = check+1
        if maxi < count :
            maxi = count
            maxstr = str_1
            
    compress = re.sub(maxstr,string_3,string)
    compress =  str(x) + compress +   maxstr +string_3
            
            
    return compress

def compression(string) :
    x = 2
    count = 0
    str_1 = string
    compressed = "0" + string
    strlen = len(string)//2 + 1
    if (strlen > 9) :
        strlen = 9
    while(x <= strlen) :
        compress = pattern(string,x)

        if( len(str_1) >= len(compress)) :
            compressed = compress
            str_1 = compressed
        x+=1
    
    
    return compressed



def decompress(s) :
    num = int(s[0])
    string = s[1:]
    decompress = s[1:]

    if(num) :
    
        str_1 = string[len(string)- (num+1) : len(string)-1]
        str_2 = string[len(string)-1]
    
        decompress = re.sub(string[len(string)- num-1:],"",string)
    
    
        decompress = re.sub(str_2,str_1,decompress)
    return decompress


def compressed(s) :
    compressed = s
    compress = s
    count = 0
    while(len(compressed) >=len(compress) ) :
        
        compressed = compress
        compress = compression(compressed)
        count = count+1
    if(count ==1) :
        compressed = compress
        compressed = str(count) + compressed
    else :
        compressed = str(count - 1) + compressed
    return compressed




def decompressed(string) :
    num  = int(string[0])
    decompres = string[1:]
    i = 0
    while(i<num) :
        decompres = decompress(decompres)
        i = i+1
        
    return decompres



    
    

           
        

f = open("texting.txt","r")                 #  f is open the text file  
fileread = f.readlines()                    #      its read the fullah line

f1 = open("write.txt","w+")             # This file is use to write the compress file 
i =0


for s in fileread :
    s=s.strip()                                          # its use to delete unwnated space 
    compress = compressed(s)
    print(compress)
    f1.writelines(compress)                  # This write  the file in the write.txt
    f1.writelines("\n")                        
    
f.close()
f1.close()


f3 = open("decom.txt","w+")           
f1 =  open("write.txt","r+")

fileread1 = f1.readlines()

for compress in fileread1 :
    
    compress = compress.strip()
    decompres = decompressed(compress)
    print(decompres)
    f3.writelines(decompres)

f3.close()
f1.close()




