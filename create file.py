#1) create a file intro.txt in python and ask the user to write a single line of text by user input?.
def input_txt():
    k=str(input("Enter your text::"+"\n"))
    n=open("D:\Python Training\intro.txt", "w")
    n.write(k)
    n.close()
def read_text():
    n=open("D:\Python Training\intro.txt", "r")
    print("\n"+"user entered text is::"+"\n"+n.read())
    n.close()
input_txt()
read_text()
