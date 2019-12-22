import argparse

class Argv():

    def __init__(self):
        self.__args = argparse.Namespace()
        self.__parser = argparse.ArgumentParser()
        self.ParserArguments()
        self.Parse()

    def ParserArguments(self):
        self.__parser.add_argument(
                "filename",
                type=str,
                help="gnuplot script filename to parse via plotex")
        #self.__parser.add_argument(
        #        "-v", "--verbose",
        #        action="store_true",
        #        help="increase output verbosity")
        self.__parser.add_argument(
                "-p", "--profile",
                type=str,
                default='default',
                help="select profile module")
        group = self.__parser.add_mutually_exclusive_group()
        group.add_argument(
                "-a", "--append",
                type=str,
                nargs='+',
                default='',
                help="append terminal header options")
        group.add_argument(
                "-r", "--replace",
                type=str,
                nargs='*',
                default='',
                help="replace terminal header options")
        self.__parser.add_argument(
                "-t", "--terminal",
                type=str,
                default='',
                help="set terminal")
        self.__parser.add_argument(
                "-d", "--display",
                action='store_true',
                help="display profile settings")
        #self.__parser.add_argument(
        #        "-i", "--ignore-latex",
        #        action='store_true',
        #        help="use default gnuplot terminal instead of terminal set by plotex")
                

    def Parse(self):
        self.__args = self.__parser.parse_args()

    def GetArgs(self):
        return self.__args
