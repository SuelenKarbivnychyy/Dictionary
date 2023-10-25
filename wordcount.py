import string



def tokenize(filename):
    """
    Return a list of words from the given string.
    """     

    words_list = []
    with open(filename) as file:
        
        data = file.readlines()
        
        for line in data:
            words = line.rstrip().split(" ")
            words_list.extend(words)
                     
        return words_list 



def normalize(words):
    """
    Normalize the words to be all lower case letter and without any ponctuation
    """

    words_result = []

    for word in words:        
        translator = str.maketrans("", "", string.punctuation)
        word_without_ponct = word.translate(translator)
        words_result.append(word_without_ponct.lower())

    return words_result



def words_count(words_list):
    """
    Take in a list of strings and return a dictionary of each string and the number of times it appears in the list.
    """

    result = {}

    for item in words_list:
        
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1 

    return result               




def print_word_count(dict_of_words):
    """
    Take in a dictionary of word counts and print each key and value from the dictionary.
    """

    for word, count in dict_of_words.items():
        print(word, count)



list_of_words = tokenize("test.txt")
# print(list_of_words)  
normal_words = normalize(list_of_words)
# print(normal_words)
dict_count = words_count(normal_words)
# print(dict_count) 
print_word_count(dict_count)