import header as h
import time #To convert epoch to the usual time

#Take data from the SN.log (Global data base)
with open("input/SN.log", "r") as f:
    for line in f:
        if line[0] == 'U':
            splitted_line = line.split(" ")
            h.SerNums_in_DB += [int(splitted_line[4])]
            h.EQIPMENT_IDs += [splitted_line[2]]

#Function, that returns command to load the datat
def write_one_value_to_log(SN, field, value):
      return 0

#Take data from the product of Analyze.cxx
with open("/afs/cern.ch/user/i/ibordule/prod/DB_creator/output/summary/log_to_global/globalLog.txt", "r") as f:
    for line in f:
        if line[0] != 'S': #not for the first line (header)
            
            splitted_line = line.split("\t")
            h.SN += [int(splitted_line[0])]
            h.Status += [int(splitted_line[1])]
            h.PartID += [splitted_line[2]]
            h.FPGAver += [splitted_line[3]]
            h.NegTime += [int(splitted_line[4])] #Epoch
            h.NegDeadChCount += [int(splitted_line[5])]
            # Then we have extra \t
            h.NegStatus += [int(splitted_line[7])]
            # extra \t
            h.NegBoardID += [int(splitted_line[9])]
            # extra \t
            if splitted_line[11] != '\n': #if the positive mode results exist 
                 h.PosTime += [int(splitted_line[11])] #Epoch
                 h.PosDeadChCount += [int(splitted_line[12])]
                 # extra \t
                 h.PosStatus += [int(splitted_line[14])]
                 # extra \t
                 h.PosBoardID += [int(splitted_line[16])] #except \n
                 #print splitted_line[16] #except \n
            else:  #if there is no positive mode result
                 h.PosTime += ['-']
                 h.PosDeadChCount += ['-']
                 h.PosStatus +=  ['-']
                 h.PosBoardID += ['-']

with open("output/log_to_DB.txt", "w") as f:
    for i in range(0, len(h.SerNums_in_DB)): #for all chips, that have already registered in Global base
        flag_founded = 0
        if h.SerNums_in_DB[i] > 99999: #Correct the numbers of SN
            while h.SerNums_in_DB[i] > 99999:
                h.SerNums_in_DB[i] = h.SerNums_in_DB[i] - 100000
        for j in range(0, len(h.SN)): #Search for this SN in the local DB
            if h.SerNums_in_DB[i] == h.SN[j]: #If the chip is founded
                # Write in the Global Base...
                # general Status of the chip
                """
                if h.Status[j] == 4:
                    StatusText = "Perfect"
                if h.Status[j] == 3:
                    StatusText = "PerfectNeg"
                if h.Status[j] == 2:
                    StatusText = "PerfectPos"
                if h.Status[j] == 1:
                    StatusText = "Passed"
                if h.Status[j] == 0:
                    StatusText = "Failed"
                """
                #f.write("--aItem VMM3_STATUS_TSU " + h.EQIPMENT_IDs[i] + " " + StatusText + " T" + "\n")
                # Part Id of the chip
                #f.write("--aItem VMM3_PARTYNUMBER_TSU " + h.EQIPMENT_IDs[i] + " " + h.PartID[j] + " T" + "\n")
                #f.write("--aItem VMM3_FPGAver_TSU " + h.EQIPMENT_IDs[i] + " " + h.FPGAver[j] + " T" + "\n")
                #f.write("--aItem VMM3_Time_NEG_TSU " + h.EQIPMENT_IDs[i] + " " + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(h.NegTime[j])) + " T" + "\n")
                #if h.PosTime[j] != '-':
                #    f.write("--aItem VMM3_Time_POS_TSU " + h.EQIPMENT_IDs[i] + " " + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(h.PosTime[j])) + " T" + "\n")
                #f.write("--aItem VMM3_DeadChCount_NEG_TSU " + h.EQIPMENT_IDs[i] + " " + str(h.NegDeadChCount[j]) + " T" + "\n")
                #if h.PosDeadChCount[j] != '-':
                #    f.write("--aItem VMM3_DeadChCount_POS_TSU " + h.EQIPMENT_IDs[i] + " " + str(h.PosDeadChCount[j]) + " T" + "\n")
                #if h.NegStatus[j] == 2:
                #    StatusText = "Perfect_Neg"
                #if h.NegStatus[j] == 1:
                #    StatusText = "Passed_Neg"
                #if h.NegStatus[j] == 0:
                #    StatusText = "Failed_Neg"
                #f.write("--aItem VMM3_STATUS_NEG_TSU " + h.EQIPMENT_IDs[i] + " " + StatusText + " T" + "\n")
                """if h.PosStatus[j] == 2:
                    StatusText = "Perfect_Pos"
                if h.PosStatus[j] == 1:
                    StatusText = "Passed_Pos"
                if h.PosStatus[j] == 0:
                    StatusText = "Failed_Pos"
                if h.PosStatus[j] == '-':
                    StatusText = "Not_defined"
                f.write("--aItem VMM3_STATUS_POS_TSU " + h.EQIPMENT_IDs[i] + " " + StatusText + " T" + "\n")"""
                #f.write("--aItem VMM3_BOARD_ID_NEG_TSU " + h.EQIPMENT_IDs[i] + " " + str(h.NegBoardID[j]) + " T" + "\n")
                if h.PosBoardID[j] != '-':
                    f.write("--aItem VMM3_BOARD_ID_POS_TSU " + h.EQIPMENT_IDs[i] + " " + str(h.PosBoardID[j]) + " T" + "\n")
                

                 
 

