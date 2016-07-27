from affix import *
import csv

dictFile = open('ru_RU_1251_UTF8.dic', 'r')
affixFile = open('ru_RU_1251_UTF8.aff', 'r')

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
    for i in range(0, len(dictBase)):
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


def compileCSV(dictBase, affixBase):
    fullBaseIndexed = createFullDict(dictBase, affixBase)
    fullBase = fullBaseIndexed[0]
    index = fullBaseIndexed[1]

    fullBaseFile = open('dictBase.csv', 'wb')
    csvFullBaseFile = csv.writer(fullBaseFile)
    csvFullBaseFile.writerow(['word', 'norm'])
    for row in fullBase:
        csvFullBaseFile.writerow(row)
    fullBaseFile.close()

    indexFile = open('index.csv', 'wb')
    csvIndexFile = csv.writer(indexFile)
    csvIndexFile.writerow(['let', 'num'])
    for row in index:
        csvIndexFile.writerow(row)
    indexFile.close()


def loadIndexFromCSV(indexSource):
    with open(indexSource, 'rb') as indexFile:
        indexReader = csv.reader(indexFile, delimiter=',')
        index = list(indexReader)
    indexFile.close()
    return index


def normWordFromBase(word, dictSource, fromTo):
    From = fromTo[0]
    To = fromTo[1]
    with open(dictSource, 'rb') as dictFile:
        dictReader = csv.reader(dictFile, delimiter=',')
        dictBase = list(dictReader)
        result = word
        for i in range(From, To):
            if dictBase[i][0] == word:
                result = dictBase[i][1]
                break
    dictFile.close()
    return result


def getFromTo(word, index):
    result = (-1, -1)
    if len(word) < 4:
        return result
    else:
        for i in range(0, len(index)-2):
            if word[0:4] == index[i][0]:
                result = (int(index[i][1]), int(index[i+1][1])-1)
                break
        if word[0:4] == index[len(index)-1][0]:
            result = (int(index[len(index)-1][1]), -1)
    return result


source = 'index.csv'
index = loadIndexFromCSV(source)
# print index[len(index)-1][0]

#
inputFile = open('input.txt', 'r')
s = inputFile.read()
print getFromTo(s, index)
print normWordFromBase(s, 'dictBase.csv', getFromTo(s, index))
# dictBase = parseDictFile(dictFile)
# affixBase = parseAffixFile(affixFile)
# dictFile.close()
# affixFile.close()

# compileCSV(dictBase, affixBase)


#
# print fullBase[16].word
# print fullBase[16].norm
