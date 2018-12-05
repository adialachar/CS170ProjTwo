import numpy as np
import math

numFeatures = 10

def Parsing():


    return 0



def KNNAlgorithm(numNeighbors, confirmedData, testData, featureList):

    #confirmedData is a 2D array
    #testData is a single point, or a 1D array with all of its traits

    #the object here is to return the K nearest neighbors of a single point
    #print("Hello its me KNN")

    if(numNeighbors % 2 == 0):
        numNeighbors += 1


    nearestNeighbors = []
    euclidean_distance = 0

    for i in range(0, len(confirmedData)):
        #print("Hey im in the first for loop")
        for j in range(0, len(featureList)):

            #print(confirmedData[i][featureList[j]
            #type(confirmedData[i][featureList[j])
            euclidean_distance += ((float(confirmedData[i][featureList[j]]) - float(testData[featureList[j]])) ** 2)
            #print("The euclidean distance between feature one of {0} and feature one of {1} is".format( confirmedData[i][featureList[j]], testData[featureList[j]]))
            #print("the euclidean distance squared is {}".format(euclidean_distance))
            #print("The euclidean distance is {}".format(math.sqrt(euclidean_distance)))
            

        dict = {'classification': confirmedData[i][0], 'ED': math.sqrt(euclidean_distance)}
        nearestNeighbors.append(dict)
        euclidean_distance = 0
        

    nearestNeighbors = sorted(nearestNeighbors, key = lambda i: i["ED"])

    

    #print(nearestNeighbors)
    nearestNeighbors = nearestNeighbors[0:numNeighbors]             

    #print(nearestNeighbors)

    successes = 0

    for i in range (0,len(nearestNeighbors)):

        if (nearestNeighbors[i]["classification"] == testData[0]):
            #print(testData[0])
            successes += 1

    success_rate = float(successes)/len(nearestNeighbors)
    #print(success_rate)

    if (success_rate > 0.5):

        return 1
    else:
        return 0




def Forward_Selection(confirmedData, testData):

    #first take all of the individual traits, then take the best rate. 
    list = []
    success_list = []
    other_list = []
    #len(testData)i
    #while something idk
    for i in range(1, numFeatures + 1):
        for j in range(0,len(testData)): 
            list.append(KNNAlgorithm(5,confirmedData, testData[j], [i]))
            #otherlist.append(

        success_rate = sum(list)/len(list)
        print("The success rate for feature {0} seems to be {1}".format(i,success_rate))
        list.clear()



    #for i in range(1, numFeatures + 1):
     #   for j in range(0, len(testData)):
      #      list.append(KNNAlgorithm(5,confirmedData, testData[j], bestFeatures.append(i))


       # list.clear()
        #success_list.append( {"Feature":"Success Rate":success_rate 
        




    #print(success_rate)


def main():
    filename = "CS170_SMALLtestdata__3.txt"
    file = open(filename, "r")
    #print(file.read())
    data = file.readlines()
    
    


    orgData = []
    for line in data:
        orgData.append(line.split())
        #print("hi")



    organizedData = np.asarray(orgData)

    organizedData = organizedData.transpose()


    #print(organizedData[0])
    print("This is the data we are testing against")
    print(orgData[0])
    print("Here are the results")


    confirmedData = [orgData[1],orgData[2], orgData[3], orgData[4], orgData[5], orgData[6]]

    
    #figure out how to partition the data

    firstFifth = int(len(orgData)/5 )
    print(firstFifth)
    
    confirmedData = orgData[0:firstFifth]

    #print(confirmedData)

    testData = orgData[firstFifth + 1: (len(orgData)) - 1]
    #print(testData)

    Forward_Selection(confirmedData,testData)
    
    #KNNAlgorithm(2,confirmedData, testData, [1])

    



if __name__=="__main__":
    main()
