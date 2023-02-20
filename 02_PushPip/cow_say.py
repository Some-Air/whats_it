import cowsay
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--listcows', help='lists all cowfiles', action='store_true')
parser.add_argument('-n', '--wrap_text', help='the message will not be word-wrapped', action='store_true')

parser.add_argument('-b', '--borg', default=[''], help='initiates Borg mode', action='store_true')
parser.add_argument('-d', '--dead', default=[''], help='causes the cow to appear dead', action='store_true')
parser.add_argument('-g', '--greedy', default=[''], help='invokes greedy mode', action='store_true')
parser.add_argument('-p', '--paranoia', default=[''], help='causes a state of paranoia to come over the cow', action='store_true')
parser.add_argument('-s', '--stoned', default=[''], help='makes the cow appear thoroughly stoned', action='store_true')
parser.add_argument('-t', '--tired', default=[''], help='yields a tired cow', action='store_true')
parser.add_argument('-w', '--wired', default=[''], help='initiates wired mode', action='store_true')
parser.add_argument('-y', '--youthful', default=[''], help="brings on the cow's youthful appearance", action='store_true')                    

parser.add_argument('message', nargs='?', help='A string to wrap in the text bubble')
parser.add_argument('-f', '--cowfile', required=False, help='specifies a particular cow picture file')
parser.add_argument('-e', '--eyes', default='oo', required=False, help="cow's eyes (2 characters)")
parser.add_argument('-T', '--tongue', default='', required=False, help="cow's tongue (2 characters)")
parser.add_argument('-W', '--width', default=40, required=False, help='specifies roughly where the message should be wrapped', type=int)

args = parser.parse_args()
  
if args.listcows:
    cowlist = sorted(cowsay.list_cows())
    print(cowsay.list_cows())
else:
    moo = cowsay.cowsay(args.message,
                        eyes=args.eyes,
                        tongue=args.tongue,
                        width=args.width,
                        wrap_text=args.wrap_text,
                        cowfile=args.cowfile)
    print(moo)
