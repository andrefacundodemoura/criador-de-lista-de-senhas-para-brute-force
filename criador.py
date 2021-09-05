from itertools import combinations
from tkinter import *

janela=Tk()
janela.title('brute')
janela.configure(background='gray')

result = Text(janela, height = 20, width = 200)
result.insert(INSERT, '                   resultado: \n')
result.pack()

a=(0,1,2,3,4,5,6,7,8,9,
   '!','@','.','°','%','&','*','-','_','=','+',
   'a','A','b','B','c','C','d','D',
   'e','E','f','F','g','G','h','H',
   'i','I','j','J','k','K','l','L',
   'm','M','n','N','o','O','p','P',
   'q','Q','r','R','s','S','t','T',
   'u','U','v','V','w','W','x','X',
   'y','Y','z','z',)
lista=list(range(4,17))
cont=0
for n in lista:
    for r in combinations(a ,n):
        result.insert(INSERT,r)
        result.insert(INSERT,'\n')

janela.geometry('650x650')
janela.mainloop()
