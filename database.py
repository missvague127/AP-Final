from operator import truediv
from optparse import Values


class Response():
    def __init__(self , result , entries):
        self.result = result
        self.entries = entries

class MyEntry():
    id

class UserEntry(MyEntry):
    def __init__(self , name , ncode , _pass , phone , email , joined):
        self.name=name
        self.ncode =ncode
        self._pass=_pass
        self.phone=phone
        self.email=email
        self.joined=joined
    
    def __eq__(self , other):
        if (self.name == other.name and self.ncode == other.ncode and self._pass==other._pass):
            if(self.phone == other.phone and self.email == other.email and self.joined == other.joined):
                return True
        return False
    
    def __str__(self):
        return self.name+"#"+self.ncode+"#"+self._pass+"#"+self.phone+"#"+self.email+"#"+self.joined


def handleQuery(q):

    qs = q.split()

    if(qs[0] == "INSERT"):
        ## handle it ass insert query
        return

    if(qs[0] == "SELECT"):
        ## handle it ass select query
        return handleSelectQuery(q)

    if(qs[0] == "UPDATE"):
        ## handle it ass update query
        return

    if(qs[0] == "DELETE"):
        ## handle it ass delete query
        return

    return

def handleSelectQuery(q):

    parts = q.split()
    tableName=parts[2]

    conditions= "("+q[q.find("WHERE")+6:]+")"
    print(conditions)
    entries= condResult(tableName,conditions)

    if (len(entries)==0):
        return Response("unsuccess" , entries)

    return Response("success" , entries)

def condResult(t , c):
    if(c[1]=="(" and c[len(c)-2]==")"):
        return condResult(t , c[1:len(c)-2])
    if (c.find("OR") == -1 and c.find("AND") == -1 and c.find("(") == -1 and c.find(")") == -1):
        return OneCondResult(t,c)
    tt=0
    for i in range(1,len(c)):
        if(c[i]== "("):
            tt=tt+1
        elif(c[i] == ")"):
            tt=tt-1
        elif(c[i:i+2] == "OR" and tt==0):
            return ORFunc(condResult(t,c[1:i-1]) , condResult(t,c[i+2:len(c)-1]))
        elif(c[i:i+3] == "AND" and tt==0):
            return ANDFunc(condResult(t,c[1:i-1]) , condResult(t,c[i+3:len(c)-1]))
        tc=c[i:i+3]

def OneCondResult(t,c):
    ret = []
    field =""
    value =""
    if (c.find("!=") != -1):
        parts=c.split("!=")
        field , value = parts[0] , parts[1]

    elif (c.find("==") != -1):
        parts=c.split("==")
        field , value = parts[0].strip() , parts[1].strip().replace("\"" , "")
    
    fileName= "_"+t+".txt"
    f = open(fileName , 'r')

    lines = f.readlines()
    fields=lines[0].split("\t")

    for i in range(1,len(lines)):
        for j in range(len(fields)):
            if (fields[j].strip()==field.strip()):
                values = lines[i].split()
                if (values[j].strip() == value):
                    if(t=="users"):
                        entry = UserEntry(values[0],values[1],values[2],values[3],values[4],values[5])
                        ret.append(entry)
    return ret
    
        
def ORFunc(a,b):
    ret = b
    for i in range(len(a)):
        found=0
        for j in range(len(b)):
            if (a[i]==b[j]):
                found=1
                break
        if(found == 0):
            ret.append(a[i])
    return ret

def ANDFunc(a,b):
    ret=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                ret.append(b[j])
                break
    
    return ret


        


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