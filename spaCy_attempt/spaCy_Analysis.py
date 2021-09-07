#code from https://realpython.com/sentiment-analysis-python/

import spacy
import nltk

from load_data import *
from textcat_training import *
from model_test import *

nlp = spacy.load("en_core_web_sm")
file = open('input.txt')
doc = nlp(file.read())          #read the text file into spaCy nlp constructor
file.close()
token_list = [token for token in doc]       #word tokenize the file
#print(token_list)

refined_tokens = [token for token in doc if not token.is_stop]  #filter out stop words (useless to the sentiment analysis) using spaCy default list
#print(refined_tokens)

lemmas = [                                          #Lemmatization. Also built into spaCy. This is done when calling nlp(). This is just iteratting through refined_tokens and showing the lemma list using .lemma_
    f"Token: {token}, Lemma: {token.lemma_}\n"
    for token in refined_tokens]
#print(lemmas)

#print(refined_tokens[1].vector)                    #this is jsut here to check what the text vectorization looks 

if __name__ == "__main__":                          #to call the defined functions
    train, test = load_training_data(limit = 3)
    train_model(train, test)
    print('testing model')
    test_model()