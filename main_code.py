from typing import List, Tuple, Callable, Any
from match import match
from data import pollutant_production_db_IL, pollutant_production_db_CHI, AQI_Ranked



def get_AQI_avg(location) -> int:
    final="Location not in database"
    if location=="illinois":
        final=pollutant_production_db_IL[0][1]
    else:
        for i in range(len(pollutant_production_db_CHI)):
            if pollutant_production_db_CHI[i][1]==location:
                final=pollutant_production_db_CHI[i][2][0]
    return final

def location_with_AQI(AQI) -> str:
    AQI=int(AQI)
    final="Location not in database"
    if AQI==pollutant_production_db_IL[0][1]:
        final="illinois"
    else:
        for i in range(len(pollutant_production_db_CHI)):
            if AQI==pollutant_production_db_CHI[i][2][0]:
                final=pollutant_production_db_CHI[i][1]
    return final

def LocationRank(location):
    position="location not found"
    for i in range(len(AQI_Ranked)):
        if location==AQI_Ranked[i]:
            position=i+1
    return position

def get_data_IL(parameter):
    ans="Not in database"
    for i in range(len(pollutant_production_db_IL)):
        for i2 in range(len(pollutant_production_db_IL[i][0])):
            if parameter==pollutant_production_db_IL[i][0][i2]:
                ans=pollutant_production_db_IL[i][1]
    return ans

def get_year_of_data(data):
    ans="Not in database"
    for i in range(len(pollutant_production_db_IL)):
        for i2 in range(len(pollutant_production_db_IL[i][0])):
            if data==pollutant_production_db_IL[i][0][i2]:
                ans=pollutant_production_db_IL[i][2]
    return ans

def days_with_AQI(input):

    breaker=input.rfind(" ")
    location=input[breaker-breaker:breaker]
    value=input[breaker:]
    value=value.strip()
    finalList=[]
    final="I don't understand"
    for i in range(len(pollutant_production_db_CHI)):
        if location==pollutant_production_db_CHI[i][1]:
            finalList=pollutant_production_db_CHI[i][2]
    if input==["illinois"] or finalList==[]:
        pass
    else:
        if value=='good':
            final=finalList[1]
        if value=='moderate':
            final=finalList[2]
        if value=='unhealthy':
            final=finalList[3]+finalList[4]
    return final
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list=[
        (('what', 'is', 'the','aqi','of','%'), get_AQI_avg),
        (('what','location','has','an','aqi','of','_'),location_with_AQI),
        (('where','does','%','rank'),LocationRank),
        (('find', 'the', 'concentration', 'of', '%', 'in', 'illinois'),get_data_IL),
        (('for','how','many','days','was','the','aqi','of','%','_'),days_with_AQI),
        (('in','what','year','was','the','%','data','for','illinois','taken'),get_year_of_data),
        (["bye"], bye_action)
        ]

def search_pa_list(src: List[str]) -> List[str]:
    
    #VARIABLES
    matches=[]
    CurrentListMatches=0
    HighestMatches=0
    BestMatch=0
    ans=[]
    #src=str.split(src)
    # FIGURING OUT WHAT TUPLE TO USE

    # Creating a list(matches[]) of the number of matches between each value of src[] 
    # and the corresponding value of each of the 8 patterns
    for i in range(len(pa_list)):
        for i2 in range(len(pa_list[i][0])):
            if i2<len(src):
                if src[i2]==pa_list[i][0][i2]:
                    CurrentListMatches+=1
        matches.append(CurrentListMatches)
        CurrentListMatches=0

    # Figuring out which tuple has the highest match between its pattern and the given source using matches[] 
    for i in range(len(matches)):
        if matches[i]>HighestMatches:
            BestMatch=pa_list[i]
            HighestMatches=matches[i]

    # CALLING THE APPROPRIATE FUNCTION
    # Telling this block of code to run only if there is a match (if there are no matches, skip to line 150)
    if BestMatch!=0:

        # VARIABLES
        Diff=len(src)-len(BestMatch[0])
        val=[]
        i2=0

        # Checking for every item in the string of the matched tuple for %s and _s, then utilizing those symbols to determine 
        # what to send into the function
        for i3 in range(len(BestMatch[0])):
            if BestMatch[0][i3]=="%":
                while i2 in range(Diff+1): 
                    val.append(src[i3+i2])
                    i2+=1
            if BestMatch[0][i3]=="_": val.append(src[i3+Diff]);

        # Calling the function of said tuple once the loop has ended and the list of inputs is therefore complete,
        # and setting ans equal to the output of that function
        if type(val)==list:
            val=' '.join(val)
        ans=BestMatch[1](val)

    # Telling the function what to do if there are no matches(if statement) 
    # or if the function of said match returns blank list(elif statement)
    if BestMatch==0: ans="I don't understand"
    elif ans==[]: ans="No answers"

    return str(ans)

def query_loop() -> None:
    print("This is a database of information from various years combined to make a small, nonofficial climate report of Chicago and the surrounding area.\nEnter a question into the query prompt to recieve an answer.")
    while True:
        try:
            print()
            query = input("Query: ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            print(answers)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nThank you for using this database.\n")
query_loop()