# Function to count vowels (in english letters: 'a' 'e' 'i' 'o' and 'u')


def count_vowels(text):
    text.lower()
    a=0
    e=0
    i=0
    o=0
    u=0
    for x in text:
        if x =='a':
            a+=1
        elif x=='e':
            e+=1
        elif x=='i':
            i+=1
        elif x=='o':
            o+=1
        elif x=='u':
            u+=1
    
    all_vowels= a+e+i+o+u
    print("A occured : {} times.".format(a))
    print("E occured : {} times.".format(e))
    print("i occured : {} times.".format(i))
    print("O occured : {} times.".format(o))
    print("U occured : {} times.".format(u))
    print("Total of : {} vowels occured".format(all_vowels))

count_vowels("Said")





