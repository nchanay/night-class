# Count Words

from string import punctuation

with open('grimm.txt', 'r') as f:
    contents = f.read()


def top_ten(count):
    test = []
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(count.items())  # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        test.append(f'{words[i][0]}: {words[i][1]}')
    return '\n'.join(test)


alt_contents = contents.translate(str.maketrans('', '', punctuation + '‘')).lower().split()

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


dict_words = {}
for i in alt_contents:
    if i in STOPWORDS:
        pass
    else:
        dict_words[i] = dict_words.get(i, 0) + 1

print(top_ten(dict_words) + '\n')

pair_list = list(zip(alt_contents[:], alt_contents[1:]))

dict_pairs = {}
for i in pair_list:
    dict_pairs[i] = dict_pairs.get(i, 0) + 1

print(top_ten(dict_pairs) + '\n')

user_word = input("Please select a word, and I will let you know which word most often follows it : ").lower().strip()
if user_word in alt_contents:
    words = list(dict_pairs.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in words:
        if i[0][0] == user_word:
            print(i[0][1])
            break
else:
    user_word = input("Please selcet another word : ")
