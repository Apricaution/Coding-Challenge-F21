
'''
adapted from https://towardsdatascience.com/sentiment-analysis-of-a-book-through-unsupervised-learning-df876563dd1b
using the Afinn library for sentiment analysis    
'''
import matplotlib.pyplot as plt     #for use plotting collected data
import numpy as np
from numpy import mean
from afinn import Afinn             #Afinn library created by Finn Årup Nielsen. Simple and popular lexicon for senitment analysis. 3300+ scored words.

afinn = Afinn(language = 'en')
pos_index = []
neg_index = []
neutral_index = []

file = open('input.txt')
lines = file.readlines()


for line in lines:      #iterate through each line of the text
    pos = 0     #to tally positive scored lines
    neg = 0     #to tally negative scored lines
    neut = 0    #to tally neutral scored lines
    
    for word in line.split():       #iterate through each word of a line
        score_word  = int(afinn.score(word))        #score the current word
        
        if score_word > 0:          #if the word is positively scored, add a tally to the pos; if negativelty scored, add a tally to neg; etc
            pos += 1
        elif score_word < 0:
            neg += 1
        else:
            neut += 1

    n = len(line.split())           #get the length of the line in terms of words.
    
    if n != 0:                      #takes the average score of each line's positive, negative, and neutral tallies. Places the data in a range from 0 to 1.
        pos_index.append(pos/n)     #ex: if the positive score for a line is 1, the line is completely positive. If the neutral score for a line is 0, there is no neutrality.
        neg_index.append(neg/n)
        neutral_index.append(neut/n)
    elif n==0:                      #if statemtents to ensure we are not dividing by zero for a blank line. If line is blank, insert zero for each sentiment score for the line.
        pos_index.append(0)         
        neg_index.append(0)
        neutral_index.append(0)

m = np.mean(pos_index)              #gather the overall average scores for the document
n = np.mean(neg_index)
o = np.mean(neutral_index)
print("Overall Positive mean: " + str(m) + "\n" +
      "Overall Negative mean: " + str(n) + "\n" +
      "Overall Neutral mean: " + str(o))


x = np.arange(1,len(lines)+1)               #creation of a line graph to show the scores of the document by line 
plt.plot(x, pos_index, '-.', label='pos')
plt.plot(x, neg_index, '--', label='neg')
plt.plot(x, neutral_index, '-', label='neut')
plt.legend()
plt.xticks(x)
plt.xlabel('Line')
plt.ylabel('score')
plt.grid()
plt.savefig('plots.png')
plt.show()

