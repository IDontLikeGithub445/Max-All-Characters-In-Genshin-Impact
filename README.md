# Max-All-Characters-In-Genshin-Impact

Don't actually read my Im just spewing all of my thoughts here
Also there's an update log I just added, it contains all of the actually important stuff, go read that instead.
update, I've only just learned now that you can add multiple title cars to one README, so I moved the updates back here

-
-
-
-
-


Greetings I decided to just write a script to find how long it takes to max every charactor in Genshin impact

Pre-emtive warning before you go any further:
I'm not professional at all, everything is written as if I was talking to a good friend.

Anyway, this script maxes:
Lvl 90
Max Talents
Max Weapon
Max Artifacts
(Companionship EXP is automatically maxed in the process of doing everything else lol)

One thing that isnt accounted for is Duplicate Artifacts, or Duplicate Weapons, but techincally I'm maxing every single charactor, not every pair of charactors, so I think im good.

I'm going to add the dictionary ordering here, just so I can de-clutter the python script itself. I don't feel like updating old scripts, so you can go see what it used to look like.

{"Name": (Element, "Weekly Boss Talent Ascention Material (based on Fandom)", "Domain Talent Ascention Material (Also fandom)", "Weapon Name (Based on Game8 reccomended Weapon, or if a 4-star is reccomended, a random 5-star bow is chosen instead, since im too lazy to account for 4-stars. (+ indicates first reccomendation, - indicates other reccomendation, no sign indicates random selection)", "Weapon Ascention Material (Based on Game8")}


I'll leave the bare-bones verison of the explanation in the script though.

Everything is supposed to be as of world level 6, and then the highest level boss I can murder, but actually I guess when I next update it (which will probably be right after writing this), I'll go adjust everything for world level 7, and I can murder all world bosses at lvl 90, so I can update those aswell.

RNG is added for World bosses, and specifically Ley Line Outcrops, but not domains.
So its not perfect, but its probably a good estimate.

Also, don't question the optimization of my script, Im well aware looping something 20 times giving 1 resin each time is significantly less efficient than looping once, giving 20 resin. I'm not taking any chances with me an my 54% in Math Class. I'm looping it as if it was in game, 1 resin every 8 minutes.
You're lucky im not making you WAIT 8 minutes for every resin lol.
haha im not that dumb.

My script is like 800 or so lines long, 800 os you round up, and the Visual Studio IntelliSense isnt automatically popping up, so I might have placed a variable in the wrong place or something, since my puny human brain can't keep track of all of the variables. Anyway, my code is so terrible I can hardly read it myself lol, so its difficult to bug fix quickly.

## Updates
I'll update it the best I can, whenever I feel like it, so it should stay roughly correct for however long I play genshin.
I decided to move the updates off of the ReadMe doccument, just to sort of neaten the place up... ever so slightly.

(Obviously since I included RNG, only Drastic changes will show. since adding a new character could take shorter than the update before, due to RNG)





[2021]


March 13th: {No update notes} 5.78 Years


April 10th: {No update notes} 5.75 Years


April 30th: {Added Eula, Yanfei, and fixed Rosaria. Added Cyro Hypostasis, Added Azhdaha, Added Adventure EXP, and Companionship EXP, plus an option to max companionship EXP, aswell as everything else. Added Daily coms, and primogems.} 5.78 Years


May 24th: {Fixed Eula, ""optimized"" daily commissions by adding them into the loop, rather than doing all the daily coms at the end. Using this new Daily method, I can now add Realm currency and what not if I so choose. Added quadruple # for ease of navigation (#### ), so just ctrl+f "####", and navigate from there. I also added the mora required to actually ascend characters, since the wiki on character EXP didnt account for that.} 5.52 Years

##### test
Ok for some reason when I change minutes spent to 80, and resin increase to 10 (rather than 8 and 1), everything goes out of wack. It's supposed to loop 10 times less, but the final time ends up as 10.9 years. I instead reverted 80 to 8, and 10 to 1, but instead changed required resin from 20, 40, 30, 150, and so on, to 2, 4, 3, 15 and so on, and all of a sudden it only takes 1 year. I have no clue what's going on, so for consistancy's sake I'm going to just keep everything at 8 and 1 until I figure out what's going wrong.


I've figured it out, when I give like 20 or so wanderes adivce, or any similar material, I only consume 1 per loop, but I get 20 every 2 loops. meaning I have an imense backlog of materials, but the loop doesnt know that. all the loop knows is do ley line outcrop. Therefore the time spent is increased drastically, and the backlog of materials is increasded from almost none, to probably thousands. Now that I've figured this out, I'll go ahead and """"""optimize"""""" the loops using some math or things. I'm finially caving in to the 0 people who were complaining, so I'll optimize the loopage next update.


[x]: {Loops now loop 10 times less, thanks to optimization with math.}




## Sources
https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrops
https://genshin-impact.fandom.com/wiki/Character_Ascension_Materials
https://genshin-impact.fandom.com/wiki/Talent_Level-Up_Materials
https://www.reddit.com/r/Genshin_Impact/comments/joo9qg/guide_artifact_exp_calculations_and_genshin/
https://genshin-impact.fandom.com/wiki/Weapon_EXP
https://genshin-impact.fandom.com/wiki/Character_EXP
https://game8.co/games/Genshin-Impact/archives/296707
https://game8.co/games/Genshin-Impact/archives/297497
https://genshin-impact.fandom.com/wiki/Commissions
https://genshin-impact.fandom.com/wiki/Bosses
https://genshin-impact.fandom.com/wiki/Companionship_EXP

here are sources I used for my information.
   
