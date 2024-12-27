converter_choise=float(input('choose a converter:\n1. kg to pound\n2. pound to kg\n3. celsius to fahranheit\n4. fahranheit to celsius\n'))

if converter_choise ==1:
    first_converter=float(input('type how many kg u wanna convert into pound:\n'))
    print(f"{first_converter} kg is {first_converter*2.20462} pound")

elif converter_choise==2:
    second_converter=float(input('type how many pound u wanna convert into kg:\n'))
    print(f"{second_converter} pound is {second_converter*0.453592} kg")

elif converter_choise==3:
    third_converter=float(input('type what Celsius u wanna convert into Fahrenheit:\n'))
    print(f"{third_converter} Celsius is {(third_converter * 9/5) + 32} Fahrenheit")

elif converter_choise==4:
    fourth_converter=float(input('type what Fahrenheit u wanna convert into Celsius:\n'))
    print(f"{fourth_converter} Fahrenheit is {(fourth_converter - 32) / 1.8} Celsius")


#----------------------------------------------------------------------------------------------



score = int(input("Enter ur score (0-100):\n"))
if 0 <= score <= 100:
    if 90 <= score <= 100:
        grade = "A+"
    elif 80 <= score < 90:
        grade = "A"
    elif 70 <= score < 80:
        grade = "B"
    elif 60 <= score < 70:
        grade = "C"
    elif 50 <= score < 60:
        grade = "D"
    else:
        grade = "F"
        print(f"Your score is {score}, which is {grade}.")
else:
    print("Error: Please enter a score between 0 and 100.")



#---------------------------------------------------------------------------------


rub_to_usd = 0.013
usd_to_rub = 76.7
rub_to_krw = 16.7
krw_to_rub = 0.06
rub_to_uzs = 157.8
uzs_to_rub = 0.0063
usd_to_krw= 1297.5


print("Currencies:\nRUB (Rubles)\nUSD(US Dollars)\nKRW (Korean Won)\nUZS (Uzbek So'm)\n")
from_currency = input("Enter the source currency (RUB/USD/KRW/UZS):\n").upper()
to_currency = input("Enter the target currency (RUB/USD/KRW/UZS):\n").upper()


amount = float(input(f"Enter the amount in {from_currency}: "))


if from_currency == "RUB" and to_currency == "USD":
    result = amount * rub_to_usd
elif from_currency == "USD" and to_currency == "RUB":
    result = amount * usd_to_rub
elif from_currency == "RUB" and to_currency == "KRW":
    result = amount * rub_to_krw
elif from_currency == "KRW" and to_currency == "RUB":
    result = amount * krw_to_rub
elif from_currency == "RUB" and to_currency == "UZS":
    result = amount * rub_to_uzs
elif from_currency == "UZS" and to_currency == "RUB":
    result = amount * uzs_to_rub
elif from_currency == "USD" and to_currency == "KRW":
    result = amount * usd_to_krw
elif from_currency == to_currency:
    result = amount
else:
    result = None

if result != None:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}.")
else:
    print("Conversion not supported.")