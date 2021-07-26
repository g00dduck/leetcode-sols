"""Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""
import itertools

class Solution:
    def find_perms_recursive(self, nums):
        def backtrack(index: int):
            if index == len(nums):
                permutations.append(nums[:])

            for inner in range(index, len(nums)):
                nums[index], nums[inner] = nums[inner], nums[index]
                backtrack(index + 1)
                nums[index], nums[inner] = nums[inner], nums[index]

        permutations = []
        backtrack(0)

        perms_unique = []
        for perm_set in set(map(tuple, permutations)):
            perms_unique.append([item for item in perm_set])

        return perms_unique

    def find_perms_itertools(self, nums):
        permutations = []

        for perm_set in set(itertools.permutations(nums)):
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
                f"\tMethod 1: {Solution().find_perms_itertools(nums)}\n"
                f"\tMethod 2: {Solution().find_perms_recursive(nums)}\n")

        except EOFError:
            break

if __name__ == '__main__':
    main()