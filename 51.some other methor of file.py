"""
the seek() and tell()
 are used to work with file objects and theri positions within a file. these functions are part of the built in io module. which provides a consistent interface for reading and writing to various file like objests such as fils pipes and in memory buffers

 tell() return the current position of seek pointer within the file
 """

# with open("temp.txt","r") as f:
#     print(type(f))


    #move to the 10th byte in the file
    # f.seek(11)

    #tell()
    # print(f.tell())


    #read next 5 byte
    # data= f.read(5)
    # print(data)

with open("temp2.txt","w") as f:
    #truncate() _ sirf specific charcter hi rahenge file me baki sab nikal jayenge
    f.truncate(3)