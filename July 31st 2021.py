import random
import math

#Crtl + f "####" for navigaton purposes
#-

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
#I find it kind of sus that you have like thousands of slivers by the time this """simulation""" is done, so you can easily choose if you want to trust these thousands of slivers here
#Options are True or False
Get_Sliver = True

#Serenity Pot
#What do you want to buy from the teapot
#Nvm not added yet :p

####Material Keys
#I shorten materials such as boss drops and domain drops, so I've just included a list here for reference

#Boss Stuff = ["Plume", "Claw", "Sigh", "Tail", "Ring", "Locket", "Tusk", "Legacy", "Shadow", "Crown", "Branch", "Scale"]
#Character Talent Stuff = ["Freedom", "Resistance", "Ballad", "Prosperity", "Diligence", "Gold", "Transience", "Elegance", "Light"]
#Weapon Ascention Stuff = ["Decarabian", "Wolf", "Dandelion", "Guyun", "Elixer", "Aero_Chocolate", "Branch2", "Narukami", "Mask"]
#Common Ascention Materials are ignored, as you can grind them while waiting for resin, so they dont add any time.

####Characters
Characters_List = {
    #"Name": (Element, "Weekly Boss", "Domain Talent Material", "Weapon Name", "Weapon Ascention Material")
    "Venti": ("Anemo", "Tail", "Ballad", "Skyward Harp", "Wolf"), #-
    "Sucrose": ("Anemo", "Locket", "Freedom", "Skyward Atlas", "Wolf"), #- 
    "Jean": ("Anemo", "Plume", "Resistance", "Aquila Favonia", "Decarabian"), #+
    "TravelerA": ("Anemo", "Sigh", "ThreeMondstat", "Skyward Blade", "Wolf"), #+
    "Xiao": ("Anemo", "Shadow", "Prosperity", "Primordial Jade Winged-Spear", "Guyun"), #+
    "Kazuha":("Anemo", "Scale", "Diligence", "Freedom-Sworn", "Decarabian"),#+
 

    "Qiqi": ("Cryo", "Tail", "Prosperity", "Skyward Blade", "Wolf"), #+
    "Kaeya": ("Cryo", "Locket", "Ballad", "Aquila Favonia", "Decarabian"), #+
    "Chongyun": ("Cryo", "Sigh", "Diligence", "Skyward Pride", "Wolf"), #+
    "Diona": ("Cryo", "Legacy", "Freedom", "Amos' Bow", "Dandelion"),
    "Ganyu": ("Cryo", "Shadow", "Diligence", "Amos' Bow", "Dandelion"), #+
    "Rosaria": ("Cryo", "Shadow", "Ballad", "Staff of Homa", "Aero_Chocolate"), #+
    "Eula":("Cryo", "Crown", "Resistance", "Song of Broken Pines", "Decarabian"), #+
    "Ayaka":("Cyro", "Branch", "Elegance", "Mistsplitter Reforged", "Branch2"),#+
    

    "Keqing": ("Electro", "Ring", "Prosperity", "Aquila Favonia", "Decarabian"), #+
    "Fishcl": ("Electro", "Locket", "Ballad", "Skyward Harp", "Wolf"), #+
    "Lisa": ("Electro", "Claw", "Ballad", "Lost Prayer to the Sacred Winds", "Dandelion"),
    "Razor": ("Electro", "Claw", "Resistance", "Wolf's Gravestone", "Dandelion"), #+
    "Beidou": ("Electro", "Sigh", "Gold", "Wolf's Gravestone", "Dandelion"), #+
    "TravelerE":("Electro", "Crown", "ThreeInazuma", "Better than Anemo but worse than Geo", "None"),
 

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
    "Xiangling": ("Pyro", "Claw", "Diligence", "Skyward Spine", "Dandelion"), #+
    "Amber": ("Pyro", "Sigh", "Freedom", "Amos' Bow", "Dandelion"), #+
    "Xinyan": ("Pyro", "Tusk", "Gold", "The Unforged", "Elixer"), #+
    "Hu Tao": ("Pyro", "Legacy", "Diligence", "Staff of Homa", "Aero_Chocolate"), #+
    "Yanfei": ("Pyro", "Branch", "Gold", "Lost Prayer to the Sacred Winds", "Dandelion"), #+
}

