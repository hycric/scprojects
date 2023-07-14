"""
File: anagram.py
Name: Richard Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm
dl = []
# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    This function is designed to find all anagrams for the word input by user.
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        read_dictionary()
        start = time.time()
        bingo = find_anagrams(s)
        num_a = len(bingo)
        end = time.time()
        print(str(num_a)+" anagrams: ", end='')
        print(bingo)
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():   # Reads the file Dictionary into anagram.py
    with open(FILE, 'r') as f:
        for word in f:
            dl.append(word.strip())


def find_anagrams(s):
    """
    This function is the function then creates a list of the input then sends to final_anagrams_helper for further analyis.
    :param s: str, Word input
    :return: lst, returns a list containing all the anagrams of the inputted word
    """
    switch = 0
    wl = list(s)
    final = []
    print('Searching...')
    final_list = find_anagrams_helper(wl, [], len(s), final)
    return final_list


def find_anagrams_helper(wl, current_lst, ans_len, final):  # ans_len = 3
    """
    :param wl: list, list of the word
    :param current_lst: list, the current condition of the list
    :param ans_len: int, the length of the inputted list
    :param final: list, the final condition of the list
    :return: list, return a list of anagrams
    """
    if len(current_lst) == ans_len:
        word = generate_word(current_lst)
        if word not in final and word in dl:
            final.append(word)
            print("Found: "+word)
            print('Searching...')
    else:
        for ch in wl:
            if current_lst.count(ch) == wl.count(ch):
                pass
            else:
                # Choose
                current_lst.append(ch)
                guard = 0
                if len(current_lst) == 3:
                    if has_prefix(generate_sub_s(current_lst)):
                        pass
                    else:
                        guard = 1
                # Early Stopping
                if guard == 0:
                    # Explore
                    find_anagrams_helper(wl, current_lst, ans_len, final)
                # Un-choose
                current_lst.pop()
    return final


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
