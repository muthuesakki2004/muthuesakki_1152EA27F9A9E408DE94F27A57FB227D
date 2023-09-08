def factorial(n): # recursive solution
   if (n==1 or n==0):
      return 1
   else:
      return n * factorial(n - 1)
# main
num = 6
print("Factorial of",num,"is", factorial(num))