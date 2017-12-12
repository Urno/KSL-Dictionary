#단어 분석 by KoNLPy
from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations

import konlpy
import nltk

#형태소 분석
# -*- coding: utf-8 -*-
from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
pprint (kkma.nouns(u"아버지가 방에 들어가신다. 그 방에는 내 동생이 있다."))


#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
# 문장의 설정
sentence = u'만 6세 이하의 초등학교 취학 전 자녀를 양육하기 위해서는'
words = konlpy.tag.Twitter().pos(sentence)

# 3가지 구문의 정의(명사구, 동사구, 형용사구)
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""

#문장의 구문을 분류하는 작업, 결과는 tree set 형태
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(words)
print("# Print whole tree")
print(chunks.pprint())


#명사구만 출력하는 경우
print("\n# Print noun phrases only")
for subtree in chunks.subtrees():
    if subtree.label()=='NP':
        print(' '.join((e[0] for e in list(subtree))))
        print(subtree.pprint())

# tree set 보기
chunks.draw()


#NLTK를 활용한 연어 탐색

#한국 법률 용어 사전 읽어들이기
measures = collocations.BigramAssocMeasures()
doc = kolaw.open('constitution.txt').read()

#가장 많이 나온 단어/품사 5위 출력
print('\nCollocations among tagged words:')
tagged_words = Kkma().pos(doc)
finder = collocations.BigramCollocationFinder.from_words(tagged_words)
pprint(finder.nbest(measures.pmi, 10))

#3회 이상 나오는 단어 출력
print('\nCollocations among words:')
words = [w for w, t in tagged_words]
ignored_words = [u'안녕'] #관련없는 문자 제거
finder = collocations.BigramCollocationFinder.from_words(words)
finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
finder.apply_freq_filter(3)
pprint(finder.nbest(measures.pmi, 10))

#가장 많이 나오는 품사 출력
print('\nCollocations among tags:')
tags = [t for w, t in tagged_words]
finder = collocations.BigramCollocationFinder.from_words(tags)
pprint(finder.nbest(measures.pmi, 5))
