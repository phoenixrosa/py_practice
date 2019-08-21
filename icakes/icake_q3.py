"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""


def highest_product(list_of_ints):
    # brute method
    # 1) O(n^3) = evaluate all possible products and keep highest
    # 2) use highest integers --> but what about negative integers?
    # 3) keep track of highest product of 2 & smallest product of 2 (most positive / most negative)

    # + edge case checking
    if len(list_of_ints) < 2:
        raise IndexError("list must have more than 3 integers")

    # what do we need to keep track?
    highest_product_2 = max(list_of_ints[0] * list_of_ints[1], list_of_ints[1] * list_of_ints[2])
    smallest_product_2 = min(list_of_ints[0] * list_of_ints[1], list_of_ints[1] * list_of_ints[2])
    highest_product_1 = max(list_of_ints[0], list_of_ints[1], list_of_ints[2])
    smallest_product_1 = min(list_of_ints[0], list_of_ints[1], list_of_ints[2])
    max_product = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for sample in list_of_ints[3:]:
        max_product = max(max_product, highest_product_2 * sample, smallest_product_2 * sample)
        # print max_product

        highest_product_2 = max(highest_product_2, highest_product_1 * sample, smallest_product_1 * sample)
        highest_product_1 = max(highest_product_1, sample)
        # print "hp2: " + str(highest_product_2)
        # print "hp1: " + str(highest_product_1)

        smallest_product_2 = min(smallest_product_2, smallest_product_1 * sample, highest_product_1 * sample)
        smallest_product_1 = min(smallest_product_1, sample)
        # print "sp2: " + str(smallest_product_2)
        # print "sp1: " + str(smallest_product_1)
    # print "-----"

    return max_product


def highest_product_of_k_items(k, list_of_ints):
    # extended problem from above
    # edge case check
    if len(list_of_ints) < k:
        raise IndexError("list must have more than %i integers", k)

    # keep list of products, index is # - 1 - 1
    last_k_index = k - 2
    highest_products = []
    smallest_products = []
    max_product = 1

    # initialize
    # incorrect ???
    for i in list_of_ints[:k-1]:
        print "i: " + str(i)
        max_product *= i
        highest_products.append(max_product)
        smallest_products.append(max_product)
        highest_products[0] = max(highest_products[0], i)
        smallest_products[0] = min(smallest_products[0], i)
    max_product *= list_of_ints[k-1]
    print highest_products
    print smallest_products
    print max_product
    print " ==== "

    # k is 1 item
    if k == 1:
        for sample in list_of_ints[k:]:
            max_product = max(max_product, sample)

    # k is 2 or more items
    if k > 1:
        for sample in list_of_ints[k-1:]:
            print "comparing " + str(sample)
            max_product = max(max_product, highest_products[last_k_index] * sample, smallest_products[last_k_index] * sample)

            # update list of products
            for j in xrange(last_k_index, 0, -1):
                highest_products[j] = max(highest_products[j], highest_products[j-1] * sample, smallest_products[j-1] * sample)
                smallest_products[j] = min(smallest_products[j], smallest_products[j-1] * sample, highest_products[j-1] * sample)
                print "j: " + str(j)
                print highest_products
                print smallest_products
            highest_products[0] = max(highest_products[0], sample)
            smallest_products[0] = min(smallest_products[0], sample)

    return max_product



sample_set1 = [1, 5, 6, 8, 2, 3]        # 240
sample_set2 = [1, 5, 6, -8, 2, 3]       # 90
sample_set3 = [1, -5, -6, 8, 2, 3]      # 240
sample_set4 = [1, -5, -6, -8, 2, -3]    # 96
sample_set5 = [-1, -5, -6, -8, -2, -3]  # -6
sample_set6 = [0]
sample_set7 = [0, 0, 0, 0, 0, 0]
sample_set8 = [-1, 0, 1, 0, 1, 0]        # 0


"""
print highest_product(sample_set1)
print highest_product(sample_set2)
print highest_product(sample_set3)
print highest_product(sample_set4)
print highest_product(sample_set5)
#print highest_product(sample_set6)
print highest_product(sample_set7)
print highest_product(sample_set8)
"""


print highest_product_of_k_items(3, sample_set4)

