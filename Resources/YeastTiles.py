import os, shutil, webbrowser
from PIL import Image
import PIL.ImageOps

# Get current directory
currdir= os.getcwd()
# Get list of files in current directory
allfiles=os.listdir(currdir)

# Define a query gene
queryGene="EXO1"

# Open the SGD webpage for the query gene
baseURL="http://www.yeastgenome.org/cgi-bin/locus.fpl?locus="
webbrowser.open_new_tab(baseURL+queryGene)

# Get the images relevant to the query gene
queryfiles=[]
for x in allfiles:
    # Don't add any directory names
    if queryGene in x and queryGene!=x:
        queryfiles.append(x)
print queryfiles

# Let's create a new directory (if it doesn't exist) and put the images in it
if queryGene not in allfiles:
    os.mkdir(queryGene)
# Copy the images into the correct folder
for x in queryfiles:
    shutil.copy(x,os.path.join(queryGene,x))

# Open the three files
im1=Image.open(queryfiles[0])
im2=Image.open(queryfiles[1])
im3=Image.open(queryfiles[2])
# Create an empty file to paste into
blank=Image.new("RGB",(126*3,126),color=0)
# Paste files
blank.paste(im1,(0,0))
blank.paste(im2,(126,0))
blank.paste(im3,(126*2,0))

# Save output
blank.save(queryGene+"ThreeTiles.jpg")
blank=blank.transpose(Image.ROTATE_90)
blank.save(queryGene+"Vertical.jpg")
blank=PIL.ImageOps.invert(blank)
blank.save(queryGene+"Inverted.jpg")
blank=blank.resize((1260,3*1260),Image.ANTIALIAS)
blank.save(queryGene+"Enlarged.jpg")