if len(Only_Do) >= 1:
    for Key in Characters_List.copy().keys():
        if Key not in Only_Do:
            Characters_List.pop(Key)

Needs_PrimoGeovishap = ["Xiao", "Rosaria", "Hu Tao"]
Needs_CryoCube = ["Eula"]
Needs_MaguuKenki = ["Kazuha"]
Needs_PyroCube = []
Needs_MechaCube = ["Ayaka"]


####No more human input required below this line


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

####Variables Before Functions
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
MaguuBodyCount = 0
MechaCubeBodyCount = 0

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


####Variables After Functions
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
Inazuma_Domain_Count = 0
Any_Artifact_Domain_Count = 0
Mondstat_Domain_Count2 = 0 #Might aswell count which province domain im doing for weapon Ascention materials
Liyue_Domain_Count2 = 0
Inazuma_Domain_Count2 = 0
 

Wits = 0
Experience = 0
Advice = 0
Three_Star_Artifacts = 0
Four_Star_Artifacts = 0
Mystic_Enchancement = 0
Magic_Crystal_Needed = 0
Spares = False

PrimoShards = 0
MarionetteCore = 0
Perpetual_Heart = 0
 
Math_Var_1 = 0 #Generic Variable made for math, instead of making like 700 new ones for every item. 
Math_Var_2 = 0 #another one

