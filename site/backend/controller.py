import os, time, socket, time

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
    path = dir + "/" + file
    f = open(path, 'r')
    f.close()
    return f

# Writes to a file    
def writeFile(file, dir, str):
    path = dir + "/" + file
    f = open(path, 'w')
    f.write(str)
    f.close()

# Clear contents of a file
def clearFile(file, dir):
    path = dir + "/" + file
    with open(path, 'w'):
        pass

# Deletes a file
def deleteFile(file, dir):
    path = dir + "/" + file
    if os.path.exists(path):
        os.remove(path)

# Returns all files in directory as a list
def getFiles(dir):
    if os.path.isdir(dir):
        f = os.listdir(dir)
        return f
                
# Gets last modified date of file   
def fileModified(file, dir):
    path = dir + "/" + file
    modified = time.strftime("%a, %d %B %Y %H:%M:%S GMT", time.gmtime(os.path.getmtime(path)))
    return modified

# Check if two given files have the same modified date
def modifiedComparisson(file1, dir1, file2, dir2):
    modified1 = fileModified(file1, dir1)
    modified2 = fileModified(file2, dir2)
    return (modified1 == modified2)

# Gets file size
def fileSize(file, dir):
    path = dir + "/" + file
    size = os.path.getsize(path)
    return size

# Creates a socket that uses IPv4 and TCP
# Then sends a given request to the host
# Returns the response from the host
def sendRequest(request, url, port):
    # Splitting the url into a host and target, afterwards cleanup of target
    (host, target) = str(url).replace("http://", '').replace("https://", '').split("/", 1)
    target = target.split('#', 1)[0].split('?', 1)[0]

    # Append target with / if not already starting with it
    if not target.startswith('/'):
        target = '/' + target

    # Create IPV4 and TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Send the request
    sendRequest = (("GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n"%(target, host)).encode("ascii"))
    s.send(sendRequest)
    
    # Start recieving response in terms of chunks of 4096 bytes
    r = b''
    r = s.recv(4096)
    response = ''
    while r:
        response = response+r
        r = s.recv(4096)
    s.close()
    return response

def test():
    string = "Hello World!"
    createFolder("test")
    writeFile("wut.txt", "test", string)
    writeFile("wat.txt", "test", string)
    time.sleep(1)
    writeFile("wot.txt", "test", string)
    print("wut.txt last modified: " + fileModified("wut.txt", "test"))
    print("wat.txt last modified: " + fileModified("wat.txt", "test"))
    print("wot.txt last modified: " + fileModified("wot.txt", "test"))
    print("List of files in folder test: " + str(getFiles("test")))
    print("wut.txt == wat.txt?: " + str(modifiedComparisson("wut.txt", "test", "wat.txt", "test")))
    print("wut.txt == wot.txt?: " + str(modifiedComparisson("wut.txt", "test", "wot.txt", "test")))
    
test()
