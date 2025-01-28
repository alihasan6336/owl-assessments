def intersection_of_lists(list1, list2):

    set1 = set(list1)

    set2 = set(list2)

   

    intersected_set = set1 & set2

   

    intersected_list = sorted(list(intersected_set))


   

    return intersected_list


list1 = [1, 2, 3, 4, 5]

list2 = [3, 4, 5, 6, 7]

result = intersection_of_lists(list1, list2)

print(result)