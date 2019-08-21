"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.
"""


def get_products_of_all_ints_except_at_index(list_of_ints):
    # brute method
    list_of_products = [1] * len(list_of_ints)
    #print list_of_products
    for i in xrange(0, len(list_of_ints)):
        for j in xrange(0, len(list_of_ints)):
            if i != j:
                list_of_products[i] *= list_of_ints[j]
                #print list_of_products
    return list_of_products


def get_products_of_all_ints_except_at_index_optimized(list_of_ints):
    #  runs in O(n) time & O(n) space
    # + edge case / error checking
    if len(list_of_ints) < 2:
        raise IndexError("list must have at least 2 integers")

    list_of_products = [1] * len(list_of_ints)
    #list_of_products2 = [1] * len(list_of_ints)
    stored_before = 1
    stored_after = 1
    for i in xrange(0, len(list_of_ints)):
        list_of_products[i] *= stored_before
        stored_before = stored_before * list_of_ints[i]
        #print stored_before
        #print list_of_products

        list_of_products[len(list_of_ints)-1-i] *= stored_after
        stored_after = stored_after * list_of_ints[-1-i]
        #print stored_after
        #print list_of_products2

    return list_of_products


sample_set1 = [1, 7, 3, 4]
sample_set2 = [1, 2, 6, 5, 9]
sample_set3 = [0, 0, 0, 0, 0]
sample_set4 = [0]
sample_set5 = [1, 2]


#print get_products_of_all_ints_except_at_index(sample_set3)
print get_products_of_all_ints_except_at_index_optimized(sample_set2)



