word = input("Слово: ")
similar_words = input("Похожие слова: ").split()

words = {}

for cur_word in similar_words:
    word_len = len(word)
    cur_word_len = len(cur_word)
    lookup = [[0]*(cur_word_len+1) for _ in range(word_len+1)]
    for i in range(1, word_len+1):
        for j in range(1, cur_word_len+1):
            if word[i-1] == cur_word[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])
    words[cur_word] = lookup[n][m]
keys_words = list(words.keys())
sorted_tuple = sorted(words.items(), key=lambda x: -x[1])
print("answer: ", sorted_tuple[0][0])