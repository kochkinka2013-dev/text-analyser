
text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]
for i in punctuation:
    text = text.replace(i, "")


words = text.split()

print("Количество разных слов:", len(set(words)))


word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, count in word_frequency.items():
    print(word, ":", count)


