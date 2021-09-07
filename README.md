# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!


##My Solution Attempt
I started this challenge with very little experience coding in Python and only a basic understanding of machine learning and how it functions. I took more of a tutorial route for this, but my first attempt did not end up being machine learning per say. I was looking for ways to handle sentiment analysis through Python and came across information on using the Afinn library.
Upon spending a little while reading through and learning about how to use the Afinn library, I understood how it was working, but it felt very low-level. In the file labeled "Affin_attempt", my first attempt utilizes the tools already created in the Afinn library to score each line of text, word-by-word, and then average each line's positive, negative, and neutral scores.
These scores will later be displayed on a graph (which is honestly the only thing that felt spectacular here). The overall averages of the scores would be printed out before the graph, but the data was suggesting extremely neutral standings. I felt that this was incorrect and began searching for more thurough methods of sentiment analysis.
I came across a better guide that used the spaCy library. This attempt ultimately failed because the guide seems to have outdated methods no longer supported in the current spaCy library (as I discovered searching for the issue here: https://stackoverflow.com/questions/66790649/textcat-architecture-extra-fields-not-permitted). 
However, I did learn much more about the preprocessing of data needed to preapre for proper machine learning (and sentiment analysis). You can see me messing around with the tokenization and lemmatization of the "input.txt" file in the "spaCy_attempt" folder, under "spaCy_analysis.py". After this, I began to read the guide to creating my own NLP Sentiment Analyzer. All of the code is essentially from the guide (with minor tweaks to change file names and paths as necessary) which I was inputting as I followed along and read to get an understanding of what was happening.
I understood that there needed to be training data to use to train the machine, then validated before final testing.
I went ahead and founnd the source of the "input.txt" file and copied multiple other paragraphs from those sources that I wanted to preprocess and use as training data. I created text files named "training1.txt" and "training2.txt" that I had intended to load in as training and validation data. "input.txt" would be the final test, of course.
Unfortunately, with my inexperience using Python and difficulties trying to figure out how to update the spaCy code to work in the current version of spaCy, I was unable to complete making a true machine learning sentiment analysis, but I understand the necessary process. There was some confusion about how to set up directories to send different data set to and pull from, which is in the "load_data.py" file in the "spaCy_attempt" folder.
I think that with a bit more experience, and a bit more time to scour the spaCy documentation to manually update the code to get it to run, I could potentially get the whole thing to actually take the training data I collected, tokenize and lemmatize it, then split it 80/20 for training and validation respectively. Then hopefully I'd be left with a properly trained model to test the "input.txt" file.

##Resources used
**For the Afinn attempt:
https://towardsdatascience.com/sentiment-analysis-of-a-book-through-unsupervised-learning-df876563dd1b
**For the spaCy attempt:
https://realpython.com/sentiment-analysis-python/
**Trying (and failing) to remedy outdated spaCy code:
https://stackoverflow.com/questions/66790649/textcat-architecture-extra-fields-not-permitted
