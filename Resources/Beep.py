# Import some functions from a library
import winsound
# Define a list of musical pitches and durations
music=((784,1),(880,1),(698,1),(349,1),(523,3))
# Loop through each note and play it with the Beep function
for x in music:
    winsound.Beep(x[0],250*x[1])
