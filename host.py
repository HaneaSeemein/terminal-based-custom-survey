# import client
class questions:
    def __init__(self,question,o1,o2,o3,o4):
        self.question=question
        self.o1=o1
        self.o2=o2
        self.o3=o3
        self.o4=o4
        self.c1=0
        self.c2=0
        self.c3=0
        self.c4=0        
        
def create_question():
 code = input("Enter a unique id:")
 noqs = int(input("enter the number of questions to generate: "))
 ql=[]
 ql.append(code)
 
 for i in range(noqs):
    print("\n\n")
    q = input("Enter the question:\n")
    a = input("Enter the first option: ")
    b = input("Enter the second option: ")
    c = input("Enter the third option: ")
    d = input("Enter the fourth option: ")
    k = questions(q, a, b, c, d )
    ql.append(k)
 return ql

#send qs through the socket programming