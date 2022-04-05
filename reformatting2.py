def text_to_lines (text, max_length):
    max_length = 10
    total_count=0
    for word_list in text:
        for char_count in text:
            print(char_count)
            char_count = len(text)
            # total_count += char_count
            # print(total_count)
        if total_count > max_length:
            word_list += "\n"
            print(word_list)
        break
    return(text)
# word_list = text.split()
        # print(word_list)
source_text = "I appreciate the help Iris (25)"
# source_text = "ASDF is the sequence of letters that appear on the first four keys on the home row of a QWERTY or QWERTZ keyboard. They are often used as a sample or test case or as random, meaningless nonsense. It is also a common learning tool for keyboard classes, since all four keys are located on Home row." # from the wikipedia
# print(source_text)
# print()
print(text_to_lines(source_text, 20))