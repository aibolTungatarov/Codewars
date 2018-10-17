def expanded_form(num):
    num = (str)(num)
    res = ""
    tens = 10**(len(num)-1)
    for i in range(len(num)):
        if (int)(num[i]) != 0:
            res += (str)((int)(((int)(num[i]))*tens)) + ' + '
        tens/=10
    return res[:-3]     # -3 because there is 2 spaces and + at the end
