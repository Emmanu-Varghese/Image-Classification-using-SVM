from Tkinter import *
from PIL import ImageTk
from PIL import Image
import ttk
import tkFileDialog
import predict
import os


root = Tk()
root.title('Image Classifier')
root.geometry('900x670+250+5')
root.resizable(False,False)
predict_val = StringVar()
qframe=ttk.Frame(root,relief=GROOVE,padding=(10,10),width=20)
fr=ttk.Frame(root,relief=GROOVE,padding=(10,10))
e=ttk.Entry(fr,width=40)
v=ttk.Entry(fr,width=4)
color_entry=ttk.Entry(fr,width=50)
lab1=ttk.Label(fr,text='Input image Directory')
lab2=ttk.Label(fr,text='Input Colour Directory')
lab3=ttk.Label(fr,text='Result')
answer_text=Text(fr,background='white',relief=RAISED,width=50)
progress=ttk.Progressbar(fr,mode="determinate",orient=HORIZONTAL,length=400,maximum=70.0,value=0.0)



################### In frame 2 ###################

qlabel=ttk.Label(qframe,text='Instructions For creating Testing Dataset')
qlabel.place(x=10,y=10)
q_text=ttk.Label(qframe,background='gray',relief=RAISED,padding=(10,10),wraplength=400)
q_text.config(text='Dataset must contain atleast 70 images.This software gives maximum accuracy when the image resolution is 640 x 480 and the object must be at center.Since HOG is used as image feature background must be of uniform colour')
q_text.place(x=10,y=30)
qlabel1=ttk.Label(qframe,text='Sample images')
qlabel1.place(x=10,y=120)

image1 = Image.open('D:\\Emmanu\\project-data\\V.jpg')
image1 = image1.resize((300,140), Image.ANTIALIAS) #The (250, 250) is (height, width)
img1 = ImageTk.PhotoImage(image1)
p1 = ttk.Label(qframe, image = img1)
p1.place(x=10,y=140)


image2 = Image.open('D:\\Emmanu\\project-data\\A.jpg')
image2 = image2.resize((300,140), Image.ANTIALIAS) #The (250, 250) is (height, width)
img2 = ImageTk.PhotoImage(image2)
p2 = ttk.Label(qframe, image = img2)
p2.place(x=10,y=300)

image3 = Image.open('D:\\Emmanu\\project-data\\F.jpg')
image3 = image3.resize((130,200), Image.ANTIALIAS) #The (250, 250) is (height, width)
img3 = ImageTk.PhotoImage(image3)
p3 = ttk.Label(qframe, image = img3)
p3.place(x=10,y=450)

class main_window:

    global e,fr,answer_box

    def get_file_name():
        e.delete(0,END)
        color_entry.delete(0,END)
        file = tkFileDialog.askdirectory(initialdir='D:\\Emmanu\\project-data\\')
        e.insert(0,file)
    def get_color_list():
        color_entry.delete(0,END)
        file = tkFileDialog.askopenfilename(initialdir='D:\\Emmanu\\project-data\\color-dir\\',filetypes=[("Text files","*.txt")])
        color_entry.insert(0,file)

    def window_run(self):
        root.mainloop()
    def clear_txt():
        v.delete(0,END)
        e.delete(0,END)
        color_entry.delete(0,END)
        answer_text.delete('1.0', END)
    def pre():
        sp=0
        cp=0
        path=e.get()
        image_path=color_entry.get()
        path1=path+'//'
        shape_list=[]
        colour_list=[]
        g_colour_list=[]
        listing1 = os.listdir(path1)
        for i,file in enumerate(listing1):
            print file
            shape_list.append(predict.predict_shape(path1+file,int(v.get())))
            colour_list.append(predict.predict_color(path1+file))
            progress.config(value=i)
        print shape_list[1]
        answer_text.insert('0.0','Prediction List according to Shape\n')
        pos = answer_text.index("end")
        answer_text.insert(pos,shape_list)
        if int(v.get())!=3:
            pos = answer_text.index("end")
            answer_text.insert(pos,'\n\nPrediction List according to color\n')
            pos = answer_text.index("end")
            answer_text.insert(pos,colour_list)
        print shape_list
        va=float(v.get())
        for i in (shape_list):
            if i==va:
                sp+=1
        pos = answer_text.index("end")
        answer_text.insert(pos,'\nShape Accuracy-\t')
        pos = answer_text.index("end")
        sp=float(sp)
        base=len(shape_list)
        per=(sp/base)*100
        answer_text.insert(pos,per)
        f=open(image_path,"r")
        for line in f:
            g_colour_list.append(int(line.strip('\n')))
        print g_colour_list
        k=[i for i, j in zip(colour_list, g_colour_list) if i == j]
        cp=len(k)
        cp=float(cp)
        base=len(colour_list)
        per=(cp/base)*100
        if int(v.get())!=3:
            pos = answer_text.index("end")
            answer_text.insert(pos,'\nColour Accuracy-\t')
            pos = answer_text.index("end")
            answer_text.insert(pos,per)

    fr.pack(expand = 'yes', fill = 'both',side=LEFT)
    fr.pack_propagate(False)
    qframe.pack(expand = 'yes', fill = 'both',side=RIGHT)
    qframe.pack_propagate(False)
    lab1.place(x=10,y=0)
    e.place(x=10,y=20)
    v.place(x=280,y=20)

    b=Button(fr,text='Browse',command=get_file_name,width=10,height=1)
    bc=Button(fr,text='Browse',command=get_color_list,width=10,height=1)
    b.place(x=330,y=20)
    bc.place(x=330,y=78)
    predict_btn=Button(fr,text='Predict',command=pre,width=15)
    predict_btn.place(x=150,y=110)
    progress.place(x=10,y=150)
    lab3.place(x=10,y=180)
    lab2.place(x=10,y=58)
    color_entry.place(x=10,y=78)
    answer_text.place(x=10,y=200)
    clear_btn=Button(fr,text='Clear',width=20,command=clear_txt)
    clear_btn.place(x=130,y=600)



def main():

    mw=main_window()
    mw.window_run()

if __name__ == '__main__':main()
