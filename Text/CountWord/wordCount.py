#Function to count word 

def word_count(text):
    word_count=0

    # We can repalce all possible symbols for precise answer
    text=text.replace("?","")
    text=text.replace("!","")
    text=text.replace(",","")
    text=text.replace(".","")

    for word in text.split():
        word_count +=1

    print("Number of Words: {}".format(word_count))


word_count("This is a test text to count a word, the result should be Fourteen ? ! . ")


