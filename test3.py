def number_translator(x):
    if x == 1:
        return 3
    elif x == 2:
        return 3
    elif x == 3:
        return 5
    elif x == 4:
        return 4
    elif x == 5:
        return 4
    elif x == 6:
        return 3
    elif x == 7:
        return 5
    elif x == 8:
        return 5
    elif x == 9:
        return 4
    elif x == 10:
        return 3
    elif x == 11:
        return 6
    elif x == 12:
        return 6
    elif x == 14:
        return 8
    elif x == 15:
        return 7
    elif x == 16:
        return 7
    elif x == 17:
        return 9
    elif x == 18:
        return 8
    elif x == 19:
        return 8
    elif x == 20:
        return 6
    elif x == 30:
        return 6
    elif x == 40:
        return 5
    elif x == 50:
        return 5
    elif x == 60:
        return 5
    elif x == 70:
        return 7
    elif x == 80:
        return 6
    elif x == 90:
        return 6

count = 0
for element in range(1, 1001):
    if element < 21:
        count += number_translator(element)              # for numbers 1 - 20
    elif 20 < element < 100:
        count += number_translator(int(str(element)[0]) * 10) + number_translator(int(str(element)[1]))  # for numbers 21 through 100
    elif element % 100 == 0 and element != 1000:
        count += number_translator(int(str(element)[0])) + 7   # for numbers divisible by 100, but not 1000
    elif element == 1000:
        count += 11                                          # just for 1000
    elif element % 100 < 20:
        count += number_translator(int(str(element)[0])) + 10 + number_translator(int(str(element)[1:3]))      # now I add in numbers like 101 - 120, 201 - 220, etc.
    else:
        count += number_translator(int(str(element)[0])) + 10 + number_translator(int(str(element)[1]) * 10) + number_translator(int(str(element)[2])) # now the rest( 121, 122, 123, 225, 256, 984, etc.)

print(count)