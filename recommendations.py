# This program deals with collaborative filtering.


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
            print "sum_of_squares = %d"%sum_of_squares
            sum_of_squares = sum_of_squares + pow(prefs_dict[p1][item] - prefs_dict[p2][item],2)
# Avoiding division by zero scenario
    score = 1/(1+sum_of_squares)
    print "Similarity score for the 2 %s and %s critics is %f"%(p1,p2,score)
    


# Testing the code
#sim_distance(critics,'Lisa Rose','Gene Seymour')

