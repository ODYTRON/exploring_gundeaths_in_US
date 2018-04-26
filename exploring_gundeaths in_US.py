
# coding: utf-8

# ## US Gun Deaths Data

# In[80]:


# import modules
import csv

# csv file handler
#here we use the csv module
csvopener = open('guns.csv')
csvreader = csv.reader(csvopener)
data = list(csvreader)

print(data[:5])

# OR 
# first_5 = data[:5]
# print(first_5)


# ## Remove Headers From A List Of Lists

# In[81]:


# hold headers to display
# keep an instance of dataset keep only 0
headers = data[:1]
# permanently remove header from dataset
# slice row 0 not including 1 to the end of the dataset
data = data[1:]
# print headers
print (headers)
#print first 5 rows without header
print (data[:5])


# ## Count Gun Deaths By Year

# In[82]:


# that is how list comprehension works we iterate to slice the apropriate column
years = [row[1] for row in data]
# test column
#print (years)
# that is an empty dictionary
year_counts = {}

# loop through years
for rows in years:
# if the year is in dict put it as a key and add 1 as value
    if rows in year_counts:
        year_counts[rows] = year_counts[rows] + 1
# else put year as a key and  set value as 1 and so on till the end of the loop
    else:
        year_counts[rows] = 1
        
#here we have the sum of gun deaths for each year in a printed dict
            
print (year_counts)


# ## Count Gun Deaths By Month And Year

# In[83]:


# import module date time
import datetime

# create with list comprehension a datetime.datetime object for each row
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]

print (dates[:5])


# In[84]:


# make an empty dictionary
date_counts = {}
# now loop through the object dates
for date_rows in dates:
#if the iterated row is in dict put plus one in the value
#it uses the whole row as a key and the increment as value
#see above
    if date_rows in date_counts:
        date_counts[date_rows] = date_counts[date_rows] + 1
# else put the whole row as a key and set value as 1 and so on till the end of the loop
# it works as value initiator
    else:
        date_counts[date_rows] = 1
# then print the dataset with a good visual way
date_counts


# ## Count Gun Deaths By Race And Sex

# In[85]:


sex_counts = {}
race_counts = {}

sex = [rowsa[5] for rowsa in data]

race = [rowsb[7] for rowsb in data]

for sex_rows in sex:
    if sex_rows in sex_counts:
        sex_counts[sex_rows] = sex_counts[sex_rows] + 1
    else:
        sex_counts[sex_rows] = 1

for race_rows in race:
    if race_rows in race_counts:
        race_counts[race_rows] = race_counts[race_rows] + 1
    else:
        race_counts[race_rows] = 1
        
sex_counts

    
race_counts





# #### In order to iterate through a column and count how many times a record is occuring you have to do the following steps :
# 
# 0. Make an empty dictionary 
# 
# 1. With list comprehension save in a variable the column you want from dataset
# 
# 2. iterate through the subset of your dataset and:
# 
# 3. if the iterated row is in the dictionary add the row as key in the dictionary and put an increment as a value
# 
# 4. else if the iterated row isn't in the dictionary add the row as a key and set 1 as a value
# 
# 5. Print the dictionary by simply provide the name of the variable without the command print
# 
# # inferences - deductions - conclusions 
# 
# 
# * Sex
# 
# ** The sample  shows that M > F Witch means that even the population of men is greater than the women or the male subjects are kean to use violence and participate in crimes
# 
# * Race
# 
# ** The sample shows that the number of white subjects is much greater than any other racial group and this is maybe due to the greater ammounts of white population in USA. There are many other parameters from the demographics (census data) which we have to compare in order to deduct safe conclusions for the rest of the races. 
# 
# * Crimes per month in a given year
# 
# ** A plot analysis for each year will show as the distribution of the crimes then we can visualy infer simple conclusions. Mean analysis , standard diviation and other descriptive statistics can be very helpful if we perform them.  

# ## Read the second dataset census- demographics

# In[86]:



# read and manipulate census data to compare with the previous dataset



# method 1 #


# make an empty_list to use it later

