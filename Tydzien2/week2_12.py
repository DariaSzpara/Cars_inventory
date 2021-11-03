a = "Lorem ipsum dolor sit amet"
def split(word):
    return [char for char in word]
word = "Lorem ipsum dolor sit amet"
x = len(split(word))
i =int(1)
b =int(0)
while i <= x:
    vowels = {"a", "ą", "e", "ę", "i", "o", "u", "A", "Ą", "E", "Ę", "I", "O", "U"}
    i = i+1
    if any(char in vowels for char in split(word[b])):
       print("vowel")
    else:
        print("consonant")
    b = b+1