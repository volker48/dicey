import random
from flask import Flask, abort

app = Flask(__name__)

r = random.SystemRandom()

words = []

with open('eff_large_wordlist.txt', 'r') as f:
    for line in f:
        _, word = line.split()
        words.append(word)

def get_words(num_words=6):
    return ' '.join(r.sample(words, num_words))

@app.route('/')
def index():
    return get_words()

@app.route('/<int:num_words>')
def custom_number(num_words):
    if num_words < 6:
        abort(400, 'the minimum number of words is 6')
    return get_words(num_words)
    

if __name__ == '__main__':
    app.run()
