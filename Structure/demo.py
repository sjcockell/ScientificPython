# Text like this, beginning with "#" is a comment.
# Comments are for humans to read and computers to ignore.

# CALCULATOR
# Python works as a calculator
print 2+2
print (2+2)*5
print ((12+12)/6)**2 # the symbol ** means "to the power of"

# VARIABLES
# Variables store values for later retrival
# The equals sign means: "store what is evaluated on the right
# using the name on the left"
a = 2+2
b = a*5
c = b**2
print a,b,c

# Variables can be of several different types
# Integer type variable (e.g. for counting)
a = 10
print a

# String type variable (e.g. for storing words)
a = "ten"
print a

# Float type variable (e.g. for storing real numbers)
a = 10.0
print a
a = 10
print a

# Python automatically chooses types for variables
# based on what you use them to store.
# A common mistake is to assume that integers should
# behave the same way as real numbers (floats)
print 10/6
print 10.0/6.0
print round(10.0/6.0)

# We can manually change the type of variables if we have to
a = 12
b = float(a)
print a,b

# CONDITIONS
# Python can test if conditional statements are true or false
print 3 > 4
print 4 > 3

# The symbol for "is equal to?" is "==", not "="
# We saw above that "=" is the assignment operator for variables
print 3 == 4
print 3 == 3 # If you try "print 3 = 3" you will get an error
print int(round(10.0/6.0)) == 10/6

# COLLECTIONS
# Python has various methods of grouping variables together

# Lists
testlist=[99,98,97,96,95,94,93,92,91]
# We can access list elements by their index
print testlist[3]
# Note that python indices start from zero
print testlist[0]
# We can use negative indices to access elements at the end of lists
print testlist[-1]
# We can access sections of lists by index
print testlist[2:5]
print testlist[3:]
# And we can find the length of lists
print len(testlist)
# We can easily add to lists
print testlist
testlist.append(90)
print len(testlist)
print testlist
# Lists don't have to be filled with numbers
fruits=["apples","pears","oranges","apples","bananas"]

# Dictionaries
# Another grouping method which is often useful is a dictionary
# It works quite differently to a list
# Here is an inventory at a zoo
zoo={}
zoo["elephant"]=4
zoo["monkey"]=12
zoo["giraffe"]=2
zoo["squirrel"]=100

print zoo
print zoo["squirrel"]
# Here is a small English dictionary
# Definitions from http://dictionary.reference.com/
English={}
English["elephant"]="Either  of  two  large,  five-toed  pachyderms  of  the  family  Elephantidae,  characterized  by  a  long,  prehensile  trunk  formed  of  the  nose  and  upper  lip."
English["monkey"]="Any mammal of the order Primates, including the guenons, macaques, langurs, and capuchins, but excluding humans, the anthropoid apes, and, usually, the tarsier and prosimians."
English["giraffe"]="A tall, long-necked, spotted ruminant, Giraffa camelopardalis, of Africa: the tallest living quadruped animal."
English["squirrel"]="Any of numerous arboreal, bushy-tailed rodents of the genus Sciurus, of the family Sciuridae."
print English
print English["squirrel"]

# LOOPS
# Computers specialise in performing repetitive tasks
# Programming loops is the main way to command computers
# to perform such tasks.
testlist=[99,98,97,96,95,94]

# for every element in testlist
for x in testlist:
    # note the indent <--
    # Python insists that blocks of related code
    # are represented by consistent indentation
    v1=x**2
    v2=x**3
    v3=x**4
    # print out a report, including the value of x, x**2 etc.
    print x,v1,v2,v3

# The for statement executes the block of indented code
# with each of the elements of testlist assigned to variable x in turn
# 7 times tables
for x in xrange(1,13):
    print "7 * "+str(x)+" = "+str(7*x)

# IF-THEN-ELSE
# In order for computers to be able to automatically make decisions
# we need a way to give them instructions to follow if a certain
# set of conditions are true.  We do this with an if-statement
z=33
# The test condition here is "z>10".  It can evaluate to "true" or "false"
# Only one of the two blocks of code below will be executed
if (z>10):
    # This indented block of code is executed if the condition is true
    print "z is big!"
    q=5
else:
    # This indented block of code is executed if the condition is false
    print "z is small!"
    q=1
# q has been assigned a value, depending on the value of z (whether it's big or small)
print q

# FUNCTIONS

# Often we want to repeat complicated set of instructions several times, but with different input
# but not in a single for-loop.  In this case it can be useful to define a function.  These are
# analagous to mathematical functions, they take some arguments as input, carry out some tasks, and
# optionally provide some output.  Typically, the advantage of installing Python packages is that they
# contain many complicated, interesting functions, that we can re-use if we just know what input data
# to supply them, and what they do.

# First let's look at an imported function
import random
# randint(a,b) generates random integers in range [a,b] including both endpoints
print random.randint(0,10)
print random.randint(0,10)
print random.randint(0,10)

# We can define our own function of a and b which does something different
def myfunc(a,b):
    c=a+b
    d=a**2
    return(c*d)

print myfunc(10,29)
print myfunc(1,2)
print myfunc(10.3,45.9)

# Multiplication tables
def multiTab(y):
    print str(y)+" times tables:\n"
    for x in xrange(1,13):
        print str(x)+" * "+str(y)+" = "+str(x*y)
    print "\n"

for z in xrange(1,13):
    multiTab(z)
