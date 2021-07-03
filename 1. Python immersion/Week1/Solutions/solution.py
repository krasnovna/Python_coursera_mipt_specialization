import sys

# first task
'''
digit_string = sys.argv[1]

s = 0 
for w in digit_string:
	s = s + int(w)

print(s)
'''

# second task
'''
steps_num = int ( sys.argv[1] )
print("\n".join( [(steps_num - w)*' ' + w*'#'  for w in range(1,steps_num+1) ]) )
'''

# third task
import sys 
import math
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

D = b**2 - 4*a*c
x1 = (-b+math.sqrt(D))/(2*a)
x2 = (-b-math.sqrt(D))/(2*a)
print(int(x1))
print(int(x2))



































