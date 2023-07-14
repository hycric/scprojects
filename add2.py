"""
File: add2.py
Name: Richard Huang
------------------------
Function Reverses the values of a ListNode and add up the values of each Listnode accordingly.
Then converts the value type to ListNode.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # l1
    a = ""
    while l1.next is not None:    # Run a while loop to retrieve all values in l1.
        a += str(l1.val)
        l1 = l1.next
    a = a + str(l1.val)
    a_1 = list(a)                 # Make sure the separate digits are sorted in a list.
    a_f = ''
    for num in reversed(a_1):     # With reversed for loop we concat the values into a str, which we then convert to int
        a_f += num
    a_f = int(a_f)
    print(a_f)
    # l2
    b = ""
    while l2.next is not None:
        b += str(l2.val)
        l2 = l2.next
    b = b + str(l2.val)
    b_1 = list(b)
    b_f = ''
    for num in reversed(b_1):
        b_f += num
    b_f = int(b_f)
    total = a_f + b_f
    total = str(total)
    # l3                        # Convert the value into a ListNode.
    l3 = ListNode(int(total[0]), None)
    for i in range(1, len(total)):
        new_node = ListNode(int(total[i]), None)
        new_node.next = l3
        l3 = new_node
    return l3


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
