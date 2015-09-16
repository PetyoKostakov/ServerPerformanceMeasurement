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
        longStr = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis metus tempor, pharetra est vitae, vulputate ipsum. Suspendisse lobortis erat nec tortor elementum suscipit. Donec sit amet sagittis magna. Pellentesque iaculis enim pharetra, auctor leo vitae, semper ipsum. Sed ultrices purus quis sagittis efficitur. Fusce in velit dolor. Cras aliquam porta dui, sodales mollis lectus mollis sit amet. Integer eu diam sodales, ultricies odio id, suscipit erat. Suspendisse sit amet elementum urna. Aliquam porttitor sollicitudin purus, vel interdum nunc blandit id. Donec a dolor risus. Phasellus ultricies sollicitudin tempus.Aliquam erat leo, malesuada eget vestibulum sit amet, placerat vel justo. Morbi a leo non elit venenatis cursus non eget libero. Etiam semper magna sollicitudin vulputate bibendum. Quisque egestas quis neque quis pharetra. Praesent ac velit pretium, ultrices turpis at, sagittis enim. Donec in ante purus. Ut dolor enim, volutpat ut finibus quis, pulvinar sit amet dolor. Nam consectetur vel orci quis blandit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed hendrerit ligula bibendum justo pellentesque tempus.Mauris tincidunt cursus nisi, et dictum odio condimentum eget. Morbi nulla massa, vehicula at dui id, tempus lobortis ex. Ut porttitor velit quis lectus placerat, ut pretium nunc ultrices. Aenean a facilisis dolor, sit amet dapibus tortor. Proin interdum hendrerit ante, ac tempor tellus mollis eget. In iaculis fermentum arcu sed malesuada. Aenean porta felis est, at varius erat varius quis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Sed pellentesque sapien nibh, eget bibendum leo feugiat ut. Fusce euismod tempus maximus. Phasellus feugiat lacus eu libero vulputate, nec rutrum purus aliquet. Integer sit amet justo fringilla, luctus erat ac, varius mauris. Suspendisse quis ipsum metus. Donec congue imperdiet est eu mattis. Etiam lacinia urna ac hendrerit scelerisque. Quisque sed scelerisque risus, et congue ipsum. Donec ac quam porta, scelerisque lorem ac, efficitur ipsum. Fusce libero quam, consequat ut porta in, porttitor vitae ex. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Phasellus porta cursus justo quis egestas. Proin urna lectus, ultricies a ligula sit amet, euismod interdum nibh. Proin eu quam lacinia, eleifend orci ut, tincidunt ligula. Vivamus placerat, turpis fringilla rhoncus pharetra, erat urna dictum orci, ultricies tincidunt nisl velit sed risus. Maecenas fermentum tincidunt euismod. Praesent nec dictum ipsum. In ante turpis, facilisis nec lobortis in, euismod ac erat. Vestibulum ac aliquet ante. Integer posuere ultrices justo vel ultricies. Sed est nulla, molestie vel pretium id, sagittis nec arcu. In ornare eleifend enim eleifend lacinia. Morbi ante neque, congue id malesuada vitae, gravida eu massa. Vivamus blandit dictum malesuada. Proin at nunc orci. Nullam eget velit purus. Sed mollis nisl dictum ultricies fermentum. Curabitur ac elit luctus, mattis massa ut, facilisis neque. Donec elementum placerat accumsan. Cras cursus vitae nulla in porttitor. Donec a metus quis libero tempor laoreet. Curabitur dignissim, odio vitae facilisis."
        strArr = []
        str = ""

        for timeConcat in range(1, 20):
            for charsConcat in range(0, len(longStr)):
                strArr.append(longStr[charsConcat])

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