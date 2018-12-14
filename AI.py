import numpy as np
import math
from collections import defaultdict
from copy import deepcopy
import random
from collections import Counter
import itertools
numFeatures = 10

def Backwards_Elimination():


    return 0



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
        #print("Hey im in the first for loop")
        #print("This is i: {}".format(i))
        for j in range(0, len(featureList)):
            #print("This is j: {}".format(j))
            #print(confirmedData[i][featureList[j]
            #type(confirmedData[i][featureList[j])
            if (testData is not confirmedData[i]):
                euclidean_distance += ((float(confirmedData[i][featureList[j]]) - float(testData[featureList[j]])) ** 2)
            #print("The euclidean distance between feature {0} of {1} and feature {2} of {3} is {4}".format( featureList[j], confirmedData[i][featureList[j]], featureList[j], testData[featureList[j]], euclidean_distance))
            #print("the euclidean distance squared is {}".format(euclidean_distance))
            #print("The euclidean distance is {}".format(math.sqrt(euclidean_distance)))
            

        dict = {'classification': int(float(confirmedData[i][0])), 'ED': math.sqrt(euclidean_distance)}
        nearestNeighbors.append(dict)
        euclidean_distance = 0
        

    nearestNeighbors = sorted(nearestNeighbors, key = lambda i: i["ED"])

    

    #print(nearestNeighbors)
    nearestNeighbors = nearestNeighbors[0:numNeighbors]             

    #print(nearestNeighbors)

    successes = 0

    for i in range (0,len(nearestNeighbors)):

        if (nearestNeighbors[i]["classification"] == int(float(testData[0]))):
            #print(testData[0])
            if (nearestNeighbors[i]["ED"] is not 0):
                successes += 1

    success_rate = float(successes)/len(nearestNeighbors)
    #print(success_rate)

    #print(success_rate)



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
    #len(testData)i
    #while something idik
     
    for i in range(1, numFeatures + 1):
        for j in range(0,len(testData)):                            #change this back to [i]
            LIST.append(KNNAlgorithm(3,confirmedData, testData[j], [i]))
            #otherlist.appendorted(rates_list, key = lambda i: i["SR"])

        success_rate = sum(LIST)/len(LIST)
        #print(sum(LIST))
        #print(len(LIST))
        #print("The success rate for feature {0} seems to be {1}".format(i,success_rate))
        success_list.append({"Feature": int(i), "SuccessRate": success_rate})
        super_list.append(LIST)
        LIST.clear()


    success_list = sorted(success_list, key = lambda i: i["SuccessRate"])
    #print("The most successful feature is {0} with a success rate of {1}".format(success_list[-1]["Feature"],success_list[-1]["SuccessRate"])) 


    featureList = [success_list[-1]["Feature"]]

    

    #print(success_list)
    #print(featureList)
    return Forward_Selection_Helper(confirmedData, testData, featureList,False)

    
    '''
    
    for j in range(0, len(testData)):
        other_list.append(KNNAlgorithm(5,confirmedData,testData[j], [6,5,4]))


    print(sum(other_list))
    print(len(other_list))
    success_rate = sum(other_list)/len(other_list)
    print(success_rate)
    '''

    





    #for i in range(1, numFeatures + 1):
     #   for j in range(0, len(testData)):
      #      list.append(KNNAlgorithm(5,confirmedData, testData[j], bestFeatures.append(i))


       # list.clear()
        #success_list.append( {"Feature":"Success Rate":success_rate 
        




    #print(success_rate)


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
        #print("The success rate for {0} is {1}".format(featureList, success_rate))
        if(FLL + 1 == len(featureList)):
            toPush = {"FL":deepcopy(featureList), "SR":success_rate}
            rates_list.append(toPush)


        if(appended == True):
            featureList.pop()
            appended = False
        success_list.clear()        
    #print(rates_list)

    rates_list = sorted(rates_list, key = lambda i: i["SR"]) 

    #print(rates_list)


    if (not isSecondPass):
        return Forward_Selection_Helper(confirmedData, testData, rates_list[-1]["FL"], True)
    else:
        print(rates_list[-1])
        return rates_list[-1]







    #print(len(featureList))






