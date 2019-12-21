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
        self.__parser.add_argument(
                "-v", "--verbose",
                action="store_true",
                help="increase output verbosity")
   
    def Parse(self):
        self.__args = self.__parser.parse_args()

    def GetArgs(self):
        return self.__args
