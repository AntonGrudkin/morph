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

affixStruct = namedtuple('affixStruct', ['key', 'rem', 'add', 'pat', 'arr', 'neg'])


def parseAffixString(str):
    s = str.split(' ')
    p = parsePattern(s[4][:-1])
    return affixStruct(s[1], s[2], s[3], p[0], p[1], p[2])


def matchPattern(str, affix):
    if str[-len(affix.pat):] == affix.pat:
        if affix.arr != '':
            if affix.neg and str[-(len(affix.pat)+1)] not in affix.arr:
                return 1
            elif not affix.neg and str[-(len(affix.pat)+1)] in affix.arr:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


def applyAffix(str, affix):
    if matchPattern(str, affix):
        if affix.rem != '0':
            if affix.add != '0':
                return str[:-len(affix.rem)]+affix.add
            else:
                return str[:-len(affix.rem)]
        else:
            if affix.add != '0':
                return str + affix.add
            else:
                return str
    else:
        return '-1'


def parseAffixFile(affixFile):
    affixContent = affixFile.readlines()[3:]
    affixBase = []
    for i in range(0, len(affixContent)):
        try:
            affixBase.append(parseAffixString(affixContent[i]))
        except:
            pass
    return affixBase
