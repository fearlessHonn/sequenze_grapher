import argparse
from get_sequence_from_string import get_sequence_from_string

parser = argparse.ArgumentParser(description='Get sequence from string')
parser.add_argument('-s', '--string', help='String to get sequence from', required=True, type=str)
parser.add_argument('-r', '--range', help='The origin range of the sequence', required=False, type=int, default=100)
parser.add_argument('-p', '--plot', help='If True, the sequence will be plotted', required=False, type=bool, default=True)
parser.parse_args()

get_sequence_from_string(sequence=parser.parse_args().string, origin_range=parser.parse_args().range,
                         plot=parser.parse_args().plot)
