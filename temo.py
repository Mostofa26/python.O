unit= input("is this temperature in celsius or fahrenheite (C/F):")
temp = float (input("enter the temperature: "))

if unit =="C":
    temp =round ((9* temp) /5+32,1)
    print(f" the temperature in fahrenheite is: {temp}°F")
elif unit =="F":
      temp =round ((temp-32)/1.8, 1)
      print ((f" the temperature in celsius is: {temp}°C"))
else:
    print(f"{unit}is an invalid unitof mesurement")