import math
import time
import calendar

#common math functions
print (math.ceil(4.4))
print (math.fabs(-2))
print (math.factorial(6))
print (math.fsum([1,2,3,4]))
print (math.gcd(2,22))
print (math.pow(2,3))

#trigonometry
print (math.acos(0))
print (math.cos(0))

#math constants
print (math.pi)
print (math.e)

#print epoch time jan 1st 12:00am 1970
print ("Current EPOCH time: ", time.time())

#print process time(typically used to measure process time of function call)
print ("CPU time:", time.clock())

#local time; get time struct
ltime = time.localtime(time.time())
print ("Current local time: ", ltime)

#format time struct
fltime = time.asctime(time.localtime(time.time()))
print ("Current formatted local time: ", fltime)

#sleep the main thread for x second; .001 = 1 millisecond ; 1 = 1 second
time.sleep(2)

#calendar print a given month of a year
cmonth = calendar.month(2010, 1)
print ("Calendar month below:")
print (cmonth)
