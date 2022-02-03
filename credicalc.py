import argparse
import math


parser = argparse.ArgumentParser(description="Calculadora de Empréstimo")


parser.add_argument("-a1", "--type",
                    help="Takes the payment type of the loan")
parser.add_argument("-a2", "--principal",
                    help="Takes the principal amount of the loan")
parser.add_argument("-a3", "--periods",
                    help="Takes the period in months that you'll need to pay the loan")
parser.add_argument("-a4", "--interest",
                    help="Takes the interest rate")
parser.add_argument("-a5", "--payment",
                    help="Takes the monthly payment")

args = parser.parse_args()
#print(args)
#Namespace(interest='10', periods='10', principal='100000', type='diff')

list_args = [args.type, args.principal, args.periods, args.interest, args.payment]

#comprehension (lists, tuples, dicts)
list_args = [item for item in list_args if item != None]
#new_list = []
#for item in list_args:
#    if item != None:
#        new_list.append(item)
#list_args = new_list

if args.type not in ("annuity", "diff"):
    print("Incorrect parameters.")

elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")

elif args.interest == None:
    print("Incorrect parameters")

elif len(list_args) < 4:
    print("Incorrect parameters")

elif args.principal and int(args.principal) < 0 or args.periods and int(args.periods) < 0 or args.interest and float(args.interest) < 0:
    print("Incorrect parameters")

list_args = [item for item in list_args if item != None]

# if args.principal and args.periods or args.interest or args.payment != None:
#     int(args.principal)
#     args.periods = int(args.periods)
#     float(args.interest)
#     int(args.payment)

if args.principal is not None:
    args.principal = int(args.principal)

if args.periods is not None:
    args.periods = int(args.periods)

if args.interest is not None:
    args. interest = float(args.interest) / 100 / 12

if args.payment is not None:
    args.payment = int(args.payment)


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier


def half_round(n):
    print(int(n * 10 % 10) < 1)
    if (int(n * 10 % 10) < 1):
        return int(round_half_down(n, 1))
    return int(round_half_up(n, 1))

def convert_month(months):
    years = 0
    if args.periods >= 12:
        years = args.periods // 12
        args.periods -= years * 12
    return years, months

def diff_payment(args):
    total = 0
    for month in range(0, args.periods):
        diff_pay = args.principal / args.periods + args.interest * (args.principal - (args.principal * month - 1) / args.periods)
        print(f'Month {month + 1}: payment is {half_round(diff_pay)}, {diff_pay}')
        total += diff_pay
    overpay = total - args.principal
    print(f"Overpayment = {round(overpay)}")

def annuity_payment(args):
    if args.principal == None:
        args.principal = args.payment / ((args.interest * (1 + args.interest) ** args.periods) / ((1 + args.interest) ** args.periods - 1))
        overpay = -(args.principal - args.payment * args.periods)
        print(f'Your loan principal = {round(args.principal)}!')
        print(f'Overpayment = {round(overpay)}')

    elif args.payment == None:
        args.payment = args.principal * args.interest * (1 + args.interest) ** args.periods / ((1 + args.interest) ** args.periods - 1)
        overpay = -(args.principal - math.ceil(args.payment) * args.periods)
        print(f'Your annuity payment = {round(args.payment)}')
        print(f'Overpayment = {round(overpay)}')

    elif args.periods == None:
        logaritimando = args.payment / (args.payment - args.interest * args.principal)
        args.periods = round(math.log(logaritimando, 1 + args.interest))
        overpay = -(args.principal - math.ceil(args.payment) * args.periods)
        years, months = convert_month(args.periods)
        print(f"It will take {years} years to repay this loan!")
        print(f'Overpayment = {round(overpay)}')

if args.type == "diff":
    diff_payment(args)

elif args.type == "annuity":
    annuity_payment(args)
