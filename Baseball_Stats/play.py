import pandas as pd
from Django_Stats.models import Player

def load_player_data(apps, schema_editor):
    stats_df = pd.read_csv("~/Desktop/Projects/Baseball/Stats_Files/Master.txt", names=["lahmanID", "playerID", "managerID", "hofID", "birthYear", "birthMonth", "birthDay", "birthCountry", "birthState", "birthCity", "deathYear", "deathMonth", "deathDay", "deathCountry", "deathState", "deathCity", "nameFirst", "nameLast", "nameNote", "nameGiven", "nameNick", "weight", "height", "bats", "throws", "debut", "finalGame", "college", "lahman40ID", "lahman45ID", "retroID", "holtzID", "bbrefID"])

    stats_df.fillna(0, inplace=True)

    for row in stats_df.iterrows():
        lahmanID = row[1].lahmanID
        player_key = row[1].playerID
        managerID = row[1].managerID
        hofID = row[1].hofID
        birthYear = row[1].birthYear
        birthMonth = row[1].birthMonth
        birthDay = row[1].birthDay
        birthCountry = row[1].birthCountry
        birthState = row[1].birthState
        birthCity = row[1].birthCity
        deathYear = row[1].deathYear
        deathMonth = row[1].deathMonth
        deathDay = row[1].deathDay
        deathCountry = row[1].deathCountry
        deathState = row[1].deathState
        deathCity = row[1].deathCity
        nameFirst = row[1].nameFirst
        nameLast = row[1].nameLast
        nameNote = row[1].nameNote
        nameGiven = row[1].nameGiven
        nameNick = row[1].nameNick
        weight = row[1].weight
        height = row[1].height
        bats = row[1].bats
        throws = row[1].throws
        debut = row[1].debut
        finalGame = row[1].finalGame
        college = row[1].college
        lahman40ID = row[1].lahman40ID
        lahman45ID = row[1].lahman45ID
        holtzID = row[1].holtzID
        bbrefID = row[1].bbrefID
        Player.objects.create(lahmanID=lahmanID, player_key=player_key, managerID=managerID, hofID=hofID, birthYear=birthYear, birthMonth=birthMonth, birthDay=birthDay, birthCountry=birthCountry, birthState=birthState, birthCity=birthCity, deathCountry=deathCountry, deathState=deathState, deathCity=deathCity, deathYear=deathYear, deathMonth=deathMonth, deathDay=deathDay, nameFirst=nameFirst, nameLast=nameLast, nameNote=nameNote, nameGiven=nameGiven, nameNick=nameNick, weight=weight, height=height, bats=bats, throws=throws, debut=debut, finalGame=finalGame, college=college, lahman40ID=lahman40ID, lahman45ID=lahman45ID, holtzID=holtzID, bbrefID=bbrefID)
