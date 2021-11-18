import matplotlib.pyplot as plt
from math import *


def get_sequence_from_string(sequence: str, origin_range: int = 100, plot: bool = True, plot_args: list = None,
                             plot_kwargs: dict = None, print_values: bool = False) -> list:
    """
    This function returns and plots the values of a given sequence in a given origin range.
    The sequence has to use 'n' as it's variable.

    :param sequence: The sequence to be plotted.
    :param origin_range: The origin range of the sequence.
    :param plot: If True, the sequence will be plotted.
    :param plot_args: arguments for the plot function.
    :param plot_kwargs: keyword arguments for the plot function.
    :param print_values: If True, the values of the sequence will be printed.
    :return: A list of the values of the sequence.
    """

    sequence = sequence.replace('^', '**')

    values = []
    for n in range(1, origin_range):
        values.append(eval(sequence))

    if plot:
        if plot_args is None:
            plot_args = ['ok']
        if plot_kwargs is None:
            plot_kwargs = {'label': 'Sequence'}

        plt.plot(values, *plot_args, **plot_kwargs)
        plt.show()

    if print_values:
        print(values)

    return values
