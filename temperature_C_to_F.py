#write a code to convert from celcius to fahrenheit
#formula- C/5 = F - 32 / 9

temp = float(input('enter temperature: '))
unit = input('convert from Celcius to Fahreheit: ')

#conversion logic

if unit == 'C':
    print(temp, 'C = ', round((temp * 9/5) + 32, 2), 'F')
elif unit == 'F':
    print(temp, 'F = ', round((temp - 32) * 5/9, 2), 'C')
else:
    print('Invalid Input Enter C or F')
