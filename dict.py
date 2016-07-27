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


wordStruct = namedtuple('wordStruct', ['word', 'norm'])

def createFullDict(dictBase, affixBase):
    fullDict = []
    index = [('1', 0)]
    indexCounter = 0
    for i in range(0, 1000):
        for j in range(0, len(affixBase)):
            if affixBase[j].key in dictBase[i].keys:
                try:
                    newWord = applyAffix(dictBase[i].word, affixBase[j])
                    if newWord != '-1':
                        fullDict.append(wordStruct(newWord, dictBase[i].word))
                        if newWord[:4] != index[indexCounter][0]:
                            index.append((newWord[:4], len(fullDict)-1))
                            indexCounter += 1
                except:
                    print dictBase[i].word + " | " + dictBase[i].keys
                    print affixBase[j].key + " | " + affixBase[j].rem + " | " + affixBase[j].add + " | " + affixBase[j].pat + " | " + affixBase[j].arr + " | " + str(affixBase[j].neg)
                    break
    return (fullDict, index)

dictBase = parseDictFile(dictFile)
fullBaseIndexed = createFullDict(dictBase, affixBase)
fullBase = fullBaseIndexed[0]
index = fullBaseIndexed[1]

print fullBase[1900].word
print fullBase[1900].norm
print index[18][0]
print fullBase[index[18][1]-1].word
print fullBase[index[18][1]-1].norm
print fullBase[index[18][1]].word
print fullBase[index[18][1]].norm
