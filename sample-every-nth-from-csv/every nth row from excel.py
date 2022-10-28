import pandas as pd

# Pandas opens the csv containing lat,long,alt and speed data
df = pd.read_csv("BY6701_LoLaAlSp.csv")


# open the guidance file in write mode to clear all values inside
with open("guidance.txt","w") as guidance_file:
    guidance_file.write("")

# function which take 4 inputs, lat,long,alt and speed
# formats the values into "message"
# append the message  to the guidance file
def write_to_file(lat,long,alt,speed):
    message = ("%s %s %s %s\n" % (long,lat,alt,speed))
    #print(message)
    with open("guidance.txt","a") as guidance_file:
        guidance_file.write(message)

# sets up 4 lists for each measured variable
lats = df["Latitude"]
longs = df["Longitude"]
alts = df["Altitude"]
speeds = df["Speed"]

# initialises values for counter and number of waypoints
# i think counter could be replaced with i, but it works so im leaving it :)
counter = 0
waypoints = 0
# iterates through each row in the dataframe
# sets lat to the corresponding value of lats[] etc
# calls function write_to_file passing in the 4 relevant values
# increments counter (again, could have just used i) and waypoints
for i in df.index:
    print(i)
    print(df.index)
    print(counter)
    print("")
    if counter % 10 == 0:
        lat = round(lats[counter],4)
        long = round(longs[counter],4)
        alt = round(alts[counter],1)
        speed = round(speeds[counter],1)
        write_to_file(lat,long,alt,speed)
        counter += 1
        waypoints += 1
    else:
        counter += 1
        
# outputs number of waypoints
print(waypoints)
