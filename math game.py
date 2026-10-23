import tkinter as tk
import random,time

bg="white"
riddle=""
delay=1
size=500
a=""
solves=0
fail=0
st=time.time()
art=-1
data=[0]*5
data2=[0]*5

#window setup
window = tk.Tk()
window.title("BLEH")
window.geometry(str(size) + "x" + str(size))
canvas=tk.Canvas(window, width=(size), height=(size), bg="white")
canvas.pack()




def render():
    global a,size,riddle,bg,score,solves,fail,data,data2
    canvas.delete("all")
    aaa=a[:]
    while len(aaa)<6:
        aaa="_"+aaa
    tt=time.time()-st
    canvas.create_rectangle(0,0,size,size, fill=bg)
    canvas.create_text(size//2,size//10, text="What is the answer to:", fill="black", font=("Arial", size//15))
    canvas.create_text(size//2,size//5, text=riddle, fill="black", font=("Arial", size//10))
    canvas.create_text(size//2,size-size//10, text=aaa, fill="black", font=("Arial", size//10))
    canvas.create_text(size//8,size-size//10, text="Time:"+str(round(tt,2))+"s", fill="black", font=("Arial", size//30))
    canvas.create_text(size//8,size-size//7, text="Solves:"+str(solves)+"/"+str(fail), fill="black", font=("Arial", size//30))
    if tt<=60:
        window.after(delay,render)
    else:
        canvas.create_rectangle(0,0,size,size, fill="white")
        canvas.create_text(size//2,size//2, text=" ".join([str(e)+(" + "," - "," * "," // "," % ")[i] for i,e in enumerate(data2)]), fill="red", font=("Arial", size//20))
        canvas.create_text(size//2,size//3, text=" ".join([str(e)+(" + "," - "," * "," // "," % ")[i] for i,e in enumerate(data)]), fill="green", font=("Arial", size//20))
        canvas.create_text(size//8,size-size//10, text="Time:"+str(round(tt,2))+"s", fill="black", font=("Arial", size//30))
        canvas.create_text(size//8,size-size//7, text="Solves:"+str(solves)+"/"+str(fail), fill="black", font=("Arial", size//30))

def nextriddle():
    global riddle,answer,art
    answer=(random.randint(0,50),random.randint(0,4),random.randint(1,50))
    riddle=str(answer[0])+(" + "," - "," * "," // "," % ")[answer[1]]+str(answer[2])
    art=answer[1]
    if answer[1]==0:
        answer=answer[0]+answer[2]
    elif answer[1]==1:
        answer=answer[0]-answer[2]
    elif answer[1]==2:
        answer=answer[0]*answer[2]
    elif answer[1]==3:
        answer=answer[0]//answer[2]
    elif answer[1]==4:
        answer=answer[0]%answer[2]

def check():
    global a,answer,bg,solves,fail,data,art,data2
    if int(a)==answer:
        bg="green"
        solves+=1
        data[art]+=1
    else:
        bg="red"
        fail+=1
        data[art]+=1
        print("CORRECT:",answer)
    nextriddle()
    a=""

def move(event):
    global a
    if event.keysym== "BackSpace":
        a=a[:-1]
    elif event.keysym=="Return":
        check()
    elif (event.keysym).isdigit() and len(a)<6:
        a+=event.keysym
    elif event.keysym=="minus" and len(a)==0:
        a+="-"

window.bind("<Key>", move)


nextriddle()
render()
window.mainloop()
