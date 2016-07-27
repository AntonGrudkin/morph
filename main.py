from dict import loadIndexFromCSV, normWord


def morphNorm(text, dictSource='dictBase.csv', indexSource='index.csv'):
    index = loadIndexFromCSV(indexSource)
    words = text.split(' ')
    normWords = []
    for word in words:
        if len(word) < 4:
            normWords.append(word)
        else:
            normWords.append(normWord(word, dictSource, index))
    return ' '.join(normWords)


# inputFile = open('input.txt', 'rb')
# s = inputFile.read()
# inputFile.close()
#
# outputFile = open('output.txt', 'wb')
# outputFile.write(morphNorm(s))
# outputFile.close()