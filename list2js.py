import csv

with open("hanzi_meaning_decomp.txt") as f:
    ls = f.readlines()[1:]
    entries = []
    for l in csv.reader(ls, quotechar='"', delimiter=',',
                        quoting=csv.QUOTE_ALL, skipinitialspace=True):
        entries.append("'{}': '({}): {}'".format(l[0], l[1], l[2]))
    js = 'hanzi2rad = {' + ','.join(entries) + '};'

    with open('hanzi2rad.js', 'w') as f2:
        f2.write(js)
