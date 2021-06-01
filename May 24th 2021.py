import random
import math

#Crtl + f "####" for navigaton purposes


#Murder one boss per week, instead of all 4 a week. Saves 120 resin worth of time, if you're only trying to max one character
#Murder all four bosses per week, instead of 1.
#Options are 1 or 4 respectfully
Boss_Method = 4

#Standard Outcrops - Ley Line Outcrops
#Rhodeia's Rage - Limited Event starting April 9th 2021, but lets pretend its indefinite
#Options are "EXP" or "RhoRage" respectfully
EXP_Method = "EXP"

#Only do these characters:
#I added this because its easier to just write their names in a list, rather than copy and paste and make a new dictionary any everything like that
Only_Do = []

#Get slivers from daily commision rewards
#I find it kind of sus that you have like thousands of slivers by the time this """simulation""" is done, so you can easily toggle slivers here
#Options are True or False
Get_Sliver = True

####Characters
Characters_List = {
    #"Name": (Element, "Weekly Boss", "Domain Talent Material", "Weapon Name", "Weapon Ascention Material")
    "Venti": ("Anemo", "Tail", "Ballad", "Skyward Harp", "Wolf"), #-
    "Sucrose": ("Anemo", "Locket", "Freedom", "Skyward Atlas", "Wolf"), #- 
    "Jean": ("Anemo", "Plume", "Resistance", "Aquila Favonia", "Decarabian"), #+
    "TravelerA": ("Anemo", "Sigh", "ThreeMondstat", "Skyward Blade", "Wolf"), #+
    "Xiao": ("Anemo", "Shadow", "Prosperity", "Primordial Jade Winged-Spear", "Guyun"), #+ 
 

    "Qiqi": ("Cryo", "Tail", "Prosperity", "Skyward Blade", "Wolf"), #+
    "Kaeya": ("Cryo", "Locket", "Ballad", "Aquila Favonia", "Decarabian"), #+
    "Chongyun": ("Cryo", "Sigh", "Dilligence", "Skyward Pride", "Wolf"), #+
    "Diona": ("Cryo", "Legacy", "Freedom", "Amos' Bow", "Dandelion"),
    "Ganyu": ("Cryo", "Shadow", "Dilligence", "Amos' Bow", "Dandelion"), #+
    "Rosaria": ("Cryo", "Shadow", "Ballad", "Staff of Homa", "Aero_Chocolate"), #+
    "Eula":("Cryo", "Crown", "Resistance", "Song of Broken Pines", "Decarabian"), #+
    

    "Keqing": ("Electro", "Ring", "Prosperity", "Aquila Favonia", "Decarabian"), #+
    "Fishcl": ("Electro", "Locket", "Ballad", "Skyward Harp", "Wolf"), #+
    "Lisa": ("Electro", "Claw", "Ballad", "Lost Prayer to the Sacred Winds", "Dandelion"),
    "Razor": ("Electro", "Claw", "Resistance", "Wolf's Gravestone", "Dandelion"), #+
    "Beidou": ("Electro", "Sigh", "Gold", "Wolf's Gravestone", "Dandelion"), #+
 

    "TravelerG": ("Geo", "Tail+Sigh", "Everything", "Gods dont need weapons", "None"),
    "Ninguang": ("Geo", "Locket", "Prosperity", "Memory of Dust", "Aero_Chocolate"), #+
    "Noelle": ("Geo", "Claw", "Resistance", "The Unforged", "Elixer"), #-
    "Albedo": ("Geo", "Tusk", "Ballad", "Skyward Blade", "Wolf"), #-
    "Zhongli": ("Geo", "Tusk", "Gold", "Vortex Vanquisher", "Aero_Chocolate"), #+
 

    "Xingqui": ("Hydro", "Tail", "Gold", "Skyward Blade", "Wolf"), #+
    "Mona": ("Hydro", "Ring", "Resistance", "Skyward Atlas", "Wolf"), #- 
    "Barbara": ("Hydro", "Ring", "Freedom", "Skyward Atlas", "Wolf"), #- 
    "Tartagalia": ("Hydro", "Legacy", "Freedom", "Skyward Harp", "Wolf"), #+
 

    "Klee": ("Pyro", "Ring", "Freedom", "Lost Prayer to the Sacred Winds", "Dandelion"), #+
    "Diluc": ("Pyro", "Plume", "Resistance", "Wolf's Gravestone", "Dandelion"), #+
    "Bennett": ("Pyro", "Plume", "Resistance", "Skyward Blade", "Wolf"), #+
    "Xiangling": ("Pyro", "Claw", "Dilligence", "Skyward Spine", "Dandelion"), #+
    "Amber": ("Pyro", "Sigh", "Freedom", "Amos' Bow", "Dandelion"), #+
    "Xinyan": ("Pyro", "Tusk", "Gold", "The Unforged", "Elixer"), #+
    "Hu Tao": ("Pyro", "Legacy", "Dilligence", "Staff of Homa", "Aero_Chocolate"), #+
    "Yanfei": ("Pyro", "Branch", "Gold", "Lost Prayer to the Sacred Winds", "Dandelion"), #+
}

