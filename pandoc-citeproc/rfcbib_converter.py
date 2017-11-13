# This script processes the rfc.bib file from: https://tm.uka.de/~bless/bibrfcindex.html 
# It strips out a few unnecessary fields to prettify the resulting references.
import sys

i = sys.argv[1]
lines = open(i).readlines()
for line in lines:
    if line.startswith("  pages=") or line.startswith("  institution="):
        continue
    print line,

        