for _ in range(len(Characters_List)):#Do for every character in the Dictionary
    Name = random.choice(list(Characters_List.keys()))#Do in a random order just for entertainment purposes
    Character = Characters_List.pop(Name)#Get which character they are
    Element = Character[0] #what element they are
    WiiSports = Character[1] #and their required Materials, shortened to mat, lenghtned to Matt, lenghtned to WiiSports
    Teachings = Character[2] #Talent level up
    WeaponName = Character[3] #Weapon
    Ascentions = Character[4] #Weapon level up
 
    ####Cheating Variable Making
    ElementFragment = Element + "Fragment"
    ElementShard = Element + "Shard"
    ElementChunk = Element + "Chunk"
    ElementGem = Element + "Gem"
    ElementBossSpecific = Element + "Boss"
    ElementBossBodyCount = Element + "BodyCount"
    if Name in Needs_CryoCube or Name in Needs_PyroCube:#Second Elemental Boss Variants
        ElementBossSpecific = Element + "2Boss"
        ElementBossBodyCount = Element + "2BodyCount"
    TeachingsCommon = Teachings + "Common"
    TeachingsRare = Teachings + "Rare"
    TeachingsEpic = Teachings + "Epic"
    if Teachings in ["Freedom", "Resistance", "Ballad"]:#Counting each domain
        Talent_Domain = "Mondstat_Domain_Count"
    elif Teachings in ["Prosperity", "Diligence", "Gold"]:
        Talent_Domain = "Liyue_Domain_Count"
    elif Teachings in ["Transience", "Elegance", "Light"]:
        Talent_Domain = "Inazuma_Domain_Count"
    AscentionsUncommon = Ascentions + "Uncommon"
    AscentionsRare = Ascentions + "Rare"
    AscentionsEpic = Ascentions + "Epic"
    AscentionsLeggy = Ascentions + "Leggy"
    if Ascentions in ["Decarabian", "Wolf", "Dandelion"]:#Counting each domain
        Weapon_Domain = "Mondstat_Domain_Count2"
    elif Ascentions in ["Guyun", "Elixer", "Aero_Chocolate"]:
        Weapon_Domain = "Liyue_Domain_Count2"
    elif Ascentions in ["Branch", "Narukami", "Mask"]:
        Weapon_Domain = "Inazuma_Domain_Count2"

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
 

    if Name not in ["TravelerG", "TravelerE"]: #Subtract Traveler 2 and 3's EXP cost, since a lvl 90 Anemo is also a lvl 90 Geo. oh and their weapon too. None of that allowed
        ####Character EXP
        Character_EXP_Needed = 8363300 #Now counts down from 8.3m, rather than count up from 0. Saves me a step later.
        while Character_EXP_Needed > 0: #Level character to 90 based on Ley Lines
            Minutes_Spent_Resin += 80 #(8*10) 
            Resin_Count += 10 #(1*10)
            Total_Resin += 10 #(1*10)
            
            Check_Daily_Minutes += 80 #(8*10)
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

            if Advice > 0:#Instead of adding EXP directly, this allows EXP to carry over to other Characters
                Math_Var_1 = math.ceil(Character_EXP_Needed/1000)#check how many advice we need
                if Math_Var_1 > Advice:#if we need more than we have, use em all
                    Character_EXP_Needed -= 1000*Advice
                    Mora_Cost += 200*Advice
                    Advice = 0
                elif Math_Var_1 < Advice:#if we need less than we have, only take away as many as we need
                    Math_Var_2 = Advice - Math_Var_1
                    Character_EXP_Needed -=1000*Math_Var_2
                    Mora_Cost += 200*Math_Var_2
                    Advice -= Math_Var_2

            if Experience > 0:
                Math_Var_1 = math.ceil(Character_EXP_Needed/5000)#check how many Experience we need
                if Math_Var_1 > Experience:#if we need more than we have, use em all
                    Character_EXP_Needed -= 5000*Experience
                    Mora_Cost += 1000*Experience
                    Experience = 0
                elif Math_Var_1 < Experience:#if we need less than we have, only take away as many as we need
                    Math_Var_2 = Experience - Math_Var_1
                    Character_EXP_Needed -=5000*Math_Var_2
                    Mora_Cost += 1000*Math_Var_2
                    Experience -= Math_Var_2
 

            if Wits > 0:
                Math_Var_1 = math.ceil(Character_EXP_Needed/20000)#check how many Wits we need
                if Math_Var_1 > Wits:#if we need more than we have, use em all
                    Character_EXP_Needed -= 20000*Wits
                    Mora_Cost += 4000*Wits
                    Wits = 0
                elif Math_Var_1 < Wits:#if we need less than we have, only take away as many as we need
                    Math_Var_2 = Wits - Math_Var_1
                    Character_EXP_Needed -=20000*Math_Var_2
                    Mora_Cost += 4000*Math_Var_2
                    Wits -= Math_Var_2
        
        Mora_Cost += 420000 #(20,000 + 40,000 + 60,000 + 80,000 + 100,000 + 120,000) #Character Ascention Costs

        ####Weapons
        Weapon_EXP_Needed = 9064450#Its weapon time
        while Weapon_EXP_Needed > 0:#Might aswell save 1 line and do this under the same "If" statement
            Minutes_Spent_Resin += 80 #(8*10)#I would have normally put weapons at the very end but thats ok
            Resin_Count += 10 #(1*10)
            Total_Resin += 10 #(1*10)

            Check_Daily_Minutes += 80 #(8*10)
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
                Weapon_EXP_Needed -= Spare_EXP
                Mora_Cost += Spare_EXP/5
                Spare_EXP = 0
                Spares = False
            
            if Mystic_Enchancement > 0:
                Weapon_EXP_Needed -= 10000*Mystic_Enchancement#Always use all of the mystic enhancement
                Mora_Cost += 1000*Mystic_Enchancement
                Mystic_Enchancement = 0

                if Weapon_EXP_Needed < 0:#because this takes care of overflow anyway
                    Spare_EXP = abs(Weapon_EXP_Needed) #I could put this in one line but im too lazy
                    Spare_EXP = Spare_EXP/400
                    Spare_EXP = math.floor(Spare_EXP)
                    Spare_EXP = Spare_EXP * 400#The standard tiny ore things
                    Spares = True
                
 
        ####Weapon Ascention Materials
        while True:
            Minutes_Spent_Resin += 80 #(8*10)
            Resin_Count += 10 #(1*10)
            Total_Resin += 10 #(1*10)

            Check_Daily_Minutes += 80 #(8*10)
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
        Mora_Cost += 150000 #(5000 + 15000 + 20000 + 30000 + 35000 + 45000)

    ####Character Talent Materials (Weekly Bosses)  
    while not Boss_Check(WiiSports): #Check if we have enough weekly boss materials
        Minutes_Spent_Resin += 80 #(8*10)
        Resin_Count += 10 #(1*10)
        Total_Resin += 10 #(1*10)

        Check_Daily_Minutes += 80 #(8*10)
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
    if Name not in ["TravelerA", "TravelerG", "TravelerE"]: #Travelers doesnt require elemental materials, so exclude them
        while True: #just loops untill all conditions inside are met
            Minutes_Spent_Resin += 80 #(8*10)
            Resin_Count += 10 #(1*10)
            Total_Resin += 10 #(1*10)

            Check_Daily_Minutes += 80 #(8*10)
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
 
            if eval(ElementShard) < 9: #Check if we have enough shards
                if eval(ElementFragment) >= 3: #Try and craft a shard
                    globals()[ElementShard] = eval(ElementShard) + 1
                    globals()[ElementFragment] = eval(ElementFragment) - 3
                    Mora_Cost += 300

            if eval(ElementChunk) < 9: #Check if we have enough chunks
                if eval(ElementShard) >= 3: #Try and craft a chunk
                    globals()[ElementChunk] = eval(ElementChunk) + 1
                    globals()[ElementShard] = eval(ElementShard) - 3
                    Mora_Cost += 900

            if eval(ElementGem) < 6: #Check if we have enough gems
                if eval(ElementChunk) >= 3: #Try and craft a gem
                    globals()[ElementGem] = eval(ElementGem) + 1
                    globals()[ElementChunk] = eval(ElementChunk) - 3
                    Mora_Cost += 2700
                    


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


        ####Character Ascention Materials (Non Elemental-specific Bosses)
        if Name in Needs_PrimoGeovishap: 
            while PrimoShards < 46:
                Minutes_Spent_Resin += 80 #(8*10)
                Resin_Count += 10 #(1*10)
                Total_Resin += 10 #(1*10)

                Check_Daily_Minutes += 80 #(8*10)
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
        
        if Name in Needs_MaguuKenki: 
            while MarionetteCore < 46:
                Minutes_Spent_Resin += 80 #(8*10)
                Resin_Count += 10 #(1*10)
                Total_Resin += 10 #(1*10)

                Check_Daily_Minutes += 80 #(8*10)
                if Check_Daily_Minutes >= 1440:
                    Do_Daily()

                if Resin_Count >= 40:
                    MaguuBodyCount += 1
                    MarionetteCore += 3
                    Resin_Count -= 40
                    Mora_Cost -= 5200
                    Adventure_EXP += 200
                    Companionship_EXP += 45
            MarionetteCore -= 46
        
        if Name in Needs_MechaCube: 
            while Perpetual_Heart < 46:
                Minutes_Spent_Resin += 80 #(8*10)
                Resin_Count += 10 #(1*10)
                Total_Resin += 10 #(1*10)

                Check_Daily_Minutes += 80 #(8*10)
                if Check_Daily_Minutes >= 1440:
                    Do_Daily()

                if Resin_Count >= 40:
                    MechaCubeBodyCount += 1
                    Perpetual_Heart += 3
                    Resin_Count -= 40
                    Mora_Cost -= 5200
                    Adventure_EXP += 200
                    Companionship_EXP += 45
            Perpetual_Heart -= 46


        ####Character Talent Materials (Domain Based)
        while True:#Might aswell do the Teachings and what not under the same "If"
            Minutes_Spent_Resin += 80 #(8*10)
            Resin_Count += 10 #(1*10)
            Total_Resin += 10 #(1*10)

            Check_Daily_Minutes += 80 #(8*10)
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
    ####Character Talent Materials (Travelers)
    else: #Since both Travelers dont follow traditional Teachings methods
        if Teachings == "ThreeMondstat":
            TeachingsList = {#Use a janky method to save code space, rather than have to copy and paste the domain code 3 times for each teaching
                "Freedom": (9, 18, 18),
                "Resistance": (0, 33, 36),
                "Ballad": (0, 12, 60)
            }
        elif Teachings == "Everything":#I am using really janky methods to save space
            TeachingsList = {
                "Freedom": (3, 6, 6),
                "Resistance": (0, 11, 12),
                "Ballad": (0, 4, 20),
                "Prosperity": (6, 12, 12),
                "Diligence": (0, 22, 24),
                "Gold": (0, 8, 40)
            }
        elif Teachings == "ThreeInazuma":#Commence the Jank
            TeachingsList = {
                "Transience":(9, 33, 36),
                "Elegance":(0, 12, 60),
                "Light":(0, 33, 18),
            }
        
        for _ in range(len(TeachingsList)):
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
            elif Teachings in ["Prosperity", "Diligence", "Gold"]:
                Talent_Domain = "Liyue_Domain_Count"
            elif Teachings in ["Transience", "Elegance", "Light"]:
                Talent_Domain = "Inazuma_Domain_Count"
 

            while True:#this is literally the same code from above lol
                Minutes_Spent_Resin += 80 #(8*10)
                Resin_Count += 10 #(1*10)
                Total_Resin += 10 #(1*10)

                Check_Daily_Minutes += 80 #(8*10)
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
for _ in range(Character_Count_x5):#5, 5-Star artifacts for each character, Both Travelers are included, because maybe you want one Anemo set up, and one Geo setup
    Artifact_EXP_Needed = 269800
    while Artifact_EXP_Needed > 0:
        Minutes_Spent_Resin += 80 #(8*10)
        Resin_Count += 10 #(1*10)
        Total_Resin += 10 #(1*10)

        Check_Daily_Minutes += 80 #(8*10)
        if Check_Daily_Minutes >= 1440:
            Do_Daily()

        if Resin_Count >= 20:
            Any_Artifact_Domain_Count += 1
            Resin_Count -= 20
            Mora_Cost -= 2525 
            Three_Star_Artifacts += 7
            Four_Star_Artifacts += 3
            Adventure_EXP += 100
            Companionship_EXP += 20
 

        if Four_Star_Artifacts > 0: #Instead of just adding EXP directly on, this lets any spare artifacts carry over.           
            Math_Var_1 = math.ceil(Artifact_EXP_Needed/2520)#check how many Four Star Artifacts we need
            if Math_Var_1 > Four_Star_Artifacts:#if we need more than we have, use em all
                Artifact_EXP_Needed -= 2520*Four_Star_Artifacts
                Mora_Cost += 2520*Four_Star_Artifacts
                Four_Star_Artifacts = 0
            elif Math_Var_1 < Four_Star_Artifacts:#if we need less than we have, only take away as many as we need
                Math_Var_2 = Four_Star_Artifacts - Math_Var_1
                Artifact_EXP_Needed -=2520*Math_Var_2
                Mora_Cost += 2520*Math_Var_2
                Four_Star_Artifacts -= Math_Var_2

        if Three_Star_Artifacts > 0:
            Math_Var_1 = math.ceil(Artifact_EXP_Needed/1260)#check how many Four Star Artifacts we need
            if Math_Var_1 > Three_Star_Artifacts:#if we need more than we have, use em all
                Artifact_EXP_Needed -= 1260*Three_Star_Artifacts
                Mora_Cost += 1260*Three_Star_Artifacts
                Three_Star_Artifacts = 0
            elif Math_Var_1 < Three_Star_Artifacts:#if we need less than we have, only take away as many as we need
                Math_Var_2 = Three_Star_Artifacts - Math_Var_1
                Artifact_EXP_Needed -=1260*Math_Var_2
                Mora_Cost += 1260*Math_Var_2
                Three_Star_Artifacts -= Math_Var_2

            
