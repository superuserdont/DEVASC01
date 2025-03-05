#gives numbers that are divisible by 7 and are multiples of 5

numbers = [n for n in range (1500,2701) if n%7 == 0 and n%5 == 0]

print('these are the numbers divisible by 7 and multiples of 5: ')
print(numbers)