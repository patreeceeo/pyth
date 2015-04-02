import os
from os import path as ospath

def unix(inputstr):
    parts = [ospath.expanduser(part) for part in inputstr.split('/')]
    if inputstr[0] == '/':
        return os.sep + ospath.join(*parts)
    else:
        return ospath.join(*parts)

        
    

