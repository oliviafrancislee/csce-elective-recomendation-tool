import pprint
import math
import os, sys
import re
import matplotlib.pyplot as plt

#get tracked elective list data and clean
def clean_tracked_elective_list():
    f = open("data/tracked_elective_list.txt", "r")

    tracked_elective_list_dict = {}
    line = f.readline().strip()
    track = line.split(": ")[1].strip()
    tract_dict = {}

    line = f.readline().strip()
    while line != "":
        if line.startswith("Track"):
            tracked_elective_list_dict[track] = tract_dict
            track = line.split(": ")[1].strip()
            tract_dict = {}
        elif line == "Untracked":
            tracked_elective_list_dict[track] = tract_dict
            track = "Untracked"
            tract_dict = {}
        elif "CSCE" in line:
            if line.split("CSCE")[0] == "":
                (id, name) = line.split("CSCE")[1].split(maxsplit=1)
                tract_dict[("CSCE "+id, name)] = ()
        line = f.readline().strip()
    tracked_elective_list_dict[track] = tract_dict
    f.close()
    return tracked_elective_list_dict





#get course_catalog data and clean
def clean_course_catalog_data():
    file_path = "data/course_catalog.txt" #path to the course catalog file
    #Read in the course catalog file
    with open(file_path, 'r') as file:
        #lines is a list of strings where each string is a line in the file
        lines = file.readlines() #get all the lines in the file and place them in a list

    course_catalog = {}
    course_name = None
    course_description = None

    #concatenante the values in lines from line[0] till a value '\n' is found
    for line in lines[0:]: #iterate through the lines in the course catalog
        if line == '\n': 
            #if the line is empty, add the course name and description to the course catalog
            course_catalog[course_name] = course_info
            course_name = None
            course_description = None
        elif course_name is None: 
            #if the course name is not set, set the course name to the current line
            course_name = line.strip()
        else:
            strip_line = line.strip()
            #if the course name is set, set the course description to the current line
            course_description = strip_line.split("Prerequisite")[0]
            split_tuple = re.split(r'(?<=ours.) |(?<=our.)', course_description)
            credit_list = []
            for i in range(len(split_tuple)-1):
                credit_list.append(split_tuple[i])
            course_info = ("".join(credit_list), split_tuple[len(split_tuple)-1])
    return course_catalog


# add course catalog descriptions to tracked elective list dictionary
def clean():
    tracked_elective_list_dict = clean_tracked_elective_list()
    course_catalog = clean_course_catalog_data()
    for key in tracked_elective_list_dict.keys():
        for (course_id, course_name) in tracked_elective_list_dict[key].keys():
            for course in course_catalog.keys():
                if course_id in course:
                    tracked_elective_list_dict[key][(course_id, course_name)] = course_catalog[course]

    tracked_elective_list_dict['Systems'].pop(('CSCE 456', 'Real-Time Computing'))   #returns a dictionary of track key values parodied with sub-dictionary of course_id and course_name as a key paired to a tuple of course credit and course description
    return tracked_elective_list_dict




#call lengths function to get the average lengths of all documents title and body
# add up all the lengths for the body and title separately and divide by the number of documents
def totalAvgDocLen():
    doc_Lengths = docLengths() #get the document lengths
    avgTitleLen = 0
    avgBodyLen = 0
    
    #add up all the lengths for the body and title separately and divide by the number of documents
    for doc in doc_Lengths.keys(): #for each document in the document lengths dictionary
        avgTitleLen += doc_Lengths[doc]['title'] #add the title length to the average title length
        avgBodyLen += doc_Lengths[doc]['body'] #add the body length to the average body length
    
    #divide the total title length by the number of documents to get the average title length
    avgTitleLen = avgTitleLen/len(doc_Lengths)
    #divide the total body length by the number of documents to get the average body length
    avgBodyLen = avgBodyLen/len(doc_Lengths)

    return {'title' : avgTitleLen, 'body' : avgBodyLen}

    
#lengths function to get lengths of all documents title and body.
def docLengths():
    #get the cleaned tracked elective list dictionary
    tracked_elective_list_dict = clean() 

    #make a dictionary of document titles keys paired to a dictionary of title length and body length
    #doc_lengths = {
                    # ('CSCE 456', 'Real-Time Computing'): zone_lengths = {
                    #                                          'title': 2, 
                    #                                          'body': 100 }, 
                    # ('CSCE 470', 'Info Ret'): zone_lengths = {              
                    #                                          'title': 2, 
                    #                                          'body': 100 }
                    # }

    doc_lengths = {}
    for track in tracked_elective_list_dict.keys(): #for each track in the tracked elective list dictionary
        for (course_id, course_name) in tracked_elective_list_dict[track].keys(): #for each course in the track (each key in the sub-dictionary) iterate through the titles
            
            zone_lengths = {}

            #calculate the length of the course title
            title_length = len(course_name.split()) #split the course name into words
            #calculate the length of the course description
            body_length = len(tracked_elective_list_dict[track][(course_id, course_name)][1].split()) #get the course description and split it into words

            #add the title and body length to the zone_lengths dictionary
            zone_lengths["title"] = title_length
            zone_lengths["body"] = body_length

            #add the zone_lengths dictionary to the doc_lengths dictionary
            doc_lengths[(course_id, course_name)] = zone_lengths

    return doc_lengths


