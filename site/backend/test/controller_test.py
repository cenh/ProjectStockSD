import sys, time
sys.path.append('..')
from controller import *

string = "\nHello World!"
longString = "\nHello World!\nHow are you doing?\nI'm doing well!"

def files_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    writeFile("test/wot.txt", string)
    print("Contents of wut.txt: " + readFile("test/wut.txt"))
    print("Contents of wat.txt: " + readFile("test/wat.txt"))
    print("Contents of wot.txt: " + readFile("test/wot.txt"))
    deleteFolder("test", force=True)

def folder_test():
    createFolder("test")
    createFolder("test/test")
    createFolder("test/hej")
    createFolder("test/fedt")
    print("List of all sub-dirs in folder test: " + str(getDirs("test")))
    deleteFolder("test", force=True)

def last_modified_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    time.sleep(1)
    writeFile("test/wot.txt", string)
    print("wut.txt last modified: " + str(fileModified("test/wut.txt")))
    print("wut.txt last modified converted: " + convertTime(fileModified("test/wut.txt")))
    print("wat.txt last modified: " + str(fileModified("test/wat.txt")))
    print("wat.txt last modified converted: " + convertTime(fileModified("test/wat.txt")))
    print("wot.txt last modified: " + str(fileModified("test/wot.txt")))
    print("wot.txt last modified converted: " + convertTime(fileModified("test/wot.txt")))
    deleteFolder("test", force=True)

def last_modified_comparison_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    time.sleep(1)
    writeFile("test/wot.txt", string)
    print("wut.txt last modified converted: " + convertTime(fileModified("test/wut.txt")))
    print("wat.txt last modified converted: " + convertTime(fileModified("test/wat.txt")))
    print("wot.txt last modified converted: " + convertTime(fileModified("test/wot.txt")))
    print("wut.txt == wat.txt?: " + str(modifiedComparison("test/wut.txt", "test/wat.txt")))
    print("wut.txt == wot.txt?: " + str(modifiedComparison("test/wut.txt", "test/wot.txt")))
    deleteFolder("test", force=True)

def files_ext_test():
    print("Creating files wut.txt, wat.txt, wot.txt, tad.dat")
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    writeFile("test/wot.txt", string)
    writeFile("test/tad.dat", string)
    print("List of all .txt files in folder test: " + str(getFilesExt("test", ".txt")))
    print("List of all .dat files in folder test: " + str(getFilesExt("test", ".dat")))
    deleteFolder("test", force=True)

def clear_file_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    print("Contents of wut.txt before clearing: " + readFile("test/wut.txt"))
    clearFile("test/wut.txt")
    print("Contents of wut.txt after clearing: " + readFile("test/wut.txt"))
    deleteFolder("test", force=True)
    
def socket_test():
    res = sendRequest("http://example.org/index.html", 80)
    createFolder("socketTest")
    writeFile("socketTest/Contents.txt", res)
    print("Contents of request response: " + readFile("socketTest/Contents.txt"))
    deleteFolder("socketTest", force=True)
    
    # only run test code if run directly, not on imports
if __name__ == '__main__':
    print("Starting files test!")
    start_time = time.time()
    files_test()
    print("Files test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(3)
    print("Starting folder test!")
    start_time = time.time()
    folder_test()
    print("Folder test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(3)
    print("Starting last modified test!")
    start_time = time.time()
    last_modified_test()
    print("Last modified test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(3)
    print("Starting last modified comparison test!")
    start_time = time.time()
    last_modified_comparison_test()
    print("Last modified comparison test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(3)
    print("Starting files extention test!")
    start_time = time.time()
    files_ext_test()
    print("Files extension test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(3)
    print("Starting clear file test!")
    start_time = time.time()
    clear_file_test()
    print("Clear file test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(3)
    print("Starting socket test!")
    start_time = time.time()
    socket_test()
    print("Socket test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
