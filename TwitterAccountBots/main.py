import sys
import getopt
from TwitterCore.Core.AccountsCore import TwitterCreator

def main(argv):

    fromRow = 1
    toRow = -1
    inputFile = None
    driverType = 'proxy'
    opts, args = getopt.getopt(argv, "f:t:i:d:")

    if (opts):
        for o, a in opts:
            if o in ("-f"):
                fromRow = int(a)
            elif o in ("-t"):
                toRow = int(a)
            elif o in ("-i"):
                inputFile = a
            elif o in ("-d"):
                driverType = a
    while not inputFile:
        #inputFile = raw_input('Input file path: ')
        inputFile = input('Input file path: ')

    creator: TwitterCreator = TwitterCreator()
    print('Process started')
    creator.start(callbacks=[creator.desktopCreateUserPhone], inputFile=inputFile, fromRow=fromRow, toRow=toRow,
                  driverType=driverType)
    print('Process ended')


if __name__ == "__main__":
    main(sys.argv[1:])
