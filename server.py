import os
from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

winner15_data = {"unstructured": {"nominees": [], "awards": ["Cecil B. DeMille Award", "Best Motion Picture - Drama", "Best Motion Picture - Comedy or Musical", "Best Screenplay - Motion Picture", "Best Television Series - Drama", "Best Television Series - Comedy or Musical", "Best Mini-Series Or Motion Picture Made for Television", "Best Animated Feature Film", "Best Foreign Language Film", "Best Dressed", "Worst Dressed", "Best Performance by an Actor in a Motion Picture - Drama", "Best Performance by an Actor in a Television Series - Drama", "Best Performance by an Actress in a Motion Picture - Drama", "Best Performance by an Actress in a Television Series - Drama", "Best Performance by an Actor in a Motion Picture - Comedy or Musical", "Best Performance by an Actor in a Television Series - Comedy or Musical", "Best Performance by an Actress in a Motion Picture - Comedy or Musical", "Best Performance by an Actress in a Television Series - Comedy or Musical", "Best Performance by an Actor In a Supporting Role in a Motion Picture", "Best Performance by an Actress In a Supporting Role in a Motion Picture", "Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television", "Best Performance by an Actress in a Mini-Series or Motion Picture Made for Television", "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television", "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television", "Best Director - Motion Picture", "Best Original Score - Motion Picture", "Best Original Song - Motion Picture"], "winners": ["Batman", "Boyhood", "The Grand Budapest Hotel", "Birdman", "Affair", "Transparent", "Fargo", "How To", "Leviathan", "Bomer", "Knightley", "Eddie Redmayne", "Kevin Spacey", "Julianne Moore", "Wilson", "Michael Keaton", "Jeffrey Tambor", "Adams", "Rodriguez", "JK Simmons", "Patricia Arquette", "Billy Bob Thornton", "Maggie Gyllenhaal", "Matt Bomer", "Froggatt", "Linklater", "Johann Johannsson", "Glory"], "hosts": ["Amy Poehler", "Tina Fey"], "presenters": [["Don Cheadle", "Julianna Margulies"], ["Meryl Streep"], ["Robert Downey, Jr."], ["Kristen Wiig", "Bill Hader"], ["Adam Levine", "Paul Rudd"], ["Bryan Cranston", "Kerry Washington"], ["Jennifer Lopez", "Jeremy Renner"], ["Kevin Hart", "Salma Hayek"], ["Lupita Nyongo", "Colin Farrell"], ["none"], ["none"], ["Gwyneth Paltrow"], ["David Duchovny", "Katherine Heigl"], ["Matthew McConaughey"], ["Chris Pratt", "Anna Faris"], ["Amy Adams"], ["Jane Fonda", "Lily Tomlin"], ["Ricky Gervais"], ["Bryan Cranston", "Kerry Washington"], ["Jennifer Aniston", "Benedict Cumberbatch"], ["Jared Leto"], ["Jennifer Lopez", "Jeremy Renner"], ["Adrien Brody", "Kate Beckinsale"], ["Seth Meyers", "Katie Holmes"], ["Jamie Dornan", "Dakota Johnson"], ["Harrison Ford"], ["Sienna Miller", "Vince Vaughn"], ["Prince"]]}, "structured": {"Best Screenplay - Motion Picture": {"nominees": ["The Grand Budapest Hotel", "Gone Girl", "Boyhood", "The Imitation Game"], "presenters": ["Kristen Wiig", "Bill Hader"], "winner": "Birdman"}, "Worst Dressed": {"nominees": ["none"], "presenters": ["none"], "winner": "Knightley"}, "Best Director - Motion Picture": {"nominees": ["Richard Linklater", "Wes Anderson", "Ava Duvernay", "David Fincher", "Alejandro Gonzalez Inarritu"], "presenters": ["Harrison Ford"], "winner": "Linklater"}, "Best Foreign Language Film": {"nominees": ["Force Majeure", "Gett: the Trial of Viviane Amsalem", "Ida", "Tangerines"], "presenters": ["Lupita Nyongo", "Colin Farrell"], "winner": "Leviathan"}, "Best Performance by an Actor in a Television Series - Comedy or Musical": {"nominees": ["Louis C. K.", "Don Cheadle", "Ricky Gervais", "William H. Macy"], "presenters": ["Jane Fonda", "Lily Tomlin"], "winner": "Jeffrey Tambor"}, "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television": {"nominees": ["Joanne Froggatt", "Uzo Aduba", "Kathy Bates", "Allison Janney", "Michelle Monaghan"], "presenters": ["Jamie Dornan", "Dakota Johnson"], "winner": "Froggatt"}, "Best Original Score - Motion Picture": {"nominees": ["Johann Johannsson", "Alexandre Desplat", "Trent Reznor", "Antonio Sanchez", "Hans Zimmer"], "presenters": ["Sienna Miller", "Vince Vaughn"], "winner": "Johann Johannsson"}, "Best Mini-Series Or Motion Picture Made for Television": {"nominees": ["The Missing", "The Normal Heart", "Olive Kitteridge", "True Detective"], "presenters": ["Jennifer Lopez", "Jeremy Renner"], "winner": "Fargo"}, "Best Original Song - Motion Picture": {"nominees": ["Big Eyes", "Mercy Is", "Opportunity", "Yellow Flicker Beat"], "presenters": ["Prince"], "winner": "Glory"}, "Best Dressed": {"nominees": ["none"], "presenters": ["none"], "winner": "Bomer"}, "Best Television Series - Comedy or Musical": {"nominees": ["Girls", "Jane the Virgin", "Orange is the New Black", "Silicon Valley"], "presenters": ["Bryan Cranston", "Kerry Washington"], "winner": "Transparent"}, "Cecil B. DeMille Award": {"nominees": ["George Clooney"], "presenters": ["Don Cheadle", "Julianna Margulies"], "winner": "Batman"}, "Best Performance by an Actor In a Supporting Role in a Motion Picture": {"nominees": ["Robert Duvall", "Ethan Hawke", "Edward Norton", "Mark Ruffalo"], "presenters": ["Jennifer Aniston", "Benedict Cumberbatch"], "winner": "JK Simmons"}, "Best Performance by an Actor in a Television Series - Drama": {"nominees": ["Clive Owen", "Liev Schreiber", "James Spader", "Dominic West"], "presenters": ["David Duchovny", "Katherine Heigl"], "winner": "Kevin Spacey"}, "Best Performance by an Actress in a Motion Picture - Drama": {"nominees": ["Jennifer Aniston", "Felicity Jones", "Rosamund Pike", "Reese Witherspoon"], "presenters": ["Matthew McConaughey"], "winner": "Julianne Moore"}, "Best Motion Picture - Comedy or Musical": {"nominees": ["Birdman", "Into the woods", "Pride", "St. Vincent"], "presenters": ["Robert Downey, Jr."], "winner": "The Grand Budapest Hotel"}, "Best Performance by an Actress in a Motion Picture - Comedy or Musical": {"nominees": ["Amy Adams", "Emily Blunt", "Helen Mirren", "Julianne Moore", "Quvenzhane Wallis"], "presenters": ["Ricky Gervais"], "winner": "Adams"}, "Best Performance by an Actress In a Supporting Role in a Motion Picture": {"nominees": ["Jessica Chastain", "Keira Knightley", "Emma Stone", "Meryl Streep"], "presenters": ["Jared Leto"], "winner": "Patricia Arquette"}, "Best Performance by an Actress in a Mini-Series or Motion Picture Made for Television": {"nominees": ["Jessica Lange", "Frances Mcdormand", "Frances O'Connor", "Allison Tolman"], "presenters": ["Adrien Brody", "Kate Beckinsale"], "winner": "Maggie Gyllenhaal"}, "Best Performance by an Actress in a Television Series - Drama": {"nominees": ["Ruth Wilson", "Claire Danes", "Viola Davis", "Julianna Margulies", "Robin Wright"], "presenters": ["Chris Pratt", "Anna Faris"], "winner": "Wilson"}, "Best Performance by an Actor in a Motion Picture - Comedy or Musical": {"nominees": ["Ralph Fiennes", "Bill Murray", "Joaquin Phoenix", "Christoph Waltz"], "presenters": ["Amy Adams"], "winner": "Michael Keaton"}, "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television": {"nominees": ["Alan Cumming", "Colin Hanks", "Bill Murray", "Jon Voight"], "presenters": ["Seth Meyers", "Katie Holmes"], "winner": "Matt Bomer"}, "Best Television Series - Drama": {"nominees": ["The Affair", "Downton Abbey", "Game of Thrones", "The Good Wife", "House of Cards"], "presenters": ["Adam Levine", "Paul Rudd"], "winner": "Affair"}, "Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television": {"nominees": ["Martin Freeman", "Woody Harrelson", "Matthew Mcconaughey", "Mark Ruffalo"], "presenters": ["Jennifer Lopez", "Jeremy Renner"], "winner": "Billy Bob Thornton"}, "Best Animated Feature Film": {"nominees": ["How to Train Your Dragon 2", "Big Hero 6", "The Book of Life", "The Boxtrolls", "The Lego Movie"], "presenters": ["Kevin Hart", "Salma Hayek"], "winner": "How To"}, "Best Performance by an Actress in a Television Series - Comedy or Musical": {"nominees": ["Gina Rodriguez", "Lena Dunham", "Edie Falco", "Julia Louis-Dreyfux", "Taylor Schilling"], "presenters": ["Bryan Cranston", "Kerry Washington"], "winner": "Rodriguez"}, "Best Performance by an Actor in a Motion Picture - Drama": {"nominees": ["Steve Carell", "Benedict Cumberbatch", "Jake Gyllenhaal", "David Oyelowo"], "presenters": ["Gwyneth Paltrow"], "winner": "Eddie Redmayne"}, "Best Motion Picture - Drama": {"nominees": ["Foxcatcher", "The Imitation Game", "The Theory of Everything"], "presenters": ["Meryl Streep"], "winner": "Boyhood"}}}

