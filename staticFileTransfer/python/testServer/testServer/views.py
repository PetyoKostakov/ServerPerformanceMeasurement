from django.http import HttpResponse
from django.core.files import File
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