print(str(Character_Count_x5) + " artifacts maxed...")


####Mora Outcrops
print("")
print("")
print("Mora Cost (Before Mora Blossoms): " + str(Mora_Cost))#I also dont know how Escape percents or what ever they're called work, so yeah
while Mora_Cost > 0:
    Minutes_Spent_Resin += 80 #(8*10)
    Resin_Count += 10 #(1*10)
    Total_Resin += 10 #(1*10)

    Check_Daily_Minutes += 80 #(8*10)
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

zzzzzzCopyGlobals = globals().copy()
for x in zzzzzzCopyGlobals: #use an illegal method to convert every variable into a string, so that I dont have to do str() in my print statements
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
print("")
try:
    print("Domains, Outcrops and Mining: ")
    if EXP_Blossom_Count == "0":
        print("     Rhodia Body Count " + Rhodia_Count)
    if Rhodia_Count == "0":
        print("     EXP Ley Line Outcrops: " + EXP_Blossom_Count)
    print("     Mora Ley Line Outcrops: " + Mora_Blossom_Count)
    print("     Mondstat Talent Domains: " + Mondstat_Domain_Count)
    print("     Liyue Talent Domains: " + Liyue_Domain_Count)
    print("     Inazuma Talent Domains: " + Inazuma_Domain_Count)
    print("     Artifact Domains: " + Any_Artifact_Domain_Count)
    print("     Mondstat Weapon Ascention Domains: " + Mondstat_Domain_Count2)
    print("     Liyue Weapon Ascention Domains: " + Liyue_Domain_Count2)
    print("     Inazuma Weapon Ascention Domains: " + Inazuma_Domain_Count2)
    print("     Magic Crystals: " + Magic_Crystal_Needed)
