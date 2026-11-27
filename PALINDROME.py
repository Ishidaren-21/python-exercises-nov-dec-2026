def palindrome(value):
    og_text = str(value).lower()
    reversed_text=""
    for i in og_text:
        reversed_text = i + reversed_text

    if og_text == reversed_text:
        print("It is a Palindrome")
    else:
        print("It is Not a Palindrome")

palindrome("MOM")
palindrome("Ishida")
palindrome(1221)
