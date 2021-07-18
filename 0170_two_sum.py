"""Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.
"""

class Solution:
    def find_indicies_brute(self, nums, target):
        """Compare every item in the given list of numbers to every other item
        until the two items that add up to the target are found. This is the 
        brute-force, n-squared solution.

        Note: this solution was not accepted for very large data sets; maximum
        execution time was exceeded.

        Arguments:
            nums {dict} -- User-given set of numbers to find matches within.
            target {int} -- User-given target sum of numbers in given dictionary.

        Returns:
            indicies {dict} -- The indicies of the matches that add up to the target.
        """
        indicies = []

        print("\nBrute force double array solution!")
        for outer in range(len(nums)):
            for inner in range(len(nums)):
                if outer == inner:
                    continue

                print(f"\tOuter ({nums[outer]}) + inner ({nums[inner]}) = {nums[outer] + nums[inner]}.")

                if int(nums[outer] + nums[inner]) == int(target):
                    indicies.append(outer)
                    indicies.append(inner)
                    print(f"\t\tMatches found; outer index ({outer}) and inner ({inner}).")
                    return indicies

        return indicies

    def find_indicies_listindex(self, nums, target):
        """Use python's built-in index function to find the index of the target
        minus the first item in the list, followed by the next if not found, etc.

        Arguments:
            nums {list} -- User-given set of numbers to find matches within.
            target {int} -- User-given target sum of numbers in given dictionary.

        Returns:
            indicies {dict} -- The indicies of the matches that add up to the target.
        """
        indicies = []

        print("Solution using built-in index function!")
        for outer in range(len(nums) - 1):
            print(f"\tOuter ({nums[outer]}); looking for {int(target)-int(nums[outer])} in list.")
            try:
                target_index = nums.index(int(target)-int(nums[outer]), outer+1)
                if target_index == outer:
                    print("\t\tOnly found current index; trying next number.")
                    continue
            except ValueError:
                print("\t\tTarget index not found; trying next number.")
                continue

            return [outer, target_index]

        return indicies

def main():
    while True:
        try:
            print("\nEnter a set of comma separated numbers, then a target sum.\n" + 
                "I'll give you the indices of the two numbers from the set that" +
                " equal the target. Enter a blank line or EOF to quit.")
            line = input()
            if line == '':
                break
            nums = [int(num) for num in line.split(', ')]
            target = input()
            print(f'\nYou gave me: {nums} with a target sum of {target}.')
            print(f"\nThe indicies of the numbers given that add up to the target are:\n" +
                f"\tMethod 1: {Solution().find_indicies_brute(nums, target)}\n" +
                f"\tMethod 2: {Solution().find_indicies_listindex(nums, target)}")

        except EOFError:
            break

if __name__ == '__main__':
    main()