census = []

# open the dataset
f = open("census.csv", 'r')
# read the dataset
text = f.read()
# split the dataset aka put it in list 
census_list = text.split('\n')
# then we have to split the dataset one more time to make lists of lists
# we have to do it with iteration because you cannot directly split a list

for grammi in census_list:
    split_cens_row = grammi.split(',')
# append the generated list to the empty list as the loop goes 
    census.append(split_cens_row)
    
census


# In[87]:


# read and manipulate census data to compare with the previous dataset

import csv
# method 2 #

# csv file handler

#here we use the csv module
csvopener = open('census.csv')
csvreader = csv.reader(csvopener)
census = list(csvreader)
census


# In[88]:


# method 3

import csv

with open("census.csv", "r") as f:
    reader = csv.reader(f)
    census = list(reader)
    
census


# ## Calculate the deaths per race comparing with the general N

# In[89]:


# here we manually map the census data headings with the race_counts (from the initial dataset)
mapping = {
    'Asian/Pacific Islander': 15159516 + 674625,
    'Native American/Native Alaskan':3739506,
    'Black':40250635,
    'Hispanic':44618105,
    'White':197318956,
          }


# we create a new empty dictionary
race_per_hundredk = {}
# now we have to iterate through the initial race_counts dictionary
for k,v in race_counts.items():
# now we make the formula 
# the new dictionary has the key of race_counts
# and as values it has the race_counts sample value divided with the associated value
# of the mapping dictionary above
# then we myltiply it with 100K
    race_per_hundredk[k] = (v / mapping[k]) * 100000

# an example rate_per_hundredk = 0.0003356849303419181 * 100000
# 0.0003356849303419181 is a tyny number, this percentage cannot help us
# so we multiply.  
#"rate per 100000". This tells you the number of people in a given group 
#out of every 100000 that were killed by guns in the US. 
# print the dictionary
race_per_hundredk


# ## Filter races by the intent of "murder"

# In[90]:


# now we will filter results only for Homicide
# extract intent column method 1
intents = [row_intent[3] for row_intent in data]
intents


# In[91]:


# now we will filter results only for Homicide
# extract intent column method 2

intent2 = []

for row_intent2 in data:
    intent2.append(row_intent2[3])
    
intent2
    
    


# In[92]:


# now we will filter results only for Homicide
# extract race column method 1
races = [row_race[7] for row_race in data]
races


# In[93]:


# now we will filter results only for Homicide
# extract race column method 2

race2 = []

for row_race2 in data:
    race2.append(row_race2[7])
    
race2


# ### compare intent column with race and calculate the results in a new dictionary using enumerate 

# In[94]:


# then we create an empty dictionary
homicide_race_counts = {}

# with a for loop we enumerate races by index and value
for i,race in enumerate(races):
# if the current iterated value is not in the dictionary
# put the race as key and with value 0 "create it 
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
# if the index of races matches with the word 'Homicide' in the intense column
# then put the race as a key and increment by 1 for the specific race
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1
        
# print the dictionary        
homicide_race_counts    


# In[95]:


# now we must perform the same methodology to compare our sample with the general N
# we create a new empty dictionary
race_per_hundredk = {}
# now we have to iterate through the initial homocide_race_counts dictionary
for k,v in homicide_race_counts.items():
# now we make the formula 
# the new dictionary has the key of race_counts
# and as values it has the race_counts sample value divided with the associated value
# of the mapping dictionary above
# then we myltiply it with 100K
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# 
# 
# # inferences - deductions - conclusions 
# 
# 
# IT SEEMS THAT BLACK AND HISPANIC ORIGIN PEOPLE IN US BETWEEN THE YEARS 2012 - 2014 ARE KEEN TO GET INVOLVED IN CRIMES SUCH AS HOMOCIDE  
# 
# 
# **Here are some next steps i must perform:
# 
# * Figure out the link, if any, between month and homicide rate.
# * Explore the homicide rate by gender.
# * Explore the rates of other intents, like Accidental, by gender and race.
# * Find out if gun death rates correlate to location and education.

