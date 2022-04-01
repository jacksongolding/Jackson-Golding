# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import math
import Week0.ageswap
import Week0.matrix
import Week0.animation
import Week1.infodblist
import Week1.fibonacci
import Week2.factorial
import Week2.imperativelcm
import Week2.ooplcm
import Coop.OopFib
import Coop.cube
import Coop.cuberoot
import Coop.sqrt
import Coop.square


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0_sub_menu = [
  ["Age Swap", Week0.ageswap.swapTest],
  ["Matrix", Week0.matrix.matrixTest],
  ["Animation", Week0.animation.ship]
]

week1_sub_menu = [
  ["Lists and Loops", Week1.infodblist.tester],
  ["Fibonacci", Week1.fibonacci.fibonacciTest]
]

week2_sub_menu = [
  ["Factorial", Week2.factorial.factorialTest],
  ["Imperative LCM", Week2.imperativelcm.lcmTest],
  ["OOP LCM", Week2.ooplcm.ooplcmTest]
]
sub_menu = [
    ["Fibonacci", Week1.fibonacci.fibonacciTest],
    ["Factorial", Week2.factorial.factorialTest],
    ["Imperative LCM", Week2.imperativelcm.lcmTest],
    ["OOP LCM", Week2.ooplcm.ooplcmTest],
    ["OOP Fib", Coop.OopFib.Fibtest2],
    ["Cube", Coop.cube.cube],
    ["Cube Root", Coop.cuberoot.cubrt],
    ["Square Root", Coop.sqrt.sqrt],
    ["Square", Coop.square.square],
]

patterns_sub_menu = [
    ["Matrix", Week0.matrix.matrixTest],
    ["Animation", Week0.animation.ship]
]

other_sub_menu = [
    ["Age Swap", Week0.ageswap.swapTest],
    ["Lists and Loops", Week1.infodblist.tester]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    menu_list.append(["Other", other_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Math" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Patterns" + banner
    buildMenu(title, patterns_sub_menu)
def other_submenu():
    title = "Other" + banner
    buildMenu(title, other_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
