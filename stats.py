
def get_num_words(string_in_book) :
    return f"Found {len(string_in_book)} total words"


def count_char(word_list):
    
    charDict = {}
    for word in word_list:
        for char in word:
            lowerchar = char.lower()
            if lowerchar in charDict:
                charDict[lowerchar] += 1;
            else:
                charDict[lowerchar] = 1
    
    return charDict

def sorted_list(my_dict):
    char_value_list = []
    for char_value in my_dict:
        char_dict = {}
        char_dict['char'] = char_value
        char_dict['num'] = my_dict[char_value]
        char_value_list.append(char_dict)
    def sort_on(items):
        return items['num']
    char_value_list.sort(reverse=True, key=sort_on)
    return char_value_list

def print_value(any_list):
    for list_item in any_list:
        print(f"{list_item['char']}: {list_item['num']}")