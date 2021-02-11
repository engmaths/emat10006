#!/usr/bin/env python
#
# Filename      : averages.py
# Author        : Oscar Benjamin
# Date          : Feb 2021
# Description   : Command line script to display averages of some numbers.


def main(*arguments):
    """Command-line interface to display statistics about integers

    Examples
    ========

    $ ./averages.py 1 2 3
    Mean: 2
    Median: 2
    Mode: 1, 2, 3

    $ ./averages.py --file t.txt
    Mean: 2
    Median: 2
    Mode: 1, 2, 3

    Optional arguments
    ==================

    --mean   : show mean
    --median : show median
    --mode   : show mode
    --file   : read input from file

    """
    # Check for binary flags in the command-line arguments:
    flags, positional_arguments = handle_options(arguments)

    from_file = '--file' in flags

    if any(f in flags for f in ['--mean', '--mode', '--median']):
        # mean, median and mode default to False if any are given
        # explicitly
        options = {
            'show_mean': '--mean' in flags,
            'show_median': '--median' in flags,
            'show_mode': '--mode' in flags,
        }
    else:
        # mean, median and mode all default to True if none are given
        # explicitly
        options = {
            'show_mean': True,
            'show_median': True,
            'show_mode': True,
        }


    # Numbers from a file or from arguments?
    if from_file:
        #  $ python averages.py --file filename.txt

        if len(positional_arguments) != 1:
            print('Error: expected one non-flag input when -file is specified')
            return

        [filename] = positional_arguments
        numbers = load_numbers(filename)
    else:
        #  $ python averages.py 1 2 3
        number_strings = positional_arguments
        numbers = [int(numstr) for numstr in number_strings]

    #  Options handled. Now compute and display the result:
    display_stats(numbers, **options)


#---------------------------------------------------------------#
#                 Input/output functions                        #
#---------------------------------------------------------------#


def handle_options(arguments):
    """Separate flag arguments from a list of command line arguments

    Input is a list of strings and output is a list of flags and a list of
    non-flags.

    Example:

    >>> handle_options(['12', '--mean', '13'])
    (['--mean'], ['12', '13'])
    """
    positional_arguments = []
    flags = []
    for arg in arguments:
        if arg.startswith('--'):
            flags.append(arg)
        else:
            positional_arguments.append(arg)
    return flags, positional_arguments


def display_stats(numbers, *, show_mean=True, show_median=True, show_mode=True):
    """Display statistics for a list of numbers"""
    if show_mean:
        print('Mean:', format_number(mean(numbers)))

    if show_median:
        print('Median:', format_number(median(numbers)))

    if show_mode:
        print('Mode:', ', '.join(str(num) for num in mode(numbers)))


def format_number(float_number):
    """Convert number to string without decimal points if possible.

    The argument can be int or float. If its value is an integer then the
    formatted string will not have a decimal point like 2.0.

    Examples

    >>> format_number(2.0)
    '2'
    >>> format_number(2.1)
    '2.1'
    """
    # Check if the float is an exact integer:
    int_number = int(float_number)
    if int_number == float_number:
        return str(int_number)    # e.g. 123
    else:
        return str(float_number)  # e.g. 2.1


def load_numbers(filename):
    """Load numbers from an ASCII text file.

    The file should have one number per line like:
    12
    3
    14
    """
    with open(filename) as input_file:
        numbers = [int(line.strip()) for line in input_file]
    return numbers


#---------------------------------------------------------------#
#                 Statistical functions                         #
#---------------------------------------------------------------#


def mean(numbers):
    """Mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def median(numbers):
    """Median of a list of numbers."""
    N = len(numbers)
    sorted_numbers = sorted(numbers)

    # Need to handle even/odd cases differently
    is_odd = ((N % 2) == 1)
    if is_odd:
        numbers_median = sorted_numbers[N//2]
    else:
        a = sorted_numbers[N//2-1]
        b = sorted_numbers[N//2]
        numbers_median = (a + b) / 2

    return numbers_median


def mode(numbers):
    """Mode of a list of numbers.

    Returns a list of the most common numbers
    """
    # Count occurrences of each number:
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    # Find those with the greatest count
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode


#---------------------------------------------------------------#
#                 Command line entry point                      #
#---------------------------------------------------------------#


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    main(*arguments)