# ### Explore the homocide rate by gender

# In[96]:



# Isolate sex data in a single column with method 1 list comprehension look above

sex_data = [row_sex[5] for row_sex in data]
sex_data



# In[97]:


# then we create an empty dictionary
homicide_gender_counts = {}

# with a for loop we enumerate sex_data by index and value
for i,sex in enumerate(sex_data):
# if the current iterated value is not in the dictionary
# put the sex as key and with value 0 "create it 
    if sex not in homicide_gender_counts:
        homicide_gender_counts[sex] = 0
# if the index of races matches with the word 'Homicide' in the intense column
# then put the sex as a key and increment by 1 for the specific gender
    if intents[i] == "Homicide":
        homicide_gender_counts[sex] += 1
        
# print the dictionary        
homicide_gender_counts  


# # Explore the rates Suicide intent , by gender and race.

# In[98]:


#  First we count how many males and females died with suicide intent
#  we create an empty dictionary
suicide_gender_counts = {}

# with a for loop we enumerate sex_data by index and value
for i,sex in enumerate(sex_data):
# if the current iterated value is not in the dictionary
# put the sex as key and with value 0 "create it 
    if sex not in suicide_gender_counts:
        suicide_gender_counts[sex] = 0
# if the index of races matches with the word 'Suicide' in the intense column
# then put the sex as a key and increment by 1 for the specific gender
    if intents[i] == "Suicide":
        suicide_gender_counts[sex] += 1
        
# print the dictionary        
suicide_gender_counts  


# In[99]:


# count suicides for each race

# then we create an empty dictionary
suicide_race_counts = {}

# with a for loop we enumerate races by index and value
for i,race in enumerate(races):
# if the current iterated value is not in the dictionary
# put the race as key and with value 0 "create it 
    if race not in suicide_race_counts:
        suicide_race_counts[race] = 0
# if the index of races matches with the word 'Homicide' in the intense column
# then put the race as a key and increment by 1 for the specific race
    if intents[i] == "Suicide":
        suicide_race_counts[race] += 1
        
# print the dictionary        
suicide_race_counts  


# In[100]:


# now we must perform the same methodology to compare our sample with the general N
# we create a new empty dictionary
race_per_hundredk = {}
# now we have to iterate through the initial suicide_race_counts dictionary
for k,v in suicide_race_counts.items():
# now we make the formula 
# the new dictionary has the key of race_counts
# and as values it has the race_counts sample value divided with the associated value
# of the mapping dictionary above
# then we myltiply it with 100K
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[101]:


# Now i will explore the sample by suicide intent by gender and sex. unfortunatly we dont have census data for sex to compare
# this is a simplistic way but for large dataset i think that it will delay all sources somehow

# i made lists for every race and its gender

natives_m = 0
natives_f = 0
hispanics_m = 0
hispanics_f = 0
whites_m = 0
whites_f = 0
asians_m = 0
asians_f = 0
blacks_m = 0
blacks_f = 0

for data_rows in data:
    if data_rows[3] == 'Suicide' and data_rows[5] == 'M' and data_rows[7] == 'Native American/Native Alaskan':
        natives_m += 1

    if data_rows[3] == 'Suicide' and data_rows[5] == 'F' and data_rows[7] == 'Native American/Native Alaskan':
        natives_f += 1
    
    if data_rows[3] == 'Suicide' and data_rows[5] == 'M' and data_rows[7] == 'Hispanic':
        hispanics_m += 1

    if data_rows[3] == 'Suicide' and data_rows[5] == 'F' and data_rows[7] == 'Hispanic':
        hispanics_f += 1
        
    if data_rows[3] == 'Suicide' and data_rows[5] == 'M' and data_rows[7] == 'White':
        whites_m += 1

    if data_rows[3] == 'Suicide' and data_rows[5] == 'F' and data_rows[7] == 'White':
        whites_f += 1
        
    if data_rows[3] == 'Suicide' and data_rows[5] == 'M' and data_rows[7] == 'Asian/Pacific Islander':
        asians_m += 1

    if data_rows[3] == 'Suicide' and data_rows[5] == 'F' and data_rows[7] == 'Asian/Pacific Islander':
        asians_f += 1
        
    if data_rows[3] == 'Suicide' and data_rows[5] == 'M' and data_rows[7] == 'Black':
        blacks_m += 1

    if data_rows[3] == 'Suicide' and data_rows[5] == 'F' and data_rows[7] == 'Black':
        blacks_f += 1

