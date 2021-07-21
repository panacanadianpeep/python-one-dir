# EXAMPLE 1
## How to loop over characters in a string.
a = "this is a string..."
for i in a:
  print(i)


## OUTPUT:
# t
# h


# i


# s



# i
# s

# a

# s
# t
# r
# i
# n
# g
# .
# .
# .


# EXAMPLE 2
# Saving data to a list
b = []
a = input("Please enter your name: ")
b.append(a)
print(b)

## OUTPUT:
# Please enter your name: Justin
# ['Justin']

print(b[0][0])

## OUTPUT:
# 'P'


# EXAMPLE 3

# for h in range(math.floor(len(dataToBeCompressed)/2)):
5 / 2
c = len(dataToBeCompressed)
b = c / 2
a = math.floor(b) + 1
range(a)

# EXAMPLE 4
a = ['1', 'a', 'b', '20a'] # one dimensional list/array

b = [                      # two dimensional list/array
  [1, 2, 3, 4],
  [2, 4, 6, 8]
]

# EXAMPLE 5
name = "Justin"
for h in range(len(name)):
  if (h+1) % 3 == 0:
    # 0, 1, 2, 3, 4, 5
    # 1, 2, 3, 4, 5, 6
    print(name[h])

# EXAMPLE 6
a = '456'

# EXAMPLE 7 - file access
filename = "some_file.txt"
with open(filename, "r") as open_file:
  # inside this code block the file is open
  text = open_file.readlines()
# the file has been closed.


some_string = "abcdefghijklmnop"
print(some_string[2])  # prints 'c'
print(some_string[-1])  # prints p
