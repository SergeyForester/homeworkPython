#1
def my_round(number, ndigits):
    number=number*(10**ndigits)+0.41
    number = number//1
    return number/(10**ndigits)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#2

def lucky_ticket(ticket):
  ticket = str(ticket)
  t1 = ticket[:3]
  t2 = ticket[3:]
  sum1 = 0
  sum2 = 0
  for i in t1 : 
    sum1 = sum1 + int(i)
  #print (sum1)
  for i in t2 : 
    sum2 = sum2 + int(i)
  #print (sum2)
  if sum1 == sum2 : print ('Вам повезет')
  else : print ("В следующий раз повезет")
  
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
