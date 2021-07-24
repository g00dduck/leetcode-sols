"""A transformation sequence from word beginWord to word endWord using a dictionary 
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the 
number of words in the shortest transformation sequence from beginWord to 
endWord, or 0 if no such sequence exists.

Constraints:

    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.

"""
from typing import List

class Solution:
    def pretty_print_map(self, grid: List[List[str]]) -> str:
        pretty_map = ""
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                pretty_map = pretty_map + f"\t{grid[x][y]}"
            pretty_map += "\n"

        return pretty_map

    def get_num_islands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        # Get our flag checker!
        visited_coords = [[0 for _y in range(len(grid[0]))] for _x in range(len(grid))]

        # Start map traversal!
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # If this is water or land we've already visited, we're not 
                # intereseted; move to next coord.
                if int(grid[x][y]) == 0:
                    print("This is water! Continuing traversal.") 
                    continue
                if visited_coords[x][y] == 1:
                    print("We've been here! Continuing traversal.")
                    continue

                # This is a piece of unvisited land! Start an island search.
                searching_island = True
                water_N = False
                water_E = False
                water_S = False
                water_W = False
                search_x = x
                search_y = y
                search_direction = "N"
                while searching_island:
                    visited_coords[search_x][search_y] = 1
                    print(f"Searching island!! On coord ({search_x}, {search_y}) going {search_direction}. "
                        f"Visited land map:\n{self.pretty_print_map(visited_coords)}")

                    # Check for borders/water first, then visited land. When found,
                    # either quit searching or change direction. If neither are 
                    # found, continue searching in the same direction.
                    if search_direction == "N":
                        search_y = search_y - 1
                        if search_y == -1:
                            print("** On a border cell; resetting coord and changing direction.")
                            water_N = True
                            search_direction = "E"
                            search_y = 0
                        elif int(grid[search_x][search_y]) == 0:
                            print("** There's water to the north of here!! Changing direction.")
                            water_N = True
                            search_direction = "E"
                        elif visited_coords[search_x][search_y] == 1:
                            print("** We've been here before! Quit searching.")
                            searching_island = False
                        else:
                            print("** Continuing north!")
                            search_direction = "N"
                    elif search_direction == "E":
                        search_x = search_x + 1
                        if search_x == len(grid) or int(grid[search_x][search_y]) == 0:
                            water_E = True
                            search_direction = "S"
                            if search_x == len(grid):
                                search_x = len(grid) - 1
                        elif visited_coords[search_x][search_y] == 1:
                            searching_island = False
                        else:
                            search_direction = "E"
                    elif search_direction == "S":
                        search_y = search_y + 1
                        if search_y == len(grid[0]) or int(grid[search_x][search_y]) == 0:
                            water_S = True
                            search_direction = "W"
                            if search_y == len(grid[0]):
                                search_y = len(grid[0]) - 1
                        elif visited_coords[search_x][search_y] == 1:
                            searching_island = False
                        else:
                            search_direction = "S"
                    elif search_direction == "W":
                        search_x = search_x - 1
                        if search_x == -1 or int(grid[search_x][search_y]) == 0:
                            water_W = True
                            search_direction = "N"
                            if search_x == -1:
                                search_x = 0
                        elif visited_coords[search_x][search_y] == 1:
                            searching_island = False
                        else:
                            search_direction = "W"

                    if water_N and water_E and water_S and water_W:
                        num_islands += 1
                        searching_island = False
                print("\nFinished searching island! Continuing traversal.")

        return num_islands

def main():
    #while True:
        #try:
            island_map = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]            

            print(f"Here's the island map we're working with:\n{Solution().pretty_print_map(island_map)}")
            print(f"\nThis map contains {Solution().get_num_islands(island_map)} islands!")

        #except EOFError:
        #    break

if __name__ == '__main__':
    main()