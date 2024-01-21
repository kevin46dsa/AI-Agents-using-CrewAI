import os
from crewai import Agent, Task, Process,Crew

#uses OPEN AI GPT-4
api = os.environ.get("Open_API_Key")


# Travel Planner

ItenaryPlanner = Agent(
    role="Itenary Planner",
    goal="Find out the best restraunts, Things to do and fun activities in the area",
    backstory="",
    verbose=True,    # verbose= True gives a detailes output 
    allow_delegation=False
)

HotelPlanner = Agent(
    role="Hotel Planner",
    goal="Find out the cheapest and most well reviewed Hotel to stay that is within 2/3 mile radious from the fun activities",
    backstory="",
    verbose=True,    # verbose= True gives a detailes output 
    allow_delegation=False
)

CommutePlanner = Agent(
    role="Commute Planner",
    goal="Find out and plan the directions as well as mode of transportation from the hotel suggested by the Hotel planner to the Point of intrests and fun activities suggested by the Itenary planner",
    backstory="",
    verbose=True,    # verbose= True gives a detailes output 
    allow_delegation=False
)

task1 = Task(
    description="I want to go to Florida, Miami with my parents this summer find out places that we can visit, things that we can do etc that are family friendly",
    agent=ItenaryPlanner,
)

task2 = Task(
    description="I want to go to Florida, Miami with my parents this summer find out places where we can stay. the Hotels should be clean should have good review and should be within our budget which is 50-150$ per night",
    agent=HotelPlanner,
)

task3 = Task(
    description="I want to go to Florida, Miami with my parents this summer find out the most efficient and fastest ways to travel using public transport include all the bust stop or train station names",
    agent= CommutePlanner,
)

crew = Crew(
    agents=[ItenaryPlanner,HotelPlanner,CommutePlanner],
    tasks=[task1,task2,task3],
    verbose=2,
    process=Process.sequential,

)

result = crew.kickoff()
print("---------------Here is the Result-----------------")
print(result)