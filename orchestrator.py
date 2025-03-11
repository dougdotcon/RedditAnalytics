#!/usr/bin/env python3
import os
import argparse
import glob

# Imports internos do projeto
from src.utils import tools
from src.data import create_SR_list, parser as p, merge as m
from src.utils import delete as d
from src.analysis import top_subs as t, metrics as a
from src.visualization import graphs as g, update_images as img

parser = argparse.ArgumentParser(
    description='This is the orchestrator for Reddit_TopSort most of the other .py scripts can be run from here with a simple flag',
)
parser.add_argument('File',
                    metavar='file',
                    nargs='?',
                    type=str,
                    default='',
                    help='the path to comment file, should be line a line seperated json file')
parser.add_argument('-u',
                       '--update',
                       action='store_true',
                       help='update the map of subreddits')
parser.add_argument('-m',
                       '--merge',
                       action='store_true',
                       help='merge files in the output directory')
parser.add_argument('-d',
                       '--delete',
                       action='store_true',
                       help='delete files in the output directory that have already been processed')
parser.add_argument('-a',
                       '--analyze',
                       const=-1,
                       default=None,
                       type=int,
                       nargs='?',
                       help='analyze files in the output directory and calculate adj matrix')
parser.add_argument('-t',
                       '--top',
                       const=-1,
                       default=None,
                       type=int,
                       nargs='?',
                       help='analyze files in the output directory and calculate adj matrix')
parser.add_argument('-g',
                       '--graph',
                       action='store_true',
                       help='graph adj_matrix')
parser.add_argument('-i',
                       '--images',
                       action='store_true',
                       help='load subreddit icons for every SR in a SR_List')

def main():
    args = parser.parse_args()

    # Must update if there are no valid lists to use
    if len((glob.glob("subreddit_lists/SR_List*"))) == 0:
        args.update = True

    if args.update:
        print('Loading list of top subreddits with create_SR_list.py')
        create_SR_list.main()

    map, map_filename = tools.subreddit_map()
    outputDir = os.path.join('output', tools.grabSlice(map_filename, 'SR_List', '.'))

    if args.File:
        print('Parsing Reddit Comments')
        p.parseFile(args.File, outputDir)

    if args.merge:
        m.mergeFiles(outputDir)

    if args.images:
        img.load_images(outputDir)

    if args.delete:
        d.clearFiles(outputDir)

    if args.top:
        t.top_subs(outputDir, args.top)

    if args.analyze:
        a.analyze(outputDir, args.analyze)

    if args.graph:
        g.graph(outputDir)

if __name__ == "__main__":
    main()
