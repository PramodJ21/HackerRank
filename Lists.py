'''
Consider a list (list = []). You can perform the following commands:
1.insert i e: Insert integer i at position e.
2.print: Print the list.
3.remove e: Delete the first occurrence of integer e.
4.append e: Insert integer e at the end of the list.
5.sort: Sort the list.
6.pop: Pop the last element from the list.
7.reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of
the 7 types listed above. Iterate through each command in order and perform the corresponding operation on 
your list.
'''

N = int(input())
lst = []
data = []

for i in range(N):
    data.append(input())

for each in data:
    if 'insert' in each:
        insrt = each.split(' ')
        lst.insert(int(insrt[1]),int(insrt[2]))

    if 'remove' in each:
        rmv = each.split(' ')
        lst.remove(int(rmv[1]))

    if 'append' in each:
        apnd = each.split(' ')
        lst.append(int(apnd[1]))

    if 'sort' in each:
        lst.sort()

    if 'pop' in each:
        lst.pop()

    if 'reverse' in each:
        lst.reverse()

    if 'print' in each:
        print(lst)
