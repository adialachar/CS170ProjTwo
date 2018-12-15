import numpy as np
import math
from collections import defaultdict
from copy import deepcopy
import random
from collections import Counter
import itertools
numFeatures = 10

def Backwards_Elimination(confirmedData, testData):
    
    featureList = []
    rates_list = []
    success_list = []
    featureListCopy = []
    for i in range(1, numFeatures + 1):
        featureList.append(i)
        #featureListCopy.append(i)

    featureListCopy = deepcopy(featureList)
    print("This is the featureList copy")
    print(featureListCopy)
    currNumFeatures = deepcopy(len(featureList))

    for i in range(0, currNumFeatures):
        featureList.remove(featureList[i])
        print("Feature {} should be removed from the list below".format(i+1))
        print(featureList)
        for j in range(0, len(testData)):

            #currFeature = deepcopy(featureList[i])
            
            
            rates_list.append(KNNAlgorithm(3, confirmedData, testData[j], featureList))
            
        SR = sum(rates_list)/len(rates_list)

        success_list.append({"Feature": featureList , "SuccessRate": SR})
        rates_list.clear()
        featureList = deepcopy(featureListCopy)
        print("this lis {0} and this list {1} should be the same right now".format(featureList, featureListCopy))


    #print(success_list) 

    success_list = sorted(success_list, key = lambda i: i["SuccessRate"])
    print(success_list)
    return Backwards_Elimination_Helper(confirmedData, testData, success_list[-1]["Feature"])

    
def Backwards_Elimination_Helper(confirmedData, testData, featureList):
    
    currNumFeatures = deepcopy(len(featureList))
    featureListCopy = deepcopy(featureList)
    success_list = []
    rates_list = []

    for i in range(0, currNumFeatures):
        featureList.remove(featureList[i])
        for j in range(0, len(testData)):
            rates_list.append(KNNAlgorithm(3, confirmedData, testData[j], featureList))

        SR = sum(rates_list)/len(rates_list)
        success_list.append({"Feature": featureList, "SuccessRate": SR})
        rates_list.clear()
        featureList = deepcopy(featureListCopy)




    success_list = sorted(success_list, key = lambda i: i["SuccessRate"])
    print(success_list)

    best = success_list[-1]
    if (len(best["Feature"]) == 3):
        print(best)
        return best
    else:
        return Backwards_Elimination_Helper(confirmedData, testData, best["Feature"])
        




def Your_Own_Algorithm(confirmedData, testData):

    #if the number of failures is ever greater than the ratio (1 - sum of first list), break, and iterate to the next one on the list
    #and then figure out how to move all the problem datasets so that the next recursive call or next test of the feature h
        LIST = []
        success_list = []
        other_list = []
        feat = [1,2,6]
        super_list = []
        someDumbBool = False
        curr_num_failures = 0
        least_fails_so_far = math.inf
        list_of_bad_inputs = []
        list_of_bad_indexes = []
        for i in range(1, numFeatures + 1):
            for j in range(0,len(testData)):                            #change this back to [i]
                toPush = KNNAlgorithm(3,confirmedData, testData[j], [i])
                if (toPush == 0):
                    curr_num_failures += 1
                    list_of_bad_inputs.append(testData[j])
                    list_of_bad_indexes.append(j)
                if(curr_num_failures > least_fails_so_far):
                    print("Current number of failures for feature {0}, which is {1}, has exceeded the least so far, which is {2}".format(i,curr_num_failures, least_fails_so_far))
                    print("hii")
                    someDumbBool = True
                    break
                LIST.append(toPush)
                
                
            if(not someDumbBool):
                print("hi")
                least_fails_so_far = deepcopy(curr_num_failures)
                success_rate = sum(LIST)/len(LIST)
                curr_num_failures = 0
                success_list.append({"Feature": int(i), "SuccessRate": success_rate})
                super_list.append(LIST)
                LIST.clear()





            else:
                print("hello")
                curr_num_failures = 0
                someDumbBool = False
                
                                                                                        

        success_list = sorted(success_list, key = lambda i: i["SuccessRate"])
                                                                
        featureList = [success_list[-1]["Feature"]]
        print(featureList)

        print(success_list)

        list_o = list(set(list_of_bad_indexes))

        print(list(set(list_of_bad_indexes)))
        print(list_o)

        print(len(list_o))
        #print(list_of_bad_inputs)
        list_for_new_stuff = []
        for k in range(0, len(list_o)):
            #print(testData[list_of_bad_indexes[i]])
            #print("About to remove index {} from the list".format(
            list_for_new_stuff.append(testData[list_o[k]])
            #testData.remove(testData[list_o[k]])
            #del testData[list_o[i]]
            print("hi") 
            #print(list_of_bad_indexes[i])
        
        

        for k in range(0, len(list_o)):
            testData.remove(list_for_new_stuff[k])
            print("bye")




        print(len(testData))
        testData = list_for_new_stuff + testData
        print(len(testData))
        return Your_Own_Algorithm_Helper(confirmedData, testData, featureList, False)



