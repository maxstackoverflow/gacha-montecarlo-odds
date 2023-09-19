from random import *

numberOfTrials = 100000
sizeOfRandom = 10000000

def calculateGachaOdds():
    totalString = ""
    for x in range (1, 30):
        masterList = []
        masterList.extend(calculateOldMain(x))
        masterList.extend(calculateOldIndividual(x))
        masterList.extend(calculateNewMain(x))
        masterList.extend(calculateNewMMOdds(x))
        masterList.extend(calculateAnniStepUp(x))
        rowString = ",".join(map(str, masterList))
        totalString = totalString + rowString + "\n"
    
    f = open("probability.csv", "a")
    f.write(totalString)

def calculateAnniStepUp(steps):
    numberOfFeatured = 1 if steps >= 6 else 0
    numberOfQuarterRolls = 10
    numberOfThirdRolls = 10 if steps >= 1 else 0
    numberOf5_12thRolls = 10 if steps >= 2 else 0
    numberOfHalfRolls = 0 if steps <= 3 else ((steps - 3) * 10) - 1
    
    listOfSuccesses = []
    
    for x in range (0, numberOfTrials):
        seed()
        successes = 0
        if numberOfFeatured > 0:
            successes = successes + getNumberOfSuccess(numberOfFeatured, 1/12)
        if numberOfQuarterRolls > 0:
            successes = successes + getNumberOfSuccess(numberOfQuarterRolls, 1/400)
        if numberOfThirdRolls > 0:
            successes = successes + getNumberOfSuccess(numberOfThirdRolls, 1/300)
        if numberOf5_12thRolls > 0:
            successes = successes + getNumberOfSuccess(numberOf5_12thRolls, 5/1200)
        if numberOfHalfRolls > 0:
            successes = successes + getNumberOfSuccess(numberOfHalfRolls, 1/200)
        
        listOfSuccesses.append(successes)
    
    atLeastOne = len(list(filter(lambda x: x >= 1, listOfSuccesses)))
    atLeastTwo = len(list(filter(lambda x: x >= 2, listOfSuccesses)))
    atLeastFive = len(list(filter(lambda x: x >= 5, listOfSuccesses)))
    average = sum(listOfSuccesses) / numberOfTrials
    probabilityOfOne = atLeastOne / numberOfTrials
    probabilityOfTwo = atLeastTwo / numberOfTrials
    probabilityOfFive = atLeastFive / numberOfTrials
    probabilities = [probabilityOfOne, probabilityOfTwo, probabilityOfFive, average]
    return probabilities

def calculateNewMMOdds(steps):
    numberOfGuarantees = 1 if steps >= 25 else 0
    numberOfNew = 2 if steps >= 20 else 1 if steps >= 10 else 0
    numberOfFeatured = 4 if steps >= 16 else 3 if steps >= 13 else 2 if steps >= 6 else 1 if steps >= 3 else 0
    numberOfMax = 0
    numberOfOnePercent = 0
    numberOfFlat = (steps * 10) - numberOfNew - numberOfFeatured
    
    return simulateForOddsOfNSuccess(numberOfGuarantees, numberOfNew, numberOfFeatured, numberOfMax, numberOfOnePercent, numberOfFlat)

def calculateOldIndividual(steps):
    numberOfGuarantees = 0
    numberOfNew = 0
    numberOfFeatured = 0
    numberOfMax = 5 if steps >= 25 else 4 if steps >= 20 else 3 if steps >= 15 else 2 if steps >= 10 else 1 if steps >= 5 else 0
    numberOfOnePercent = (steps * 10) - numberOfMax
    numberOfFlat = 0
    
    return simulateForOddsOfNSuccess(numberOfGuarantees, numberOfNew, numberOfFeatured, numberOfMax, numberOfOnePercent, numberOfFlat)

def calculateOldMain(steps):
    numberOfGuarantees = 0
    numberOfNew = 0
    numberOfFeatured = 5 if steps >= 25 else 4 if steps >= 20 else 3 if steps >= 15 else 2 if steps >= 10 else 1 if steps >= 5 else 0
    numberOfMax = 0
    numberOfOnePercent = 0
    numberOfFlat = (steps * 10) - numberOfFeatured

    return simulateForOddsOfNSuccess(numberOfGuarantees, numberOfNew, numberOfFeatured, numberOfMax, numberOfOnePercent, numberOfFlat)

def calculateNewMain(steps):
    numberOfGuarantees = 1 if steps >= 25 else 0
    numberOfNew = 0
    numberOfFeatured = 5 if steps >= 25 else 4 if steps >= 20 else 3 if steps >= 15 else 2 if steps >= 10 else 1 if steps >= 5 else 0
    numberOfMax = 0
    numberOfOnePercent = 0
    numberOfFlat = (steps * 10) - numberOfFeatured

    return simulateForOddsOfNSuccess(numberOfGuarantees, numberOfNew, numberOfFeatured, numberOfMax, numberOfOnePercent, numberOfFlat)

def simulateForOddsOfNSuccess(guaranteed, newDrop, featuredDrop, maxDrop, onePercentDrop, halfPercentDrop):
    listOfSuccesses = []
    
    for x in range (0, numberOfTrials):
        seed()
        successes = guaranteed
        if newDrop > 0:
            successes = successes + getNumberOfSuccess(newDrop, 1/3)
        if featuredDrop > 0:
            successes = successes + getNumberOfSuccess(featuredDrop, 1/9)
        if maxDrop > 0:
            successes = successes + getNumberOfSuccess(maxDrop, 1/5)
        if onePercentDrop > 0:
            successes = successes + getNumberOfSuccess(onePercentDrop, 1/100)
        if halfPercentDrop > 0:
            successes = successes + getNumberOfSuccess(halfPercentDrop, 1/200)
        
        listOfSuccesses.append(successes)
    
    atLeastOne = len(list(filter(lambda x: x >= 1, listOfSuccesses)))
    atLeastTwo = len(list(filter(lambda x: x >= 2, listOfSuccesses)))
    atLeastFive = len(list(filter(lambda x: x >= 5, listOfSuccesses)))
    average = sum(listOfSuccesses) / numberOfTrials
    probabilityOfOne = atLeastOne / numberOfTrials
    probabilityOfTwo = atLeastTwo / numberOfTrials
    probabilityOfFive = atLeastFive / numberOfTrials
    probabilities = [probabilityOfOne, probabilityOfTwo, probabilityOfFive, average]
    return probabilities
        

def getNumberOfSuccess(trials, odds):
    hits = 0
    for y in range (0, trials):
        randomNum = randrange(0, sizeOfRandom)
        if randomNum < (sizeOfRandom * odds):
            hits = hits + 1
    return hits
    

calculateGachaOdds()
