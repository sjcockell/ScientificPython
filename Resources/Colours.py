# Some external libraries are required for this code to run
import Tkinter, numpy

# How many frames to draw in animation
nframes=100000
# How many frames to wait between drawing letters
txtframe=20

# Prepare to create a window
window = Tkinter.Tk()

# Define window size
w,h = 750,750

# Generate list of letters to display
txt=list("abcdefghijklmnopqrstuvwxyz0123456789")

# Randomly generate starting RGB colour
colour=numpy.array(numpy.random.randint(0,255,3),dtype=numpy.uint8)

# Create animation 
for i in xrange(0,nframes):
    # Specify text in the title bar
    window.title("http://www.staff.ncl.ac.uk/conor.lawless/ScientificPython Frame number: "+str(i))
    # Create canvas to draw on
    C=Tkinter.Canvas(window, width=w, height=h)
    C.pack()
    # Convert colour to something Tkinter understands
    newcol= "#%02x%02x%02x" % tuple(colour)
    # Draw coloured rectangle to window
    C.create_rectangle(0,0, w, h, fill=newcol,outline=newcol)
    # Draw a letter to window
    C.create_text(w/2,h/2,text=txt[(i/txtframe)%len(txt)],fill="white",font=("Arial", "150","bold"))
    # Commit changes to the screen
    C.update()
    # Clear the canvas for the next set of rectangles
    C.destroy()
    # Update colour slightly, ready for next frame
    colnew=colour+numpy.random.randint(-1,2,3)*2
    colnew=[max(min(col,255),0) for col in colnew]
    colour=numpy.array(colnew,dtype=numpy.uint8)
# Close the window
window.destroy()
