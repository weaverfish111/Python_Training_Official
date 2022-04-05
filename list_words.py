# Richard Weaver
# 22/03/2022
# list_words.py

# Test String
original = "The apple doesn't fall far from the tree."

# Function to clean up string (Removes Caps + Punctuation)
def cleanup(string):
    lowercase = string.lower()
    punct = lowercase.strip("!.,!?;:()[]")
    clean_text = punct
    return(clean_text)

# Function which calls on cleanup function, then creates a sorted list of words from original string.
def text_to_unique_words(string):
    unique_words = []
    cleanwords_list = string.split()
    
    # For Loop iterating over words in cleanwords_list.
    for word in cleanwords_list:
        word = cleanup(word)
        if word not in unique_words:
            unique_words.append(word)
    sorted_unique_words = sorted(unique_words)
    print(*sorted_unique_words, sep="\n")
    return(sorted_unique_words)

# Driver Code
text_to_unique_words(original)


