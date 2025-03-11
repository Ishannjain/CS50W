import sys
try:
   x=int(input())
   y=int(input())
except ValueError:
    print("value error")
try:
   result=x/y
except ZeroDivisionError:
  print("error")
  sys.exit(1)
print(result)