import re

def separate(string) :      # This  function gives you a priority of the string  
	string1 = string          # for example  sulaiman = {"s" :"1", "u": "1" , "l":"1" , "a"" :"2" , "i" : "1","m" : 1, "n" : "1"}
	count = 0
	str3 ={}
	for i in string :
		count = 0
		for j in string1 :
			if(i==j) :
				count += 1
		string1 = string1.replace(i,"")
		if i not in str3.keys() :
		    str3.update({i  :count})
	
	if i not in str3.keys() :
		str3.update({i  :count})

	return str3 

def compresing(s) :         # This function takes the keys and values if word get more value is became first priority  its set orderly 
	str3 = separate(s)
	keys = ""                   # eg: {"s" :"1", "u": "1" , "l":"1" , "a"" :"2" , "i" : "1","m" : 1, "n" : "1"} =  return value is "asulimn"
	compress =""
	for i in str3.values() :
		maximum = 0
		for v in str3.items() :
			if(maximum < v[1]):
				maximum =v[1]
				keys    = v[0]
		compress+= keys
		str3[keys] = 0
	return(compress)


def binconvert(string , compres) :  # this function is to convert binary values 
	length = len(compres) -1             # for eg : asulimn its calculate  a = 0 , s = 10, u = 110 , l = 1110 , i = 11110 , m = 111110  
	binary = "0"                           #  and n = 111111 .
	count = 1
	for i in compres :                    # if the string is sulaiman = its return 1011011100111101111100111111  
		string = re.sub(i,binary,string)
		
		if(length > count) :
			binary ="1" + binary
		else :
			binary = re.sub("0","1",binary)
		count +=1
	return string


def bintohexad(compress) :          # this function is used for change the binary valyue in to hexa decimal value 
	hexa = ""                        #   if eg  1011011100111101111100111111 its return 0 + b73df3f . 0 for the length of the  28 its diviede by for its 0 .
	count =0
	for i in range(4,len(compress)+1,4) :          #  if eg 111101 its will be  return     211d
		str1 = compress[len(compress)-i:len(compress)-(i-4)]
		hexa  = str(hexadecimal(str1)) + hexa
	strength = len(compress) - ((len(compress)// 4 ) *4)
	if(strength == 0 ) :
		hexa = str(strength)+  hexa 
	else :
		hexa = str(strength)+ str1[0:(strength+2)] + hexa
	return(hexa)


def hexadecimal(str1) :     # this function was used to binary to hexa decimal  value   eg : 1111 = f 

	hexa = (int(str1[0]) * 8) +  (int(str1[1]) * 4) + (int(str1[2]) * 2) + (int(str1[3]) * 1)
	if(hexa == 10) :
		hexa = "a"
	elif(hexa ==11) :
		hexa ="b"
	elif(hexa ==12) :
		hexa ="c"
	elif(hexa == 13) :
		hexa ="d"
	elif(hexa == 14) :
		hexa ="e"
	elif(hexa ==15) :
		hexa ="f"
	return(hexa)


def compressed(s) :   # this function is used to compress the string and return back
	compress = compresing(s)         # if eg sulaiman =  07asulimn0b73df3f
	length = len(compress)
	length = str(length)
	if(len(length) == 1 ) :
		length = "0" + length
	compressing = binconvert(s,compress)
	compressing = bintohexad(compressing) 
	compressing = str(length) +compress + compressing
	return compressing 




def decompress(compres) :         
	length = int(compres[0:2])
	decompress = compres[length+2:]
	count = int(decompress[0])
	decom = decompress[count+1 :]
	decompress = decompress[1:count+1]
	for i in range(0,len(decom)) :
		decompress = decompress + hexatobin(decom[i]) 
	return decompress



def hexatobin(hexavalue) :      # this function is used for binary to hexa decimal value if "b" = "1011" 
	if(hexavalue == '0') :
		hexavalue = "0000"
	elif(hexavalue == '1') :
		hexavalue = "0001"
	elif(hexavalue == '2') :
		hexavalue = "0010"
	elif(hexavalue == '3') :
		hexavalue = "0011"
	elif(hexavalue == '4') :
		hexavalue = "0100"
	elif(hexavalue == '5') :
		hexavalue = "0101"
	elif(hexavalue == '6') :
		hexavalue = "0110"
	elif(hexavalue == '7') :
		hexavalue = "0111"
	elif(hexavalue == '8') :
		hexavalue = "1000"
	elif(hexavalue == '9') :
		hexavalue = "1001"
	elif(hexavalue == 'a') :
		hexavalue = "1010"
	elif(hexavalue == 'b') :
		hexavalue = "1011"
	elif(hexavalue == 'c') :
		hexavalue = "1100"
	elif(hexavalue == 'd') :
		hexavalue = "1101"
	elif(hexavalue == 'e') :
		hexavalue = "1110"
	elif(hexavalue == 'f') :
		hexavalue = "1111"

	return hexavalue


def decompressed(compress)	 :    # this function is used to decompress the string if the string is  07asulimn0b73df3f : its became sulaiman
	string = ""
	decompres = decompress(compress)
	length  = int(compress[0:2])
	priority = compress[2:length+2]
	decom = ""
	for i in decompres :
		decom = decom + i

		if(i=="0" or (len(priority)-1 == len(decom))) :
			string += bintocompress(decom,priority)
			decom =""
	return string 

		




def bintocompress(decompres,priority) :
	length = len(decompres)
	if(decompres[len(decompres)-1] =="0") :
		letter = priority[len(decompres)-1]
	else :
		letter = priority[len(priority)-1]
	return letter 
	




	









s = input("enter the string :")
compressing = compressed(s)
print("\n")
print("compressed string  : ",compressing,end="\n\n\n" )


decompress = decompressed(compressing)
print("decompressed string :" , decompress)




		

		

