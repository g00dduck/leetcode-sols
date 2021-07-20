"""Given an array of strings words and a width maxWidth, format the text such that 
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you 
can in each line. Pad extra spaces ' ' when necessary so that each line has exactly 
maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the 
number of spaces on a line does not divide evenly between words, the empty slots on 
the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is 
inserted between words.

Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
"""
from typing import List

class Solution:
    def full_justify_loop(self, words: List[str], max_width: int) -> List[str]:
        # Start by getting lines to justify.
        buffer = ""
        lines = []
        line = []
        for index, word in enumerate(words):
            print(f"\tWord {index}: {word}")
            print(f"\t\tBefore:")
            print(f"\t\t\tBuffer: {buffer}")
            print(f"\t\t\tLine: {line}")
            print(f"\t\t\tLines: {lines}")
            print(f"\t\tAfter:")

            buffer += word + " "
            line.append(word)

            # Overflow reached, append line
            if len(buffer) - 1 > max_width:
                print(f"\t\t\tBuffer: {buffer}")
                line.pop()
                lines.append(line)
                line = [word]
                buffer = word + " "
            else:
                print(f"\t\t\tBuffer: {buffer}")
            print(f"\t\t\tLine: {line}")
            print(f"\t\t\tLines: {lines}")
        lines.append(line)

        # Then add spaces to the words to justify. 
        print("\tFinding spaces to justify...")
        justified_lines = []
        for index, line in enumerate(lines):
            word_count = len(line)
            print(f"\t\tLine: {line}\tWord count: {word_count}")
            char_length = sum(len(word) for word in line)
            space_count = max_width - char_length
            print(f"\t\t{char_length} characters out of {max_width} used; need {space_count} spaces to fill.")
            print("*" * max_width)
            if word_count == 1 or index == len(lines) - 1:
                justified_lines.append(f'{{:<{max_width}}}'.format(' '.join(line)))
            else:
                word_index = 0
                for _i in range(space_count):
                    line[word_index] += " "
                    word_index += 1
                    if word_index == len(line) - 1:
                        word_index = 0
                print(''.join(line))
                justified_lines.append(''.join(line))

        return justified_lines

def main():
    while True:
        try:
            print("\nEnter a set of space separated words, then a max width.\n" + 
                "I'll justify the words to fit within that width!\n" + 
                "Enter a blank line or EOF to quit.")
            line = input()
            if line == '':
                break
            words = [str(word) for word in line.split(' ')]
            max_width = input()
            
            print(f'\nYou gave me: {words} with a target sum of {max_width}.')
            print(f"\nThe justified text is as follows:\n" +
                f"\tMethod 1:\n{Solution().full_justify_loop(words, int(max_width))}")

        except EOFError:
            break

if __name__ == '__main__':
    main()