if len(Only_Do) >= 1:
    for Key in Characters_List.copy().keys():
        if Key not in Only_Do:
            Characters_List.pop(Key)


Needs_PrimoGeovishap = ["Xiao", "Rosaria", "Hu Tao"]
Needs_CryoCube = ["Eula"]

print("Settings:")
print("     " + str(len(Characters_List)) + " Character(s)...")
Character_Count_x5 = len(Characters_List) * 5#For some reason, making a copy of the dictionary itself wasnt working, because the key got deleted from both Dictionaries at the smae time, which is weird because I never told it to edit a dictionary called "Characters_List2". So, I scrapped a second dictionary, and just did the calculations at the beginning.
Character_Count_Over4 = math.ceil(len(Characters_List)/4)#Level 4 characters at once for Companionship EXP
if EXP_Method == "EXP":
    print("     EXP Method: EXP Ley Line Outcrops")
else:
    print("     EXP Method: Rhodeia's Rage")
if Boss_Method == 1:
    print("     Boss Method: Murder 1 Weekly Boss per week")
if Boss_Method == 4:
    print("     Boss Method: Murder all 4 Weekly Bosses per week")
print("")
print("")

Dvalin_Loot = ["Plume", "Claw", "Sigh"]
Wolf_Loot = ["Tail", "Ring", "Locket"]
Childe_Loot = ["Tusk", "Legacy", "Shadow"]
Azhdaha_Loot = ["Crown", "Branch", "Scale"]



#I know there's a way to set multiple variables at once, but im just so used to this anything else looks weird
Weeks_Waited = 0
 

Dvalin_Body_Count = 0
Wolf_Body_Count = 0
Childe_Body_Count = 0
Azhdaha_Body_Count = 0

PrimoVishapBodyCount = 0

Plume = 0
Claw = 0
Sigh = 0
Tail = 0
Ring = 0
Locket = 0
Tusk = 0
Legacy = 0
Shadow = 0
Crown = 0
Branch = 0
Scale = 0

def Boss_Check(WiiSports2):
    ####Weekly Boss Loot Check Function thing
    global Tail
    global Sigh
    if WiiSports == "Tail+Sigh":
        if Tail >= 12 and Sigh >= 6:
            Tail -= 12
            Sigh -= 6
            return True
    else:
        if eval(WiiSports2) >= 18:#If Geo Traveler didnt require both Tails and Sighs, I could have just done this all at once, without needed the function
            globals()[WiiSports2] = eval(WiiSports2) - 18
            return True
 

def Boss_Loot(WiiSports2):
    ####Weekly Boss Loot Function thing
    global Dvalin_Body_Count
    global Wolf_Body_Count
    global Childe_Body_Count
    global Azhdaha_Body_Count
    global Tail
    global Sigh



    if WiiSports2 in Dvalin_Loot:
        for x in random.sample(Dvalin_Loot, 2):
            globals()[x] = eval(x) + 1
        Dvalin_Body_Count += 1
 

    if WiiSports2 in Wolf_Loot:
        for x in random.sample(Wolf_Loot, 2):
            globals()[x] = eval(x) + 1
        Wolf_Body_Count += 1
    
    if WiiSports2 in Childe_Loot:
        for x in random.sample(Childe_Loot, 2):
            globals()[x] = eval(x) + 1
        Childe_Body_Count += 1
 

    if WiiSports2 == "Tail+Sigh":
        if Tail < 12:
            for x in random.sample(Wolf_Loot, 2):
                globals()[x] = eval(x) + 1
            Wolf_Body_Count += 1
        else:
            for x in random.sample(Dvalin_Loot, 2):
                globals()[x] = eval(x) + 1
            Dvalin_Body_Count += 1
    
    if WiiSports2 == "ALL":
        for x in random.sample(Dvalin_Loot, 2):
            globals()[x] = eval(x) + 1
        Dvalin_Body_Count += 1
        for x in random.sample(Wolf_Loot, 2):
            globals()[x] = eval(x) + 1
        Wolf_Body_Count += 1
        for x in random.sample(Childe_Loot, 2):
            globals()[x] = eval(x) + 1
        Childe_Body_Count += 1
        for x in random.sample(Azhdaha_Loot, 2):
            globals()[x] = eval(x) + 1
        Azhdaha_Body_Count += 1
 

def Do_Daily():
    global Adventure_EXP
    global Companionship_EXP
    global Mora_Cost
    global Primogems
    global Check_Daily_Minutes
    ####Daily Commisions Function thing
    Adventure_EXP += 1500 #(1000 + 500)
    Companionship_EXP += 280 #(180 + 100) #2 NPC comms, worth 35, and 2 generic quests, "Kill Quests" as I'll call them, worth 55
    Mora_Cost -= 22550 #(10225 + 12325) #^
    Primogems += 60 #(40 + 20)
    Check_Daily_Minutes -= 1440
    if Get_Sliver:
        try:
            Daily_Element = random.choice(["Anemo", "Cryo", "Electro", "Geo", "Hydro", "Pyro"])
            Daily_Element = Daily_Element + "Fragment"
            globals()[Daily_Element] = eval(Daily_Element) + 1
        except:
            pass



