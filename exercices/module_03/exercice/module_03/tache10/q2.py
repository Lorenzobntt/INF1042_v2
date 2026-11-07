
c = float(input("Temperature en Celsius : "))

if c < -273.15:
    print("Temperature impossible")
else:
    f = c * 9 / 5 + 32
    k = c + 273.15

    print("Celsius :", c)
    print("Fahrenheit :", round(f, 2))
    print("Kelvin :", round(k, 2))