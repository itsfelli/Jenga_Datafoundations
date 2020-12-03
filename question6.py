# This program writes to a file the numbers 1 to 100,
#and their squares and square roots

import math

def calc ():
    
    outfile=open ("calculations.txt","w")


    for i in range (1,101):
        square= i*i
        root= math.sqrt (i)

        print (i,"\t",square,"\t",format(root, ".3f"),"\n",file=outfile)



    outfile.close ()


calc ()
    
