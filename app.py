import random
from flask import Flask

app = Flask(__name__)

word_lookup = {}

r = random.SystemRandom()

with open('eff_large_wordlist.txt', 'r') as f:
    for line in f:
        index, word = line.split()
        word_lookup[index] = word

def get_word():
    ints = [r.randrange(1, 7) for _ in range(5)]
    strs = [str(i) for i in ints]
    index = ''.join(strs)
    return word_lookup[index]

@app.route('/<int:num_words>')
def index(num_words):
    words = []
    for _ in range(num_words):
        words.append(get_word())
    return ' '.join(words)
    

if __name__ == '__main__':
    app.run()
