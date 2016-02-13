import os
from sklearn import svm
from mood import *
import pandas as p

PATH = 'Lyrics/'

tagval=[]
lyrics_x=[]
data = []
f1 = open('data.csv','w')
count = 0
abc="name,lyrics,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18\n"
f1.write(abc)

for filename in os.listdir('SocialTags/'):
        try:
                count += 1
                xyz = filename.replace('.txt','').replace('\"',' ').replace('\'','').replace(',','')
                temp = [xyz]
                mood=[0 for i in xrange(18)]
                f = open('SocialTags/'+filename,'r')
                tags = f.read().replace('\n',' ')
                tags = tags.split(',')
                flag = 0
                for x in xrange(18):
                        for word in tags:
                                if word.strip() in g[x]:
                                        mood[x] = 1
                                        flag = 1
                filename=PATH +filename
                f = open(filename,'r')
                lyrics = f.read().replace('\n',' ')
                lyrics = lyrics.replace('\"',' ')
                temp.extend([lyrics])
                temp.extend(mood)
                if flag == 1:
                        data.append(temp)
                        abc=str(temp[0])+',\"'+str(temp[1])+'\",'+str(mood)+"\n"
                        f1.write((abc.replace('[','').replace(']','')))
                        print count
                print len(data),count
        except:
                pass
        
f1.close()

