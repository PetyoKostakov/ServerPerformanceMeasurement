from django.http import HttpResponse
from django.core.files import File
import json
import os

def fileRequest(req):
    fileName = req.GET['fileName']
    method = req.GET['method']
    dataToWrite = req.GET['dataToWrite']

    print(fileName)
    print(method)
    print(dataToWrite)

    if method == 'read':
        with open(os.path.join('temp', fileName)) as f:
            lines = f.readlines()

        f.close()
        return HttpResponse(lines)
    else:
        file = open(os.path.join('temp', fileName), "w")
        file.write(dataToWrite)
        file.close()
        return HttpResponse(dataToWrite)

    return HttpResponse('hello')


def resourceRequest(req):
    def concatBigString():
        strArr = []
        str = ""

        for timeConcat in range(1, 20):
            for charsConcat in range(1, 256):
                strArr.append(unicode(chr(charsConcat), errors='replace'))

            str += "".join(strArr)

        return str

    def generateObject():
        tel = {}

        for num in range(0, 5):
           tel["prop" + str(num)] = {
               "prop": concatBigString()
           }

        return tel

    return HttpResponse(json.dumps(generateObject()))