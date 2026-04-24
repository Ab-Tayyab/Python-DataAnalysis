# Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its corresponding length.
# Example Output: ({"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5})

given_list = ["apple","banana","kiwi","cherry","mango"]
createDictionary = {}
for i in given_list:
    createDictionary[i] = len(i)

# output 
for key,value in createDictionary.items():
    print(key," : ",value)