Minutes_Spent_Resin = 0
Check_Daily_Minutes = 0 
Total_Resin = 160
Mora_Cost = 0
Resin_Count = 160
Adventure_EXP = 0
Companionship_EXP = 0
Primogems = 0

EXP_Blossom_Count = 0
Rhodia_Count = 0
Mora_Blossom_Count = 0
Mondstat_Domain_Count = 0
Liyue_Domain_Count = 0
Any_Artifact_Domain_Count = 0
Mondstat_Domain_Count2 = 0#Might aswell count which province domain im doing for weapon Ascention materials
Liyue_Domain_Count2 = 0
 

Wits = 0
Experience = 0
Advice = 0
Three_Star_Artifacts = 0
Four_Star_Artifacts = 0
Mystic_Enchancement = 0
Magic_Crystal_Needed = 0
Spares = False



PrimoShards = 0
 

for _ in range(len(Characters_List)):#Do for every character in the Dictionary
    Character_EXP = 0
    Name = random.choice(list(Characters_List.keys()))#Do in a random order just for entertainment purposes
    Character = Characters_List.pop(Name)#Get which character they are
    Element = Character[0] #what element they are
    WiiSports = Character[1] #and their required Materials, shortened to mat, lenghtned to Matt, lenghtned to WiiSports
    Teachings = Character[2] #Talent level up
    WeaponName = Character[3] #Weapon
    Ascentions = Character[4] #Weapon level up
 
    ####Variable Making
    ElementFragment = Element + "Fragment"
    ElementShard = Element + "Shard"
    ElementChunk = Element + "Chunk"
    ElementGem = Element + "Gem"
    ElementBossSpecific = Element + "Boss"
    ElementBossBodyCount = Element + "BodyCount"
    if Name in Needs_CryoCube:
        ElementBossSpecific = Element + "2Boss"
        ElementBossBodyCount = Element + "2BodyCount"
    TeachingsCommon = Teachings + "Common"
    TeachingsRare = Teachings + "Rare"
    TeachingsEpic = Teachings + "Epic"
    if Teachings in ["Freedom", "Resistance", "Ballad"]:#Counting each domain
        Talent_Domain = "Mondstat_Domain_Count"
    else:
        Talent_Domain = "Liyue_Domain_Count"
    AscentionsUncommon = Ascentions + "Uncommon"
    AscentionsRare = Ascentions + "Rare"
    AscentionsEpic = Ascentions + "Epic"
    AscentionsLeggy = Ascentions + "Leggy"
    if Ascentions in ["Decarabian", "Wolf", "Dandelion"]:#Counting each domain
        Weapon_Domain = "Mondstat_Domain_Count2"
    else:
        Weapon_Domain = "Liyue_Domain_Count2"
 

    if ElementFragment not in globals():#Im too lazy to write out each variable, so I'll force python to do it for me
        globals()[ElementFragment] = 0
        globals()[ElementShard] = 0
        globals()[ElementChunk] = 0
        globals()[ElementGem] = 0
    if ElementBossSpecific not in globals():
        globals()[ElementBossSpecific] = 0
        globals()[ElementBossBodyCount] = 0
    if TeachingsCommon not in globals():
        globals()[TeachingsCommon] = 0
        globals()[TeachingsRare] = 0
        globals()[TeachingsEpic] = 0
    if AscentionsUncommon not in globals():
        globals()[AscentionsUncommon] = 0
        globals()[AscentionsRare] = 0
        globals()[AscentionsEpic] = 0
        globals()[AscentionsLeggy] = 0
 

    if Name != "TravelerG": #Subtract Traveler 2's EXP cost, since a lvl 90 Anemo is also a lvl 90 Geo. oh and their weapon too. None of that allowed
        ####Character EXP
        while Character_EXP < 8363300: #Level character to 90 based on Ley Lines
            Minutes_Spent_Resin += 8
            Resin_Count += 1
            Total_Resin += 1
            
            Check_Daily_Minutes += 8
            if Check_Daily_Minutes >= 1440:
                Do_Daily()

            if EXP_Method == "EXP":
                if Resin_Count >= 20:
                    EXP_Blossom_Count += 1
                    Wits += random.randint(4, 5)
                    Experience += random.randint(6, 7)
                    Resin_Count -= 20
                    Adventure_EXP += 100
                    Companionship_EXP += 20

            if EXP_Method == "RhoRage":
                if Resin_Count >= 40:
                    Rhodia_Count += 1
                    Wits += 10
                    Experience += random.randint(16, 18)
                    Advice += random.randint(19, 21)
                    Adventure_EXP += 200
                    Companionship_EXP += 40

            if Advice > 0:
                Advice - 1
                Character_EXP += 1000
                Mora_Cost += 200

            if Experience > 0:
                Experience -= 1
                Character_EXP += 5000
                Mora_Cost += 1000
 

            if Wits > 0:#Instead of adding EXP directly, this allows EXP to carry over to other Characters
                Wits -= 1
                Character_EXP += 20000
                Mora_Cost += 4000
        Mora_Cost += 420000 #(20,000 + 40,000 + 60,000 + 80,000 + 100,000 + 120,000) #Character Ascention Costs

        ####Weapons
        Weapon_EXP = 0#Its weapon time
        while Weapon_EXP < 9064450:#Might aswell save 1 line and do this under the same "If" statement
            Minutes_Spent_Resin += 8#I would have normally put weapons at the very end but thats ok
            Resin_Count += 1
            Total_Resin += 1

            Check_Daily_Minutes += 8
            if Check_Daily_Minutes >= 1440:
                Do_Daily()

            if Resin_Count >= 10:
                Magic_Crystal_Needed += 3
                Resin_Count -= 10
                Mystic_Enchancement += 6
                Mora_Cost += 100
                Adventure_EXP += 50
                Companionship_EXP += 10
 

            if Spares:
                Weapon_EXP += Spare_EXP
                Mora_Cost += Spare_EXP/5
                Spare_EXP = 0
                Spares = False
            
            if Mystic_Enchancement > 0:
                Mystic_Enchancement -= 1
                Weapon_EXP += 10000
                Mora_Cost += 1000
                if Weapon_EXP > 9064450:
                    Spare_EXP = Weapon_EXP - 9064450 #I could put this in one line but im too lazy
                    Spare_EXP = Spare_EXP/400
                    Spare_EXP = math.floor(Spare_EXP)
                    Spare_EXP = Spare_EXP * 400
                    Spares = True
 
        ####Weapon Ascention Materials
        while True:
            Minutes_Spent_Resin += 8
            Resin_Count += 1
            Total_Resin += 1

            Check_Daily_Minutes += 8
            if Check_Daily_Minutes >= 1440:
                Do_Daily()

            if Resin_Count >= 20:
                globals()[Weapon_Domain] = eval(Weapon_Domain) + 1
                globals()[AscentionsUncommon] = eval(AscentionsUncommon) + 3
                globals()[AscentionsRare] = eval(AscentionsRare) + 2
                Resin_Count -= 20
                Mora_Cost -= 2200
                Adventure_EXP += 100
                Companionship_EXP += 20

            
            #Since I did the Talent Domains, and bosses Code first, this is all techincally stolen from down below.
            if eval(AscentionsLeggy) < 6: #Check if we have enough leggy
                if eval(AscentionsEpic) >= 3: #Try and craft a leggy
                    globals()[AscentionsLeggy] = eval(AscentionsLeggy) + 1
                    globals()[AscentionsEpic] = eval(AscentionsEpic) - 3
                    Mora_Cost += 1075
 

            if eval(AscentionsEpic) < 14: #Check if we have enough epic
                if eval(AscentionsRare) >= 3: #Try and craft a epic
                    globals()[AscentionsEpic] = eval(AscentionsEpic) + 1
                    globals()[AscentionsRare] = eval(AscentionsRare) - 3
                    Mora_Cost += 350
            
            if eval(AscentionsRare) < 14: #Check if we have enough uncommon
                if eval(AscentionsUncommon) >= 3: #Try and craft a uncommon
                    globals()[AscentionsRare] = eval(AscentionsRare) + 1
                    globals()[AscentionsUncommon] = eval(AscentionsUncommon) - 3
                    Mora_Cost += 125
 

            if eval(AscentionsLeggy) >= 6 and eval(AscentionsEpic) >= 14 and eval(AscentionsRare) >= 14 and eval(AscentionsUncommon) >= 5:#Im going to check all at once because I dont trust myself to use my previous statements, that are also checking for quantity of chunks and shards
                globals()[AscentionsLeggy] = eval(AscentionsLeggy) - 6
                globals()[AscentionsEpic] = eval(AscentionsEpic) - 14
                globals()[AscentionsRare] = eval(AscentionsRare) - 14
                globals()[AscentionsUncommon] = eval(AscentionsUncommon) - 5
                break #exit the loop
        print(WeaponName + " Maxed...")#Just so that I know things are actually going on, and a loop isnt running inifnitely because I wrote some code wrong
        Mora_Cost += 5000 #(Cant find the data on the wiki so I've gotta do it myself in game, and I don't feel like leveling up a weapon rn)

    ####Character Talent Materials (Weekly Bosses)  
    while not Boss_Check(WiiSports): #Check if we have enough weekly boss materials
        Minutes_Spent_Resin += 8
        Resin_Count += 1
        Total_Resin += 1

        Check_Daily_Minutes += 8
        if Check_Daily_Minutes >= 1440:
            Do_Daily()

        if Boss_Method == 1:
            if Resin_Count >= 30:#Half off weekly bosses
                Boss_Loot(WiiSports)
                Weeks_Waited += 1
                Resin_Count -= 30
                Mora_Cost -= 8100 #Assuming LVL 90 bosses
                Adventure_EXP += 300
                Companionship_EXP += 70
            
        if Boss_Method == 4:
            if Resin_Count >= 150:#3 attempts weekly, for half off Trounce Domains and Wolf, but there are 4 bosses so its 30*3 + 60, rather than 30*4
                Boss_Loot("ALL")
                Weeks_Waited += 1
                Resin_Count -= 150
                Mora_Cost -= 32400
                Adventure_EXP += 1200
                Companionship_EXP += 280


    ####Character Ascention Materials (Bosses)
    if Name not in ["TravelerA", "TravelerG"]: #Traveler doesnt require Anemo or Geo materials, so exclude them
        while True: #just loops untill all conditions inside are met
            Minutes_Spent_Resin += 8
            Resin_Count += 1
            Total_Resin += 1

            Check_Daily_Minutes += 8
            if Check_Daily_Minutes >= 1440:
                Do_Daily()

            if Resin_Count >= 40:
                globals()[ElementBossBodyCount] = eval(ElementBossBodyCount) + 1
                globals()[ElementFragment] = eval(ElementFragment) + 3
                globals()[ElementShard] = eval(ElementShard) + 2
                globals()[ElementBossSpecific] = eval(ElementBossSpecific) + 2
                Resin_Count -= 40
                Mora_Cost -= 5200
                Adventure_EXP += 200
                Companionship_EXP += 45
 

            if eval(ElementGem) < 6: #Check if we have enough gems
                if eval(ElementChunk) >= 3: #Try and craft a gem
                    globals()[ElementGem] = eval(ElementGem) + 1
                    globals()[ElementChunk] = eval(ElementChunk) - 3
                    Mora_Cost += 2700
 

            if eval(ElementChunk) < 9: #Check if we have enough chunks
                if eval(ElementShard) >= 3: #Try and craft a chunk
                    globals()[ElementChunk] = eval(ElementChunk) + 1
                    globals()[ElementShard] = eval(ElementShard) - 3
                    Mora_Cost += 900
            
            if eval(ElementShard) < 9: #Check if we have enough shards
                if eval(ElementFragment) >= 3: #Try and craft a shard
                    globals()[ElementShard] = eval(ElementShard) + 1
                    globals()[ElementFragment] = eval(ElementFragment) - 3
                    Mora_Cost += 300
 

            if eval(ElementGem) >= 6 and eval(ElementChunk) >= 9 and eval(ElementShard) >= 9 and eval(ElementFragment) >= 1:#Im going to check all at once because I dont trust myself to use my previous statements, that are also checking for quantity of chunks and shards
                if Name not in Needs_PrimoGeovishap:
                    if eval(ElementBossSpecific) > 46:
                        globals()[ElementGem] = eval(ElementGem) - 6
                        globals()[ElementChunk] = eval(ElementChunk) - 9
                        globals()[ElementShard] = eval(ElementShard) - 9
                        globals()[ElementFragment] = eval(ElementFragment) - 1
                        globals()[ElementBossSpecific] = eval(ElementBossSpecific) - 46
                        break #exit the loop
                else:
                    globals()[ElementGem] = eval(ElementGem) - 6
                    globals()[ElementChunk] = eval(ElementChunk) - 9
                    globals()[ElementShard] = eval(ElementShard) - 9
                    globals()[ElementFragment] = eval(ElementFragment) - 1
                    break #exit the loop


        ####Character Ascention Materials (Specifically Primogeovishaps)
        if Name in Needs_PrimoGeovishap: 
            while PrimoShards < 46:
                Minutes_Spent_Resin += 8
                Resin_Count += 1
                Total_Resin += 1

                Check_Daily_Minutes += 8
                if Check_Daily_Minutes >= 1440:
                    Do_Daily()

                if Resin_Count >= 40:
                    PrimoVishapBodyCount += 1
                    PrimoShards += 3
                    Resin_Count -= 40
                    Mora_Cost -= 5200
                    Adventure_EXP += 200
                    Companionship_EXP += 45
            PrimoShards -= 46

        ####Character Talent Materials (Domain Based)
        while True:#Might aswell do the Teachings and what not under the same "If"
            Minutes_Spent_Resin += 8
            Resin_Count += 1
            Total_Resin += 1

            Check_Daily_Minutes += 8
            if Check_Daily_Minutes >= 1440:
                Do_Daily()

            if Resin_Count >= 20:
                globals()[Talent_Domain] = eval(Talent_Domain) + 1
                globals()[TeachingsCommon] = eval(TeachingsCommon) + 3
                globals()[TeachingsRare] = eval(TeachingsRare) + 2
                Resin_Count -= 20
                Mora_Cost -= 2375
                Adventure_EXP += 100
                Companionship_EXP += 20
            
            if eval(TeachingsEpic) < 114: #Check if we have enough gems
                if eval(TeachingsRare) >= 3: #Try and craft an Epic
                    globals()[TeachingsEpic] = eval(TeachingsEpic) + 1
                    globals()[TeachingsRare] = eval(TeachingsRare) - 3
                    Mora_Cost += 550
            
            if eval(TeachingsRare) < 63: #Check if we have enough gems
                if eval(TeachingsCommon) >= 3: #Try and craft an Epic
                    globals()[TeachingsRare] = eval(TeachingsRare) + 1
                    globals()[TeachingsCommon] = eval(TeachingsCommon) - 3
                    Mora_Cost += 175
            
            if eval(TeachingsEpic) >= 114 and eval(TeachingsRare) >= 63 and eval(TeachingsCommon) >= 9:
                globals()[TeachingsEpic] = eval(TeachingsEpic) - 114
                globals()[TeachingsRare] = eval(TeachingsRare) - 63
                globals()[TeachingsCommon] = eval(TeachingsCommon) - 9
                break
    else: #Since both Travelers dont follow traditional Teachings methods
        if Teachings == "ThreeMondstat":
            TeachingsList = {#Use a janky method to save code space, rather than have to copy and paste the domain code 3 times for each teaching
                "Freedom": (9, 18, 18),
                "Resistance": (0, 33, 36),
                "Ballad": (0, 12, 60)
            }
        if Teachings == "Everything":#I am using really janky methods to save space
            TeachingsList = {
                "Freedom": (3, 6, 6),
                "Resistance": (0, 11, 12),
                "Ballad": (0, 4, 20),
                "Prosperity": (6, 12, 12),
                "Dilligence": (0, 22, 24),
                "Gold": (0, 8, 40)
            }
        
        for x in range(len(TeachingsList)):
            Teachings = random.choice(list(TeachingsList.keys()))
            TeachingsCommon = Teachings + "Common"#Reuse previous code lol
            TeachingsRare = Teachings + "Rare"
            TeachingsEpic = Teachings + "Epic"
            if TeachingsCommon not in globals(): #Create variables just incase they havent already been made
                globals()[TeachingsCommon] = 0
                globals()[TeachingsRare] = 0
                globals()[TeachingsEpic] = 0
 

            Teaching2 = TeachingsList.pop(Teachings)
            Common_Needed = Teaching2[0]
            Rare_Needed = Teaching2[1]
            Epic_Needed = Teaching2[2]
 

            if Teachings in ["Freedom", "Resistance", "Ballad"]:#Counting each domain
                Talent_Domain = "Mondstat_Domain_Count"
            else:
                Talent_Domain = "Liyue_Domain_Count"
 

            while True:#this is literally the same code from above lol
                Minutes_Spent_Resin += 8
                Resin_Count += 1
                Total_Resin += 1

                Check_Daily_Minutes += 8
                if Check_Daily_Minutes >= 1440:
                    Do_Daily()

                if Resin_Count >= 20:
                    globals()[Talent_Domain] = eval(Talent_Domain) + 1
                    globals()[TeachingsCommon] = eval(TeachingsCommon) + 3
                    globals()[TeachingsRare] = eval(TeachingsRare) + 2
                    Resin_Count -= 20
                    Mora_Cost -= 2375
                    Adventure_EXP += 100
                    Companionship_EXP += 20
                
                if eval(TeachingsEpic) < Epic_Needed: #Check if we have enough books
                    if eval(TeachingsRare) >= 3: #Try and craft an Epic
                        globals()[TeachingsEpic] = eval(TeachingsEpic) + 1
                        globals()[TeachingsRare] = eval(TeachingsRare) - 3
                        Mora_Cost += 550
                
                if eval(TeachingsRare) < Rare_Needed: #Check if we have enough books
                    if eval(TeachingsCommon) >= 3: #Try and craft an Epic
                        globals()[TeachingsRare] = eval(TeachingsRare) + 1
                        globals()[TeachingsCommon] = eval(TeachingsCommon) - 3
                        Mora_Cost += 175
                
                if eval(TeachingsEpic) >= Epic_Needed and eval(TeachingsRare) >= Rare_Needed and eval(TeachingsCommon) >= Common_Needed:
                    globals()[TeachingsEpic] = eval(TeachingsEpic) - Epic_Needed
                    globals()[TeachingsRare] = eval(TeachingsRare) - Rare_Needed
                    globals()[TeachingsCommon] = eval(TeachingsCommon) - Common_Needed
                    break

    print(Name + " Maxed...")#Just so that I know things are actually going on, and a loop isnt running inifnitely because I wrote some code wrong
    print('-')#Break text



