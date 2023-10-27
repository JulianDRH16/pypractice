f_temperature = input("Write temperature in Fahrenheit: ")
f_temperature = float(f_temperature)

c_temperature= (f_temperature - 32)/1.8
print(type(c_temperature))

text_result = f"The temperature in celcius is {c_temperature}"
print(text_result)