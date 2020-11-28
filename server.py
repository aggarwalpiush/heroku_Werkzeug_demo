#! usr/bin/env python
# *-- coding : utf-8 --*

import re
from nltk.tokenize import TweetTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)


def apply_tweettokenizer(inputtext):
    tt = TweetTokenizer()
    return tt.tokenize(inputtext)



def remove_num(str):
    string_no_numbers = re.sub("\d+", " ", str)
    return string_no_numbers



@app.route('/post/', methods=['POST', "GET"])
def post_something():
    tweet = request.args.get('tweet')
    result_dict = {}
    tweet_rn = remove_num(tweet)
    tokenized_text = apply_tweettokenizer(tweet_rn)
    result_dict['text'] = tweet
    result_dict['tokens'] = str(tokenized_text)
    return jsonify(result_dict)


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)