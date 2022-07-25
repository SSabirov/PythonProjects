#program to check if string entered is palindrome. f.e "race car"

def is_palindrome(text):
    lower_case_text = text.lower()
    no_space_text = lower_case_text.replace(" ","")
    return no_space_text == no_space_text[::-1]



result=is_palindrome('Burger')
print(result)
result=is_palindrome('Race car')
print(result)
    
