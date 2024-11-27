#17 the password validator
passwords = input()
for word in passwords:
    if (len(word)>=8 and any(word.islower() for word in passwords) and any(word.isupper() for word in passwords) and any(word.isdigit() for word in passwords)):
        print("strong")
    else:
        print("weak")
