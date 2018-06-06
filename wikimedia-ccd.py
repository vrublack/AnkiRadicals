# from https://sourceforge.net/projects/hanzidecomposition/files/ (linked from https://commons.wikimedia.org/wiki/Commons_talk:Chinese_characters_decomposition)

with open('wiki_hanz_decomposition_ok.csv') as f:
    decomp = {}
    for l in f:
        ss = l[:-1].split(',')
        decomp[ss[0]] = ss[1:]


POS_IND = 1
LEFT_COMP_IND = 2
RIGHT_COMP_IND = 5


def decompose(hanzi):
    l = []
    _decompose(hanzi, l)
    return l

def _decompose(hanzi, l):
    if hanzi not in decomp:
        return None
    d = decomp[hanzi]
    left = d[LEFT_COMP_IND]
    right = d[RIGHT_COMP_IND]
    if d[POS_IND] == '一':
        l.append(left)
        return
    #l.append(left)
    for l_hanzi in left:
        _decompose(l_hanzi, l)
    for r_hanzi in right:
        if r_hanzi != '*':
            #l.append(right)
            _decompose(r_hanzi, l)

print('Done.')