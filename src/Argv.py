
import argparse

class Argv():

    __args = argparse.Namespace()
    __parser = argparse.ArgumentParser()
        
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

    def __init__(self):
        self.ParserArguments()
        self.Parse()

    def GetArgs(self):
        return self.__args

#argv = Argv()
#print(argv.GetArgs())