funny_tweets = [
    {
        "text": "@LewisCardy @aidan_hodgy Ok Cardy remember that 1v2 at 5-5 last map v Ross GG and King Powerful hahahaha best 1v2 av ever done\n", 
        "names": "Cardy "
    }, 
    {
        "text": "@WhattheCheng: Ryan Seacrest: \"Who are you wearing\" Kevin Spacey: \"Joseph A Banks\" Ahhahahaha \ud83d\ude02 #GoldenGlobes\n", 
        "names": "Ryan Seacrest Kevin Spacey Joseph "
    }, 
    {
        "text": "If anything, I will make sure to watch Amy Poehler and Tina Fey's Golden Globes monologue later hahahaha best hosts ever those two\n", 
        "names": "Amy Poehler Tina Fey "
    }, 
    {
        "text": "Hahahahahaha Michael Keaton wrote another note to @sethmeyers on the red carpet \ud83d\ude02\ud83d\ude02\n", 
        "names": "Michael Keaton "
    }, 
    {
        "text": "RT @marie_cunicella: Hahahahahaha Michael Keaton wrote another note to @sethmeyers on the red carpet \ud83d\ude02\ud83d\ude02\n", 
        "names": "Michael Keaton "
    }, 
    {
        "text": "Kiera Knightley hahahahaha are you serious? I'm sad it's by my mothership, CHANEL. #GoldenGlobes #ERedCarpet\n", 
        "names": "Kiera Knightley "
    }, 
    {
        "text": "\"@mrbradgoreski: Jennifer Aniston's hair is up!!!!!!!!! My #ERedCarpet dreams have come true!!! #GoldenGlobes2015\" hahahahaa\n", 
        "names": "Jennifer Aniston "
    }, 
    {
        "text": "Jessica Chastain looks beautiful, duh, please marry me now hahahaha just kidding (but really, please) #GoldenGlobes\n", 
        "names": "Jessica Chastain "
    }, 
    {
        "text": "hahahaha the game over shirt show to Clooney was great!! #RedCarpet\n", 
        "names": "Clooney "
    }, 
    {
        "text": "Julia LD: \"...It's still called 'Veep'.\" hahahahaha #takenoshit #loveyou #GoldenGlobes\n", 
        "names": "Julia "
    }, 
    {
        "text": "Hahahahaha Maggie Gyllenhaal: \"It's MiuMiu; what else do you want to know?\" Ouch, Seacrest. #ERedCarpet #GoldenGlobes\n", 
        "names": "Maggie Gyllenhaal "
    }, 
    {
        "text": "hahahahahaa Emma Stone as the real life Big eyes #GoldenGlobes #TinaAndAmy\n", 
        "names": "Emma Stone "
    }, 
    {
        "text": "Wtf they joked about Emma Stone having large eyes hahahahahaha \ud83d\ude02 #GoldenGlobes\n", 
        "names": "Emma Stone "
    }, 
    {
        "text": "#GoldenGlobes Tina and Amy hahahaha so funny\n", 
        "names": "Tina Amy "
    }, 
    {
        "text": "Love it when Tina and Amy try to define \"cake\" and \"birthdays\" - bahahahahaha! #GoldenGlobes #WOMC\n", 
        "names": "Tina Amy "
    }, 
    {
        "text": "\"In the movie, Meryl Streep is a witch who sends people to complete quests for collecting another golden globe.\" Ahahahahahahahah cok iyi!\n", 
        "names": "Meryl Streep "
    }, 
    {
        "text": "I turned it onto the golden globes just in time to see them roast Bill Cosby lmao hahahahahaha\n", 
        "names": "Bill Cosby "
    }, 
    {
        "text": "Hahahahahaha the #BillCosby joke has my whole house trying to impersonate Bill Cosby... #GoldenGlobes\n", 
        "names": "Bill Cosby "
    }, 
    {
        "text": "Tina and Amy are the queens of everything. and of couuuuurse they had to take the Bill Cosby subject omg hahahaha #GoldenGlobes\n", 
        "names": "Tina Amy "
    }, 
    {
        "text": "Haaahahahaha ... Tina Fey and Amy Poehler are Hilarious on #GoldenGlobes2015\n", 
        "names": "Tina Fey Amy Poehler "
    }, 
    {
        "text": "Omg I can't believe Amy and Tina just went there with bill Cosby hahahahaha it was perfect #GoldenGlobes\n", 
        "names": "Amy Tina bill Cosby "
    }, 
    {
        "text": "hahahahaha... they just randomly picked Cumberbatch to present with Jennifer A. #ILikeIt #GoldenGlobes\n", 
        "names": "Cumberbatch Jennifer A. "
    }, 
    {
        "text": "#GoldenGlobes Bill Cosby joke funny as hell #hahahahalololololohehehehe he made a joke about himself so there u have it #TinaandAmy enjoying\n", 
        "names": "Bill Cosby "
    }, 
    {
        "text": "You were mean Tina And Amy . Ahahahaha loved it. #GoldenGlobes\n", 
        "names": "Tina And Amy "
    }, 
    {
        "text": "@goldenglobes Benedict Cumberbatch tho hahahahahahah \ud83d\ude02\ud83d\ude02\ud83d\ude02\ud83d\ude02\ud83d\ude02got to love him\n", 
        "names": "Benedict Cumberbatch "
    }, 
    {
        "text": "That Bill Cosby joke was so awkward. hahahaha #GoldenGlobes #oops  #ohnotheydidnt #ohyestheydid\n", 
        "names": "Bill Cosby "
    }, 
    {
        "text": "RT @Fanny_Nobody: Tina and Amy are the queens of everything. and of couuuuurse they had to take the Bill Cosby subject omg hahahaha #Golden\u2026\n", 
        "names": "Tina Amy "
    }, 
    {
        "text": "RT @larasdias: You were mean Tina And Amy . Ahahahaha loved it. #GoldenGlobes\n", 
        "names": "Tina And Amy "
    }, 
    {
        "text": "Billly Bob wins so far for best speech hahahaha #GoldenGlobes\n", 
        "names": "Billly Bob "
    }, 
    {
        "text": "men, this golden globes are really ACID, Rick Gervais virus infected everybody hahahaha and Tina and Amy!\n", 
        "names": "Rick Gervais Tina Amy "
    }, 
    {
        "text": "What an interesting choice for Michael Keaton hahahaha #GoldenGlobes\n", 
        "names": "Michael Keaton "
    }, 
    {
        "text": "RT @thomasnizio: men, this golden globes are really ACID, Rick Gervais virus infected everybody hahahaha and Tina and Amy!\n", 
        "names": "Rick Gervais Tina Amy "
    }, 
    {
        "text": "Ahahahaha Meryl is like \"Well, if I must....\" #GoldenGlobes\n", 
        "names": "Meryl "
    }, 
    {
        "text": "benedict cumberbatch w the photobomb hahahahah I sometimes love the golden globes more than the oscars\n", 
        "names": "benedict cumberbatch "
    }, 
    {
        "text": "Omg Benedict just photobombed Meryl Streep during the awards!!!!! I just can't hahahaha #GoldenGlobes\n", 
        "names": "Omg Benedict "
    }, 
    {
        "text": "Hahahahahah RT @ComplexMag Jeremy Renner had the opportunity to make a boob joke and he took it. #GoldenGlobes https://t.co/7CBg5ObHXF\n", 
        "names": "Jeremy Renner "
    }, 
    {
        "text": "RT @sheilarmeyer: Hahahahahah RT @ComplexMag Jeremy Renner had the opportunity to make a boob joke and he took it. #GoldenGlobes https://t.\u2026\n", 
        "names": "Jeremy Renner "
    }, 
    {
        "text": "If Lana doesn't win the golden globe for big eyes then hahahahaha someone will die.\n", 
        "names": "Lana "
    }, 
    {
        "text": "#GoldenGlobes OMG they OD'd on Bill Cosby hahahaha\n", 
        "names": "Bill Cosby "
    }, 
    {
        "text": "Hahahahaha RT \u201c@MenInBlazers: Alan Cumming is dressed like a tiny midfield prospect Arsene Wenger would sign #GoldenGlobes\u201d\n", 
        "names": "Alan Cumming Arsene Wenger "
    }, 
    {
        "text": "Ricky Gervais hahahahaha that glass of wine #GoldenGlobes\n", 
        "names": "Ricky Gervais "
    }, 
    {
        "text": "RT @sheilarmeyer: Hahahahahah RT @ComplexMag Jeremy Renner had the opportunity to make a boob joke and he took it. #GoldenGlobes https://t.\u2026\n", 
        "names": "Jeremy Renner "
    }, 
    {
        "text": "LOL Gervais mentioning Streep . . . hahahaha #GoldenGlobes\n", 
        "names": "Gervais "
    }, 
    {
        "text": "OMG RICKY GERVAIS hahahahaa #GoldenGlobes\n", 
        "names": "RICKY GERVAIS "
    }, 
    {
        "text": "hahahaha Ricky Gervais is too hilarious at award shows #GoldenGlobes\n", 
        "names": "Ricky Gervais "
    }, 
    {
        "text": "Ricky Gervais just had me CRACKING up! Practicing cuz he didn't want to end up like John Travolta....bwahahahaha! #GoldenGlobes\n", 
        "names": "Ricky Gervais "
    }, 
    {
        "text": "I'm dying seeing the bored faces of people listening to Amy Adams acceptance speech at the Golden Globes hahahahaha\n", 
        "names": "Amy Adams "
    }, 
    {
        "text": "\"@JohnyMyko: Jeremy Renner Made The Obvious Jennifer Lopez\u2019s \u2018Golden Globes\u2019 Joke, so great: https://t.co/AWcT4MlAm7\" ahahahahahahah!!\n", 
        "names": "Jeremy Renner Jennifer Lopez "
    }, 
    {
        "text": "Haw to train your dragon twooo hahahahaha #GoldenGlobesEnTNT #GoldenGlobes\n", 
        "names": "Haw "
    }, 
    {
        "text": "Hahahahaha not Kit Herrington no Jon Snow himself was at the golden globes and he's crying because he's a bastard. http://t.co/7DCA6Q0TxX\n", 
        "names": "Kit Herrington Jon Snow "
    }, 
    {
        "text": "Lily Tomlin and Jane Fonda are absolute legends 'men finally getting the recognition they deserve for comedy' hahahahaha #GoldenGlobes\n", 
        "names": "Lily Tomlin Jane Fonda "
    }, 
    {
        "text": "Don Cheadle: House of Cards!!!!! Bahahahaha!!! #GoldenGlobes\n", 
        "names": "Don Cheadle "
    }, 
    {
        "text": "Alexandro Gonzalez was like my english is terrible . Buhahahahah #GoldenGlobes\n", 
        "names": "Alexandro Gonzalez "
    }, 
    {
        "text": "\"More people will see the Farmers commercial than all my movies combined,\" J.K. Simmons // Hahahahaha #GoldenGlobes\n", 
        "names": "J.K. Simmons "
    }, 
    {
        "text": "Frances McDormand's reaction while listening the speeches are the best!!! Hahahahahahaha!!! #GoldenGlobes\n", 
        "names": "Frances McDormand "
    }, 
    {
        "text": "My friend Calum is lying on the ground crying loudly whenever they show Emma Stone during the Golden Globes. Ahahahaha whatta sucker.\n", 
        "names": "Calum Emma Stone "
    }, 
    {
        "text": "Buhahahahah Wes Anderson with the Best Speech of the night #GoldenGlobes\n", 
        "names": "Wes Anderson "
    }, 
    {
        "text": "\"@glamourmag: Is Matthew McConaughey *extra* southern tonight? #GoldenGlobes\"  Hahahahahaha but it was wonderful right\n", 
        "names": "Matthew McConaughey "
    }, 
    {
        "text": "Bahahahaha Eddie Redmayne cut his honeymoon short to attend the #GoldenGlobes! Hope he feels it was worth it! :D\n", 
        "names": "Eddie Redmayne "
    }, 
    {
        "text": "So I just watched the opening monologue for the golden globes with amy and tina and that bill cosby joke at the end ahahahhahahahaha\n", 
        "names": "tina "
    }, 
    {
        "text": "http://t.co/DulCEQGeYX i died laughing hahahaha i love tina fey and amy poehler \ud83d\ude02\ud83d\ude02\ud83d\ude02  #gg2015\n", 
        "names": "tina fey "
    }, 
    {
        "text": "Tina and Amy hit the Golden Globes once again hahahahaha\n", 
        "names": "Tina Amy "
    }
]

# url_for("static", filename="style.css")
# url_for("static", filename="logic.js")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/winners")
def winners():
	structured_data = winner15_data['structured']
	return render_template('winners.html', data=structured_data)

@app.route("/jokes")
def jokes():
	data = funny_tweets
	return render_template('jokes.html', data=data)
	

if __name__ == "__main__":
    app.run()
