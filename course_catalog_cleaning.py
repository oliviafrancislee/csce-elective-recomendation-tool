import math
import os, sys
import re
import pprint
""" 
f = open("data/course_catalog.txt", "r")

course_catalog_dict = {}

line = f.readline()

while line != "":
    print(line)
    line = f.readline()

    if line == "\n":
        course_name = f.readline().strip()
        course_description = f.readline().strip()
        course_catalog_dict[course_name] = course_description

f.close()
 """
file_path = "data/course_catalog.txt" #path to the course catalog file
#Read in the course catalog file
with open(file_path, 'r') as file:
    #lines is a list of strings where each string is a line in the file
    lines = file.readlines() #get all the lines in the file and place them in a list


course_catalog = {}
course_name = None
course_description = None

#save lines[0] as the first key in the dictionary 
#course_catalog[lines[0]] = []

#concatenante the values in lines from line[0] till a value '\n' is found
for line in lines[0:]: #iterate through the lines in the course catalog
    #print(line)
    if line == '\n': 
        #if the line is empty, add the course name and description to the course catalog
        course_catalog[course_name] = course_description
        course_name = None
        course_description = None
    elif course_name is None: 
        #if the course name is not set, set the course name to the current line
        course_name = line.strip()
    else:
        strip_line = line.strip()
        #if the course name is set, set the course description to the current line
        course_description = strip_line.split("Prerequisite")[0]

#print the contents of the dictionary
print(course_catalog)
