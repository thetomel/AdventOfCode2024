def isSafeDec(raport):

    size = len(raport)

    for i in range(size-1):

        if int(raport[i])>int(raport[i+1]):
            diff = abs(int(raport[i])-int(raport[i+1]))
            if diff > 3:
                return False
            else:
                continue
        else:
            return False

    return True

def isSafeInc(raport):

    size = len(raport)

    for i in range(size-1):

        if int(raport[i])<int(raport[i+1]):
            diff = abs(int(raport[i])-int(raport[i+1]))
            if diff > 3:
                return False
            else:
                continue
        else:
            return False

    return True


def main():

    f = open('input.txt', 'r')

    safeRaports = 0
    safeRaportsDam = 0 
    for line in f:

        tempArray = line.split()

        if(isSafeInc(tempArray) or isSafeDec(tempArray)):
            safeRaports+=1
        # if(isSafeIncDam(tempArray) or isSafeDecDam(tempArray)):
        #     safeRaportsDam+=1

    print(f"There are: {safeRaports} safe raports")
    # print(f"There are: {safeRaportsDam} safe raports")


if __name__ == "__main__": 
    main()