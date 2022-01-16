"""
Given n as input, print the following pattern
n = 2
1+1*1+1*1*1=3 
2+2*2+2*2*2=14
"""

n = 4
num = 0
for i in range(1,n+1):
  num = i+i*i+i*i*i
  print(f"{i}+{i}*{i}+{i}*{i}*{i}={num}")
