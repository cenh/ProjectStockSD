# TODO:
# checkFile and checkDir to replace checks in other functions

import os, time, socket, time, shutil

# Chceks if a path leads to a file
def checkFile(path):
    if not os.path.isfile(path):
        raise ValueError('Not a correct path to a file')
    else:
        pass

# Check if a path leads to a directory
def checkDir(path):
    if not os.path.isdir(path):
        raise ValueError('Not a correct path to a directory')
    else:
        pass

# Creates a folder with given directory name
def createFolder(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        pass

# Deletes a folder with given directory name
def deleteFolder(path, force=False):
    if os.path.isdir(path):
        if not os.listdir(path):
            if not force:
                raise ValueError('Directory not empty')
        shutil.rmtree(path)
    else:
        raise ValueError('Not a folder')

# Reads a file
def readFile(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            res = f.read()
        return res
    else:
        raise ValueError('Not correct path to a file')

# Writes to a file
def writeFile(path, string):
    with open(path, 'w') as f:
        for chunk in string:
            f.write("%s" % chunk)

# Clear contents of a file
def clearFile(path):
    if os.path.exists(path):
        with open(path, 'w'):
            pass
    else:
        raise ValueError('Not correct path to a file')

# Deletes a file
def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        raise ValueError('Not correct path to a file')

# Returns all files in directory as a list
def getFiles(path):
    if os.path.isdir(path):
        res = []
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                res.append(f)
        return res
    else:
        raise ValueError('Not a directory')

# Returns all executables in a directory
def getFilesExt(path, ext):
    if os.path.isdir(path):
        res = []
        for f in os.listdir(path):
            if f.endswith(ext):
                res.append(f)
        return res
    else:
        raise ValueError('Not a directory')

# Returns all directories for the path
def getDirs(path):
    if os.path.isdir(path):
        res = []
        for d in os.listdir(path):
            if os.path.isdir(os.path.join(path, d)):
                res.append(d)
        return res
    else:
        raise ValueError('Not a directory')

# Gets last modified date since epoch of file, returns seconds since epoch
def fileModified(path):
    if os.path.isfile(path):
        modified = os.path.getmtime(path)
        return modified
    else:
        raise ValueError('Not a file')

# Takes epoch (Function above) and converts it to a readable format
def convertTime(epoch):
    modified = time.strftime("%a, %d %B %Y %H:%M:%S GMT", time.gmtime(epoch))
    return modified

# Check if two given files have the same modified date
def modifiedComparison(path1, path2):
    modified1 = fileModified(path1)
    modified2 = fileModified(path2)
    return (modified1 == modified2)

# Gets file size
def fileSize(path):
    if os.path.isfile(path):
        size = os.path.getsize(path)
        return size
    else:
        raise ValueError('Not a file')

# Creates a socket that uses IPv4 and TCP
# Then sends a given request to the host
# Returns the response from the host
def sendRequest(url, port):
    # Splitting the url into a host and target, afterwards cleanup of target
    (host, target) = url.replace("http://", '').replace("https://", '').split("/", 1)
    target = target.split('#', 1)[0].split('?', 1)[0]

    # Append target with / if not already starting with it
    if not target.startswith('/'):
        target = '/' + target

    # Create IPV4 and TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host, port))

    # Send the request
    request = (("GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n"%(target, host)).encode("ascii"))
    s.send(request)

    # Start recieving response in terms of chunks of 4096 bytes
    r = s.recv(4096)
    response = ''
    while r:
        response = response+str(r)
        r = s.recv(4096)

    msg = response.split('\n', 1)[0].split(' ', 2)[2]
    body = response.split("\r\n\r\n", 1)[1]

    s.close()
    return (msg, body)
