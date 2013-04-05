# Libraries are required for this code to run
import Tkinter, random

# How many rectangles to display
nrectangles=50
# How many frames to draw in animation
nframes=100000
# Create a list of colours (repeated nframes times)
COLORS=['forest green','white','dark orange']*nframes

# Shuffle the long list of colours, like a deck of cards
random.shuffle(COLORS)

# Prepare to create a window
window = Tkinter.Tk()

# Define window size as a fraction of screen size
w = window.winfo_screenwidth()*0.8
h = window.winfo_screenheight()*0.8

# Gap needed between rectangles to fit all of the rectangles required into the window
delta=int(round(float(min(w,h))/float(nrectangles*2)))

# Which element of COLORS list to start from
x=0

# Create animation
for i in xrange(0,nframes):
    # Specify text in the title bar
    window.title("Introduction to scientific computing with Python. Frame number: "+str(i))
    # Create canvas to draw on
    C=Tkinter.Canvas(window, width=w, height=h)
    C.pack()
    # Draw nested rectangles
    for z in xrange(0,nrectangles):
        # Get the correct colour for current rectangle from list
        newcol=COLORS[x+z]
        # Draw the rectangle to the canvas
        C.create_rectangle(0+z*delta,0+z*delta, w-z*delta, h-z*delta, fill=newcol,outline=newcol)
    # Commit changes to the screen
    C.update()
    # Clear the canvas for the next set of rectangles
    C.destroy()
    # Update the element number for the starting colour
    x-=1
