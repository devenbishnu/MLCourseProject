import numpy
import os


#
# parse connect 4 data file into usable format
#
def get_connect_four():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, r'connectfour\connectfour.data')
    loaded = numpy.loadtxt(filename, str)
    result = []
    for i in loaded:
        parsed = i.split(',')
        for j in range(len(parsed)):
            if (parsed[j] == 'b') or (parsed[j] == 'draw'):
                parsed[j] = 0
            if parsed[j] == 'x' or (parsed[j] == 'win'):
                parsed[j] = 1
            if parsed[j] == 'o' or (parsed[j] == 'loss'):
                parsed[j] = -1
        result.append(parsed)
    return result


#
# parse tictac_final data file into usable format
#
def get_tictac_final():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,
                            r'tictactoedatasets\tictac_final.txt')
    result = numpy.loadtxt(filename, int)
    return result


#
# parse tictac_multi data file into usable format
#
def get_tictac_multi():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,
                            r'tictactoedatasets\tictac_multi.txt')
    result = numpy.loadtxt(filename, int)
    return result


#
# parse tictac_single data file into usable format
#
def get_tictac_single():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,
                            r'tictactoedatasets\tictac_single.txt')
    result = numpy.loadtxt(filename, int)
    return result
