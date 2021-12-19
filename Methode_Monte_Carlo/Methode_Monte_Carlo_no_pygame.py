
import random



s = 700
HIT = 0
Total = 0
lauched = True



while lauched:

    l = random.sample(range(1,s), 2)
    if (l[0] - s) * (l[0] - s) + (l[1] - s) * (l[1] - s) <= s * s:
        HIT = HIT + 1 
        Total = Total + 1
    else:
        Total = Total + 1
    
    print (f"pi = {HIT/Total*4}")