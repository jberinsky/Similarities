# Jason Berinsky
# CS 50 Problem Set 7
# Finds similarities between two files, either by line, by sentence, or by substring of chosen length

from nltk.tokenize import sent_tokenize, word_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    astrip = a.splitlines()
    bstrip = b.splitlines()
    lines = same(astrip, bstrip)
    trim = trimmer(lines)
    return trim


def sentences(a, b):
    """Return sentences in both a and b"""
    astrip = sent_tokenize(a)
    bstrip = sent_tokenize(b)
    lines = same(astrip, bstrip)
    trim = trimmer(lines)
    return trim


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    astrings = []
    bstrings = []
    a_len = len(a) - n + 1
    b_len = len(b) - n + 1
    for i in range(a_len):
        tempa = ""
        for j in range(n):
            tempa = tempa + a[i + j]
        astrings.append(tempa)

    for k in range(b_len):
        tempb = ""
        for l in range(n):
            tempb = tempb + b[k + l]
        bstrings.append(tempb)

    lines = []
    lines = same(astrings, bstrings)
    trim = trimmer(lines)
    return trim


def same(astrip, bstrip):
    lines = []
    for i in range(len(astrip)):
        for k in range(len(bstrip)):
            if astrip[i] == bstrip[k]:
                lines.append(bstrip[k])
    return lines


def trimmer(lines):
    trim = []
    for i in range(len(lines)):
        add = True
        for k in range(len(trim)):
            if lines[i] == trim[k]:
                add = False
        if add == True:
            trim.append(lines[i])
    return trim