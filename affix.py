from collections import namedtuple


def parsePattern(pattern):
    pat = ''
    arr = ''
    neg = 1
    if pattern[0] == '[':
        arr = pattern.split(']')[0][1:]
        pat = pattern.split(']')[1]
        if arr[0] == '^':
            arr = arr[1:]
        else:
            neg = 0
    else:
        pat = pattern
    return (pat, arr, neg)

myAffixStruct = namedtuple('myAffixStruct', ['key', 'rem', 'add', 'pat', 'arr', 'neg'])


def parseAffixString(str):
    s = str.split(' ')
    p = parsePattern(s[4][:-1])
    return myAffixStruct(s[1], s[2], s[3], p[0], p[1], p[2])


def matchPattern(str, affix):
    if str[-len(affix.pat):] == affix.pat:
        if affix.neg and str[-(len(affix.pat)+1)] not in affix.arr:
            return 1
        elif not affix.neg and str[-(len(affix.pat)+1)] in affix.arr:
            return 1
        else:
            return 0
    else:
        return 0


def applyAffix(str, affix):
    if matchPattern(str, affix):
        return str[:-len(affix.rem)]+affix.add
    else:
        return '-1'

affixFile = open('ru_RU_1251_UTF8.aff', 'r')
affixContent = affixFile.readlines()

print affixContent[177]
# print parseAffixString(affixContent[31])

inputFile = open('input.txt', 'r')
s = inputFile.read()
print s
myAffix = parseAffixString(affixContent[177])
print applyAffix(s, myAffix)
