"""A valid number can be split up into these components (in order):

    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One or more digits.

For example, all the following are valid numbers: 
    ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: 
    ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""
import re

class Solution:
    def is_valid_grammar(self, test: str) -> bool:
        """[summary]

        Arguments:
            test {str} -- The string to test for a valid number

        Returns:
            valid {bool} -- Whether or not the given string is a valid number.
        """
        return False

    def is_valid_traverse(self, test: str) -> bool:
        """[summary]

        Arguments:
            test {str} -- The string to test for a valid number

        Returns:
            valid {bool} -- Whether or not the given string is a valid number.
        """
        has_sign = False
        has_dot = False
        has_e = False

        prev_char = ""
        for index, character in enumerate(test):
            if character == "+" or character == "-":
                if index != 0 and prev_char != "e":
                    return False
            elif character not in "0123456789.eE":
                return False
            elif character.lower() == "e" and prev_char not in "0123456789.":
                return False

            prev_char = character.lower()

        return True

    def is_valid_regex(self, test: str) -> bool:
        """We can use a regex to test if the given string matches any of the
        defined number patterns, specifically using the start/end of string 
        operators and the boolean OR operator to follow the definitions exactly.

        Arguments:
            test {str} -- The string to test for a valid number

        Returns:
            valid {bool} -- Whether or not the given string is a valid number.
        """
        sign_pattern = "[+-]?"
        int_pattern = "\d+"
        dec_pattern = "(\d+\.)|(\d+\.\d+)|(\.\d+)"
        enote_pattern = f"[eE]{sign_pattern}{int_pattern}"
        
        number_pattern = re.compile(f"^{sign_pattern}(({dec_pattern})|{int_pattern})({enote_pattern})?$")

        match = number_pattern.match(test)
        print(match)
        if match is not None:
            return True

        return False

def main():
    while True:
        try:
            print("\nEnter a string and I will tell you if it's a valid number.\n" + 
                "Enter a blank line or EOF to quit.")
            line = input()
            if line == '':
                break
            
            print(f"\nYou gave me: {line}")
            print(f"\nDetermining if this is a valid number...\n" +
                f"\tMethod 1: {Solution().is_valid_regex(line)}\n" +
                f"\tMethod 2: {Solution().is_valid_traverse(line)}")

        except EOFError:
            break

if __name__ == '__main__':
    main()