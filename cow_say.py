from cowsay import cowsay, list_cows
import argparse

parser = argparse.ArgumentParser()
#Optional flags:
parser.add_argument('-l', '--listcows', help='lists all cowfiles', action='store_true')
parser.add_argument('-n', help='the message will not be word-wrapped', action='store_true')
parser.add_argument('-b', '--borg', help='initiates Borg mode', action='store_true')
parser.add_argument('-d', '--dead', help='causes the cow to appear dead', action='store_true')
parser.add_argument('-g', '--greedy', help='invokes greedy mode', action='store_true')
parser.add_argument('-p', '--paranoia', help='causes a state of paranoia to come over the cow', action='store_true')
parser.add_argument('-s', '--stoned', help='makes the cow appear thoroughly stoned', action='store_true')
parser.add_argument('-t', '--tired', help='yields a tired cow', action='store_true')
parser.add_argument('-w', '--wired', help='initiates wired mode', action='store_true')
parser.add_argument('-y', '--youthful', help="brings on the cow's youthful appearance", action='store_true')                    
#Optional not_flags:
parser.add_argument('message', help='A string to wrap in the text bubble')
parser.add_argument('-f', '--file', required=False, help='specifies a particular cow picture file')
parser.add_argument('-e', '--eye_string', required=False, help="cow's eyes (2 characters)")
parser.add_argument('-T', '--tongue_string', required=False, help="cow's tongue (2 characters)")
parser.add_argument('-W', '--width', required=False, help='specifies roughly where the message should be wrapped', type=int)

args = parser.parse_args()
if args.listcows:
    cowlist=sorted(cowsay.list_cows())
    print(*cowlist)
elif args.listcows == False and args.message == '':
    print('You were supposed to type something')
else:
    moo = cowsay.cowsay(args.message, eyes=args.eyes[0:2], tongue=args.tongue[0:2], width=args.width)
    print(moo)
