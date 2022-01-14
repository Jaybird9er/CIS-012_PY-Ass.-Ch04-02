def returnRomanThousandsPlace(thousandsPlace):
    if thousandsPlace % 3 == 0:
        return "MMM"
    else:
        return "M" * (thousandsPlace % 3)

def returnRomanHundredsPlace(hundredsPlace):
    if hundredsPlace == 0:
        return ""
    elif hundredsPlace % 9 == 0:
        return "CM"
    elif hundredsPlace % 9 > 5:
        hundreds = (hundredsPlace % 9 - 5) * "C"
        return 'D' + hundreds
    elif hundredsPlace % 9 == 5:
        return 'D'
    elif hundredsPlace % 9 == 4:
        return "CD"
    else:
        return (hundredsPlace % 9) * "C"

def returnRomanTensPlace(tensPlace):
    if tensPlace == 0:
        return ""
    elif tensPlace % 9 == 0:
        return "XD"
    elif tensPlace % 9 > 5:
        tens = (tensPlace % 9 - 5) * "X"
        return 'L' + tens
    elif tensPlace % 9 == 5:
        return 'L'
    elif tensPlace % 9 == 4:
        return "XL"
    else:
        return (tensPlace % 9) * "X"

def returnRomanOnesPlace(onesPlace):
    if onesPlace == 0:
        return ""
    elif onesPlace % 9 == 0:
        return "IX"
    elif onesPlace % 9 > 5:
        ones = (onesPlace % 9 - 5) * "I"
        return 'V' + ones
    elif onesPlace % 9 == 5:
        return 'V'
    elif onesPlace % 9 == 4:
        return "IV"
    else:
        return (onesPlace % 9) * "I"

print("Enter a year between 1000 to 3000: ")
userYear = int(input())

thousandsPlace = userYear - userYear % 1000
userYear -= thousandsPlace
hundredsPlace = userYear - userYear % 100
userYear -= hundredsPlace
tensPlace = userYear - userYear % 10
userYear -= tensPlace
onesPlace = userYear

print('\n')
print("Your number in roman numerals is: ", end = '')
print(returnRomanThousandsPlace(thousandsPlace), end = '')
print(returnRomanHundredsPlace(hundredsPlace), end = '')
print(returnRomanTensPlace(tensPlace), end = '')
print(returnRomanOnesPlace(onesPlace), end = '')

#print(type(returnRomanHundredsPlace(hundredsPlace)))
