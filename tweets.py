import matplotlib.pyplot as plt

## Function loading in positive and negative words lists
def load_words(filename):
    content = open(filename)
    lines = content.read().splitlines()
    content.close()
    return lines
def load_positive_words():
    return load_words("pos_words.txt")
def load_negative_words():
    return load_words("neg_words.txt")

## The Positive and Negative Words Lists.
pos_words = load_positive_words()
neg_words = load_negative_words()

## Function working out negative or positive score for each individual word.
def sentiment_of_word(word):
    score = 0
    if word in pos_words:
        score += 1
    elif word in neg_words:
        score -= 1
    else:
        score = score
    return(score)

## Function for calculating sentiment of whole text.
def sentiment_of_text(text):
    total_text_score = 0
    word = text.split()
## For loop that goes through the text, calculates sentiment score of each word and then adds total_score together.
    for sentiment in word:
        sentiment = sentiment.strip("!.,!?;:()[]")
        score = sentiment_of_word(sentiment)
        total_text_score += score
    return(total_text_score)

## Driver Code - evaluating sentiment of Trump tweets
with open("trump.txt", encoding="utf8") as tweet_file:
     tweets = tweet_file.read().splitlines()
positive = 0
negative = 0
neutral = 0
for tweet in tweets:
    # print(tweet) #test print
    sentiment = sentiment_of_text(tweet)
    if sentiment > 0:
        positive += 1
    elif sentiment < 0:
        negative += 1
    else:
        neutral += 1
print(f"positive is {positive}")
print(f"negative is {negative}")
print(f"neutral is {neutral}")
    

my_data = [positive,negative,neutral]
my_labels = 'Positive','Negative','Neutral'
plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
plt.title("Trump's Tweets")
plt.axis('equal')
plt.show()


# import matplotlib.pyplot as plt

# labels = ['Positive', 'Negative', 'Neutral']
# sizes = [425, 236, 336]
# # Plot
# plt.pie(sizes, labels=labels, 
#         autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal')
# plt.show()

# if sentiment == 1:
#     positive += 1


"""
Your tweets variable will then contain a list of strings, each string being the text of a single tweet.

Calculate the sentiment of each tweet, keeping track of the number of positive, as well as the negative and neutral tweets. Which loop strategy can you use to do this?

Take the calculated numbers and use these to make a nice pie chart: matplotlib.pyplot.pie — Matplotlib 3.1.0 documentation. The chart should have three parts: positive, negative and neutral. 
Also make sure the chart has descriptive labels and appropriate colors! Have a look at the Matplotlib docs.
"""

# for sentiments in tweets [5]:
#     print(sentiments)
#     # sentiment_of_word()

# print(type(tweets))
# print(tweets [18])