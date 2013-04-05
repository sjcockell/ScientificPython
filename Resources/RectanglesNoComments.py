import Tkinter, random

nrectangles=50
nframes=100000
COLORS=['forest green','white','dark orange']*nframes

random.shuffle(COLORS)

window = Tkinter.Tk()

w = window.winfo_screenwidth()*0.8
h = window.winfo_screenheight()*0.8

delta=int(round(float(min(w,h))/float(nrectangles*2)))

x=0

for i in xrange(0,nframes):
    window.title("Introduction to scientific computing with Python. Frame number: "+str(i))
    C=Tkinter.Canvas(window, width=w, height=h)
    C.pack()

    for z in xrange(0,nrectangles):
        newcol=COLORS[x+z]
        C.create_rectangle(0+z*delta,0+z*delta, w-z*delta, h-z*delta, fill=newcol,outline=newcol)
    C.update()
    C.destroy()
    x-=1
