from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title('Machine Learning(Beta)')
root.geometry('480x240')
Label(root,text='sepal length:').grid()
Label(root,text='sepal width:').grid()
Label(root,text='petal length:').grid()
Label(root,text='petal width:').grid()
S_len=StringVar()
S_wid=StringVar()
P_len=StringVar()
P_wid=StringVar()
Entry(root,textvariable=S_len).grid(row=0,column=1)
Entry(root,textvariable=S_wid).grid(row=1,column=1)
Entry(root,textvariable=P_len).grid(row=2,column=1)
Entry(root,textvariable=P_wid).grid(row=3,column=1)
def submit():
    print(S_len.get())
    print(S_wid.get())
    print(P_len.get())
    print(P_wid.get())
    from sklearn import datasets
    from sklearn.linear_model import LogisticRegression
    #import numpy as np
    iris=datasets.load_iris()
    x=iris.data
    y=iris.target
#print(iris)
    clf= LogisticRegression()
    clf.fit(x,y)
    L=[]
    L.append(eval(S_len.get()))
    L.append(eval(S_wid.get()))
    L.append(eval(P_len.get()))
    L.append(eval(P_wid.get()))
    p=clf.predict([L])
    if p==[0]:
        print('Iris-Setosa')
    elif p==[1]:
        print('Iris-Versicolour')
    else:
        print('Iris-Virginica')
def file_type():
    Label(root,text='what type of file are you giving?').grid(row=6,column=1)
    var=StringVar()
    var.set('Radio')
    radio=Radiobutton(root,text='excel',variable=var,value='.xlsx').grid(row=8,column=0)
    radio=Radiobutton(root,text='csv',variable=var,value='.csv').grid(row=11,column=0)
    radio=Radiobutton(root,text='word',variable=var,value='.docx').grid(row=14,column=0)
    Button(root,text='add',fg='blue',command=excepted).grid(row=16,column=1)
def excepted():
    val=tmsg.askquestion('conformation','are you sure to add  this file')
    if val == 'yes':
        tmsg.showinfo('confarmed','you successfully add file')
    else:
        tmsg.showerror('error','try again')
    
def testing(m):
    print(m)
t=5000    
Scrollbar(root).grid(column=1000,sticky=E)    
Button(root,text='add file',fg='blue',command=file_type).grid(row=5,column=0)    
Label(root,text='© MOLLA SAROAYR HOSSAIN',fg='red').grid(row=20,column=5)
Button(root,text='submit',fg='blue',command=submit).grid(row=4,column=1)
Button(root,text='testing',fg='blue',command=lambda:testing(t)).grid(row=5,column=1)



root.mainloop()

