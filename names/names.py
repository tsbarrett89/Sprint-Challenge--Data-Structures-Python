import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class BSTNode:
    def __init__ (self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if target == self.value:
            duplicates.append(target)
        if target > self.value:
            if self.right is None:
                return False
            else:
                self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:
                self.left.contains(target)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

names_BST = BSTNode(names_1[0])
for each in names_1:
    names_BST.insert(each)

for each in names_2:
    names_BST.contains(each)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
