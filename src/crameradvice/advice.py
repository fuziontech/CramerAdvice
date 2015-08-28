from __future__ import absolute_import

import fileinput
import os
import operator
import random
import tempfile

from crameradvice.markovstate import MarkovState
from crameradvice.parser import (
    parse_message,
)

USERNAME_FILTER = lambda u: u[1] == "davidcramer"
#USERNAME_FILTER = lambda u: True
IRC_LOGS = os.path.join('data', 'messages.txt')
KJV = os.path.join('data', 'KingJamesProgramming')


def main():
    markov = MarkovState(n=3)

    def charinput(paths):
        fi = fileinput.input(paths)
        for line in fi:
            for char in line:
                yield char
        fi.close()

    with open(IRC_LOGS, 'r') as f:
        with tempfile.TemporaryFile() as tf:
            user_messages = filter(USERNAME_FILTER, map(parse_message, f))
            get_message = operator.itemgetter(2)
            user_messages = map(get_message, user_messages)
            strip = operator.methodcaller("strip", "\r")
            user_messages = map(strip, user_messages)
            user_messages = "\n".join(user_messages)
            #TODO: regex out usernames and replace : with @ at the beginning
            #TODO: regex out all web links

            tf.writelines(user_messages)
            markov.train(iter(user_messages), noparagraphs=False)

    # Train the learner with the king james bible
    filepaths = map(lambda f: os.path.join(KJV, f), os.listdir(KJV))
    markov.train(charinput(filepaths), noparagraphs=False)

    prob = random.random()
    nodes = random.randint(5, 40)
    print "with nodes = {} and prob = {}".format(nodes, prob)
    return markov.generate(nodes, prob=prob, startf=lambda t: t == "fuziontech")

if __name__ == "__main__":
    print main()