####Artifacts
for x in range(Character_Count_x5):#5, 5-Star artifacts for each character, Both Travelers are included, because maybe you want one Anemo set up, and one Geo setup
    Artifact_EXP = 0
    while Artifact_EXP < 269800:
        Minutes_Spent_Resin += 8
        Resin_Count += 1
        Total_Resin += 1

        Check_Daily_Minutes += 8
        if Check_Daily_Minutes >= 1440:
            Do_Daily()

        if Resin_Count >= 20:
            Any_Artifact_Domain_Count += 1
            Resin_Count -= 20
            Mora_Cost -= 2525 
            Three_Star_Artifacts += 6
            Four_Star_Artifacts += 2
            Adventure_EXP += 100
            Companionship_EXP += 20
 

        if Four_Star_Artifacts > 0:
            Four_Star_Artifacts -= 1
            Artifact_EXP += 2520
            Mora_Cost += 2520
 

        if Three_Star_Artifacts > 0: #Instead of just adding EXP directly on, this lets any spare artifacts carry over.
            Three_Star_Artifacts -= 1
            Artifact_EXP += 1260
            Mora_Cost += 1260
print(str(Character_Count_x5) + " artifacts maxed...")


####Mora Outcrops
print("")
print("")
print("Mora Cost (Before Mora Blossoms): " + str(Mora_Cost))#I also dont know how Escape percents or what ever they're called work, so yeah
while Mora_Cost > 0:
    Minutes_Spent_Resin += 8
    Resin_Count += 1
    Total_Resin += 1

    Check_Daily_Minutes += 8
    if Check_Daily_Minutes >= 1440:
        Do_Daily()

    if Resin_Count >= 20:
        Resin_Count -= 20
        Mora_Cost -= 60000
        Mora_Blossom_Count += 1
        Adventure_EXP += 100
        Companionship_EXP += 20


