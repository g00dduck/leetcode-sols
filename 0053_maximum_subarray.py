"""Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.
"""

class Solution:
    def max_sub_array_greedy(self, nums):
        """Find the maximum sum from a contigous subset of the set of given
        numbers. Use the maximum item in the subset as a baseline -- this
        lets us account for a set of entirely negative numbers. Otherwise, we
        just count up each element, starting over at zero if the sum decreases.
        We compare this to the current maximum sum each iteration to keep track
        of the global maximum.

        Arguments:
            nums {dict} -- User given set of numbers to find max sum from

        Returns:
            int -- The maximum sum of the given set of numbers
        """

        max_sum = max(nums)
        curr_sum = 0

        if max_sum >= 0:
            for num in nums:
                curr_sum = max(0, curr_sum + num)
                max_sum = max(max_sum, curr_sum)

        return max_sum

def main():
    while True:
        try:
            print('\nEnter a set of comma separated numbers. I\'ll give you' +
                ' the max sum from a contiguous subset from the set. Enter ' +
                'a blank line or EOF to quit!')
            line = input()
            if line == '':
                break
            nums = [int(num) for num in line.split(', ')]
            print(f'You gave me: {nums}')
            print(f'The maximum sum is: {Solution().max_sub_array_greedy(nums)}!')
        except EOFError:
            break

if __name__ == '__main__':
    main()