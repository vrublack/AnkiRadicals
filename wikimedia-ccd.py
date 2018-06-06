# from https://sourceforge.net/projects/hanzidecomposition/files/ (linked from https://commons.wikimedia.org/wiki/Commons_talk:Chinese_characters_decomposition)

with open('wiki_hanz_decomposition_ok.csv') as f:
    decomp = {}
    for l in f:
        ss = l[:-1].split(',')
        decomp[ss[0]] = ss[1:]


POS_IND = 1
LEFT_COMP_IND = 2
RIGHT_COMP_IND = 5


def decompose(hanzi, keep_duplicates=True):
    l = []
    _decompose(hanzi, l)
    if not keep_duplicates:
        dupl_rem = []
        for comp in l:
            if comp not in dupl_rem:
                dupl_rem.append(comp)
        l = dupl_rem
    return l

def _decompose(hanzi, l):
    if hanzi == '*':
        return
    if hanzi not in decomp:
        return
    d = decomp[hanzi]
    left = d[LEFT_COMP_IND]
    right = d[RIGHT_COMP_IND]
    if right =='*' and len(left) == 1:
        l.append(left)
        return
    #l.append(left)
    for l_hanzi in left:
        _decompose(l_hanzi, l)
    for r_hanzi in right:
        #l.append(right)
        _decompose(r_hanzi, l)

print('Loaded Wikimedia CCD.')



# from https://docs.google.com/spreadsheets/d/1j5-67vdCUeAuIzmikeCgNmXaFZTuXtT4vesjnrqSOjI/edit#gid=512136205 (linked from https://ankiweb.net/shared/info/39888802)
with open('Copy of Most Common 3000 Chinese - ANKI with Traditional.csv') as f:
    for l in f:
        ss = l.split(',')
        hanzi = ss[0]
        dec = decompose(hanzi, keep_duplicates=False)
        if len(dec) == 0:
            print('WARNING')
        print('{}: {}'.format(hanzi, ' '.join(dec)))

print('Done.')
