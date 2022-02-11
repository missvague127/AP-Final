class Table():
    def __init__(self , name , fields):
        self.name=name
        self.fields=fields

class Field():
    def __init__(self , name ,isUnique , type , typeLimit):
        self.name = name
        self.isUnique = isUnique
        self.type = type
        self.typeLimit = typeLimit


class Response():
    def __init__(self , result ,message , entries ):
        self.result = result
        self.message=message
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
        return self.name+"\t"+self.ncode+"\t"+self._pass+"\t"+self.phone+"\t"+self.email+"\t"+self.joined

class AccountEntry(MyEntry):
    def __init__(self , accnumber , ownerNcode , balance , alias, fav,createTime):
        self.accnumber=accnumber
        self.ownerNcode =ownerNcode
        self.balance=balance
        self.alias=alias
        self.fav=fav
        self.createTime=createTime
    
    def __eq__(self , other):
        if (self.accnumber == other.accnumber and self.ownerNcode == other.ownerNcode ):
            if(self.createTime == other.createTime and self.balance==other.balance):
                if(self.alias==other.alias and self.fav== other.fav):
                    return True
        return False
    
    def __str__(self):
        return self.accnumber+"\t"+self.ownerNcode+"\t"+self.balance+"\t"+self.alias+"\t"+self.fav+"\t"+self.createTime
    
    def prettyStr(self):
        return self.accnumber+" "+self.alias+" "+self.balance

class TransactionEntry(MyEntry):
    def __init__(self , accfrom, accto, amount, time, desc):
        self.accfrom = accfrom
        self.accto=accto
        self.amount = amount
        self.time=time
        self.desc = desc

    def __eq__(self , other):
        if (self.accfrom == other.accfrom and self.accto == other.accto ):
            if(self.time == other.time and self.amount==other.amount):
                if(self.desc==other.desc):
                    return True
        return False
    
    def __str__(self):
        return self.accfrom+"\t"+self.accto+"\t"+self.amount+"\t"+self.time+"\t"+self.desc

    



def handleQuery(q):

    qs = q.split()

    if(qs[0] == "INSERT"):
        ## handle it ass insert query
        return handleInsertQuery(q)

    if(qs[0] == "SELECT"):
        ## handle it ass select query
        return handleSelectQuery(q)

    if(qs[0] == "UPDATE"):
        ## handle it ass update query
        return handleUpdateQuery(q)

    if(qs[0] == "DELETE"):
        ## handle it ass delete query
        return handleDeleteQuery(q)

    return


#------------------------------------------------------------------------handle select query and conditions
def handleSelectQuery(q):

    parts = q.split()
    tableName=parts[2]

    conditions= "("+q[q.find("WHERE")+6:]+")"
    #print(conditions)
    entries= condResult(tableName,conditions)

    if (len(entries)==0):
        return Response("unsuccess","no entries found" , entries)

    return Response("success" , "", entries)

def condResult(t , c):
    if(c[1]=="(" and c[len(c)-2]==")"):
        return condResult(t , c[1:len(c)-1])
    if (c.find("OR") == -1 and c.find("AND") == -1 and c[1:len(c)-1].find("(") == -1 and c[1:len(c)-1].find(")") == -1):
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
        field , value = parts[0].strip().replace("\"" , "").replace("(","").replace(")","") , parts[1].strip().replace("\"" , "").replace("(","").replace(")","")

    elif (c.find("==") != -1):
        parts=c.split("==")
        field , value = parts[0].strip().replace("\"" , "").replace("(","").replace(")","") , parts[1].strip().replace("\"" , "").replace("(","").replace(")","")
    
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
                    elif(t=="accounts"):
                        entry = AccountEntry(values[0],values[1],values[2],values[3],values[4],values[5])
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

def selectAll(t):
    ret =[]
    fileName= "_"+t+".txt"
    f = open(fileName , 'r')

    lines = f.readlines()
    fields=lines[0].split("\t")
    
    for i in range(1,len(lines)):
        values = lines[i].strip().split("\t")
        if(t=="users"):
            entry = UserEntry(values[0],values[1],values[2],values[3],values[4],values[5])
            ret.append(entry)
        elif(t=="accounts"):
            entry = AccountEntry(values[0],values[1],values[2],values[3],values[4],values[5])
            ret.append(entry)

    return ret

