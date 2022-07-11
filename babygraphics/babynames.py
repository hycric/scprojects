"""
File: babynames.py
Name: Richard Huang
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:                   # if name is not in the dictionary name_data
        name_data[name] = {year: rank}          # add input to dictionary
    else:  # name 在 data 裏面
        if year not in name_data[name]:         # if name is in name_data but year is not
            name_data[name][year] = rank        # add input to name
        else:
            if rank < name_data[name][year]:    # if name and year is in name_data but rank is above original
                name_data[name] = {year: rank}  # updates rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.
    會取出檔名為「filename」的文字檔中的所有資料,並加到 name_data 內。

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    lst = []
    lst1 = []
    temp_rank = ''
    with open(filename, 'r') as f:
        for ch in f:
            lst += ch.split(',')
        for c in lst:
            lst1.append(c.strip())
        year = lst1[0]
        for j in lst1:
            count = 0
            if j.isdigit():
                item = int(j)
                count = 1  # 以免 轉換成 int 後 到下個判斷是 .isalpha 會產生error
                if item <= 1000:
                    rank = str(item)  # 換回 type str
                    temp_rank = rank
            if j.isalpha():
                if count == 0:
                    name = j
                    add_data_for_name(name_data, year, temp_rank, name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []
    name_list = list(name_data.keys())        # 讓我們知道 keys有哪些
    target = target.lower()                   # --> Case Insensitive
    for name in name_list:
        name1 = name.lower()
        if name1.find(target) != -1:
            matching_names.append(name)
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
