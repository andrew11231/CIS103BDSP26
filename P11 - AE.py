#Andrew Espinoza
import time
srtime = time.ctime()
print('Program started at: ',srtime)
genfiles = 'C:/temp/points.txt'
datagenfiles = open(genfiles,'r')
gradfiles = "C:/temp/gradess.txt"
datagradfiles = open(gradfiles,'w')
errorfiles = "C:/temp/errorrr.txt"
dataerrorfiles = open(errorfiles,'w')
def main():
    recd = 0
    cnta = 0
    cntb = 0
    cntc = 0
    cntd = 0
    cntf = 0
    errd = 0
    line1 = datagenfiles.readline()
    while line1 != '':
        (idd,nam,grd) = line1.split(',')
        idd = idd.strip()
        nam = nam.strip()
        grd = grd.strip()
        try:
            grd = int(grd)
            if grd > 1000:
                dataerrorfiles.write(line1)
                errd = errd +1
            elif grd < 0:
                dataerrorfiles.write(line1)
                errd = errd +1
            else:
                if (grd >= 900):
                    grade = 'A'
                    cnta = cnta + 1
                elif (grd >= 800):
                    grade = 'B'
                    cntb = cntb + 1
                elif (grd >= 700):
                    grade = 'C'
                    cntc = cntc + 1
                elif (grd >= 600):
                    grade = 'D'
                    cntd = cntd + 1
                elif (grd <= 599):
                    grade = 'F'
                    cntf = cntf + 1
                datagradfiles.write(idd+', '+nam+', '+str(grd)+', '+grade+'\n')
        except:
            dataerrorfiles.write(line1)
            errd = errd +1
        line1 = datagenfiles.readline()
        recd = recd + 1
            
    print('\n'+'Number of records read:'+ str(recd))
    print("Number of A's:",cnta)
    print("Number of B's:",cntb)
    print("Number of C's:",cntc)
    print("Number of D's:",cntd)
    print("Number of F's:",cntf)
    print('Number of graded records:',cnta+cntb+cntc+cntd+cntf)
    print('Number of error records:',errd)
    




main()
endtime = time.ctime()
print('\n'+'Program ended at: ',endtime)
datagenfiles.close()
datagradfiles.close()
dataerrorfiles.close()
