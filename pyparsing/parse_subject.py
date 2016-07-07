# subject pyparsing definition

#
# This is an oversimplified syntax of the mbox's summary
#

from pyparsing import Word, alphanums, Literal, OneOrMore, printables, Optional
from common import start, end, colon, opensquare, closesquare

prefix        = opensquare + OneOrMore(Word(alphanums+"/,")) + closesquare
target        = Word(alphanums+"/_-.+")
summary       = OneOrMore(Word(printables))
subject       = start + Optional(prefix) + target + colon + summary + end
