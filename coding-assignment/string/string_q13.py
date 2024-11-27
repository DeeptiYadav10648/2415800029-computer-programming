#13 Find the Most Frequent Word in a String
st = input()
a = st.split()
freq_word=""
mcount = 0
for word in a:
    count=a.count(word)
    if count>mcount:
        mcount = count
        freq_word=word
print(freq_word)
