#2) create a text file myfile. Txt in python and ask the user to write seperate 3 lines  with three input statement from the user?
limit=int(input("How Many lines::" " "))
def input_txt():
    n=open("D:\Python Training\myfile.txt", "w")
    for i in range(limit):
        txt=str(input("Enter your first line::"))
        n.write(txt+"\n")
    n.close()
def read_text():
    n=open("D:\Python Training\myfile.txt", "r")
    print("\n"+"User Entered Text Is"+"\n")
    for i in range(limit):
        print(n.readline()) 
    n.close()

input_txt()
read_text()