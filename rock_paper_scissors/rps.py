#!/usr/bin/python

import sys
'''
the function takes n as an input parameter
n represents the number of rounds played
asking for all possible permutations so recursion will most likely be needed
if recursion is needed then we need a base case
 * You'll want to define a list with all of the possible Rock Paper Scissors plays.
 * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
base cases would be if n == 0 then there would be no plays so return an empty list
if n == 1 there would only be one possible permutation which would mean you can only play either rock, paper, or scissors so the list would contain 
  [["rock"], ["paper"], ["scissors"]]
  3 permutations
if n == 2 the list would be
  [[rock, rock][rock, paper][rock, scissors]['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']
  9 permutations
n == 3
  [[rock rock rock][rock paper scissors][rock paper paper][rock scissors scissors][rock scissors paper][rock rock scissors] [rock rock paper] [rock paper rock] [rock scissors rock],
  [paper paper paper] [paper paper rock] [paper paper scissors] [paper rock scissors] [paper scissors rock] [paper rock rock] [paper scissors scissors] [paper scissors paper] [paper rock paper],
  [scissors scissors scissors] [scissors scissors rock] [scissors scissors paper] [scissors rock scissors] [ scissors paper scissors] [scissors rock rock] [scissors paper paper] [scissors paper rock] [scissors rock paper]]
  27 permutations
Seems like Big O would be O(3^n)
'''


def rock_paper_scissors(n):
    rps = [["rock"], ["paper"], ["scissors"]]
    all_possible_plays = []
    # Base Case
    if n == 0:
        return [all_possible_plays]
    if n == 1:
        return rps

    for sublist in rock_paper_scissors(n - 1):
        for i in rps:
            all_possible_plays.append(sublist + i)
    return all_possible_plays

print(rock_paper_scissors(5))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
