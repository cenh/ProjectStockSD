import sys, time, os, filecmp
sys.path.append('..')
from controller import *

string = "\nHello World!"
longString = "\nHello World!\nHow are you doing?\nI'm doing well!"

def files_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    writeFile("test/wot.txt", string)
    return (readFile("test/wut.txt") == string
            and readFile("test/wat.txt") == longString
            and readFile("test/wot.txt") == string)

def folder_test():
    createFolder("test")
    createFolder("test/test")
    createFolder("test/hej")
    createFolder("test/fedt")
    ex_res = ['fedt', 'hej', 'test'] # Expected result
    return (all(x in ex_res for x in getDirs("test")))

def last_modified_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    time.sleep(1)
    writeFile("test/wot.txt", string)
    wut_os = os.path.getmtime("test/wut.txt")
    wat_os = os.path.getmtime("test/wat.txt")
    wot_os = os.path.getmtime("test/wot.txt")
    return (wut_os == fileModified("test/wut.txt")
            and wat_os == fileModified("test/wat.txt")
            and wot_os == fileModified("test/wot.txt"))

def last_modified_comparison_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    time.sleep(1)
    writeFile("test/wot.txt", string)
    wut_os = os.path.getmtime("test/wut.txt")
    wat_os = os.path.getmtime("test/wat.txt")
    wot_os = os.path.getmtime("test/wot.txt")
    return (modifiedComparison("test/wut.txt", "test/wat.txt")
            and modifiedComparison("test/wut.txt", "test/wot.txt") == False)

def files_ext_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    writeFile("test/wat.txt", longString)
    writeFile("test/wot.txt", string)
    writeFile("test/tad.dat", string)
    ex_res1 = ['wot.txt', 'wat.txt', 'wut.txt']
    ex_res2 = ['tad.dat']
    return (all(x in ex_res1 for x in getFilesExt("test", ".txt"))
            and all(x in ex_res2 for x in getFilesExt("test", ".dat")))

def clear_file_test():
    createFolder("test")
    writeFile("test/wut.txt", string)
    ex_res = ''
    clearFile("test/wut.txt")
    return (readFile("test/wut.txt") == ex_res)

    # Just returns true for now
def socket_test():
    (msg, body) = sendRequest("http://128.199.39.136/example/", 80)
    createFolder("socketTest")
    writeFile("socketTest/Contents.txt", body)
    return (filecmp.cmp('expected_test.txt', 'socketTest/Contents.txt'))

    # only run test code if run directly, not on imports
    # Maybe run all the tests in a loop instead :/
if __name__ == '__main__':
    print("Starting files test!")
    start_time = time.time()
    res = files_test()
    print("Files test returned: " + str(res))
    print("Files test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(1)
    print("Starting folder test!")
    start_time = time.time()
    res = folder_test()
    print("Folder test returned: " + str(res))
    print("Folder test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(1)
    print("Starting last modified test!")
    start_time = time.time()
    res = last_modified_test()
    print("Last modified test returned: " + str(res))
    print("Last modified test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(1)
    print("Starting last modified comparison test!")
    start_time = time.time()
    res = last_modified_comparison_test()
    print("Last modified comparison test returned: " + str(res))
    print("Last modified comparison test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(1)
    print("Starting files extension test!")
    start_time = time.time()
    res = files_ext_test()
    print("Files extension test returned: " + str(res))
    print("Files extension test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(1)
    print("Starting clear file test!")
    start_time = time.time()
    res = clear_file_test()
    print("Clear file test returned: " + str(res))
    print("Clear file test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    time.sleep(1)
    print("Starting socket test!")
    start_time = time.time()
    res = socket_test()
    print("Socket test returned: " + str(res))
    print("Socket test took: --- %s seconds ---" % (time.time() - start_time) + '\n')
    deleteFolder("test", force=True)
    deleteFolder("socketTest", force=True)

