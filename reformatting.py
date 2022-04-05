##Richard Weaver
##01/03/2022

# Function to reformat a string based on specified character length.
def text_to_lines (text, max_length):
    total_count= 0
    output_text = ""
    space = " "
    word_list = text.split()

    # For Loop iterating over each word in list
    for word in word_list:
        # print(word)
        word_length = len(word)
        if total_count + word_length +1 <= max_length: 
            output_text += word 
            output_text += space
            total_count += word_length +1     # +1 for the spaces after words?
        else:
            output_text = output_text.strip(" ")
            output_text += "\n"
            output_text += word
            output_text += space
            total_count = 0
            spaces_count = 0
            total_count += len(word)
    # Outputting new text and stripping final space from last line.        
    output_text = output_text.strip(" ")
    return(output_text)


# Test Cases
test_text1 = "Row, row, row your boat A Gently down the stream BC. Row, row, row your boat. Gently down the stream."
separate_lines = text_to_lines(test_text1, 25)
