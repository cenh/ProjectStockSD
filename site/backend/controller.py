import os, time, socket

# Creates a folder with given directory name
def createFolder(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)

# Deletes a folder with given directory name        
def deleteFolder(dir):
    if os.path.isdir(dir):
        os.removedirs(dir)

# Reads a file        
def readFile(file, dir):
    path = dir + file
    f = open(path, 'r')
    f.close()
    return f

# Writes to a file    
def writeFile(file, dir, str):
    path = dir + file
    f = open(path, 'w')
    f.write(str)
    f.close()

# Deletes a file
def deleteFile(file, dir):
    path = dir + file
    if os.path.exists(path):
        os.remove(path)

# Returns all files in directory as array
def getFiles(dir):
    if os.path.isdir(dir):
        f = []
        for file in os.path.listdir(dir):
            if os.path.isfile(f):
                length = len(f)
                f[length] = file
        return f
                

# Gets last modified date of file   
def fileCheckModified(file, dir):
    path = dir + file
    modified = time.strftime("%a, %d %B %Y %H:%M:%S GMT", time.gmtime(os.path.getmtime(path)))
    return modified

# Check if two given files have the same modified date
def lastModifiedComparisson(file1, dir1, file2, dir2):
    modified1 = fileCheckModified(file1, dir1)
    modified2 = fileCheckModified(file2, dir2)
    return (modified1 == modified2)

# Gets file size
def fileSize(file, dir):
    path = dir + file
    size = os.path.getsize(path)
    return size

# Creates a socket that uses IPv4 and TCP
# Then sends a given request to the host
# Returns the response from the host
def sendRequest(request, host, target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    str = request + "%s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n"%(target, host)).encode("ascii"))
    s.send(str)
    r = b''
    r = s.recv(4096)
    response = ''
    while r:
        response = response+r
        r = s.recv(4096)
    return response
