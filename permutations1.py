# This Python implementation is inspired by the algorithm presented in the book Computer Algorithms by Horowitz, Sahni and Rajasekeran.

def perm(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i] ,a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

a = [1,2,3]
perm(a)



# find there http://www.cyberforum.ru/python/thread1867525.html

def combinations(elements, size):
    if len(elements) == size or size == 1:
        return elements

    ret = []
    for i, item in enumerate(elements):
        for j in combinations(elements[i + 1:], size - 1):
            ret.append(item + j)
    return ret


def variations(elements, size):
    ret = []
    for i in combinations(elements, size):
        ret.extend(permutations(i))
    return ret


def permutations(elements):
    if len(elements) <= 1:
        return elements

    ret = []
    for i, item in enumerate(elements):
        for j in permutations(elements[:i] + elements[i + 1:]):
            ret.append(item + j)
    return ret


def main():
    print("----------------")
    input = ["a", "b", "c", "d", "f"]
    print("Input {}:".format(input))
    print("Combinations:")
    print(combinations(input, 3))
    print("Permutations:")
    print(permutations(input))
    print("Variations:")
    print(variations(input, 3))
main()
