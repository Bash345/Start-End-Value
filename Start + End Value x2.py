import random

sum1 = 0

sum2 = 0

sum3 = 0

mult = 3

for counter in range(1, 11):
    sum1 = counter*3 + sum1
    
    #print(sum1)
    
start = int(input('Start Value '))
    
end = int(input('End Value'))
    
counter = start
    
for counter in range (start, end):
    sum2 = counter*3 + sum2
    
    counter += 1
    
print(sum1)

s1 = random.randint(1, 11)
e1 = random.randint(1,11)

for counter in range (s1, e1):
    
    sum3 = counter * 3 + sum3
    
    counter += 1
    
print(sum3)
    
