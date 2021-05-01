# Max-All-Characters-In-Genshin-Impact
Greetings I decided to just write a script to find how long it takes to max every charactor in Genshin impact

Lvl 90
Max Talents
Max Weapon
Max Artifacts

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

I'll update it the best I can, whenever I feel like it, so it should stay roughly correct for however long I play genshin.
I guess I'll add a very brief changelog, aswell as running my code once, and writing how long it took, so you can sort of see the Time over the Updates:

(Obviously since I included RNG, only Drastic changes will show. since adding a new character could take shorter than the update before, due to RNG)
March 13th: {No update notes} 5.78 Years
April 10th: {No update notes} 5.75 Years
April 30th: {Added Eula, Yanfei, and fixed Rosaria. Added Cyro Hypostasis, Added Azhdaha, Added Adventure EXP, and Companionship EXP, plus an option to max companionship EXP, aswell as everything else. Added Daily coms, and primogems.} 


Sources
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
   
