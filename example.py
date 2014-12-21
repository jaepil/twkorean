# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong

from __future__ import print_function

from twkorean import TwitterKoreanProcessor


def print_tokens(tokens, end="\n"):
    if isinstance(tokens, list):
        print("[", end="")
    elif isinstance(tokens, tuple):
        print("(", end="")

    for t in tokens:
        if t != tokens[-1]:
            elem_end = ", "
        else:
            elem_end = ""

        if isinstance(t, (list, tuple)):
            print_tokens(t, end=elem_end)
        else:
            print(t, end=elem_end)

    if isinstance(tokens, list):
        print("]", end=end)
    elif isinstance(tokens, tuple):
        print(")", end=end)


text = u"한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ"

# Tokenize with normalization + stemmer
processor = TwitterKoreanProcessor()
# output: [한국어, 를, 처리, 하다, 예시, 이다, ㅋㅋ]
tokens = processor.tokenize_to_strings(text)
print_tokens(tokens)

# output: [
#     (한국어, Noun, 0), (를, Josa, 0), (처리, Noun, 0), (하다, Verb, 0),
#     (예시, Noun, 0), (이다, Adjective, 0), (ㅋㅋ, KoreanParticle, 0)
# ]
tokens = processor.tokenize(text)
print_tokens(tokens)


# Tokenize without stemmer
processor = TwitterKoreanProcessor(stemming=False)
# output: [한국어, 를, 처리, 하는, 예시, 입니, 다, ㅋㅋ]
tokens = processor.tokenize_to_strings(text)
print_tokens(tokens)

# output: [
#     (한국어, Noun, 0), (를, Josa, 0), (처리, Noun, 0), (하는, Verb, 0),
#     (예시, Noun, 0), (입니, Adjective, 0), (다, Eomi, 0), (ㅋㅋ, KoreanParticle, 0)
# ]
tokens = processor.tokenize(text)
print_tokens(tokens)


# Tokenize with neither normalization nor stemmer
processor = TwitterKoreanProcessor(normalization=False, stemming=False)
# output: [한국어, 를, 처리, 하는, 예시, 입니, 닼, ㅋㅋㅋㅋㅋ]
tokens = processor.tokenize_to_strings(text)
print_tokens(tokens)

# output: [
#     (한국어, Noun, 0), (를, Josa, 0), (처리, Noun, 0), (하는, Verb, 0),
#     (예시, Noun, 0), (입니, Adjective, 0), (닼, Noun, 1), (ㅋㅋㅋㅋㅋ, KoreanParticle, 0)
# ]
tokens = processor.tokenize(text)
print_tokens(tokens)
