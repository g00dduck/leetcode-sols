"""Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""
import itertools

class Solution:
    def find_perms_itertools(self, nums):
        permutations = []

        for perm_set in itertools.permutations(nums):
            perm_array = []
            for item in perm_set:
                perm_array.append(item)
            permutations.append(perm_array)

        return permutations


def main():
    while True:
        try:
            print("\nEnter a set of comma separated numbers.\n" + 
                "I'll give you all of the possible permutations from that set. " +
                "\nEnter a blank line or EOF to quit.")
            line = input()
            if line == '':
                break
            nums = [int(num) for num in line.split(', ')]

            print(f'\nYou gave me: {nums}.')
            print(f"\nThe permutations of these numbers are:\n" +
                f"\tMethod 1: {Solution().find_perms_itertools(nums)}\n")

        except EOFError:
            break

if __name__ == '__main__':
    main()