Days_Spent_Resin = round(Minutes_Spent_Resin/1440, 2)
Weeks_Spent_Resin = round(Minutes_Spent_Resin/10080, 2)
Years_Spent_Resin = round(Minutes_Spent_Resin/525600, 2)
Minutes_Spent_Bosses = Weeks_Waited*10080
Years_Spent_Bosses = round(Weeks_Waited/52.143, 2)


print("")
while Character_Count_Over4 > 0:#You literally have so much spare Companionship EXP I literally dont need to do anything fancy
    if Companionship_EXP >= 29100:
        Companionship_EXP -= 29100
        Character_Count_Over4 -= 1
        print("Another 4 characters companionship EXP Maxed...")

Mora_Cost = Mora_Cost*-1 #Negative Mora cost, is positive Spare Mora
Wishes = round(Primogems/160, 2)

CopyGlobals = globals()
for x in CopyGlobals: #use an illegal method to convert every variable into a string, so that I dont have to do str() in my print statements
    globals()[x] = str(eval(x))

####Print Statements
print("---")
print("Resin:")
print("     Minutes Spent waiting for Resin: " + Minutes_Spent_Resin)
print("     Days Spent waiting for Resin: " + Days_Spent_Resin)
print("     Weeks Spent waiting for Resin: " + Weeks_Spent_Resin)
print("     Years Spent waiting for Resin: " + Years_Spent_Resin)
print("     Resin Spent: " + Total_Resin)
print("")
print("")
try:
    print("Domains, Outcrops and Mining: ")
    if EXP_Blossom_Count == "0":
        print("    Rhodia Body Count " + Rhodia_Count)
    if Rhodia_Count == "0":
        print("    EXP Ley Line Outcrops: " + EXP_Blossom_Count)
    print("    Mora Ley Line Outcrops: " + Mora_Blossom_Count)
    print("    Mondstat Talent Domains: " + Mondstat_Domain_Count)
    print("    Liyue Talent Domains: " + Liyue_Domain_Count)
    print("    Artifact Domains: " + Any_Artifact_Domain_Count)
    print("    Mondstat Weapon Ascention Domains: " + Mondstat_Domain_Count2)
    print("    Liyue Weapon Ascention Domains: " + Liyue_Domain_Count2)
    print("    Magic Crystals: " + Magic_Crystal_Needed)
