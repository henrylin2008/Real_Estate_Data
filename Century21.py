
# coding: utf-8

# In[101]:

import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

#remove all \n in the string 
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text


# In[102]:

l=[]
base_url="https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10): 
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all: 
        d={}
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        except: 
            d["Locality"]=None
            
        d["Price"]=item.find("h4",{"propPrice"}).text.replace("\n","").replace(" ","")

        try:
            d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text
        except: 
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
        except: 
            d["Area"]=None

        try:
            d["Full Baths"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
        except: 
            d["Full Baths"]=None

        try:
            d["Half Baths"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text
        except: 
            d["Half Baths"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):
    #         print(column_group)
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
    #             print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text: 
                    d["Lot Size"]=feature_name.text
        l.append(d)


# In[97]:

len(l)


# In[103]:

import pandas
df=pandas.DataFrame(l)
df


# In[105]:

df.to_csv("output.csv")


# In[ ]:
# Address Area    Beds    Full Baths  Half Baths  Locality    Lot Size    Price
# 0   0 Gateway   None    None    None    None    Rock Springs, WY 82901  NaN $725,000
# 1   1003 Winchester Blvd.   None    4   4   None    Rock Springs, WY 82901  0.21 Acres  $452,900
# 2   600 Talladega   3,154   5   3   None    Rock Springs, WY 82901  NaN $396,900
# 3   3239 Spearhead Way  3,076   4   3   1   Rock Springs, WY 82901  Under 1/2 Acre, $389,900
# 4   522 Emerald Street  1,172   3   3   None    Rock Springs, WY 82901  Under 1/2 Acre, $254,000
# 5   1302 Veteran's Drive    1,932   4   2   None    Rock Springs, WY 82901  0.27 Acres  $252,900
# 6   1021 Cypress Cir    1,676   4   3   None    Rock Springs, WY 82901  Under 1/2 Acre, $210,000
# 7   913 Madison Dr  1,344   3   2   None    Rock Springs, WY 82901  Under 1/2 Acre, $209,000
# 8   1344 Teton Street   1,920   3   2   None    Rock Springs, WY 82901  Under 1/2 Acre, $199,900
# 9   4 Minnies Lane  1,664   3   2   None    Rock Springs, WY 82901  2.02 Acres  $196,900
# 10  9339 Sd 26900   2,560   None    None    None    Rocksprings, TX 78880   NaN $1,700,000
# 11  RR674P13 Hwy 377    2,000   None    None    None    Rocksprings, TX 78880   NaN $1,100,000
# 12  0 Hwy 41    None    None    None    None    Rocksprings, TX 78880   NaN $1,080,000
# 13  9339 Sd 26900   2,560   None    None    None    Rocksprings, TX 78880   NaN $908,350
# 14  CR450 Hwy 377   None    None    None    None    Rocksprings, TX 78880   NaN $905,000
# 15  Cr 240 Cr 240   1,398   None    None    None    Rocksprings, TX 78880   NaN $695,000
# 16  RR674 Hwy 377   1,738   None    None    None    Rocksprings, TX 78880   NaN $605,000
# 17  9770a Sd 26900  1,080   None    None    None    Rocksprings, TX 78880   NaN $559,805
# 18  Lot17 CR 2630   None    None    None    None    Rocksprings, TX 78880   NaN $504,000
# 19  Tr12,16 CR 520  None    None    None    None    Rocksprings, TX 78880   NaN $410,000
# 20  32575 S Shadow Mountain Road    2,318   3   2   None    Black Canyon City, AZ 85324 NaN $299,900
# 21  32750 S Shangrila Drive 2,120   3   2   None    Black Canyon City, AZ 85324 NaN $167,500
# 22  0000 Black Canyon Highway   None    None    None    None    Black Canyon City, AZ 85324 5 Acres $150,000
# 23  34775 S CHOLLA Drive    1,220   3   2   None    Black Canyon City, AZ 85324 NaN $129,500
# 24  33403 S. HA-WA-SI TERRACE   2,000   4   2   None    BLACK CANYON CITY, AZ 85324 NaN $129,000
# 25  34263 S Bertha Street   2,260   5   2   None    Black Canyon City, AZ 85324 NaN $80,000
# 26  33160 S Canyon Road 1,248   3   2   None    Black Canyon City, AZ 85324 NaN $77,900
# 27  19421 E Todd Evans Road 1,404   3   2   None    Black Canyon City, AZ 85324 NaN $70,500
# 28  18688 E AGUA Vista  None    None    None    None    Black Canyon City, AZ 85324 0.7 Acres   $70,000
# 29  50600 N Old Black Canyon Road   None    None    None    None    Black Canyon City, AZ 85324 3 Acres $67,500
# 30  20101 E SQUAW VALLEY Road   None    None    None    None    Black Canyon City, AZ 85324 NaN $54,900
# 31  33259 S Canyon Road 1,056   3   1   None    Black Canyon City, AZ 85324 NaN $45,600
# 32  34558 S ROADRUNNER RD   784 2   1   None    Black Canyon City, AZ 85324 Under 1/2 Acre  $40,000
# 33  19260 E Scenic Loop Road    None    None    None    None    Black Canyon City, AZ 85324 2.35 Acres  $30,000
# 34  19000 E MAREN Avenue    None    None    None    None    Black Canyon City, AZ 85324 2.05 Acres  $29,000
# 35  19350 E SAGUARO Drive   None    None    None    None    Black Canyon City, AZ 85324 0.73 Acres  $28,995
# 36  20650 E Amethyst Place  None    None    None    None    Black Canyon City, AZ 85324 0.31 Acres  $15,000


