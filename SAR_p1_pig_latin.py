#!/usr/bin/env python
#! -*- encoding: utf8 -*-

"""
1.- Pig Latin

Nombre Alumno: Carlos Tecles del Romero

Nombre Alumno: Álvaro López Oró
"""

import sys
import pdb

def piglatin_word(word):
    """
    This function recieves a word in english (encoding)
    and translate it to PigLatin

    :param word: word given to Pig Latin
    :return: translated word
    """
    the_vowels = 'aeiouyAEIOUY'
    if not word[0].isalpha():
        return word
    elif word[0] in the_vowels:
        word += 'yay'
        return word
    else:
        prefix = ''
        rest = ''
        i = 0
        while i < len(word):
            prefix += word[i]
            i += 1
            if word[i] in the_vowels:
                break
        while i < len(word):
            rest += word[i]
            i += 1
        res = rest + prefix + 'ay'
        return res




def piglatin_sentence(sentence):
    """
    This function recieves a sentence in english and translate it to PigLatin

    :param sentence: the sentence given to PigLatin
    :return: translated sentence
    """
    t = sentence.split()
    res = ''
    for index in range(len(t)):
        res = res + ' ' + piglatin_word(t[index])
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1:
        i = 1
        sentence = ''
        while i < len(sys.argv):
            sentence += sys.argv[i]
            i += 1
        print "%s is %s in PigLatin" % (sentence,piglatin_sentence(sentence))
    else:
        while True:
            input = raw_input('Type string: ')
            if input is ' ':
                break
            else:
                print(piglatin_sentence(input))
            pass
