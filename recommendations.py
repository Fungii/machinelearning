# This program deals with collaborative filtering.
# Chapter 2 : Programming Collective Intelligence

from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

# Calculates the eucliden distance between 2 critcs for their shared movie ratings.
def sim_distance(prefs_dict,p1,p2):
    si = {}
    for item in prefs_dict[p1]:
        if item  in prefs_dict[p2]:
            si[item] =1
    if (len(si) == 0):
        print "Citics %s and %s do not have any common movies among them"%(p1,p2)
        return 0
# Computing scores
    sum_of_squares = 0
    for item in prefs_dict[p1]:
        if item in prefs_dict[p2]:
            sum_of_squares = sum_of_squares + pow(prefs_dict[p1][item] - prefs_dict[p2][item],2)
# Avoiding division by zero scenario
    score = 1/(1+sum_of_squares)
    return score
    



# Function to calculate pearson coefficient
def sim_pearson(prefs,p1,p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] =1
   
    if (len(si) == 0):
        print "No review common to %s and %s \n"%(p1,p2)
        return 0
    n = len(si)
    sum1 = sum(prefs[p1][item] for item in si)
    sum2 = sum(prefs[p2][item] for item in si)

    sumsq1 = sum(pow(prefs[p1][item],2) for item in si)
    sumsq2 = sum(pow(prefs[p2][item],2) for item in si)

    pSum = sum(prefs[p1][item]*prefs[p2][item] for item in si)

    num = pSum - (sum1*sum2/n)
    den = sqrt((sumsq1 - pow(sum1,2)/n)*(sumsq2 - pow(sum2,2)/n))
    if den ==0 : return 0
    r = num/den
    return r


#Function to rank critics
def rank_critics(prefs,p1,similarity=sim_pearson):
    scores = []
    for person in prefs:
        if person == p1: continue
        scores.append((similarity(prefs,person,p1),person))
    scores.sort()
    scores.reverse()
    return scores

def getRecommendations(prefs,person,similarity=sim_pearson):
    total = {}
    simSum = {}
    recommendations = {}
    result = []
    
    #Loop through the main dict
    for others in prefs:
        if others == person:continue # Not comparing with self
        sim = similarity(prefs,person,others)
        if sim <= 0 : continue
        for items in prefs[others]:
            if items in prefs[person]:continue # Avoiding getting reccos for movies already seen
            total.setdefault(items,0)
            total[items]+=prefs[others][items]*sim
            simSum.setdefault(items,0)
            simSum[items]+=sim

    #Ceating recommendation list
    for items in total:
        recommendations[items] = total[items]/simSum[items]
    for items in recommendations:
        result.append((items,recommendations[items]))
    return result

# Function to invert dictionary
def transformDict(prefs):
    invert = {}
    for person in prefs:
        for item in prefs[person]:
            invert.setdefault(item,{})
            invert[item][person] = prefs[person][item]

    return invert


#Earlier methods compared user against user but this method is not scalable to large number of users.
#Item based filtering calculates similarity between items and not users.
def itemBasedFiltering(prefs):
    result = {}
    itemPrefs = transformDict(prefs)

    for item in itemPrefs:
        scores = rank_critics(itemPrefs,item,sim_distance)
        result[item] = scores

    return result


# Now we write a function to get user recommendations by item based filtering.
def itemRecommendations(prefs,user):
    itemMatch = itemBasedFiltering(prefs) # Building item based similarity database
    userPrefs = prefs[user]
    result = []
    totalSim = {}
    scores = {}
    for (items,ratings) in userPrefs.items():
        for (similarity,item2) in itemMatch[items]:
            if item2 in userPrefs: continue
            scores.setdefault(item2,0)
            totalSim.setdefault(item2,0)
            scores[item2] += similarity*ratings;
            totalSim[item2] += similarity
    #Creating final score list
    for items in scores:
        result.append((items,scores[items]/totalSim[items]))
    return result
