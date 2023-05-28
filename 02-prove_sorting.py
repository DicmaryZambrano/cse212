"""
CSE212 
(c) BYU-Idaho
02-Prove - Problem 1.1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def sort_list(data):
    count = 0
    for sort_pos in range(len(data)-1, 0, -1):
        for swap_pos in range(0, sort_pos):
            if data[swap_pos] > data[swap_pos+1]:
                data[swap_pos], data[swap_pos+1] = data[swap_pos+1], data[swap_pos]
                count += 1
    print(count)
        
numbers = [9,8,7,6,5]
sort_list(numbers)
print(numbers)  #[1, 2, 3, 4, 6, 8, 9]