'''
    LIST = []
    Features_And_Rates = []
    counter = 0
    featureList = list(set(featureList))
    for i in range(1, numFeatures + 1):
        featureList.append(i)
        featureList = list(set(featureList))
        for j in range(0, len(testData)):
            #print("Here is the feature list im about to send to the KNN algorithm {}".format(featureList))    
            LIST.append(KNNAlgorithm(5, confirmedData, testData[j],featureList))
            
            

        success_rate = sum(LIST)/len(LIST)
        print("The success rate for the features")
        for k in range(0, len(featureList)):
            print(featureList[k], end = ' ')

        print("is {}".format(success_rate))
        #f_l = tuple(featureList)


        #print(type(f_l))

        f_l = deepcopy(featureList)

        toPush = {"F_L":f_l, "Success_Rate":success_rate}
        
        #print("I am going to push toPush the dict. Its contents are {}".format(toPush))
        Features_And_Rates.append(toPush)
    




        featureList.pop()
        LIST.clear()
        #toPush.clear()




    #ogList = deepcopy(Features_And_Rates)

    Features_And_Rates = sorted(Features_And_Rates, key = lambda i: i["Success_Rate"])


    print("the most successful features seem to be {0} with a success rate of {1}".format(Features_And_Rates[-1]["F_L"], Features_And_Rates[-1]["Success_Rate"]))


    for i in range(0, len(Features_And_Rates)):

            Features_And_Rates[i]["F_L"] = list(set(Features_And_Rates[i]["F_L"]))


    print(Features_And_Rates)
    #print("Here is the OG list as well {}".format(ogList))
    if (sorted(Features_And_Rates[-1]["F_L"]) == sorted(featureList)):
        print(featureList)
        return featureList
    else:
        return Forward_Selection_Helper(confirmedData, testData, Features_And_Rates[-1]["F_L"])
        #print("First recrusive call")
        #print(featureList)
    print(Features_And_Rates)


    #nearestNeighbors = sorted(nearestNeighbors, key = lambda i: i[""])
'''









def main():
    filename = "CS170_SMALLtestdata__3.txt"
    file = open(filename, "r")
    #print(file.read())
    data = file.readlines()
    
    
    someDumbList = []
    anotherDumbList = []
    print(type(someDumbList))
    orgData = []
    for line in data:
        orgData.append(line.split())
        #print("hi")



    organizedData = np.asarray(orgData)
    print(len(orgData))
    #print(len(organizedData))

    organizedData = organizedData.transpose()
    print(len(organizedData))
    
    #print(organizedData[0])
    print("This is the data we are testing against")
    print(orgData[0])
    print("Here are the results")


    confirmedData = [orgData[1],orgData[2], orgData[3], orgData[4], orgData[5], orgData[6]]

    
    #figure out how to partition the data
    counter = 0
         
    while(counter < 50):
        random.shuffle(orgData)


        firstFifth = int(len(orgData)/3 )
        print(firstFifth)
    
        confirmedData = orgData[0:firstFifth]

    #print(confirmedData)

        testData = orgData[firstFifth + 1: (len(orgData)) - 1]
    #print(testData)

        toPush = Forward_Selection(confirmedData,testData)

        someDumbList.append(toPush["FL"])
        anotherDumbList.append(toPush)

        counter += 1
    #KNNAlgorithm(2,confirmedData, testData, [1])
    
    #print(Counter(map(tuple, someDumbList)))
    #print()
        anotherDumbList = sorted(anotherDumbList, key = lambda i: i["SR"])
        print(anotherDumbList)
    '''
    random.shuffle(orgData)
    #firstFifth = int(len(orgData)/3)
    #confirmedData = orgData[0:firstFifth]
    #testData = orgData[firstFifth + 1: (len(orgData))]
    confirmedData = orgData
    testData = orgData
    toPush = Forward_Selection(confirmedData, testData)
    '''








if __name__=="__main__":
    main()