def Your_Own_Algorithm_Helper(confirmedData, testData,featureList, isSecondPass):

    FLL = deepcopy(len(featureList))

    featureList = list(set(featureList))
    success_list = []
    rates_list = []
    appended = False
    featuresToCompare = []
    curr_num_failures = 0
    least_failures_so_far = math.inf
    someDumbBool = False
    list_of_bad_indexes = []

    for i in range(1, numFeatures + 1):
        featuresToCompare.append(i)

        featuresToCompare = list(set(featuresToCompare) - set(featureList))




    for i in range(0, len(featuresToCompare)):
        if (featuresToCompare[i] not in featureList):
            featureList.append(featuresToCompare[i])
            appended = True
        for j in range(0, len(testData)):

            toPush = KNNAlgorithm(3,confirmedData, testData[j], featureList)

            if (toPush == 0):
                curr_num_failures += 1
                list_of_bad_indexes.append(j)
            if (curr_num_failures > least_failures_so_far):
                print("Curernt number of failures of feature {0} is {1}, which is greater than {2}".format(featureList, curr_num_failures, least_failures_so_far))
                someDumbBool = True
                break
            success_list.append(toPush)

        if(not someDumbBool):
            success_rate = sum(success_list)/len(success_list)
            least_failures_so_far = deepcopy(curr_num_failures)
            curr_num_failures = 0
            if(FLL + 1 == len(featureList)):
                toPush = {"FL":deepcopy(featureList), "SR":success_rate}
                rates_list.append(toPush)
            print("hi")
        else:
            curr_num_failures = 0
            someDumbBool = False
            print("hello")

        if(appended == True):
            featureList.pop()
            appended = False
        
        
        success_list.clear()    
        
        
        
    list_o = list(set(list_of_bad_indexes))
    list_for_new_stuff = []

    print(list_o)


    for k in range(0, len(list_o)):
        list_for_new_stuff.append(testData[list_o[k]])


    for l in range(0, len(list_for_new_stuff)):
        testData.remove(list_for_new_stuff[l])

    print(len(testData))
    testData = list_for_new_stuff + testData
    print(len(testData))

        
        
    rates_list = sorted(rates_list, key = lambda i: i["SR"])
    print(rates_list)
    if (not isSecondPass):
        return Your_Own_Algorithm_Helper(confirmedData, testData, rates_list[-1]["FL"], True)
    else:
        print(rates_list[-1])
        return rates_list[-1]






















