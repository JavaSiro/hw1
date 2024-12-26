converter_choise=float(input('choose a converter:\n1. kg to pound\n2. pound to kg\n3. celsius to fahranheit\n4. fahranheit to celsius\n'))
if converter_choise ==1:
    first_converter=float(input('type how many kg u wanna convert into pound:\n'))
    print(f"{first_converter} kg is {first_converter*2.20462} pounds")
elif converter_choise==2: