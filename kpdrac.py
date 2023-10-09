'''input = [1, 10, 44, 12, 0, -1]

def findMax(input):
    result_max = 0
    for nums in input
        if nums > result_max:
            result_max == nums
        return result_max


    # Write code here to find the maximum

    print('The maximum of the input is: ',result_max)'''

#print ("Convet from (Clelsius to Fahrenheit or (Fahrenheit to Celcius(E)xit)
#asking_ input = input ()
#if asking input == 'C*:
#print ()


def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius (fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    choice = input("Convet from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius or (E)xit:")

    if choice == 'C':
        celsius = (input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print("Temperature In Fahrenheit:", result)
    elif choice == 'F':
        fahrenheit = (input("Enter temperature in Fahrenheit: "))
        resulti = fahrenheit_to_celsius (fahrenheit)
        print( "Temperature in Celsius:", result1)
    elif choice == 'E':
        break