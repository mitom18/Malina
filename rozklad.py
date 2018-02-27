#coding:utf-8
from math import sqrt
print (15)
cislo=input("Zadejte číslo, které mám otestovat:")
while(cislo>1):
  odm=sqrt(cislo)+1 #kvůli chybám v odmocnině
  d=2
  while(cislo%d>0)and(d<=odm):
    d+=1
  if(d>odm):
    d=cislo
  print(d)
  cislo/=d

