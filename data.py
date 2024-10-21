from typing import List, Tuple

pollutant_production_db_IL: List[Tuple[List[str],float,int]] = [
    (
     ["AQI"], # List of possible ways to reference the data
     55,      # Measurment
     2020     # Year taken
    ),
    (
     ["Ozone","O3"], 
     .082, 
     2021
    ),
    (
     ["Carbon Monoxide","CO"], 
     1.21, 
     2021
    ),
    (
     ["Sulfur Dioxide","S02"], 
     .0021, 
     2021
    ),
    (
     ["Nitrogen Dioxide","NO2"], 
     .00126, 
     2021
    )
]
pollutant_production_db_CHI: List[Tuple[str,str,List[int]]] = [
    #("AQI", "Average", [49]),
    ("AQI", "Lake County",
     [ 
     43,  #Average AQI
     239, # days per year W/ AQI between 0 & 51 (good)
     111, # days per year W/ AQI between 51 & 100 (Moderate)
     11,  # days per year W/ AQI between 101 & 150 (Unhealthy for Sensitive Groups)
     0,   # days per year W/ AQI between 151 & 200 (unhealthy)
     ]
    ),
    ("AQI", "Chicago", 
     [
     47,
     214,
     134,
     12,
     0
     ]
    ),
    ("AQI", "Northwest suburbs", 
     [
     50,
     197,
     148,
     13,
     1
     ]
    ),
    ("AQI", "Southwest suburbs", 
     [
     54,
     159,
     195,
     6,
     0
     ]
    )
]
AQI_Ranked=["Lake County","Chicago","Northwest Suburbs","Illinois","Southwest Suburbs"]
