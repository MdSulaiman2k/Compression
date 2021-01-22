'''
   #1.testcase : "ABACDFTJBDAAAACVAAAAAB"
      compressed :  "101100100010000100000100000010100011111001000000001111101"
   #2.testcase : "AAACVAAAAAB"
       compressed : "11101001111110000"

'''


import re
 
class Node:
	"""docstring for ClassName"""
	def __init__(self,frequence= None ,data =None , prelink = None , Nextlink = None ):
		self.data = data
		self.frequence = frequence
		self.prelink = prelink
		self.Nextlink = Nextlink

#-------------------------------------------------------------------------------------------------------------------------------

class  DoubleLinkedlist():
	"""docstring for  DoubleLinkedlist"""
	def __init__(self):
		self.root = None 

# this function is used to create odd number of nodes in which the root node points to the second last and third last nodes

	def insertbefore(self , frequence , data=None): # this function 
		new_node = None
		if self.root is None :
			new_node = Node(frequence , data)
		else:
			next_node    = Node(frequence , data )
			pre_node     = self.root
			new_node     = Node(next_node.frequence+pre_node.frequence, prelink= pre_node ,  Nextlink= next_node )
		self.root  = new_node

# this function is used to decompress the compressed string by traversing node to node .	
	def travelList(self,ComString):
		orgString = ""
		new_node = self.root 
		for i in ComString :
			if(i == "0" and new_node.prelink is not None):
				new_node = new_node.prelink
			else:
				if(new_node.Nextlink is not None ):
					new_node = new_node.Nextlink
				orgString  += new_node.data
				new_node = self.root
		return orgString

#-----------------------------------------------------------------------------------------------------------------------------
				

def returnMinCharOccurs(string , doublelink) :#this function is used to return a charactor which appears least no of times in a string 
	str1 = ""
	val = string[0]
	minimum = len(string)
	for i in string :
		count =  0
		for j in string :
			if(i == j and string not in str1) :
				count += 1 
		if(minimum > count) :
			minimum = count
			val = i
		str1 += i
	doublelink.insertbefore(minimum , val)
	return val

def returnMaxCharOccurs(string) : #this function is used to return a charactor which appears least no of times in a string 
	str1 = ""
	val = string[0]
	maxi = 0 
	for i in string :
		count =  0
		for j in string :
			if(i == j and string not in str1) :
				count += 1 
		if(maxi < count) :
			maxi = count
			val = i
		str1 += i
	return val
	


doublelink = DoubleLinkedlist()
string =  "AAACVAAAAAB"
val =  string 
val2 = string 
str1 =  val
str2 = val
pattern = "1" 
comString = string  
for i in str1 :
	val = returnMinCharOccurs(str1 , doublelink) 
	str1 = re.sub( val ,"" , str1 )

	val2 = returnMaxCharOccurs(str2)
	str2 = re.sub(val2 ,"",str2)

	if(str2 == "" ) :
		pattern = re.sub("1","0",pattern)
	comString = re.sub(val2 , pattern , comString )
	pattern = "0" + pattern
	if(str1 == ""):
		break

print("The Compressed String is : ",comString)

decompString = doublelink.travelList(comString)

print("The Decompressed String is : ", decompString )
		