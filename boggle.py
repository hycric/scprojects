"""
File: boggle.py
Name: Richard Huang
----------------------------------------
This file is contains a game called Boggle. Boggle.py generates all the words available in 4x4 list of Data.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
dl = []

FILE = 'dictionary.txt'


def main():
    c = 0
    main_lst = []                       # List for individual rows of input
    current_list = []                   # Current situation of the word search
    final = []                          # List for words that have been printed out
    while True:
        c += 1
        string = input(str(c) + " row of letters: ")
        if len(string) > 7:
            print("Illegal input")
            break
        if not string_checker(string):
            break
        string_list(string, main_lst)   # Appends the lists into main_lst
        if c == 4:
            break
    read_dictionary(main_lst)
    start = time.time()
    boggle(main_lst, current_list, final)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(main_lst, current_lst, final):
    """
    :param main_lst: # List for individual rows of input
    :param current_lst: lst, A list full of letters ready to be concatenated and check if exist
    :param final: lst, A list of words ready or printed out by function.
    """
    # We have to run nested for loop to make sure all inputs are taken into consideration.
    for x in range(4):                              # 由 Nest for loop 選取進入 Boggle Helper 座標
        for y in range(4):
            path = []
            boggle_helper(main_lst, current_lst, final, x, y, path)


def boggle_helper(main_lst, current_lst, final, x, y, path):
    if len(current_lst) >= 4:                       # 只取 ４ Letter 以上的單字
        word = generate_word(current_lst)
        if word in dl and word not in final:        # 若在字典裡 且 不成被列印
            final.append(word)
            print("Found " + word)

    for i in range(-1, 2):                          # 由起始 (x,y) 向四周開始組字
        for j in range(-1, 2):
            n = x + i                               # (X,Y) 應為固定值，不然會打亂收尋進度
            p = y + j
            if 0 <= n <= 3 and 0 <= p <= 3:         # 確立座標 符合 List(Index)
                if (n, p) not in path:              # 若為 未 append 過之位置
                    # Choose
                    current_lst.append(main_lst[n][p])
                    path.append((n, p))
                    guard = 0
                    if len(current_lst) >= 2:
                        if has_prefix(generate_sub_s(current_lst)):
                            pass
                        else:
                            guard = 1
                    # Early Stopping
                    if guard == 0:
                        # Explore
                        boggle_helper(main_lst, current_lst, final, n, p, path)

                    # Un-choose
                    current_lst.pop()
                    path.pop()


def string_checker(string):
    """
    :param string: str, The input of a row of letters
    :return: Bool, Returns a boolean value to indicate whether there has been an invalid input,
    which breaks the while loop
    """
    for i in range(len(string)):
        if i % 2 == 0 and string[i].isalpha == -1:
            return False
        if i % 2 != 0 and string[i] != " ":
            print("Illegal input")
            return False
        else:
            return True


def string_list(string, main_lst):
    """
    :param string: str, The verified input of a row of letters
    :param main_lst: lst, # List for individual rows of input
    :return:
    """
    a = string.split(' ')
    main_lst.append(a)


def read_dictionary(main_lst):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    main_1 = []
    for l in main_lst:
        main_1 += l
    with open(FILE, 'r') as f:
        for word in f:
            if word[0] in main_1:        # We only choose the words in the row to append in dl to make search faster.
                dl.append(word.strip())  # We need to strip() the word so that it doesn't contain \n


def generate_sub_s(current_lst):
    """
    Generates the prefix from the current_lst
    :param current_lst: lst, a list of letters of the word
    :return: str return a string(Prefix) from the concatenation of letters
    """
    sub_s = ''
    for ch in current_lst:
        sub_s += ch
    return sub_s


def generate_word(current_lst):
    """
    Generates a full word from the letters of the list
    :param current_lst: lst,  a list of letters of the word
    :return: str, returns a string from the concatenation of letters
    """
    word = ''
    for ch in current_lst:
        word += ch
    return word


def has_prefix(sub_s):
    """
    Function checks if the current prefix exists in any word of the dictionary.
    :param sub_s: str, Prefix
    :return: Boolean Value
    """
    for word in dl:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
