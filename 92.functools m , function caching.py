"""
function caching functools k help se hoti
>>>import functools
>>>@iru_cache()
# ye wo method jisse func cach hotay
caching ka matalb k koi valur k liye agar function bar bar run ho raha hai to program uski value ko cache me store kar lega jisse next time fast function execution ho sake
ye tab kaam me aayga jab kuch hi values k sath bar bar kaam karna ho
tab computational time kam karne waste iska use krtey

"""
import time
from functools import lru_cache
@lru_cache(maxsize=None)
def show(num):
    time.sleep(2)
    return num*num
print("please wait: ")
print(show(5))
print(show(6))
print(show(7))
print(show(5))
