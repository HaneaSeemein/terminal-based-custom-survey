import host
# import or send qs from socket programming after code verification
def start_survey():
    code=input("Enter the survey id")
    #send the survey with the given code
    #let the given survey be called surv
    take_survey(surv)

def take_survey(qlist):
    data = qlist
    for k in range(len(data)):
     i=k+1
     print("\n\n")
     print(data[i].question)
     print(f"1.{data[i].o1}\t2.{data[i].o2}\t3.{data[i].o3}\t4.{data[i].o4}")
    #  print("any other number\t")
     answer=int(input("Enter the choice number: "))
     if(i==1):data[i].c1=data[i].c1+1
     elif(i==2):data[i].c2=data[i].c2+1
     elif(i==3):data[i].c3=data[i].c3+1
     elif(i==4):data[i].c4=data[i].c4+1
     else:print("you chose to skip")
    # i=i+1
# questionlist = host.qs
# take_survey(questionlist)
# print(questionlist[0].c1,questionlist[0].c2,questionlist[0].c3,questionlist[0].c4,sep="\t")