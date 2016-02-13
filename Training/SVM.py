from sklearn import svm
import pandas as p
import numpy as np
import csv
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn import metrics,preprocessing,cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer

#initialise stemmer
stemmer = SnowballStemmer("english")

def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed

def tokenize(text):
	tokens = PunktWordTokenizer().tokenize(text)
	stems = stem_tokens(tokens, stemmer)
	return stems

def main():
	rd = svm.LinearSVC(penalty='l2', dual=True, tol=0.0001, 
					   C=1, fit_intercept=True, intercept_scaling=1.0, 
					   class_weight=None, random_state=None)
	tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents='unicode',  
							analyzer='word',token_pattern=r'\w{1,}',ngram_range=(1, 2), 
							use_idf=1,smooth_idf=1,sublinear_tf=1,
							#stop_words=stopwords.words('english'),
							tokenizer=tokenize)
	#A = list(np.array(p.read_table('train.tsv')))
	A = np.array(p.read_table('train.tsv'))
	X = list(A[:,1])
	Y = list(np.array(p.read_csv('train.csv'))[:,2:])
	#test = list(np.array(p.read_table('train.tsv')[:,1]))
	lentrain = len(X)
	#X_all = X + test
	print "fitting pipeline"
	tfv.fit(X)
	print "transforming data"
	X_all = tfv.transform(X)
	X = X_all[:lentrain]
	#test = X_all[lentrain:]
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


	#clf = svm.SVC()
	print " Training in progress"
	#clf.fit(X,Y)
	print "20 Fold CV Score: ", np.mean(cross_validation.cross_val_score(rd, X, Y, cv=4, scoring='roc_auc'))

if __name__ == "__main__":
        main()
'''
pred = rd.predict(w)
print pred
'''
