l=open("D:\Python Training\intro.txt", "r")
f=open("D:\Python Training\myfile.txt", "r")   
first=f.read()
second=l.read() 


def read_txt():
    l=open("D:\Python Training\intro.txt", "r")
    f=open("D:\Python Training\myfile.txt", "r") 
    print("Text from myfile.txt:"+"\n"+l.read()+"\n")  
    print("Text from intro.txt:"+"\n"+f.read()+"\n")
   
    f.close()
    l.close()

def merge_txt():
    k=open("D:\Python Training\merge.txt", "w")
    k.write(second+ "\n" +first)
    k.close()
    
def read_merge():
    s=str(input("Do you want to display the blog (y/n)? "))
    if s=="y" or "Y":
        d=int(input("How many lines do you want to see::"))
        s=open("D:\Python Training\merge.txt", "r")
        print("Merged text is:" +"\n")
        for i in range(d):
            print(s.readline())
        s.close()
        exit()
    else:
        print("no functions selected"+"\n" +"Thank You!")
        exit()

def funcation():
    s=str(input("Do you want any other function (y/n)? "))
    
    if s=="y":
        print("\n"+"add(add a text)"+"\n"+"delete(delete a line)"+"\n"+"replace(replace a line)")
        r=str(input("\n"+"Enter your funcation:: "))
        if r=="add":
            v=str(input("\n"+"Enter your adding text:: "))
            t=open("D:\Python Training\merge.txt", "a")
            t.write(v)
            t.close()
        elif r=="delete":
            p=int(input("\n"+"Enter your line number for delete:: "))
            j=open("D:\Python Training\merge.txt", "r")
            det=j.readlines()
            print(det)
            j.close()
            del det(p)
        else:
            print("no functions selected"+"\n" +"Thank You!")
            exit()
    elif s=="n":
        print("Thank you for using me")  
        exit()  
    else:
        print("no functions selected"+"\n" +"Thank You!")

read_txt()
merge_txt()
funcation()
read_merge()
