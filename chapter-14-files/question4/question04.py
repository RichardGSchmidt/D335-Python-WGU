#    14.11 LAB: File name change
#   
#   A photographer is organizing a photo collection about the national parks in the US and would like to annotate the information about each of the photos into a separate set of files. Write a program that reads the name of a text file containing a list of photo file names. The program then reads the photo file names from the text file, replaces the "_photo.jpg" portion of the file names with "_info.txt", and outputs the modified file names.
#   
#   Assume the unchanged portion of the photo file names contains only letters and numbers, and the text file stores one photo file name per line. If the text file is empty, the program produces no output.
#   
#   Ex: If the input of the program is:
#   
#   ParkPhotos.txt
#   
#   and the contents of ParkPhotos.txt are:
#   
#   Acadia2003_photo.jpg
#   AmericanSamoa1989_photo.jpg
#   BlackCanyonoftheGunnison1983_photo.jpg
#   CarlsbadCaverns2010_photo.jpg
#   CraterLake1996_photo.jpg
#   GrandCanyon1996_photo.jpg
#   IndianaDunes1987_photo.jpg
#   LakeClark2009_photo.jpg
#   Redwood1980_photo.jpg
#   VirginIslands2007_photo.jpg
#   Voyageurs2006_photo.jpg
#   WrangellStElias1987_photo.jpg
#   
#   the output of the program is:
#   
#   Acadia2003_info.txt
#   AmericanSamoa1989_info.txt
#   BlackCanyonoftheGunnison1983_info.txt
#   CarlsbadCaverns2010_info.txt
#   CraterLake1996_info.txt
#   GrandCanyon1996_info.txt
#   IndianaDunes1987_info.txt
#   LakeClark2009_info.txt
#   Redwood1980_info.txt
#   VirginIslands2007_info.txt
#   Voyageurs2006_info.txt
#   WrangellStElias1987_info.txt

# Solution:

# Varible Declaration Block
user_input = input()
lines = []
outfile = ''

# File IO block
with open(user_input, 'r') as file_in:
    lines = file_in.readlines()

# Replacing the string for each line to change names according to requirements.
for i in range(len(lines)):
    outfile += lines[i].replace('_photo.jpg', '_info.txt')

# Output only if there are lines, failure to put the print statement in an if
#   statement makes unit test fail, as eve        
if len(lines) != 0:
    print(outfile, end="")