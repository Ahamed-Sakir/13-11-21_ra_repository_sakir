def frequency(str): 
    words_str = str.split()         
    str_list = []
    words_dict = {}  
    for i in words_str:             
        if i not in str_list:
            str_list.append(i)               
    for i in range(0, len(str_list)):
        words_dict[str_list[i]] = str.count(str_list[i])    
    words_dict_sorted = sorted(words_dict.items(), key=lambda t: t[1])
    print("\nAscending order")
    for i in range(0, len(words_dict_sorted)):
        print(words_dict_sorted[i][0], ":", words_dict_sorted[i][1])
        
        
def redundant(words):
    punc = '''!'"\,<>./?@#()-[]{};:$%^&*_~'''
    for ele in words:
        if ele in punc:
            clean_words = words.replace(ele, "")
    return clean_words

with open('pg3807.txt', 'r') as file:
    words = file.read().replace('\n', '')
    clean_words = redundant(words)
    print('Formatted input\n',clean_words)
    frequency(clean_words)