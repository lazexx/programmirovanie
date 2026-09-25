import random
a = random.randint(1, 9)
b = random.choice('!@#$%^&*')+random.choice('!@#$%^&*')+random.choice('!@#$%^&*')
c = random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')+random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')+random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
print(str(a)+b+c)

