import Tkinter, numpy
nframes=100000
txtframe=20
window = Tkinter.Tk()
w,h = 750,750
txt=list("abcdefghijklmnopqrstuvwxyz0123456789")
colour=numpy.array(numpy.random.randint(0,255,3),dtype=numpy.uint8)
for i in xrange(0,nframes):
    window.title("http://www.staff.ncl.ac.uk/conor.lawless/ScientificPython Frame number: "+str(i))
    C=Tkinter.Canvas(window, width=w, height=h)
    C.pack()
    newcol= "#%02x%02x%02x" % tuple(colour)
    C.create_rectangle(0,0, w, h, fill=newcol,outline=newcol)
    C.create_text(w/2,h/2,text=txt[(i/txtframe)%len(txt)],fill="white",font=("Arial", "150","bold"))
    C.update()
    C.destroy()
    colnew=colour+numpy.random.randint(-1,2,3)*2
    colnew=[max(min(col,255),0) for col in colnew]
    colour=numpy.array(colnew,dtype=numpy.uint8)
window.destroy()