except:
    pass
print("")
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
except:
    pass
print("")
try:
    print("     Anemo Hypostasis' Body Count: " + AnemoBodyCount)#Once again, is how many of their bodies We have. Anemo Hypostasis' Body, as in the body of the Hypostasis, Count, as in how many we have. How many of the Anemo Hypostasis bodies do we have
    print("     Cryo Regisvine's Body Count: " + CryoBodyCount)
    print("     Cryo Hypostasis's Body Count: " + Cryo2BodyCount)
    print("     Electro Hypostasis' Body Count: " + ElectroBodyCount)
    print("     Geo Hypostasis' Body Count: " + GeoBodyCount)
    print("     Oceanid's Body Count: " + HydroBodyCount)
    print("     Pyro Regisvine Body Count: " + PyroBodyCount)
    print("     Primo Geovishap Body Count: " + PrimoVishapBodyCount)
    print("     Maguu Kenki Body Count: " + MaguuBodyCount)
    print("     Mecha Cube Body Count: " + MechaCubeBodyCount)
except:
    pass
print("")
print("")
print("")
import time
try:
    print("Spare Loot:")
    print("     Heros Wits: " + Wits)
    print("     Adventurers Experience: " + Experience)
    print("     Three-Star Artifacts: " + Three_Star_Artifacts)
    print("     Four-Star Artifacts: " + Four_Star_Artifacts)
