from time import sleep
import os
import pyperclip


class CColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def insert_linebreaks(original):
    """Inserts linebreaks into a string every 80 characters without breaking words."""
    result = ""
    cur_len = 0
    for word in original.split():
        if cur_len + len(word) > 80:
            result += "\n"
            cur_len = 0
        result += word + " "
        cur_len += len(word) + 1
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialClip = pyperclip.paste()
    newClip = ""
    alreadyProcessed = False

    # enable color
    os.system('color')

    while True:
        newClip = pyperclip.paste()
        if newClip[0:5] != initialClip[0:5]:
            print(f"{CColors.OKCYAN}==========================================================================={CColors.ENDC}")
            print(CColors.OKCYAN + "==                              New Clip Detected                        ==" + CColors.ENDC)
            print(f"{CColors.OKCYAN}==========================================================================={CColors.ENDC}\n {CColors.WARNING} {newClip} {CColors.ENDC} \n")
            alreadyProcessed = False
        if len(newClip) > 85 and not alreadyProcessed:
            initialClip = insert_linebreaks(newClip)
            pyperclip.copy(initialClip)
            alreadyProcessed = True

            print(f"{CColors.OKGREEN}==========================================================================={CColors.ENDC}")
            print(f"{CColors.OKGREEN}==                             Clip Processed                            =={CColors.ENDC}")
            print(f"{CColors.OKGREEN}==========================================================================={CColors.ENDC}\n {initialClip}\n")



        sleep(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
