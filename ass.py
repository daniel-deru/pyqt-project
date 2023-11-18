nTotal=0
#student number has 8 digits!
for icount in range (1,9,1):
    ndigit=int(input('enter the next digit in your student number : '))
    nTotal = nTotal + ndigit
print('the total is : ', nTotal)