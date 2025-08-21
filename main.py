import sys

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    file_path = sys.argv[1]
    from stats import get_num_words, count_char, sorted_list, print_value
    def get_book_text(filepath) :
        with open(filepath) as f:
            file_content = f.read()
            stringList = file_content.split()
        return stringList


    my_sorted_list = sorted_list(count_char(get_book_text(file_path)))
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}')
    print('----------- Word Count ----------')
    print(get_num_words(get_book_text(file_path)))
    print('----------- Character Count ----------')
    print_value(my_sorted_list)




