number_words = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

number_word = ""

switcher = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        }



for i in range(1, 1001):

    current_word = ""
    j = str(i)

    if i < 20:
        current_word += number_words[i-1]
    elif(len(j) == 2):
        current_word += switcher.get(int(j[0]))

        if (int(j[1]) - 1) != -1:
            current_word += number_words[int(j[1]) - 1]
    elif(len(j) == 3):
        current_word += number_words[int(j[0]) - 1]
        current_word += "hundred"

        k = i % 100
        l = str(k)
        if k < 20 and k!=0:
            current_word += "and"

            current_word += number_words[k - 1]
        elif (len(l) == 2):
            current_word += "and"
            current_word += switcher.get(int(l[0]))

            if (int(l[1]) - 1) != -1:
                current_word += number_words[int(l[1]) - 1]
    elif(len(j) == 4):
        current_word += "onethousand"

    print(current_word)
    number_word += current_word

print(len(number_word))