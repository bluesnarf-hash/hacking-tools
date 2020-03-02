import itertools
import string

print "---------------------------------------------------------"
print "-                                                        -"
print "-                                                        -"
print "-                     BRUTUS                             -"
print "-                                 BY Sachin Yadav        -"
print "-                                                        -"
print "-              * are required fields                     -"
print "-                                                        -"
print "---------------------------------------------------------"
       
       
try:
  input = raw_input('[-] enter the starting password if you know: ')
  min=int(raw_input('[-] set minimum length*: '))
  max=int(raw_input('[-] set maximum length*: '))
  str=raw_input('[-] enter the string character you want to include:')
  num=raw_input('[-] enter the number you want to include: ')
  special=raw_input('[-] enter speacial character you want to inlcude: ')
  payload=str+num+special
  if len(payload)<max:
    print "please enter payload value greater or equal to max value" 
    
  print "payload: "+payload
  for i in range(min,max):
      res = itertools.permutations(payload,i) # 3 is the length of your result.
      if len(input)>0:
          for i in res: 
              print input+''.join(i)
      else:
          for i in res:
              print ''.join(i)

except KeyboardInterrupt:
  print "exiting the method... "

