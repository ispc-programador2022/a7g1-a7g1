def comb(gnrnd):
   prod = []
   cleanList = []
   for x in gnrnd:
      if(x not in cleanList):
         cleanList.append(x)

   for i in range(len(cleanList)):
      for j in range(len(cleanList)-1-i):
            prod.append(cleanList[i]*cleanList[j+1+i]) 
   return prod