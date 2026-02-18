"""| Method    | Work               |
| --------- | ------------------ |
| append()  | Add item at end    |
| extend()  | Add multiple items |
| insert()  | Add at index       |
| remove()  | Remove by value    |
| pop()     | Remove by index    |
| clear()   | Remove all         |
| index()   | Find position      |
| count()   | Count element      |
| sort()    | Sort ascending     |
| reverse() | Reverse order      |
| copy()    | Duplicate list     |"""


nums = [10, 20, 30, 40]

#append() → Add item at the end
nums.append(50)
print(nums) #[10, 20, 30, 40, 50]

#extend() → Add multiple items at the end
nums.extend([60, 70])
print(nums) #[10, 20, 30, 40,50,60, 70]


#insert() → Add item at specific index
nums.insert(1, 15)
print(nums) #[10, 15, 20, 30, 40,50,60,70]

#remove() → Remove first matching value
nums.remove(20)
print(nums) #[10,15, 30, 40,50,60,70]

#pop() → Remove by index (default last)
nums.pop()
print(nums) #[10,15,30,40,50,60]


#clear() → Remove all items
nums.clear()
print(nums) #[]

nums = [10,20,30,40]

#index() → Find position of an element
print(nums.index(30)) #2

#count() → Count occurrences
nums = [1, 2, 2, 3]
print(nums.count(2)) # 2

#sort() → Sort list ascending
nums = [5, 2, 9, 1]
nums.sort()
print(nums) #[1, 2, 5, 9]

#sort(reverse=True) → Sort descending
nums.sort(reverse=True)
print(nums) #[9, 5, 2, 1]

#reverse() → Reverse list order
nums.reverse()
print(nums) #[40, 30, 20, 10]

#copy() → Make a duplicate list
new_list = nums.copy()
print(new_list)
