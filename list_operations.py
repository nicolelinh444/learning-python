##
#  Implement and demonstrate a collection of list functions below.
#

# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print("The original data for all functions is: ", ONE_TEN)

    # Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swap_first_last(data)
    print("After swapping first and last: ", data)

    # Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shift_right(data)
    print("After shifting right: ", data)

    # Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replace_even(data)
    print("After replacing even elements: ", data)

    # Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replace_neighbors(data)
    print("After replacing with neighbors: ", data)

    # Demonstrate removing the middle element.
    data = list(ONE_TEN)
    remove_middle(data)
    print("After removing the middle element(s): ", data)

    # Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    even_to_front(data)
    print("After moving even elements: ", data)

    # Demonstrate finding the second largest value.
    print("The second largest value is: ", second_largest(ONE_TEN))

    # Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", is_increasing(ONE_TEN))

    # Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", has_adjacent_duplicate(ONE_TEN))

    # Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", has_duplicate(ONE_TEN))

# Function swap_first_last
# Swap the first and last element in a list.
#  @param data the list of values to process
#
def swap_first_last(data):
   swap_data = data[0]
   data[0] = data[-1]
   data[-1] = swap_data

# Function shift_right
# Shift the elements to the right.
#  @param data the list of values to process
#

def shift_right(data):
   last_number = data[-1]
   for i in range(len(data) -1, 0, -1):
      data[i] = data [i - 1]
   data[0] = last_number

# Function replace_even
# Replace all even elements in the list with 0.
#  @param data the list of values to process
#
def replace_even(data):
   for i in range(len(data)):
      if data[i] % 2 == 0:
         data[i] = 0


# Function replace_neighbors
# Replace each value with the larger of its neighbors.
#  @param data the list of values to process
#
def replace_neighbors(data):
   copy = data[:]
   for i in range(1, len(data) -1):
      data[i] = max(copy[i - 1], copy[i + 1])

# Function  remove_middle
# Remove the middle element or elements from a list.
#  @param data the list of values to process
#

def remove_middle(data):
   n = len(data)
   middle = n // 2
   
   if n % 2 == 0:
      data.pop(middle)
      data.pop(middle - 1)
   else:
      data.pop(middle)


# Function even_to_front
# Move even elements to the front of the list.
#  @param data the list of values to process
#

def even_to_front(data):
   evens = []
   odds = []
   
   for value in data:
      if value % 2 == 0:
         evens.append(value)
      else:
         odds.append(value)
         
   data[:] = evens + odds

# Function second_largest
# Identify the second largest value in a list.
#  @param data the list of values to process
#  @return the second largest value in the list
#

def second_largest(data):
   largest = max(data)
   second = None
   
   for value in data:
      if value != largest:
         if second is None or value > second:
            second = value
   return second

# Function is_increasing
# Determine whether or not the list is in increasing order.
#  @param data the list of values to process
#  @return True if the list is in increasing order, False otherwise
#

def is_increasing(data):
   for i in range(len(data) - 1):
      if data[i] > data[i + 1]:
         return False
   return True

# Function has_adjacent_duplicate
# Determine if the list contains adjacent duplicate elements.
#  @param data the list of values to process
#  @return True if the list contains adjacent duplicates, False otherwise
#

def has_adjacent_duplicate(data):
   for i in range(len(data) - 1):
      if data[i] == data[i + 1]:
         return True
   return False

# Function has_duplicate
# Determine if the lost contains duplicate elements.
#  @param data the list of values to process
#  @return True if the list contains duplicates, False otherwise
#

def has_duplicate(data):
   for i in range(len(data)):
      for j in range(i + 1, len(data)):
         if data[i] == data[j]:
            return True
   return False

# Call function
main()