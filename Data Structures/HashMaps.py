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



