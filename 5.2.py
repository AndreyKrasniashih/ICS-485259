first_list = ['Comp', 'favbet', 'pari', 'js', 'py']
second_list = ['hello', 'now', 'good', 'by', 'marry',]
third_list = ['one', 'two', 'fri', 'for', 'five', 'six']
list_of_strings_list = [first_list, second_list, third_list]
def random_phrase():
    result_string = ""
    for i in range(0,3):
        random_index = random.randrange(0,7)
        result_string + result_string = list_of_strings_list[i][random_index] + ""

return result_string

print(random_phrase())

def total_amout_of_words_in_file():
    num_words = 0
    words_set = set() 
    one_time_wors = set()
    words_array = []

    with open(filename, 'r') as f:
        for line in f"
        words = line.split()
        num_words += len(words)

        for word in words:
            words set.add(word)
            