#------------------------------------------------------------------------handle insert query 
def handleInsertQuery(q):
    parts = q.split()
    tableName=parts[2].strip()

    values= (q[q.find("VALUES")+8:len(q)-2]).strip().split(',')

    #------------------------------------------check tables conditions
    for i in range(len(tables)):
        if(tableName == tables[i].name):
            entry=""
            for j in range(len(values)):
                thisField = tables[i].fields[j]
                if (checkFiledType(thisField.type , values[j])):
                    if(thisField.type=="CHAR"):
                        if(checkFieldLen(thisField.typeLimit , values[i])):
                            pass
                        else:
                            return Response("unsuccess" , "lenght limit for {field} is {limit}".format(field=thisField.name , limit=thisField.typeLimit), [])
                else:
                    return Response("unsuccess" ,"type of {field} should be {typeof}".format(field=thisField.name , typeof=thisField.type), [])
                #check if value should be unique
                if(thisField.isUnique):
                    if(checkUnique(tableName , thisField.name, values[j])):
                        return Response("unsuccess" , "{field} should be unique".format(field=thisField.name), [])
                    pass
                entry=entry+values[j]+"\t"
            fa=open("_"+tableName.strip()+".txt" , 'a')
            fa.write("\n"+entry)
            fa.close()
            if(tableName=="users"):
                entry = UserEntry(values[0],values[1],values[2],values[3],values[4],values[5])
            elif(tableName=="accounts"):
                entry = AccountEntry(values[0],values[1],values[2],values[3],values[4],values[5])
            return Response("success" ,"" , [entry])

def checkFiledType(type , value):
    if (type == "INTEGER"):
        try:
            int(value)
            return True
        except:
            return False
    elif(type == "BOOLEAN"):
        if(value.lower() == "true" or value.lower() == "false"):
            return True
        else:
            return False
    return True

def checkFieldLen(limit , value):
    if(len(value) <= limit):
        return True
    else:
        return False
    return False

def checkUnique(t ,field, value):
    fr =open("_"+t+".txt" , 'r')
    lines=fr.readlines()

    fields=lines[0].split("\t")
    
    for i in range(1,len(lines)):
        parts=lines[i].split()
        for j in range(len(parts)):
            if(field == fields[j]):
                if(parts[j] == value):
                    return True
    
    return False

#------------------------------------------------------------------------handle delete query 
def handleDeleteQuery(q):
    parts = q.split()
    tableName=parts[2]

    conditions= "("+q[q.find("WHERE")+6:]+")"
    #1. select entries to be deleted
    entries= condResult(tableName,conditions)
    if (len(entries)==0):
        return Response("unsuccess","no entries matches the conditions" , entries)

    #2. select all entries
    allEntries=selectAll(tableName)
    i=0
    while( i < len(allEntries)):
        for j in range(len(entries)):
            #print(i,len(allEntries) ,j, len(entries))
            if (allEntries[i] == entries[j]):
                allEntries.pop(i)
                j=len(entries)
        i=i+1
    
    fr =open("_"+tableName+".txt" , 'r')
    lines=fr.readlines()

    fields=lines[0]#.split("\t")

    fw =open("_"+tableName+".txt" , 'w')
    fw.close()

    fa =open("_"+tableName+".txt" , 'a')
    fa.write(fields)
    for i in range(len(allEntries)):
        fa.write(str(allEntries[i]))
        if(i<len(allEntries)-1):
            fa.write("\n")
    fa.close()

    

    return Response("success" , "", allEntries)

#------------------------------------------------------------------------handle update query 
def handleUpdateQuery(q):
    parts = q.split()
    tableName=parts[1]

    conditions= "("+q[q.find("WHERE")+6:q.find("VALUES")-1]+")"
    values = q[q.find("VALUES")+7:].split(',')
    #1. select entries to be deleted
    entries= condResult(tableName,conditions)
    if (len(entries)==0):
        return Response("unsuccess","no entries matches the conditions" , entries)

    #2. delete those found in 1
    allEntries=selectAll(tableName)
    i=0
    while( i < len(allEntries)):
        for j in range(len(entries)):
            #print(i,len(allEntries) ,j, len(entries))
            if (allEntries[i] == entries[j]):
                allEntries.pop(i)
                j=len(entries)
        i=i+1
    
    for i in range(len(entries)):
         entry = AccountEntry(values[0],values[1],values[2],values[3],values[4],values[5])
         allEntries.append(entry)

    fr =open("_"+tableName+".txt" , 'r')
    lines=fr.readlines()

    fields=lines[0]#.split("\t")

    fw =open("_"+tableName+".txt" , 'w')
    fw.close()

    fa =open("_"+tableName+".txt" , 'a')
    fa.write(fields)
    for i in range(len(allEntries)):
        fa.write(str(allEntries[i]))
        if(i<len(allEntries)-1):
            fa.write("\n")
    fa.close()
    return Response("success" , "" , [])





k=0
#1.read schema file and generate files if not exist
tables = []
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

for i in range(len(lines)):
    parts = lines[i].split()
    if (len(parts)==1):
        tableName = lines[i].strip()
        newTable= Table(tableName,[])
        for j in range(i+1 , len(lines)):
            if(lines[j].strip()==""):
                break
            fieldName = lines[j].split()[0]
            fieldType=lines[j].split()[len(lines[j].split())-1]
            fieldLimit=10000
            if(fieldType.find("(")!=-1):
                tesst=fieldType[fieldType.find("(")+1:fieldType.find(")")]
                fieldLimit=int(tesst)
                fieldType=fieldType[:fieldType.find("(")]
            
            fieldIsU=False
            if(len(lines[j].split())==3):
                fieldIsU=True
            
            newField=Field(fieldName,fieldIsU,fieldType,fieldLimit)
            newTable.fields.append(newField)
        tables.append(newTable)


