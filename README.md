# MapQuest
A program that utilizes MapQuest's API to give user directions and other details of the locations they desire.

The program, in detail

Describe a trip taken between a sequence of locations, the goal being to travel from the first location to 
the second, then from the second location to the third, and so on, until reaching the last location. Based on the user's input,
it will show different information about the trip, such as turn-by-turn directions, distances and times, etc.

The input

It will take input in the following format. (with no prompt)

An integer whose value is at least 2, alone on a line, that specifies how many locations the trip will consist of.
If there are n locations, the next n lines of input will each describe one location. Each location can be a city such as Irvine, CA, 
an address such as 4545 Campus Dr, Irvine, CA, or anything that the Open MapQuest API will accept as a location. 

A positive integer whose value is at least 1, alone on a line, that specifies how many outputs will need to be generated.
If there are m outputs, the next m lines of input will each describe one output. Each output can be one of the following:
STEPS for step-by-step directions, meaning a brief description of each maneuver
TOTALDISTANCE for the total distance traveled if completing the entire trip
TOTALTIME for the total estimated time to complete the entire trip
LATLONG for the latitude and longitude of each of the locations specified in the input
ELEVATION for the elevation, in feet, of each of the locations specified in the input


The output (when a route was found by MapQuest)

After reading the input and processing it, the program will generate the specified outputs in the forms described below. 
Each output preceded by a blank line, to set each one off from the others. The outputs written in the order that they were 
specified in the input.

The STEPS output will begin with the word DIRECTIONS alone on a line, followed by one line of output for each maneuver that 
needs to be made along the path from the first location to the last.
The TOTALDISTANCE output begins with the words TOTAL DISTANCE, followed by a colon and a space, followed by the total distance 
(in an integer number of miles, rounded to the nearest mile) for the entire trip.
The TOTALTIME output begins with the words TOTAL TIME, followed by a colon and a space, followed by the total time 
(in an integer number of minutes, rounded to the nearest minute) that would be required to take the entire trip.
The LATLONG output begins with the word LATLONGS alone on a line, followed by a latitude and longitude, one of each per line, 
for each of the locations specified in the input, in the order specified in the input. 
The ELEVATION output begins with the word ELEVATIONS alone on a line, followed by an integer number of feet of elevation, 
one per line, for each of the locations specified in the input, in the order specified in the input.
After the last output, a blank line will print, and then the following copyright statement, alone on a line: 
Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.

The output (when no route was found by MapQuest)

When no route was found by MapQuest, the program simply outputs a blank line, followed by NO ROUTE FOUND alone on a line. 
This also includes the scenario where one or more of the locations was not valid. 

The output (when MapQuest returns some other kind of error)

When MapQuest returns another kind of error, other than a route not being found (e.g., the AppKey was invalid, you have no 
network connectivity, or MapQuest was down), the program outputs a blank line, followed by MAPQUEST ERROR alone on a line.

An example of the program's execution

3
4533 Campus Dr, Irvine, CA
1111 Figueroa St, Los Angeles, CA
3799 S Las Vegas Blvd, Las Vegas, NV
5
LATLONG
STEPS
TOTALTIME
TOTALDISTANCE
ELEVATION

LATLONGS
33.68N 117.77W
34.02N 118.41W
36.11N 115.17W

DIRECTIONS
West on Campus Dr.
Right on Bristol
CA-73 North
Transition to I-405 North
Transition to I-110 North
Exit 9th Street
South on S Figueroa St.
Left on W 18th St.
Enter I-10 East from W 18th St.
Transition to I-15 North
Exit S Las Vegas Blvd.

TOTAL TIME: 317 minutes

TOTAL DISTANCE: 365 miles

ELEVATIONS
542
211
2001

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors
