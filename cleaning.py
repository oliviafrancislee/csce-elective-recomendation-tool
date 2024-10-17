import pprint
import math
import os, sys
import re
import matplotlib.pyplot as plt

#get tracked elective list data and clean
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

# pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(tracked_elective_list_dict)
f.close()





#get course_catalog data and clean
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

#print the contents of the dictionary
# print(course_catalog)




# add course catalog descriptions to tracked elective list dictionary
for key in tracked_elective_list_dict.keys():
    for (course_id, course_name) in tracked_elective_list_dict[key].keys():
        for course in course_catalog.keys():
            if course_id in course:
                tracked_elective_list_dict[key][(course_id, course_name)] = course_catalog[course]

# print(tracked_elective_list_dict)

tracked_elective_list_dict['Systems'].pop(('CSCE 456', 'Real-Time Computing'))



track_average_lens = {track: 0 for track in tracked_elective_list_dict.keys()}
for track in tracked_elective_list_dict.keys():
    for (credit_info, course_description) in tracked_elective_list_dict[track].values():
        track_average_lens[track] += len(course_description.split())
    track_average_lens[track] /= len(tracked_elective_list_dict[track])

for (track, value) in track_average_lens.items():
    print(track + " avg: " + str(value))


keys = list(track_average_lens.keys())
values = list(track_average_lens.values())

plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='skyblue')
plt.xlabel('Track')
plt.ylabel('Avg Course Description Length')
plt.title('Avg Course Description Length Per Track')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()