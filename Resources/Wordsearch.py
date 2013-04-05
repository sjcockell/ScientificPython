import random, numpy

target="Conor"
NLetters=15
printsol=True

# Format target and convert it to a list of uppercase letters
target=target.replace(" ","")
target=target.upper()
listarr=list(set(list(target)))
#listarr=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Generate and fill a two-dimensional array for storing the wordsearch
store=numpy.zeros((NLetters,NLetters),numpy.string0)
for y in xrange(NLetters):
    store[y,:]=[random.sample(listarr,1)[0] for i in xrange(NLetters)]

pos=0 # Number of positive (or forward) solutions
neg=0 # Number of negative (or backward) solutions

# Check if there are any horizontal solutions
xsol=[' ']*NLetters
for x in xrange(NLetters):
    bigword="".join(store[:,x])
    psol=bigword.count(target) # Positive (or forward) solution
    nsol=bigword.count(target[::-1]) # Negative (or backward) solution
    if psol>0:
        xsol[x]="+"
    if nsol>0:
        xsol[x]="-"
    if psol>0 and nsol>0:
        xsol[x]="*"
    pos+=psol
    neg+=nsol

# Check if there are any vertical solutions
ysol=[' ']*NLetters
for y in xrange(NLetters):
    bigword="".join(store[y,:])
    psol=bigword.count(target) # Positive (or forward) solution
    nsol=bigword.count(target[::-1]) # Negative (or backward) solution
    if psol>0:
        ysol[y]="+"
    if nsol>0:
        ysol[y]="-"
    if psol>0 and nsol>0:
        ysol[y]="*" 
    pos+=psol
    neg+=nsol
    
if printsol:
    # Print wordsearch and indicate solutions
    for y in xrange(NLetters):
        output="".join(store[y,:])+ysol[y]
        print(output)
    print("".join(xsol))
print(pos,neg)
    


