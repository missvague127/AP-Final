
def handleQuery(q):

    qs = q.split()

    if(qs[0] == "INSERT"):
        ## handle it ass insert query
        return

    if(qs[0] == "SELECT"):
        ## handle it ass select query
        return

    if(qs[0] == "UPDATE"):
        ## handle it ass update query
        return

    if(qs[0] == "DELETE"):
        ## handle it ass delete query
        return

    return



#1.read schema file and generate files if not exist
sch = open("schema.txt")

lines= sch.readlines()

for i in range(len(lines)):
    parts = lines[i].split()
    if (len(parts)==1):
        tableName = lines[i]
        fa=open("_"+tableName.strip()+".txt" , 'a')
        fr=open("_"+tableName.strip()+".txt" , 'r')
        if(len(fr.readlines())==0):
            for j in range(i+1 , len(lines)):
                if(lines[j].strip()==""):
                    i=j+1
                    break
                fa.write(lines[j].split()[0]+"\t")
            fa.close()