"""
with open("/input/SN.log", "r") as f:
    for line in f:
        splitted_line = line.split("\t")
        if line[0] != 'E':  #If this is not a first line
            counter += 1
            h.EQIPMENT_IDs += [splitted_line[0]] 
            h.OTHER_IDs += [splitted_line[2]]
            h.MTF_IDs += [splitted_line[3]]
            h.SerNums += [splitted_line[4]]
            if splitted_line[5] == "":
                h.Correct_OTHER_IDs += [splitted_line[6]]
                h.Correct_SerNums += [splitted_line[7][:-1]] #The last symbol is \n
            else:
                h.Correct_OTHER_IDs += [splitted_line[5]]
                h.Correct_SerNums += [splitted_line[6][:-1]] #The last symbol is \n

with open("new_list.txt", "w") as f:
    f.write('EQIPMENT_ID\tOTHER_ID\tMTF_ID\t\tSerNum\t\tCorrect_OTHERID\tCorrect_SerNum\tDuplicates\tRemove_or_Keep\n')

#Calculate dupes
    for i in range(0, len(h.OTHER_IDs)):
        Number_of_dupes = 0;
        for j in range(0, len(h.OTHER_IDs)):
            if (i != j) and (h.Correct_OTHER_IDs[i] == h.Correct_OTHER_IDs[j]):
                Number_of_dupes += 1
        h.Dupes += [Number_of_dupes]
#Decide, which dupe we will keep in base, and which we will remove. See the rule.
    for i in range(0, len(h.Dupes)):
        if h.Dupes[i] != 0:
            for j in range(0, len(h.Correct_OTHER_IDs)): #Look again for all Dupes of this chip
                if (h.Correct_OTHER_IDs[i] == h.Correct_OTHER_IDs[j]) and (i != j): #If we found one
                    if i < j: # And it is first in our list
                        h.Remove_or_Keep += ['K'] #we will keep it
                        break
                    else:
                        h.Remove_or_Keep += ['R'] #... remove it
                        break
        else: # if this chip has no Dupes
            h.Remove_or_Keep += ['K']
        f.write(h.EQIPMENT_IDs[i] +  "\t\t" + h.OTHER_IDs[i] + "\t" + h.MTF_IDs[i] + "\t" + h.SerNums[i] + "\t\t" + h.Correct_OTHER_IDs[i] + "\t" + h.Correct_SerNums[i] + "\t\t" + str(h.Dupes[i]) + "\t\t" + h.Remove_or_Keep[i] + "\n")   """ 
