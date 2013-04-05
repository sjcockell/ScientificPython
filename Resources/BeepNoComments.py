import winsound
music=((784,1),(880,1),(698,1),(349,1),(523,3))
for x in music:
    winsound.Beep(x[0],250*x[1])