except:
    pass
print("")
try:
    print("     Mora: " + Mora_Cost)
    print("     Adventure EXP: " + Adventure_EXP)
    print("     Companionship EXP: " + Companionship_EXP)
    print("     Primogems: " + Primogems)#Most likely spent on getting all of those damn 5 stars lol, so many 5 stars and 5 star weapons holy
    print("          Individual Wishes: " + Wishes)
except:
    pass
print("")
try:
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
except:
    pass
print("")
try:
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
    print("     Smoldering Pearls: " + Pyro2Boss)
except:
    pass
print("")
try:
    print("     Juvenile Jades: " + PrimoShards)
    print("     Marionette Cores: " + MarionetteCore)
    print("     Perpetual Hearts: " + Perpetual_Heart)
except:
    pass
print("")
try:
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
    print("     Coral Branch of a Distance Sea: " + Branch2Uncommon)
    print("     Jeweled Branch of a Distance Sea: " + Branch2Rare)    
    print("     Narukami's Wisdom: " + NarukamiUncommon)
    print("     Narukami's Joy: " + NarukamiRare)
    print("     Mask of the Wicked Lieutenant: " + MaskUncommon)
    print("     Mask of the Tiger's Bite: " + MaskRare)
except:
    pass
print("")
try:
    print("     Teachings of Freedom: " + FreedomCommon)
    print("     Guide to Freedom: " + FreedomRare)
    print("     Teachings of Resistance: " + ResistanceCommon)
    print("     Guide to Resistance: " + ResistanceRare)
    print("     Teachings of Ballad: " + BalladCommon)
    print("     Guide to Ballad: " + BalladRare)
    print("     Teachings of Prosperity: " + ProsperityCommon)
    print("     Guide to Prosperity: " + ProsperityRare)
    print("     Teachings of Diligence: " + DiligenceCommon)
    print("     Guide to Diligence: " + DiligenceRare)
    print("     Teachings of Gold: " + GoldCommon)
    print("     Guide to Gold: " + GoldRare)
    print("     Teachings of Transience: " + TransienceCommon)
    print("     Guide to Transience: " + TransienceRare)
    print("     Teachings of Elegance: " + EleganceCommon)
    print("     Guide to Elegance: " + EleganceRare)
    print("     Teachings of Light: " + LightCommon)
    print("     Guide to Light: " + LightRare)
except:
    pass
print("")
try:
    print("     Mystic Enchancement: " + Mystic_Enchancement)
except:
    pass

print("Complete")
while True:
    time.sleep(10)

#Check for Variable that equal 0
print("")
print("")
print("")
print("Variable that equal 0:")
Global_Dupe = dict(globals())
for x in Global_Dupe:
    if eval(x) == "0":
        print("     " + str(x))
