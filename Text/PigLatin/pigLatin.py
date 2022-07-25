#Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay)

def pig_latin(word):

    first_char = word[0]
    rest_of_the_word= word[1::]

    print(rest_of_the_word+"-"+first_char+"ay")



pig_latin('Banana')