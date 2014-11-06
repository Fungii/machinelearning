# This program deals with collaborative filtering.
<<<<<<< HEAD
# Chapter 2 : Programming Collective Intelligence
=======

from math import sqrt
>>>>>>> 17b2ab9efd38cc4462b47a33ee0eb75148585589

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
    print "Euclidean similarity score for the 2 %s and %s critics is %f"%(p1,p2,score)
    


# Testing the code
sim_distance(critics,'Lisa Rose','Gene Seymour')

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
    print "Pearson score for critics %s and %s is %f \n"%(p1,p2,r)
#Testing pearson code
sim_pearson(critics,'Lisa Rose','Gene Seymour')
