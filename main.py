# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(file_name):
    """
    Reads the content of a file
    :param file_name: string
    :return: string
    """
    # Open the file
    file = open(file_name, "r")
    # Read the content of the file
    content = file.read()
    # Close the file
    file.close()
    # Return the content
    return content


def count_words():
    """
    Counts the occurence of words in a text
    :param text: string
    :return: dictionary
    """
    # Split the text into words
    text = read_file_content("./story.txt")
    words = text.split()
    # Create an empty dictionary
    word_count = {}
    # Loop through the words
    for word in words:
        # If the word is already in the dictionary, increment the count
        if word in word_count:
            word_count[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_count[word] = 1
    # Return the dictionary
    return word_count


print(count_words())
