from __future__ import absolute_import

import os
import operator
import random

from crameradvice.markovstate import MarkovState
from crameradvice.parser import (
    parse_message,
)

USERNAME = "davidcramer"
IRC_LOGS = os.path.join('data', 'messages.txt')

def main():
    markov = MarkovState()

    with open(IRC_LOGS, 'r') as f:
        user_messages = filter(lambda m: m[1] == USERNAME, map(parse_message, f))
        get_message = operator.itemgetter(2)
        user_messages = map(get_message, user_messages)
        strip = operator.methodcaller("strip", "\r")
        user_messages = map(strip, user_messages)
        user_messages = "\n".join(user_messages)
        #TODO: regex out usernames and replace : with @ at the beginning
        #TODO: regex out all web links

    markov.train(iter(user_messages), noparagraphs=True)
    return markov.generate(random.randint(10, 25))

if __name__ == "__main__":
    print main()
