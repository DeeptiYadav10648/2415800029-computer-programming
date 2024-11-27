#3 count vowels in a string
st=input()
sum=0
vowels="aeiou"
for char in st:
    if char in vowels:
        sum=sum+1
print(sum)
