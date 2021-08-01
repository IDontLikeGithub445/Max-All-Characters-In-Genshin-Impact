# Max-All-Characters-In-Genshin-Impact

Don't actually read my Im just spewing all of my thoughts here

Also, there's an update log I just added, it contains all of the actually important stuff, go read that instead.

update, I've only just learned now that you can add multiple title cars to one README, so I moved the updates back here

## Boring stuff
Greetings I decided to just write a script to find how long it takes to max every character in Genshin impact

Preemptive warning before you go any further:

I'm not professional at all, everything is written as if I was talking to a good friend. because formality is my arch nemesis.

Anyway, this script maxes:

Lvl 90

Max Talents

Max Weapon

Max Artifacts

(Companionship EXP is automatically maxed in the process of doing everything else lol)

One thing that isn't accounted for is Duplicate Artifacts or Duplicate Weapons, but technically I'm maxing every single character, not every pair of characters, so I think im good.

I'm going to add the dictionary ordering here, just so I can de-clutter the python script itself. I don't feel like updating old scripts, so you can go see what it used to look like.

{"Name": ("Element", "Weekly Boss Talent Ascension Material (based on Fandom)", "Domain Talent Ascension Material (Also fandom)", "Weapon Name (Based on Game8 recommended Weapon, or if a 4-star is recommended, a random 5-star bow is chosen instead, since im too lazy to account for 4-stars. (+ indicates first recommendation, - indicates other recommendation, no sign indicates random selection)", "Weapon Ascension Material (Based on Game8"))}
Ayo note from the future, Im pretty sure 4 and 5-star weapons require the same exp, but Imma just stick with 5-star weapons because Im too lazy to go through all of the game8 pages again.


I'll leave the bare-bones version of the explanation in the script though.

Everything is supposed to be as of world level 6, and then the highest level boss I can murder, but actually, I guess when I next update it (which will probably be right after writing this), I'll go adjust everything for world level 7, and I can murder all world bosses at lvl 90, so I can update those as well.

RNG is added for World bosses, and specifically Ley Line Outcrops, but not domains.
So it's not perfect, but it's probably a good estimate.

Also, don't question the optimization of my script, Im well aware looping something 20 times giving 1 resin each time is significantly less efficient than looping once, giving 20 resin. I'm not taking any chances with me and my 54% in Math Class. I'm looping it as if it was in-game, 1 resin every 8 minutes.
You're lucky im not making you WAIT 8 minutes for every resin lol.
haha, im not that dumb.

My script is like 800 or so lines long, 800 os you round up, and the Visual Studio IntelliSense isn't automatically popping up, so I might have placed a variable in the wrong place or something since my puny human brain can't keep track of all of the variables. Anyway, my code is so terrible I can hardly read it myself lol, so its difficult to bug fix quickly.

##Slightly less boring stuff
The entire script is soft-coded, so in theory, if you wanted to add Steve, a Dendro-based <weapon-type doesnt matter> character, who requires Dvalin's Claw, Proficies of Freedom, <weapon name doesnt matter>, and some Mask of the Kijin, oh and Primo Geovishap scales, You'd add
   
   "Steve":("Dendro", "Claw", "Freedom", "Bonk-Stick", "Kijin"),

to the Characters_List variable
So yeah have fun
The formatting is already there but I'll paste it again

   "Name": ("Element", "Weekly Boss Talent Ascention Material", "Domain Talent Ascention Material", "Weapon Name", "Weapon Ascention Material")

## Updates
I'll update it the best I can, whenever I feel like it, so it should stay roughly correct for however long I play Genshin.
I decided to move the updates off of the ReadMe document, just to sort of neatening the place up... ever so slightly.

(Obviously, since I included RNG, only Drastic changes will show. since adding a new character could take shorter than the update before, due to RNG)

### [2021]
#### March 13th: 5.78 Years
{No update notes} 

#### April 10th: 5.75 Years
{No update notes} 


#### April 30th: 5.78 Years
{Added Eula, Yanfei, and fixed Rosaria. Added Cyro Hypostasis, Added Azhdaha, Added Adventure EXP, and Companionship EXP, plus an option to max companionship EXP, aswell as everything else. Added Daily coms, and primogems.} 

#### May 24th: 5.52 Years
Fixed Eula, ""optimized"" daily commissions by adding them into the loop, rather than doing all the daily coms at the end. Using this new Daily method, I can now add Realm currency and what not if I so choose. Added quadruple # for ease of navigation (#### ), so just ctrl+f "####", and navigate from there. I also added the mora required to actually ascend characters, since the wiki on character EXP didn't account for that 

Ok for some reason when I change minutes spent to 80, and resin increase to 10 (rather than 8 and 1), everything goes out of wack. It's supposed to loop 10 times less, but the final time ends up as 10.9 years. I instead reverted 80 to 8, and 10 to 1, but instead changed required resin from 20, 40, 30, 150, and so on, to 2, 4, 3, 15 and so on, and all of a sudden it only takes 1 year. I have no clue what's going on, so for consistency's sake I'm going to just keep everything at 8 and 1 until I figure out what's going wrong.

I've figured it out, when I give like 20 or so wanderers' advice or any similar material, I only consume 1 per loop, but I get 20 every 2 loops. meaning I have an imense backlog of materials, but the loop doesnt know that. all the loop knows is "do ley line outcrop". Therefore the time spent is increased drastically, and the backlog of materials is increased from almost none, to probably thousands. Now that I've figured this out, I'll go ahead and """"""optimize"""""" the loops using some math or things. I'm finally caving into the 0 people who were complaining, so I'll optimize the loopage next update.

#### July 31st: 5.81 years
Loops now loop 10 times less, thanks to optimization with math, Added Kazuha, I feel like waiting for at least Yoimiya as well and then I'll go ahead and release it
not that anyone cares, there are far better methods out there, just google it im sure you'll find it, but still
Ayaka and Electro Traveler works. Anyway, I also added the names of talent and weapon ascension materials further up so they're easier to find when you're adding characters. 
Speaking of, im not sure if I mentioned this anywhere, but you can add your own characters by just adding them to the "Characters_List" variable. I'll go add this closer to the top.
Added support for Pyro Cube as well, and all of Inazuma's other bits and bobs.
I've also added a couple more try and except statements to the print statements near the bottom. I also added the Character Talent materials, since I apparently forgot those. 
Anyway, my Python Intellisense is crashing trying to read an 18 line file, so who would have guessed it'd crash reading a 1000 line file. Without my Intellisense, I can't keep track of my own variables, so hypothetically if my code just straight up no longer works, that'd be why. While Intellisense is dead, the interpreter itself isn't, so I can indeed test my code. Everything seems to check out but there's no 100% guarantee 



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

in no particular order
