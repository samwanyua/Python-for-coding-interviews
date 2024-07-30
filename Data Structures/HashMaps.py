from collections import defaultdict

# Hashmaps/ Dictionaries - store key-value pairs
"""
- Each element in a hashmap consists of a key and a value.
- Keys must be unique and immutable (like strings, numbers, or tuples),
while values can be of any data type.

- A hash function is applied to the key to generate a hashcode which is a numerical value
- Hash code determines the index or "bucket" where key-value pair will be stored in the hashmap
- Collision handling (keys generating same hashcode) hashmaps employ below techniques:
    * chaining - storing multiple key-value pairs in the same bucket as a linked list
    * open addressing - finding an alternative buckets to handle collisions
- Keys are immutable data types
"""
city_map = {}  # alternatively city_map = dict()
cities = ["Calgary", "Vancouver", "Toronto"]
city_map["Canada"] = []
city_map["Canada"] += cities
print(city_map)
print(city_map.items())
# DefaultDict - all keys are already initialized
# from collections import defaultdict
towns_map = defaultdict(list)
towns = ["Nairobi", "Mombasa", "Nakuru"]
towns_map["Kenya"] += towns
print(towns_map.items())
print(towns_map.keys())
print(towns_map.values())

"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""





