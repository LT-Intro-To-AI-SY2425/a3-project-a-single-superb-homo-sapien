from typing import List, Tuple, Callable, Any
from match import match
from data import pollutant_production_db_IL, pollutant_production_db_CHI, AQI_Ranked



def get_AQI_avg(location) -> int:
    final=0
    if location=="Illinois":
        final=pollutant_production_db_IL[0][1]
    else:
        for i in range(len(pollutant_production_db_CHI)):
            if pollutant_production_db_CHI[i][1]==location:
                final=pollutant_production_db_CHI[i][2][0]
    if final==0:
        final="Location not in database"
    return(final)

def location_with_AQI(AQI) -> str:
    AQI=int(AQI)
    final=0
    if AQI==pollutant_production_db_IL[0][1]:
        final="Illinois"
    else:
        for i in range(len(pollutant_production_db_CHI)):
            if AQI==pollutant_production_db_CHI[i][2][0]:
                final=pollutant_production_db_CHI[i][1]
    return final

def LocationRank(location):
    position=0
    for i in range(len(AQI_Ranked)):
        if location==AQI_Ranked[i]:
            position=i+1
    if position==0:
        position="location not found"
    return position

def get_data_IL(parameter):
    ans=None
    for i in range(len(pollutant_production_db_IL)):
        for i2 in range(len(pollutant_production_db_IL[i][0])):
            #print(pollutant_production_db_IL[i][0][i2])
            if parameter==pollutant_production_db_IL[i][0][i2]:
                ans=pollutant_production_db_IL[i][1]
    if ans==None:
        ans="Not in database"
    return ans
#print(get_data_IL("CO"))
def days_with_AQI(data):
    location=None
    AQI=None
    if type(data)==str:
        location=data
    if type(data)==int:
        AQI=data
    if location==None:
        for i in range(len(pollutant_production_db_CHI)):
            for i2 in range(1,len(pollutant_production_db_CHI[i]):
                print(i2)
days_with_AQI()
pa_list=[
        (('What', 'is', 'the','AQI','of','%'), get_AQI_avg),
        (('what','location','has','an','AQI','of','_'),location_with_AQI),
        (('where','does','%','rank'),LocationRank),
        (('Find', 'the', 'concentration', 'of', '%', 'in', 'Illinois'),get_data_IL)
        ]
def search_pa_list(src: List[str]) -> List[str]:
    
    #VARIABLES
    matches=[]
    CurrentListMatches=0
    HighestMatches=0
    BestMatch=0
    ans=[]
    print(src)
    src=str.split(src)
    print(src)
    # FIGURING OUT WHAT TUPLE TO USE

    # Creating a list(matches[]) of the number of matches between each value of src[] 
    # and the corresponding value of each of the 8 patterns
    for i in range(len(pa_list)):
        for i2 in range(len(pa_list[i][0])):
            if i2<len(src):
                print(src[i2],pa_list[i][0][i2])
                if src[i2]==pa_list[i][0][i2]:
                    CurrentListMatches+=1
        matches.append(CurrentListMatches)
        print(matches)
        CurrentListMatches=0

    # Figuring out which tuple has the highest match between its pattern and the given source using matches[] 
    for i in range(len(matches)):
        if matches[i]>HighestMatches:
            BestMatch=pa_list[i]
            HighestMatches=matches[i]

    # CALLING THE APPROPRIATE FUNCTION
    print(BestMatch)
    # Telling this block of code to run only if there is a match (if there are no matches, skip to line 193)
    if BestMatch!=0:

        # VARIABLES
        Diff=len(src)-len(BestMatch[0])
        val=[]
        
        # Checking for every item in the string of the matched tuple for %s and _s, then utilizing those symbols to determine 
        # what to send into the function
        for i3 in range(len(BestMatch[0])):
            if BestMatch[0][i3]=="%": 
                for i2 in range(Diff+1): val.append(src[i3+i2])
            if BestMatch[0][i3]=="_": val.append(src[i3]); print(val)

        # Calling the function of said tuple once the loop has ended and the list of inputs is therefore complete,
        # and setting ans equal to the output of that function
        if type(val)==list:
            val=' '.join(val)
        print(val)
        ans=BestMatch[1](val)

    # Telling the function what to do if there are no matches(if statement) 
    # or if the function of said match returns blank list(elif statement)
    if BestMatch==0: ans=["I don't understand"]
    elif ans==[]: ans=["No answers"]


    return ans
#print(search_pa_list("Find the concentration of Carbon Monoxide in Chicago"))