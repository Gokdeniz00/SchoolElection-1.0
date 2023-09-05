import os
with open("candidates.json",'w+') as file:
    CandidateName=""
    i=1
    file.write("{\n")
    while(CandidateName != "/E"):
        print("Enter Candidate Name:")
        CandidateName= input()
        if CandidateName !="/E":
            file.write("\"{}\":0,\n".format(CandidateName))
            print("Succesfully added canditate: ",CandidateName)
            i+=1
        else:
            continue
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(size-3)
    file.truncate() 
    file.write("\n}")