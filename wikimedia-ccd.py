import csv

# from https://docs.google.com/spreadsheets/d/15atFtTRv7U5pvOFZex5ksMiutpHvaD2sqWPaFy4XCd8/edit#gid=692138841
# sourced from https://www.yellowbridge.com/chinese/radicals.php
radicals = {}
with open('Chinese Radicals Set 2 2017-04-09  - Chinese Radicals Set 2.csv') as f:
    for l in f:
        ss = l[:-1].split(',')
        # discard pronounciation
        radicals[ss[0]] = ss[2]

print('Loaded Radicals.')


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
    if hanzi in radicals:
        # it might be possible to decompose it further, but it'll get more confusing
        l.append(hanzi)
        return
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


def simplify_meaning(meaning_str):
    # heavily simplify string, sometimes missing a few meanings
    # the purpose of this is not to provide a comprehensive explanation
    # but just to aid with memorization
    meanings = meaning_str.split(';')
    if len(meanings) > 1:
        meanings[:] = meanings[:1]
    for i, m in enumerate(meanings):
        synonyms = m.split(',')
        meanings[i] = synonyms[0]
    return ','.join(meanings)


characters = {}
# from https://docs.google.com/spreadsheets/d/1j5-67vdCUeAuIzmikeCgNmXaFZTuXtT4vesjnrqSOjI/edit#gid=512136205 (linked from https://ankiweb.net/shared/info/39888802)
with open('Copy of Most Common 3000 Chinese - ANKI with Traditional.csv') as f:
        for l in csv.reader(f.readlines(), quotechar='"', delimiter=',',
                            quoting=csv.QUOTE_ALL, skipinitialspace=True):
            hanzi = l[0]
            meaning = simplify_meaning(l[8])
            characters[hanzi] = meaning

def explain_decomp(dec):
    decomp_c = []
    for radical in dec:
        # use the radical explanation, if not available use the character explanation,
        # if not available just the hanzi itself
        if radical in radicals:
            decomp_c.append(radicals[radical])
        elif radical in characters:
            decomp_c.append(characters[radical])
        else:
            decomp_c.append(radical)
    return ' + '.join(decomp_c)

with open('hanzi_meaning_decomp.txt', 'w') as out:
    out.write('Kanji,Meaning,Radicals\n')
    for hanzi in characters.keys():
        meaning = characters[hanzi]
        dec = decompose(hanzi, keep_duplicates=False)
        if len(dec) == 0:
            print('WARNING')
        decomp_expl = explain_decomp(dec)
        decomp_expl = decomp_expl.replace("'", "")
        meaning = meaning.replace("'", "")
        out.write('{},"{}","{}"\n'.format(hanzi, meaning, decomp_expl))

print('Done.')
