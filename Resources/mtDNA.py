# string package is for analysing text
# urllib is for downloading data from the web
import string, urllib

# Text file derived from http://www.mitomap.org/MITOMAP/HumanMitoSeq
URL="http://www.staff.ncl.ac.uk/conor.lawless/ScientificPython/Resources/mtDNA.txt"
textfile=urllib.urlopen(URL)
#textfile=open("H:\\mtDNA.txt","r")
lines=textfile.readlines()
textfile.close()
mtDNA=string.join(lines,sep="")

# Let's get rid of the newline caracters
mtDNA=string.replace(mtDNA,"\n","")
# Count the total number of bases
nBases=len(mtDNA)
print "Number of bases", nBases

# Count the number of each base in the genome
print "Guanine",string.count(mtDNA,"G")
print "Adenine", string.count(mtDNA,"A")
print "Thymine", string.count(mtDNA,"T")
print "Cytosine", string.count(mtDNA,"C")

# Count the number of times base sequences appear
print "GATTACA", string.count(mtDNA,"GATTACA")
print "CAT", string.count(mtDNA,"CAT")
print "TAG", string.count(mtDNA,"TAG")

# mtDNA is circular, so to emulate that, we join 3 copies together
bigmtDNA=mtDNA+mtDNA+mtDNA

bRange=500
query="CAT"
results=[]
# At every base, we count a range of positions centred at that base
# and count the number of times the query string appears
for x in xrange(nBases,2*nBases):
    xmin=x-bRange
    xmax=x+bRange
    results.append(string.count(bigmtDNA[xmin:xmax],query))

# Generate a report about the frequency of occurance of the query string
print "Lowest frequency", float(min(results))/(1+2*bRange)
print "Highest frequency", float(max(results))/(1+2*bRange)
print "Average overall frequency", float(string.count(mtDNA,query))/nBases
