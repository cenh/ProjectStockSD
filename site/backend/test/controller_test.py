import controller

# these should be in individual methods
def test():
    string = "\nHello World!"
    longString = "\nHello World!\nHow are you doing?\nI'm doing well!"
    createFolder("test")
    createFolder("test/hej")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    writeFile("test/tad.dat", string)
    writeFile("test/hej/pls.txt", string)
    time.sleep(1)
    writeFile("test/wot.txt", string)
    print("Contents of wut.txt: " + readFile("test/wut.txt"))
    clearFile("test/wut.txt")
    print("Contents of wut.txt (After clearing):" + readFile("test/wut.txt"))
    print("Contents of wat.txt: " + readFile("test/wat.txt"))
    print("wut.txt last modified: " + str(fileModified("test/wut.txt")))
    print("wat.txt last modified: " + str(fileModified("test/wat.txt")))
    print("wot.txt last modified: " + str(fileModified("test/wot.txt")))
    print("wut.txt last modified converted: " + convertTime(fileModified("test/wut.txt")))
    print("List of files in folder test: " + str(getFiles("test")))
    print("List of all .txt files in folder test: " + str(getFilesExt("test", ".txt")))
    print("List of all sub-dirs in folder test: " + str(getDirs("test")))
    print("wut.txt == wat.txt?: " + str(modifiedComparison("test/wut.txt", "test/wat.txt")))
    print("wut.txt == wot.txt?: " + str(modifiedComparison("test/wut.txt", "test/wot.txt")))
    deleteFolder("test", force=True)

def socket_test():
    res = sendRequest("http://example.org/index.html", 80)
    createFolder("socketTest")
    writeFile("socketTest/Contents.txt", res)
    print("Contents of request response: " + readFile("socketTest/Contents.txt"))
    deleteFolder("socketTest", force=True)

# only run test code if run directly, not on imports
if __name__ == '__main__':
    test()
    socket_test()
