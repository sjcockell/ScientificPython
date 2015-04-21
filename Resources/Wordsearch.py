import random, numpy, string

target="Tree"
NRows,NCols=20,20
printsol=True

# Format target and convert it to a list of uppercase letters
target=target.replace(" ","")
target=target.upper()

# Define alphabet as set of letters in target
listarr=list(set(target))

# Generate and fill a two-dimensional array of letters randomly selected
store=numpy.random.choice(listarr,size=(NRows,NCols),replace=True)

# Check if there are any vertical solutions
vpos=[0]*NCols; vneg=[0]*NCols
for x in xrange(NCols):
    bigword="".join(store[:,x])
    vpos[x]=bigword.count(target) # Positive (or forward) solution
    vneg[x]=bigword.count(target[::-1]) # Negative (or backward) solution

# Check if there are any horizontal solutions
hpos=[0]*NRows; hneg=[0]*NRows
for y in xrange(NRows):
    bigword="".join(store[y,:])
    hpos[y]=bigword.count(target) # Positive (or forward) solution
    hneg[y]=bigword.count(target[::-1]) # Negative (or backward) solution

# Print report about types of solutions found
HorizPos=sum(hpos)
HorizNeg=sum(hneg)
VertPos=sum(vpos)
VertNeg=sum(vneg)
print("Horizontal, forward solutions: "+str(HorizPos))
print("Horizontal, backward solutions: "+str(HorizNeg))
print("Vertical, forward solutions: "+str(VertPos))
print("Vertical, backward solutions: "+str(VertNeg))

def listReport(pos,neg):
    '''Generates a list reporting whether positive or negative values or both are present at each location in pos and neg'''
    N=len(pos)
    sol=[' ']*N
    for x in xrange(N):
        if pos[x]>0:
            sol[x]="+"
        if neg[x]>0:
            sol[x]="-"
        if neg[x]>0 and pos[x]>0:
            sol[x]="*"
    return(sol)
    
if printsol:
    # Show wordsearch and indicate solutions
    # Don't do this if array is large...
    print("")
    hsol=listReport(hpos,hneg)
    vsol=listReport(vpos,vneg)
    for x in xrange(NRows):
        output="".join(store[x,:])+hsol[x]
        print(output)
    print("".join(vsol))
    




