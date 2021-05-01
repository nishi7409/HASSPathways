import psycopg2
import json
engine = psycopg2.connect(
    
)

db_cursor = engine.cursor()
db_cursor.execute("SELECT * FROM database_course")
temp = db_cursor.fetchall()

# courses
courses = []
for x in range(len(temp)):
    outerFields = dict()
    outerFields["pk"] = temp[x][0]
    outerFields["model"] = "database.course"
    innerFields = dict()
    innerFields["prefix"] = temp[x][1]
    innerFields["ID"] = temp[x][2] 
    innerFields["name"] = temp[x][3]
    innerFields["description"] = temp[x][4]
    innerFields["HI"] = temp[x][5]
    innerFields["CI"] = temp[x][6]
    innerFields["DI"] = temp[x][7]
    innerFields["major_restrictive"] = temp[x][8]
    innerFields["fall"] = temp[x][9]
    innerFields["spring"] = temp[x][10]
    innerFields["summer"] = temp[x][11]
    outerFields["fields"] = innerFields
    courses.append(outerFields)

with open("./JSONfiles/courses.json", "w") as outfile:
    json.dump(courses, outfile, sort_keys=True, indent=4)


db_cursor = engine.cursor()
db_cursor.execute("SELECT * FROM database_pathway")
temp = db_cursor.fetchall()

# pathways
pathways = []
for x in range(len(temp)):
    outerFields = dict()
    outerFields["pk"] = temp[x][0]
    outerFields["model"] = "database.pathway"

    innerFields = dict()
    innerFields["pathName"] = temp[x][1]
    innerFields["pathDescript"] = temp[x][2] 
    innerFields["priority1"] = []
    innerFields["priority2"] = []
    innerFields["priority3"] = []

    db_cursor = engine.cursor()
    db_cursor.execute("SELECT * FROM database_pathway_priority1")
    priority1 = db_cursor.fetchall()
    for y in priority1:
        if y[1] == temp[x][0]:
            innerFields["priority1"].append(y[2])
    
    db_cursor = engine.cursor()
    db_cursor.execute("SELECT * FROM database_pathway_priority1")
    priority2 = db_cursor.fetchall()
    for y in priority2:
        if y[1] == temp[x][0]:
            innerFields["priority2"].append(y[2])

    db_cursor = engine.cursor()
    db_cursor.execute("SELECT * FROM database_pathway_priority3")
    priority3 = db_cursor.fetchall()
    for y in priority3:
        if y[1] == temp[x][0]:
            innerFields["priority3"].append(y[2])

    outerFields["fields"] = innerFields
    pathways.append(outerFields)

with open("./JSONfiles/pathways.json", "w") as outfile:
    json.dump(pathways, outfile, sort_keys=True, indent=4)