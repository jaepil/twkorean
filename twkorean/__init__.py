# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong

import os
import imp

from collections import namedtuple

import jpype

from .escape import to_unicode, to_utf8, unicode_type


def _init_jvm():
    if not jpype.isJVMStarted():
        jars = []
        for top, dirs, files in os.walk(imp.find_module("twkorean")[1] + "/data/lib"):
            for nm in files:
                jars.append(os.path.join(top, nm))
        jpype.startJVM(jpype.getDefaultJVMPath(),
                       "-Djava.class.path=%s" % os.pathsep.join(jars))

_init_jvm()


_TwitterKoreanProcessorBuilder = jpype.JClass(
    "com.twitter.penguin.korean.TwitterKoreanProcessorJava$Builder")

KoreanToken = namedtuple("KoreanToken", ["text", "pos", "unknown"])
KoreanSegment = namedtuple("KoreanSegment", ["start", "length", "token"])
KoreanSegmentWithText = namedtuple("KoreanSegmentWithText", ["text", "segments"])
StemmedTextWithTokens = namedtuple("StemmedTextWithTokens", ["text", "tokens"])


class TwitterKoreanProcessor(object):
    def __init__(self, normalization=True, stemming=True):
        super(TwitterKoreanProcessor, self).__init__()

        builder = _TwitterKoreanProcessorBuilder()
        if not normalization:
            builder.disableNormalizer()
        if not stemming:
            builder.disableStemmer()

        self._processor = builder.build()

    def normalize(self, text):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type)\
            else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        return decode(self._processor.normalize(encode(text)))

    # def stem(self, text):
    #     pass

    def tokenize(self, text):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type)\
            else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        tokens = self._processor.tokenize(encode(text))
        return [
            KoreanToken(
                text=decode(t.text()), pos=decode(t.pos().toString()), unknown=t.unknown()
            ) for t in tokens
        ]

    def tokenize_to_strings(self, text):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type)\
            else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        tokens = self._processor.tokenizeToStrings(encode(text))
        return [decode(t) for t in tokens]

    def tokenize_with_index(self, text):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type)\
            else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        result = []
        tokens = self._processor.tokenizeWithIndex(encode(text))
        for t in tokens:
            token = KoreanToken(text=decode(t.token().text()),
                                pos=decode(t.token().pos().toString()),
                                unknown=t.token().unknown())
            segment = KoreanSegment(start=t.start(), length=t.length(), token=token)
            result.append(segment)

        return result

    # def tokenize_with_index_with_stemmer(self, text):
    #     encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type)\
    #         else jpype.java.lang.String(to_unicode(t))
    #     decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

    #     token = self._processor.tokenizeWithIndexWithStemmer(encode(text))
    #     segments = []
    #     for segment in token.segments():
    #         token = KoreanToken(text=decode(segment.token().text()),
    #                             pos=decode(segment.token().pos().toString()),
    #                             unknown=segment.token().unknown())
    #         segment = KoreanSegment(start=segment.start(), length=segment.length(), token=token)
    #         segments.append(segment)

    #     return KoreanSegmentWithText(text=decode(token.text()), segments=segments)