except:
    pass
print("")
print("")
try:
    print("Bosses:")
    print("     Dvalin's Body Count: " + Dvalin_Body_Count)#Body count as in how many of their bodies we have, not how many bodies they have. As in 100 Dvalin corpses, not the corpses of 100 people that Dvalin has slain.
    print("     Wolf's Body Count: " + Wolf_Body_Count)
    print("     Childe's Body Count: " + Childe_Body_Count)
    print("     Azhdaha's Body Count: " + Azhdaha_Body_Count)
    print("     Weeks Spent waiting for Weekly Bosses: " + Weeks_Waited)
    print("     Minutes Spent waiting for Weekly Bosses: " + Minutes_Spent_Bosses)
    print("     Years Spent waiting for Weekly Bosses: " + Years_Spent_Bosses)
    if int(Minutes_Spent_Bosses) > int(Minutes_Spent_Resin):
        print("          Time spent waiting for weekly bosses is greater than time spent waiting for resin,")
        print("          Therefore, time spent waiting for resin is irrelevant.")
    else:
        print("          Time spent waiting for resin is greater than time spent waiting for weekly bosses,")
        print("          Therefore, time spent waiting for weekly bosses is irrelevant.")
    print("")
    print("     Anemo Hypostasis' Body Count: " + AnemoBodyCount)#Once again, is how many of their bodies We have. Anemo Hypostasis' Body, as in the body of the Hypostasis, Count, as in how many we have. How many of the Anemo Hypostasis bodies do we have
    print("     Cryo Regisvine's Body Count: " + CryoBodyCount)
    print("     Cryo Hypostasis's Body Count: " + Cryo2BodyCount)
    print("     Electro Hypostasis' Body Count: " + ElectroBodyCount)
    print("     Geo Hypostasis' Body Count: " + GeoBodyCount)
    print("     Oceanid's Body Count: " + HydroBodyCount)
    print("     Pyro Regisvine Body Count: " + PyroBodyCount)
    print("     Primo Geovishap Body Count: " + PrimoVishapBodyCount)
