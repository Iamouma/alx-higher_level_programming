#!/usr/bin/python3
def multiple_returns(sentence):
    s_len = 0
    if len(sentence) == 0:
        return (0, None)
    for i in (sentence):
        s_len += 1
    tuple = (s_len, sentence[0])
    return (tuple)
