#! usr/bin/env python
# *-- coding : utf-8 --*


from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
import re
from nltk.tokenize import TweetTokenizer


def apply_tweettokenizer(inputtext):
    tt = TweetTokenizer()
    return tt.tokenize(inputtext)



def remove_num(str):
    string_no_numbers = re.sub("\d+", " ", str)
    return string_no_numbers


@dispatcher.add_method
def get_request(tweet):
    result_dict = {}
    tweet_rn = remove_num(tweet)
    tokenized_text = apply_tweettokenizer(tweet_rn)
    result_dict['text'] = tweet
    result_dict['tokens'] = str(tokenized_text)
    return result_dict



@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('https://young-crag-93833.herokuapp.com/', 0, application)