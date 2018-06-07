from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

import sys

import csv

### ANKI 2.0 PLUGIN

hanzi2rad = {}
with open("hanzi_meaning_decomp.txt") as f:
    ls = f.readlines()[1:]
    for l in csv.reader(ls, quotechar='"', delimiter=',',
                        quoting=csv.QUOTE_ALL, skipinitialspace=True):
        hanzi2rad[l[0].decode('utf-8')] = "{} ({}): {}".format(l[0], l[1], l[2]).decode('utf-8')

kanji2rad = {}
with open("kanji_meaning_decomp.csv") as f:
    ls = f.readlines()[1:]
    for l in csv.reader(ls, quotechar='"', delimiter=',',
                        quoting=csv.QUOTE_ALL, skipinitialspace=True):
        kanji2rad[l[0].decode('utf-8')] = "{} ({}): {}".format(l[0], l[1], l[2]).decode('utf-8')


def writeRadicalFieldHSK():
    ids = mw.col.findCards('mid:1393816261464')
    for id in ids:
        card = mw.col.getCard(id)
        note = card.note()
        explained = []
        for c in note['Simplified']:
            if c in kanji2rad:
                explained.append(kanji2rad[c])
        note['Radicals'] = '<br/>'.join(explained)
        note.flush()

    mw.reset()


def writeRadicalFieldJapVocab():
    ids = mw.col.findCards('mid:1342695926185')
    for id in ids:
        card = mw.col.getCard(id)
        note = card.note()
        explained = []
        for c in note['Expression']:
            if c in kanji2rad:
                explained.append(kanji2rad[c])
        note['Radicals'] = '<br/>'.join(explained)
        note.flush()

    mw.reset()


def writeRadicalFieldJapSent():
    ids = mw.col.findCards('mid:1342695926183')
    for id in ids:
        card = mw.col.getCard(id)
        note = card.note()
        explained = []
        for c in note['Expression']:
            if c in kanji2rad:
                explained.append(kanji2rad[c])
        note['Radicals'] = '<br/>'.join(explained)
        note.flush()

    mw.reset()


action = QAction("Write radicals HSK (Mandarin Vocab)", mw)
action.triggered.connect(writeRadicalFieldHSK)
mw.form.menuTools.addAction(action)

action = QAction("Write radicals Japanese Vocabulary", mw)
action.triggered.connect(writeRadicalFieldJapVocab)
mw.form.menuTools.addAction(action)

action = QAction("Write radicals Japanese Sentences", mw)
action.triggered.connect(writeRadicalFieldJapSent)
mw.form.menuTools.addAction(action)
