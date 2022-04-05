# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:58:38 2022

Masters sweepstake calculator

@author: ConnorJones
"""
import random
import json
import pprint


def enter_names(names, num_bettors):
    """
    Enter names of golfers in ranked order, separated by ', '. Outputs blocks
    of golfers that are split by rank.

    Parameters
    ----------
    names : str
        List of golfers, highest rank first, lowest rank last as single string,
        separated by commas.
    num_betters: int
        Number of bettors that are playing.

    Returns
    -------
    Nested list of golfers separated into blocks.

    """
    split_names = names.split(', ')
    divisor = len(split_names) // num_bettors
    remainder = len(split_names) % num_bettors
    # Remove lowest ranked remainder golfers from split_names so it is
    # divisible by the number of bettors
    round_names = split_names[0:len(split_names)-remainder]
    bsize = int(len(round_names)/divisor)
    blocks = [round_names[x:x+bsize] for x in range(0, len(round_names), bsize)]
    return blocks


def randomise_blocks(blocks):
    """
    Takes blocks of golfers that are organised by blocks and randomises them.

    Parameters
    ----------
    blocks : list
        Nested list of lists of golfers with same length.

    Returns
    -------
    Randomised blocks of golfers.

    """
    rand_blocks = []
    for block in blocks:
        numberlist = list(range(0, len(block)))
        random.shuffle(numberlist)
        rblock = []
        for index in numberlist:
            rblock.append(block[index])
        rand_blocks.append(rblock)
    return rand_blocks


def assign_bettors(bettors_names, blocks):
    """
    Assigns golfers to bettors.

    Parameters
    ----------
    bettors_names : str
        String seperated by ', .
    blocks : nested list
        Nested list of golfers.
    Returns
    -------
    Golfers that are assigned to bettors as dict.

    """
    bettors = bettors_names.split(', ')

    golfers = []
    for x in range(0, len(blocks[0])):
        for block in blocks:
            golfers.append(block[x])
        
    bettors_golfers = {}
    x = 0
    for bettor in bettors:
        bettors_golfers[bettor] = golfers[0+x : len(blocks)+x]
        x += len(blocks)
    return bettors_golfers


def main():
    bettorsnames = input("Please enter all bettors names, separated by ', ': \n")
    golfersnames = input("Please enter all golfers names in ranked order, separated by ', ' (it is recommended that you write out in a text / word file first and copy and paste): \n")
    num_bettors = len(bettorsnames.split(', '))
    blocks = enter_names(golfersnames, num_bettors)
    randblocks = randomise_blocks(blocks)
    bettors_golfers = assign_bettors(bettorsnames, randblocks)
    
    with open('masters.txt', 'w') as file:
     file.write(json.dumps(bettors_golfers, indent=4, sort_keys=True)) # use `json.loads` to do the reverse
    pprint.pprint(bettors_golfers)
    print('\n The file masters.txt has just been created in the folder where this program is stored with the results.')
    input('Please press any button to close the program')


if __name__ == '__main__':
    main()
