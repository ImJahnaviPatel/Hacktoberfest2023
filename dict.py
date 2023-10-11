#Count Word Frequency
'''Define a function to count the frequency of words in a given list of words.'''
#Example:
'''
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words)''' 

#Output:

''' {'apple': 3, 'orange': 2, 'banana': 1}'''

#METHOD 1 ---->>>>>

def count_word_frequency(words):
    # TODO
    mydict={}
    for i in words:
        if(i not in mydict):
            mydict[i]=1
        else:
            mydict[i]+=1
    return mydict

#METHOD 2 ---->>>>>

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

#Explanation:

'''Define a function count_word_frequency(words) that takes a list of words as its input.

Initialize an empty dictionary word_count to store the frequency of each word in the list.

Iterate through the list of words using a for loop.

For each word, use the get() method to retrieve the current count of the word in the word_count dictionary.
If the word is not yet present in the dictionary, get() returns the default value (0).
Then, increment the count by 1 and update the dictionary.

After iterating through all the words, return the word_count dictionary containing the word frequencies.'''

#Time complexity:

'''The time complexity of this exercise is O(n), where n is the number of words in the input list.
The loop iterates through each word in the list once, and the dictionary operations (get and update)
take constant time, O(1), on average.'''

#Space complexity:

'''The space complexity of this exercise is also O(n), where n is the number of unique words in the input list.
In the worst case, all words are unique, and the word_count dictionary will have n entries.'''



################################################################################################################
#################################################################################################################

#Common Keys
'''Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.'''

#Example:

'''dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)'''

#Output:

'''{'a': 1, 'b': 5, 'c': 7, 'd': 5}'''

#METHOD 1 ----->>>>

def merge_dicts(dict1, dict2):
    for i in dict2:
        if(i not in dict1):
            dict1[i]=dict2[i]
        else:
            dict1[i]+=dict2[i]
    return dict1

#METHOD 2 ----->>>>

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


#This code snippet defines a function merge_dicts(dict1, dict2) that merges two dictionaries
# and sums the values of common keys.

'''Explanation:'''

'''Create a copy of dict1 named result. This ensures that the original dict1 is not modified during the process.
The copy() method takes O(n) time complexity, where n is the number of elements in dict1.
The space complexity is also O(n) as a new dictionary is created with the same number of elements as dict1.

Iterate through the key-value pairs of dict2 using a for loop. This loop runs for m iterations,
where m is the number of elements in dict2. For each key-value pair:
(a). Use the get() method to retrieve the current value associated with the key in the result dictionary.
If the key is not present in result, get() returns the default value (0).
(b). Add the value from dict2 to the current value (or 0, if the key is not in result) and
update the result dictionary with the new value for the key.
The get() and update operations take O(1) average time complexity.

Return the merged dictionary result.'''

#Time complexity:

'''The overall time complexity of this function is O(n + m), where n is the number of elements in dict1
and m is the number of elements in dict2.
The copy() method takes O(n) time, and the loop iterates m times with O(1) operations inside the loop.'''

#Space complexity:

'''The space complexity of this function is O(n + m) in the worst case,
where all keys in dict1 and dict2 are distinct, and the merged dictionary has n + m elements.
In the best case, where dict1 and dict2 have the same keys, the space complexity is O(n) (or O(m),
whichever is larger), as the merged dictionary has the same number of elements as the input dictionaries.'''


#####################################################################################################
#####################################################################################################

#Key with the Highest Value
'''Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.'''

#Example:

'''my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))'''

#Output:
'''b'''

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

#Explanation:

'''Call the built-in max() function with the dictionary my_dict as its first argument
and key=my_dict.get as its second argument.

The max() function iterates through the keys in the dictionary and compares the values associated with each key
using the get() method. The key parameter specifies a custom function to extract a comparison key
from each dictionary key. In this case, the get() method returns the value associated with each key,
so the max() function compares the values of the dictionary.

The time complexity of the max() function is O(n), where n is the number of elements in the dictionary my_dict.
The max() function iterates through all the keys in the dictionary once,
and the get() method has an average time complexity of O(1).

Return the key with the highest value found by the max() function.'''

#Time complexity:

'''The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict.
This is determined by the max() function, which iterates through all the keys in the dictionary.'''

#Space complexity:

'''The space complexity of this function is O(1), as it does not create any additional data structures or store
any intermediate values. The max() function only keeps track of the current maximum value and its corresponding key,
which requires constant space.'''

