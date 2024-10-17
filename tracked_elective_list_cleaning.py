import pprint
f = open("data/tracked_elective_list.txt", "r")

tracked_elective_list_dict = {}

line = f.readline().strip()
track = line.split(": ")[1].strip()
print(track)
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

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(tracked_elective_list_dict)
f.close()