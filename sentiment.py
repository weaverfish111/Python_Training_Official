## Sentiment.py
## Richard Weaver
## 08/03/2022

## Functions to import positive and negative words lists.
def load_words(filename):
    content = open(filename)
    lines = content.read().splitlines()
    content.close()
    return lines

def load_positive_words():
    return load_words("pos_words.txt")

def load_negative_words():
    return load_words("neg_words.txt")


## This function works out negative or positive score for each individual word.
def sentiment_of_word(word):
    score = 0
    if word in pos_words:
        score += 1
    elif word in neg_words:
        score -= 1
    else:
        score = score
    return(score)
## This is a personal test for individual words:
# print(sentiment_of_word("breeze"))


## This is the function for calculating sentiment of whole text.
def sentiment_of_text(text):
    total_text_score = 0
    word = text.split()
## A for loops which goes through the text, calculating sentiment of each word and then adding total_score together.
    for sentiment in word:
        sentiment = sentiment.strip("!.,!?;:()[]")
        score = sentiment_of_word(sentiment)
        total_text_score += score
    return(total_text_score)
## This is a personal test for text:
# print(sentiment_of_text("summer breeze, makes me feel agile, bless, breeze, bright"))

## The Positive and Negative Words Lists.
pos_words = load_positive_words()
neg_words = load_negative_words()

## Final test for functions
total_score = sentiment_of_text("Hey Camiel, It is very Sunny today, I like the breeze")
if total_score > 0:
    print("The text is mostly nice!")
elif total_score < 0:
    print("The text talks about mad or bad stuff :(")
else:
    print("The text is not opinionated or just messy.")
