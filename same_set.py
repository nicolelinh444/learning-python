#  Write the definition of the function same_set to determine if two lists contain the same values in any order, ignoring duplicates.
#

# Define constants.
LIST_1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
LIST_2 = [11, 11, 7, 9, 16, 4, 1]


def main():
    print("List 1 is", LIST_1)
    print("List 2 is", LIST_2)
    print("The lists contain the same elements: ", same_set(LIST_1, LIST_2))

# Function same_set
# Determine if two lists contain the same elements in any order, ignoring
#  duplicates.
#  @param l1 the first list to consider
#  @param l2 the second list to consider
#  @return True if the lists contain the same elements, False otherwise
#

def same_set(LIST_1, LIST_2):
   unique_list_1 = []
   unique_list_2 = []
   
   for x in LIST_1:
      if x not in unique_list_1:
         unique_list_1.append(x)
         
   for x in LIST_2:
      if x not in unique_list_2:
         unique_list_2.append(x)
      
   if len(unique_list_1) != len(unique_list_2):
      return False
   
   for x in unique_list_1:
      if x not in unique_list_2:
         return False
         
   return True 

# Call the main function.
main()