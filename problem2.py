denominations = [10000,5000,2000,1000,500,200,100,25,10,5,1]

val = input("Enter any value: ")

input = float(val) * 100

count = 0

while input:
  if input - denominations[0] >= 0:
    input = input - denominations[0]
    count = count + 1
  else:
    del denominations[0]

print(count)