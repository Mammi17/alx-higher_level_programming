#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_m = ()
    if len(sentence) == 0:
        tuple_m = 0, "None"
    else:
        tuple_m = len(sentence), sentence[0]
    return tuple_m
