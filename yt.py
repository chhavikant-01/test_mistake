''' PROBLEM STATEMENT
A series of workshops are held during the semester breaks by IIT Madras. Each workshop is attended by a certain number of students. Each person is identified by his or her roll number which stays constant across all the workshops.
Each workshop is represented by a list of roll numbers of the attendees. Your task is to find the set of students (roll numbers) who have attended all the workshops. If there is no student who has attended every single workshop, then return an empty set.

Write a function named social that accepts a list of lists named workshops. Each element of workshops corresponds to a workshop,
which is a list of roll numbers of students who have attended it. Return the set of students who have attended every one of these workshops.

Note:- You do not have to accept input from the user or print output to the console. You just have to write the function definition.
'''

def social (workshops):
    if len(workshops)==1:
        return set(workshops[0])
    if len(workshops)==0:
        return {}
    else:
        L = []
        for i in range(len(workshops[0])):
            if workshops[0][i] in workshops[1]:
                L.append(workshops[0][i])
        workshops.remove(workshops[0])
        workshops.remove(workshops[0])
        if L!=[]:
            workshops = [L] + workshops
            return social(workshops)