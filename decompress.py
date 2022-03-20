def decompress(someString):
    outputString = ""
    while(someString.find('[') != -1 ) and (someString.find(']') != -1 ):
        posCloseBracket = int(someString.find(']'))
        basePattern = "";
        while(someString[0:posCloseBracket].count('[') > 1 and someString[0:posCloseBracket]):
            posLastOpenBracket = int(someString[0:posCloseBracket].rfind('['))
            #find positon of penultimate open bracket
            posPenUltOpenBracket = int(someString[0:posLastOpenBracket].rfind('['))
            mult = int(someString[posPenUltOpenBracket+1:posLastOpenBracket])
            posFirstCloseBracket = int(someString.find(']'))
            pattern = someString[posLastOpenBracket+1:posFirstCloseBracket]
            #remove part that has been delt with (middle part in this case):
            someString = someString[0:posLastOpenBracket-1] + someString[posFirstCloseBracket+1:]
            if(basePattern == ""):
                basePattern = mult*pattern
            else:
                basePattern = mult*((basePattern)+pattern)
        #initial char check:
        if(someString[0].isalpha()):
            outputString += someString[0]
            someString = someString[1:]
        else:
            posOpenBracket = int(someString.find('['))
            if(not(someString[0:posOpenBracket]).isnumeric()):
                mult = 1
            else:
                mult = int(someString[0:posOpenBracket])
            posCloseBracket = int(someString.find(']'))
            pattern = someString[posOpenBracket+1:posCloseBracket]
            if(basePattern == ""):
                outputString += mult*pattern
            else:
                basePattern = mult*((basePattern)+pattern)
                outputString = outputString + basePattern
                basePattern = ""
            someString = someString[posCloseBracket+1:]
    outputString = outputString+someString
    return outputString
