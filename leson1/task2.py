def askuser(massage):
    return int(input(massage))

def answerUserage(age):
    if age < 6:
        print("Rano v shkolu")
    if age < 5:
        print("bistro v shkolu")



print(askuser("How old are you? "))