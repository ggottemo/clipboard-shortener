from time import sleep
import pyperclip


def insert_linebreaks(original):

    output = ""
    for i in range(0, len(original), 80):

        output += original[i:i+80]
        output += "\n"
        currentI = i


    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialClip = pyperclip.paste()
    newClip = ""
    alreadyProcessed = False

    while True:
        newClip = pyperclip.paste()
        if newClip[0:5] != initialClip[0:5]:
            print(f"new clip detected:\n {newClip}\n")
            alreadyProcessed = False
        if len(newClip) > 85 and not alreadyProcessed:
            initialClip = insert_linebreaks(newClip)
            pyperclip.copy(initialClip)
            alreadyProcessed = True
            print(f"new output:\n {initialClip}")

        sleep(5)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
