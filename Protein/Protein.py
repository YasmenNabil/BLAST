#na2s awl step ale bshel feha low complexity regions
blosum62 ={
    'C':{'C':9, 'S':-1, 'T':-1, 'P':-3, 'A':0,  'G':-3, 'N':-3, 'D':-3, 'E':-4, 'Q':-3, 'H':-3, 'R':-3, 'K':-3, 'M':-1, 'I':-1, 'L':-1, 'V':-1, 'F':-2, 'Y':-2, 'W':-2},
    'S':{'C':-1,'S':4,  'T':1,  'P':-1, 'A':1,  'G':0,  'N':1,  'D':0,  'E':0,  'Q':0,  'H':-1, 'R':-1, 'K':0,  'M':-1, 'I':-2, 'L':-2, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'T':{'C':-1,'S':1,  'T':4,  'P':1,  'A':-1, 'G':1,  'N':0,  'D':1,  'E':0,  'Q':0,  'H':0,  'R':-1, 'K':0,  'M':-1, 'I':-2, 'L':-2, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'P':{'C':-3,'S':-1, 'T':1,  'P':7,  'A':-1, 'G':-2, 'N':-1, 'D':-1, 'E':-1, 'Q':-1, 'H':-2, 'R':-2, 'K':-1, 'M':-2, 'I':-3, 'L':-3, 'V':-2, 'F':-4, 'Y':-3, 'W':-4},
    'A':{'C':0, 'S':1,  'T':-1, 'P':-1, 'A':4,  'G':0,  'N':-1, 'D':-2, 'E':-1, 'Q':-1, 'H':-2, 'R':-1, 'K':-1, 'M':-1, 'I':-1, 'L':-1, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'G':{'C':-3,'S':0,  'T':1,  'P':-2, 'A':0,  'G':6,  'N':-2, 'D':-1, 'E':-2, 'Q':-2, 'H':-2, 'R':-2, 'K':-2, 'M':-3, 'I':-4, 'L':-4, 'V':0,  'F':-3, 'Y':-3, 'W':-2},
    'N':{'C':-3,'S':1,  'T':0,  'P':-2, 'A':-2, 'G':0,  'N':6,  'D':1,  'E':0,  'Q':0,  'H':-1, 'R':0,  'K':0,  'M':-2, 'I':-3, 'L':-3, 'V':-3, 'F':-3, 'Y':-2, 'W':-4},
    'D':{'C':-3,'S':0,  'T':1,  'P':-1, 'A':-2, 'G':-1, 'N':1,  'D':6,  'E':2,  'Q':0,  'H':-1, 'R':-2, 'K':-1, 'M':-3, 'I':-3, 'L':-4, 'V':-3, 'F':-3, 'Y':-3, 'W':-4},
    'E':{'C':-4,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':2,  'E':5,  'Q':2,  'H':0,  'R':0,  'K':1,  'M':-2, 'I':-3, 'L':-3, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'Q':{'C':-3,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':0,  'E':2,  'Q':5,  'H':0,  'R':1,  'K':1,  'M':0,  'I':-3, 'L':-2, 'V':-2, 'F':-3, 'Y':-1, 'W':-2},
    'H':{'C':-3,'S':-1, 'T':0,  'P':-2, 'A':-2, 'G':-2, 'N':1,  'D':1,  'E':0,  'Q':0,  'H':8,  'R':0,  'K':-1, 'M':-2, 'I':-3, 'L':-3, 'V':-2, 'F':-1, 'Y':2,  'W':-2},
    'R':{'C':-3,'S':-1, 'T':-1, 'P':-2, 'A':-1, 'G':-2, 'N':0,  'D':-2, 'E':0,  'Q':1,  'H':0,  'R':5,  'K':2,  'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'K':{'C':-3,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':-1, 'E':1,  'Q':1,  'H':-1, 'R':2,  'K':5,  'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'M':{'C':-1,'S':-1, 'T':-1, 'P':-2, 'A':-1, 'G':-3, 'N':-2, 'D':-3, 'E':-2, 'Q':0,  'H':-2, 'R':-1, 'K':-1, 'M':5,  'I':1,  'L':2,  'V':-2, 'F':0,  'Y':-1, 'W':-1},
    'I':{'C':-1,'S':-2, 'T':-2, 'P':-3, 'A':-1, 'G':-4, 'N':-3, 'D':-3, 'E':-3, 'Q':-3, 'H':-3, 'R':-3, 'K':-3, 'M':1,  'I':4,  'L':2,  'V':1,  'F':0,  'Y':-1, 'W':-3},
    'L':{'C':-1,'S':-2, 'T':-2, 'P':-3, 'A':-1, 'G':-4, 'N':-3, 'D':-4, 'E':-3, 'Q':-2, 'H':-3, 'R':-2, 'K':-2, 'M':2,  'I':2,  'L':4,  'V':3,  'F':0,  'Y':-1, 'W':-2},
    'V':{'C':-1,'S':-2, 'T':-2, 'P':-2, 'A':0,  'G':-3, 'N':-3, 'D':-3, 'E':-2, 'Q':-2, 'H':-3, 'R':-3, 'K':-2, 'M':1,  'I':3,  'L':1,  'V':4,  'F':-1, 'Y':-1, 'W':-3},
    'F':{'C':-2,'S':-2, 'T':-2, 'P':-4, 'A':-2, 'G':-3, 'N':-3, 'D':-3, 'E':-3, 'Q':-3, 'H':-1, 'R':-3, 'K':-3, 'M':0,  'I':0,  'L':0,  'V':-1, 'F':6,  'Y':3,  'W':1},
    'Y':{'C':-2,'S':-2, 'T':-2, 'P':-3, 'A':-2, 'G':-3, 'N':-2, 'D':-3, 'E':-2, 'Q':-1, 'H':2,  'R':-2, 'K':-2, 'M':-1, 'I':-1, 'L':-1, 'V':-1, 'F':3,  'Y':7,  'W':2},
    'W':{'C':-2,'S':-3, 'T':-3, 'P':-4, 'A':-3, 'G':-2, 'N':-4, 'D':-4, 'E':-3, 'Q':-2, 'H':-2, 'R':-3, 'K':-3, 'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':1,  'Y':2,  'W':11}
   }
def Database(filename):
    file=open(filename)
    DB=[]
    for line in file:
        DB.append(line.rstrip())
    file.close()
    return DB

#one sequance in one line
def Query(filename):
    file = open(filename)
    Seq=(file.read())
    file.close()
    return Seq

def GetWords(seq):
    Words=[]
    for i in range(len(seq)):
        if len(seq[i:i+3]) < 3:
            continue
        else:
            Words.append(seq[i:i+3])
    return Words

def Checkwords(Words,Seq):
    if len(Words)==len(Seq)-3+1:
        return True
    else:
        return False

def GetNeighborhood(Words,T):
    list=['C','S','T','P','A','G','N','D','E','Q','H','R','K','M','I','L','V','F','Y','W']
    Neighborhood=[]
    Seeds=[]
    for i in range (len(Words)):
        for j in range (len(Words[i])):
            for k in range(len(list)):
                score = 0
                add=Words[i].replace(Words[i][j],list[k])
                if len(add)==3 and add not in Neighborhood:
                    for x in range (len(add)):
                        score+=blosum62[add[x]][Words[i][x]]
                    #print("word",Words[i],"add",add,"score",score)
                    Neighborhood.append(add)
                    if score >= T :
                        Seeds.append((add,i))
    return Neighborhood,Seeds

#hit contain [0]index in query [1]which seq in DB [2]which index in DB seq [3]seed ale 3ml hit
def Gethits(Db,Seeds):
    Hitindex=[]
    for i in range(len(Seeds)):
        for j in range(len(Db)):
            if Seeds[i][0] in Db[j]:
                indexindb=Db[j].find(Seeds[i][0])
                Hitindex.append((seeds[i][1],j,indexindb,seeds[i][0]))
    return Hitindex


def Extend(hits,seq,db):
    HSP = []
    #################Forword#################
    for i in range (len(hits)):
        finalSEQ = ""
        finalDb = ""
        count = 1
        oldscore = 0
        newscore = 0
        forword = 0
        backword = 0

        #hmshy forword w backword l7d emta
        maxcount = 0
        if len(seq) < len(db):
            minlen = len(seq)
            forword = minlen - 3 - (hits[i][0])
            backword = len(seq) - 3 - forword
            maxcount = min(forword,backword)
        elif len(db[hits[i][1]]) < len(seq):
            minlen = len(db[hits[i][1]])
            forword = minlen - 3 - (hits[i][2])
            backword = len(db[hits[i][1]]) - 3 - forword
            maxcount = min(forword,backword)


        #old score between seed and hit in db
        sindex = hits[i][0]
        dseq = db[hits[i][1]]
        dindex = hits[i][2]
        query = hits[i][3]
        dbbbb = dseq[dindex:dindex + 3]
        finalSEQ += query
        finalDb += dbbbb
        for k in range(len(hits[i][3])):
            oldscore += blosum62[query[k]][dbbbb[k]]

        #can't extend in 2 direction
        if maxcount == 0:
            #no extend
            if forword == 0 and backword == 0:
                HSP.append((query,dbbbb,oldscore,noextend))
            #extend forword
            elif forword > 0 and backword == 0:
                countf = 0
                newscore += oldscore
                for a in range(forword):
                    # 7arf 7arf l2odam
                    queryword = seq[sindex + 3 + countf]
                    ##
                    dbword = dseq[dindex + 3 + countf]

                    # newscore
                    newscore += blosum62[queryword][dbword]
                    if newscore < oldscore:
                        HSP.append((finalSEQ, finalDb, oldscore,"f"))
                        continue

                    else:
                        finalSEQ += queryword
                        finalDb += dbword
                        oldscore = newscore

                    countf += 1
                HSP.append((finalSEQ, finalDb, newscore,"f"))
            #extend backword
            elif forword == 0 and backword > 0:
                countb = 0
                newscore += oldscore
                for j in range(backword):
                    # 7arf 7arf lwara
                    queryword = seq[sindex - countb]
                    ##
                    dbword = dseq[dindex - countb]
                    #newscore
                    newscore += blosum62[queryword][dbword]
                    if newscore < oldscore:
                        finalSEQ += query
                        finalDb += dbbbb
                        HSP.append((finalSEQ, finalDb, newscore, "b"))
                        continue

                    else:
                        finalSEQ += queryword
                        finalDb += dbword
                        oldscore = newscore

                    countb += 1


        #extend in  2 direction
        elif maxcount>0:
            for j in range(maxcount):
                #forword&backword
                sindex = hits[i][0]
                #7tet 7arf mn wara + seed + 7arf mn 2odam
                queryword = seq[sindex - count]
                queryword += query
                queryword += seq[sindex+2+count]
                ##
                dbword = dseq[dindex - count]
                dbword += dbbbb
                dbword += dseq[dindex+2+count]

                #newscore
                for l in range(len(dbword)):
                    newscore += blosum62[queryword[l]][dbword[l]]
                if newscore < oldscore:
                    HSP.append((finalSEQ,finalDb,oldscore,"f&b"))
                    continue

                else:
                    HSP.append((queryword,dbword,newscore,"f&b"))

                count += 1
    return HSP

def CalcScore(H):
    Score = 0
    for i in range (len(H)):
        Score += H[i][2]
    return Score



Db=Database("ProteinDatabase.txt")
Seq=Query("Protein.txt")
Words=GetWords(Seq)
Check = Checkwords(Words,Seq)
neighborhood,seeds=GetNeighborhood(Words,10)
hits=Gethits(Db,seeds)
Hsps = Extend(hits,Seq,Db)
print(hits)
print(Hsps)
print("Score =",CalcScore(Hsps))
#print(Db)
#print(Seq)
#print(Words)
#print(Check)
#print(neighborhood)
#print(len(neighborhood))
#print(seeds)
#print(hits)
#print(Hsps)
