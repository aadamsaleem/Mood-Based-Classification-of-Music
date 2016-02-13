from sklearn import svm
import pandas as p
import numpy as np
import csv
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn import metrics,preprocessing,cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer


	#A = list(np.array(p.read_table('train.tsv')))
A = np.array(p.read_table('train.tsv'))
X = list(A[:,1])
Y = np.array(p.read_csv('train.csv'))[:,2:]
print 'Group #'
print '  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18'
print Y
#xlist = [1]
#ylist = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#X= [[each_list[i] for i in xlist] for each_list in A]
#Y= [[long(each_list[i]) for i in ylist] for each_list in A]
#y = list(np.array(p.read_table('train.tsv')
#with open('train.csv') as csvfile:
 #   temp = csv.reader(csvfile, delimiter=',')
  #  for row in temp:
   #     row = list(row)
	#    print row


