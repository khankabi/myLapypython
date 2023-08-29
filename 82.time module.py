"""
The time Module in Python
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different scenarios.

time.time()
The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time. Here's an example:

>>>example 1
As you can see, the function returns the current time as a floating-point number, which can be used for various purposes, such as measuring the duration of an operation or the elapsed time since a certain point in time.

time.sleep()
The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads. Here's an example:

>>>example2
As you can see, the function time.sleep() suspends the execution of the program for 2 seconds, allowing other parts of the program to run during that time.

time.strftime()
The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. Here's an example:

>>>example 3
As you can see, the function time.strftime() formats the current time (obtained using time.localtime()) as a string, using a specified format. The format string contains codes that represent different parts of the time value, such as the year, the month, the day, the hour, the minute, and the second.

Conclusion
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. Whether you are writing a script, a library, or an application, the time module is a powerful tool that can help you perform time-related tasks with ease and efficiency. So, if you haven't already, be sure to check out the time module in Python and see how it can help you write better, more efficient code.
"""

import time
#time.time() : example 1
# tm=time.time()
# tmminute=tm/60
# tmhour=tmminute/60
# tmday=tmhour/24
# tmmonth=tmday/31
# print(tmmonth)




#time.sleep() :exmaple 2
# print("Start:", time.time())
# time.sleep(2)
# pr/int("End:", time.time())

# example 2.0
# print("Start:", time.time())
# after= time.time()
# time.sleep(2)
# before=int(time.time()-after)
# print("End in :", before)



#time.localtime() and time.strftime() : example 3
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
for i in t:
    print(i)
#print(t)
# print(type(t))
