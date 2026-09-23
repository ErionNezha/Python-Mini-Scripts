from tkinter import *

oyna=Tk()
oyna["bg"]="white"

oq="white"
qora="black"
font="TkCaptionFont"

menyu={}
x=5000
for i in range(1,11):
	menyu[f"Taom {i}"]=x
	x+=5000

def minus(minus_taom,minus_nechta,minus_narx):
	if minus_nechta["text"]>0:
		minus_nechta["text"]-=1
		minus_narx["text"]=minus_nechta["text"]*menyu.get(minus_taom)
		
		s_str=summa["text"].split()
		s_int=int(s_str[0])
		s=s_int-menyu.get(minus_taom)
		summa["text"]=f"{s} sum"
	
def plus(p_taom,p_nechta,p_narx):
	p_nechta["text"]+=1
	p_narx["text"]=p_nechta["text"]*menyu.get(p_taom)
	
	s_str=summa["text"].split()
	s_int=int(s_str[0])
	s=s_int+menyu.get(p_taom)
	summa["text"]=f"{s} sum"

r=0	
for taom in menyu:
	taom_label=Label(text=f"{taom}({menyu.get(taom)})",bg=oq,font=font).grid(row=r,column=0,pady=50)
	
	taom_nechta=Label(text=0,bg=oq,font=font)
	taom_nechta.grid(row=r,column=2)
	
	taom_narx=Label(text=0,bg=oq,font=font)
	taom_narx.grid(row=r,column=4)
	
	taom_minus=Button(text="-1",font=font,bg="crimson",fg=oq,command=lambda minus_taom=taom,minus_nechta=taom_nechta,minus_narx=taom_narx: minus(minus_taom,minus_nechta,minus_narx)).grid(row=r,column=1)
	
	taom_plus=Button(text="+1",font=font,bg="seagreen",fg=oq,command=lambda p_taom=taom,p_nechta=taom_nechta,p_narx=taom_narx: plus(p_taom,p_nechta,p_narx)).grid(row=r,column=3)
	
	r+=1
	
for i in range(3):
	j=Label(text="_",font=font,bg=oq).grid(row=r,column=i)
	
tozalash=Button(text="Clear",font=font,bg="orangered",fg=oq).grid(row=r,column=3)

summa=Label(text="0 sum",font=font,bg=oq)
summa.grid(row=r,column=4)

r+=1

for i in range(3):
	j=Label(text="_",font=font,bg=oq).grid(row=r,column=i)
	
chek=Button(text="Chek",font=font,bg="slateblue",fg=oq).grid(row=r,column=3)

saqlash=Button(text="Saqlash",font=font,bg="gold").grid(row=r,column=4)

oyna.mainloop()