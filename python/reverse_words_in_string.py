############
#brute force

# time complexity : O(n)
# space complexity: O(n)
############

def rever_string_brute(s):
    word = s.split()
    reverse_s = word[::-1]
    return " ".join(reverse_s)




#################
#Optimized
#time complexity O(n)
#space complexity O(1)
###############



def reverse_list(lis, left, right):
    lis[left],lis[right] = lis[right], lis[left]
    left += 1
    right -= 1




def reverse_words_efficient(s):
    # Step 1: Convert string to list of characters
    char_list = list(s)

    # Step 2: Reverse the entire list of characters
    reverse_list(char_list, 0, len(char_list) - 1)

    # we now find the end of a word by increase end from start index till it finds a space to assign it as end index of the word
    start = 0
    while start < len(char_list):
        if char_list[start] != ' ':
            end = start
            while end < len(char_list) and char_list[end] != ' ':
                end += 1
            reverse_list(char_list, start, end - 1)
            start = end
        start += 1

    # Step 4: Join the list into a string and split/join to remove extra spaces
    return ' '.join(''.join(char_list).split())


# Example usage:
s = "a good   example"
print(reverse_words_efficient(s))  # Output: "example good a"

