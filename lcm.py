import sys
import getopt

HELP="This utiliy will calculate the lcm of a set of numbers"


def calculate_lcm(listOfNums):
    print "Calculating lcm for",listOfNums
    print "I have",len(listOfNums)," numbers in the list"
    return 0


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print HELP
            sys.exit(0)
    # process arguments
    _listOfNumbers = []
    for arg in args:

        if (is_int(arg) is True):
            print arg,"is an integer, accepting it"
            _listOfNumbers.append(int(arg))
        else:
            print arg,"is not an integer, rejecting it"
    lcm = calculate_lcm(_listOfNumbers)
    print "lcm is:",lcm

def _testing():
    list = [2,4,3]
    expected_lcm = 12
    if (calculate_lcm(list) != 12):
        print "ERROR, it should be 12"
    else:
        print "SUCCESS, you got it, it's 12"

if __name__ == "__main__":
    main()
    _testing()