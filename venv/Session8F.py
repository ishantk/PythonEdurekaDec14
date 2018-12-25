import re

def regularExprDemo():

    quote = "Work Hard and Get Luckier"

    result = re.findall(r".", quote)
    print(result)


    print(">>>>>>>>><<<<<<<<")
    print()

    result = re.findall(r"\w", quote)   # 1st input is a pattern which should be a raw string
    print(result)

    print(">>>>>>>>><<<<<<<<")
    print()

    result = re.findall(r"\w*", quote)
    print(result)

    print(">>>>>>>>><<<<<<<<")
    print()

    result = re.findall(r"\w+", quote)
    print(result)