except:
    pass
print("")
print("")
import time
try:
    print("Spare Loot:")
    print("     Heros Wits: " + Wits)
    print("     Adventurers Experience: " + Experience)
    print("     Three-Star Artifacts: " + Three_Star_Artifacts)
    print("     Four-Star Artifacts: " + Four_Star_Artifacts)
    print("")
    print("     Mora: " + Mora_Cost)
    print("     Adventure EXP: " + Adventure_EXP)
    print("     Companionship EXP: " + Companionship_EXP)
    print("     Primogems: " + Primogems)#Most likely spent on getting all of those damn 5 stars lol, so many 5 stars and 5 star weapons holy
    print("          Individual Wishes: " + Wishes)
    print("")
    print("     Dvalin's Plumes: " + Plume)
    print("     Dvalin's Claws: " + Claw)
    print("     Dvalin's Sighs: " + Sigh)
    print("     Tail of Boreas': " + Tail)
    print("     Ring of Boreas': " + Ring)
    print("     Spirit Locket of Boreas': " + Locket)
    print("     Tusk of Monoceros Caelis: " + Tusk)
    print("     Shard of a Foul Legacys: " + Legacy)
    print("     Shadow of the Warriors: " + Shadow)
    print("     Dragon Lord's Crowns:" + Crown)
    print("     Bloodjade Branches: " + Branch)
    print("     Gilded Scales: " + Scale)
    print("")
    print("     Anemo Slivers: " + AnemoFragment) #ok fine i just found out what they're called in-game
    print("     Anemo Fragments: " + AnemoShard) #I tried renaming these variables to include an _ between words, but everything just breaks. sorry
    print("     Hurricane Seeds: " + AnemoBoss) #Which also means I can't fix the name of the variable to match its in game name
    print("     Cryo Slivers: " + CryoFragment) 
    print("     Cryo Fragments: " + CryoShard)#Oh also, you're going to get a lot of "Undefined Variables", yeah just ignore him he's harmless
    print("     Hoarfrost Cores: " + CryoBoss)
    print("     Crystalline Bloom: " + Cryo2Boss)
    print("     Electro Slivers: " + ElectroFragment)
    print("     Electro Fragmenets: " + ElectroShard)
    print("     Lightning Prisims: " + ElectroBoss)
    print("     Geo Slivers: " + GeoFragment)
    print("     Geo Fragments: " + GeoShard)
    print("     Basalt Pillars: " + GeoBoss)
    print("     Hydro Slivers: " + HydroFragment)
    print("     Hydro Fragments: " + HydroShard)
    print("     Clensing Hearts: " + HydroBoss)
    print("     Pyro Slivers: " + PyroFragment)
    print("     Pyro Fragments: " + PyroShard)
    print("     Everflame Seeds: " + PyroBoss)
    print("     Juvenile Jades: " + PrimoShards)
    print("")
    print("     Tile of Decarabian's Tower: " + DecarabianUncommon)
    print("     Debris of Decarabian's City: " + DecarabianRare)
    print("     Boreal Wolf's Milk Tooth: " + WolfUncommon)
    print("     Boreal Wolf's Cracked Tooth: " + WolfRare)
    print("     Fetters of the Dandelion Gladiator: " + DandelionUncommon)
    print("     Chains of the Dandelion Gladiator: " + DandelionRare)
    print("     Luminous Sands from Guyun: " + GuyunUncommon)
    print("     Lustrous Stone from Guyun: " + GuyunRare)
    print("     Mist Veiled Lead Elixir: " + ElixerUncommon)
    print("     Mist Veiled Mercury Elixir: " + ElixerRare)
    print("     Grain of Aerosiderite: " + Aero_ChocolateUncommon)
    print("     Peice of Aerosiderite: " + Aero_ChocolateRare)
    print("")
    print("     Mystic Enchancement: " + Mystic_Enchancement)
    Hello = ForceExceptLol
except:
    time.sleep(5000)
