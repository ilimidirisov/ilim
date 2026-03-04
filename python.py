import math
import os
import random
import re
import sys




n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n < 5 and n % 2 == 0:
    print("Not Weird")
elif n < 20 and n % 2 == 0 and n > 5:
    print("Weird")
else:
    print("Not Weird")