print ("native americans_m",natives_m)
print ("native americans_f",natives_f)

print("#############################")
    
print ("hispanics_m",hispanics_m)
print ("hispanics_f",hispanics_f)


print("#############################")
    
print ("whites_m",whites_m)
print ("whites_f",whites_f)

print("#############################")
    
print ("asians_m",asians_m)
print ("asians_f",asians_f)

print("#############################")
    
print ("blacks_m",blacks_m)
print ("blacks_f",blacks_f)


# In[102]:




location_counts = {}
education_counts = {}

location = [locrow[9] for locrow in data]

education = [edurow[10] for edurow in data]



for location_rows in location:
    if location_rows in location_counts:
        location_counts[location_rows] =  location_counts[location_rows] + 1
    else:
        location_counts[location_rows] = 1


#location
        
location_counts
# education
    


# In[103]:


# create dictionaries to store results for each category

edu_vs_location_f = {}
edu_vs_location_h = {}
edu_vs_location_i = {}
edu_vs_location_n = {}
edu_vs_location_os = {}
edu_vs_location_ou = {}
edu_vs_location_ri = {}
edu_vs_location_si = {}
edu_vs_location_s = {}
edu_vs_location_st = {}
edu_vs_location_tr = {}


# In[104]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_f:
        edu_vs_location_f[edu] = 0

    if location[b] == "Farm":
        edu_vs_location_f[edu] += 1

print ("results for location FARM");
edu_vs_location_f


# In[105]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_h:
        edu_vs_location_h[edu] = 0

    if location[b] == "Home":
        edu_vs_location_h[edu] += 1

print ("results for location HOME");
edu_vs_location_h


# In[106]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_i:
        edu_vs_location_i[edu] = 0

    if location[b] == "Industrial/construction":
        edu_vs_location_i[edu] += 1

print ("results for Industrial/construction");
edu_vs_location_i


# In[107]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_n:
        edu_vs_location_n[edu] = 0

    if location[b] == "NA":
        edu_vs_location_n[edu] += 1

print ("results for NA");
edu_vs_location_n


# In[108]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_os:
        edu_vs_location_os[edu] = 0

    if location[b] == "Other specified":
        edu_vs_location_os[edu] += 1

print ("results for Other specified");
edu_vs_location_os


# In[109]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_ou:
        edu_vs_location_ou[edu] = 0

    if location[b] == "Other unspecified":
        edu_vs_location_ou[edu] += 1

print (" results for Other unspecified");
edu_vs_location_ou


# In[110]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_ri:
        edu_vs_location_ri[edu] = 0

    if location[b] == "Residential institution":
        edu_vs_location_ri[edu] += 1

print (" results for Residential institution");
edu_vs_location_ri


# In[111]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_si:
        edu_vs_location_si[edu] = 0

    if location[b] == "School/instiution":
        edu_vs_location_si[edu] += 1

print (" results for School/instiution");
edu_vs_location_si


# In[112]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_s:
        edu_vs_location_s[edu] = 0

    if location[b] == "Sports":
        edu_vs_location_s[edu] += 1

print (" results for Sports");
edu_vs_location_s


# In[113]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_st:
        edu_vs_location_st[edu] = 0

    if location[b] == "Street":
        edu_vs_location_st[edu] += 1

print (" results for Street");
edu_vs_location_st


# In[114]:


for b,edu in enumerate(education):

    if edu not in edu_vs_location_tr:
        edu_vs_location_tr[edu] = 0

    if location[b] == "Trade/service area":
         edu_vs_location_tr[edu] += 1

print (" results for Trade/service area");
print (edu_vs_location_tr)