def KNNAlgorithm(numNeighbors, confirmedData, testData, featureList):

    #confirmedData is a 2D array
    #testData is a single point, or a 1D array with all of its traits

    #the object here is to return the K nearest neighbors of a single point
    #print("Hello its me KNN")

    if(numNeighbors % 2 == 0):
        numNeighbors += 1

    euclidean_distance = 0


    
    nearestNeighbors = []
    euclidean_distance = 0

    for i in range(0, len(confirmedData)):
        for j in range(0, len(featureList)):
            
            if (testData is not confirmedData[i]):
                euclidean_distance += ((float(confirmedData[i][featureList[j]]) - float(testData[featureList[j]])) ** 2)
            
            
        dict = {'classification': int(float(confirmedData[i][0])), 'ED': math.sqrt(euclidean_distance)}
        nearestNeighbors.append(dict)
        euclidean_distance = 0
        

    nearestNeighbors = sorted(nearestNeighbors, key = lambda i: i["ED"])

    

    
    nearestNeighbors = nearestNeighbors[0:numNeighbors]             

    successes = 0

    for i in range (0,len(nearestNeighbors)):

        if (nearestNeighbors[i]["classification"] == int(float(testData[0]))):
        
            if (nearestNeighbors[i]["ED"] is not 0):
                successes += 1

    success_rate = float(successes)/len(nearestNeighbors)

    if (success_rate > 0.5):

        return 1
    else:
        return 0




def Forward_Selection(confirmedData, testData):

    #first take all of the individual traits, then take the best rate. 
    LIST = []
    success_list = []
    other_list = []
    feat = [1,2,6]
    super_list = []
    
     
    for i in range(1, numFeatures + 1):
        for j in range(0,len(testData)):                            #change this back to [i]
            LIST.append(KNNAlgorithm(3,confirmedData, testData[j], [i]))
    

        success_rate = sum(LIST)/len(LIST)
    
        success_list.append({"Feature": int(i), "SuccessRate": success_rate})
        super_list.append(LIST)
        LIST.clear()


    success_list = sorted(success_list, key = lambda i: i["SuccessRate"])
    
    featureList = [success_list[-1]["Feature"]]

    return Forward_Selection_Helper(confirmedData, testData, featureList,False)


def Forward_Selection_Helper(confirmedData, testData, featureList, isSecondPass):


    FLL = deepcopy(len(featureList))

    featureList = list(set(featureList))
    success_list = []
    rates_list = []
    appended = False
    featuresToCompare = []


    for i in range(1, numFeatures + 1):
        featuresToCompare.append(i)

    featuresToCompare = list(set(featuresToCompare) - set(featureList))




    for i in range(0, len(featuresToCompare)):
        if (featuresToCompare[i] not in featureList):
            featureList.append(featuresToCompare[i])
            appended = True
        for j in range(0, len(testData)):

            success_list.append(KNNAlgorithm(1,confirmedData, testData[j], featureList))
                

        
        success_rate = sum(success_list)/len(success_list)
        
        if(FLL + 1 == len(featureList)):
            toPush = {"FL":deepcopy(featureList), "SR":success_rate}
            rates_list.append(toPush)


        if(appended == True):
            featureList.pop()
            appended = False
        success_list.clear()        
    

    rates_list = sorted(rates_list, key = lambda i: i["SR"]) 

    


    if (not isSecondPass):
        return Forward_Selection_Helper(confirmedData, testData, rates_list[-1]["FL"], True)
    else:
        print(rates_list[-1])
        return rates_list[-1]







def main():
    filename = "CS170_SMALLtestdata__3.txt"
    file = open(filename, "r")
    data = file.readlines()
    
    
    someDumbList = []
    anotherDumbList = []
    print(type(someDumbList))
    orgData = []
    for line in data:
        orgData.append(line.split())
        



    organizedData = np.asarray(orgData)
    

    organizedData = organizedData.transpose()
    numFeatures = len(organizedData)
    
    

    

    
    random.shuffle(orgData)
    confirmedData = orgData
    testData = orgData
    toPush = Your_Own_Algorithm(confirmedData, testData)
    








if __name__=="__main__":
    main()
