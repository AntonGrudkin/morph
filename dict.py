from affix import *

dictFile = open('ru_RU_1251_UTF8.dic', 'r')
affixFile = open('ru_RU_1251_UTF8.aff', 'r')

affixBase = parseAffixFile(affixFile)
dictStruct = namedtuple('dictStruct', ['word', 'keys'])


def parseDictString(str):
    if '/' in str:
        s = str.split('/')
        return dictStruct(s[0], s[1])
    else:
        return dictStruct(str, '')


def parseDictFile(dictFile):
    dictContent = dictFile.readlines()
    dictBase = []
    for i in range(0, len(dictContent)):
        try:
            dictBase.append(parseDictString(dictContent[i]))
        except:
            print dictContent[i]
            break
    return dictBase


dictBase = parseDictFile(dictFile)
s = dictBase[90985]
print s.word
print s.keys
