import re

REGEX = r"(^\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\]) <(.*)> (.*)"
USERNAME = 'davidcramer'

def parse_message(message):
    parsed = re.search(REGEX, message)
    if parsed:
        return (parsed.group(1), parsed.group(2), parsed.group(3))
    else:
        return ("", "", "")

