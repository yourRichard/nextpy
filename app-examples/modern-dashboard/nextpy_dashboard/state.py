import nextpy as xt
import asyncio
import random
import time
from datetime import datetime

class State(xt.State):
    prompt:str = ""
    leftSpacing: str = "0.5rem",
    spacing: str = "0.5rem",
    oneBlockSpace = "0.5rem"

    def setFull(self):
        self.oneBlockSpace = "0.5rem",
        self.spacing = "0.5rem",
        self.leftSpacing = "0.5rem"

    def setHalf(self):
        self.oneBlockSpace = "0.5rem",
        self.spacing = "5rem",
        self.leftSpacing = "0.5rem"

    def setThree(self):
        self.oneBlockSpace = "0.5rem",
        self.spacing = "5rem",
        self.leftSpacing = "4rem"

    def setFour(self):
        self.spacing = "5rem"
        self.oneBlockSpace = "5rem",
        self.leftSpacing = "4rem"


    def emptyFunction(self):
        pass

    async def passwordGenerate(self):
        self.prompt = ""
        uppercase_letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
        lowercase_letter = uppercase_letter.lower()
        digits = "0123456789"
        symbols = "!@#$^&*"
        upper,lower,digts,syms = True,True,True,True
        all = ""

        if upper:
            all += uppercase_letter
        if lower:
            all += lowercase_letter
        if digts:
            all += digits
        if syms:
            all += symbols
        length = 10
        greet = "Generating unique password..."
        async for _ in self.typeWriterEffect(greet,True,3):
            yield
        self.prompt = ""
        password = "".join(random.sample(all,length))
        async for _ in self.typeWriterEffect(password,True,3):
            yield
    async def getDate(self):
        self.prompt = ""
        time_object = time.localtime()
        locate_time = time.strftime("Current date and year: %B/%d/%y",time_object)
        async for _ in self.typeWriterEffect(locate_time,True,3):
            yield

    async def getQuates(self):
        self.prompt = ""
        quotes = random.choice([
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "It always seems impossible until it's done. - Nelson Mandela",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Don't be afraid to die; it is more peaceful than living. - Richard Min"
        ])
        greet = "Giving the best quote to make your day..."
        async for _ in self.typeWriterEffect(greet,True,3):
            yield
        self.prompt = ""
        main_quote = f"{quotes}"
        async for _ in self.typeWriterEffect(main_quote,True,3):
            yield

    async def getMovies(self):
        self.prompt = ""
        movies_recommendations = random.choice([
        "The Shawshank Redemption by Frank Darabont - 1994",
        "The Godfather by Francis Ford Coppola - 1972",
        "Forrest Gump by Robert Zemeckis - 1994",
        "Schindler's List by Steven Spielberg - 1993",
        "The Pursuit of Happyness by Gabriele Muccino - 2006",
        "The Dark Knight by Christopher Nolan - 2008",
        "Mad Max: Fury Road by George Miller - 2015",
        "Die Hard by John McTiernan - 1988",
        "Kill Bill: Volume 1 by Quentin Tarantino - 2003",
        "Gladiator by Ridley Scott - 2000",
        "Anchorman: The Legend of Ron Burgundy by Adam McKay - 2004",
        "Superbad by Greg Mottola - 2007",
        "The Grand Budapest Hotel by Wes Anderson - 2014",
        "Ferris Bueller's Day Off by John Hughes - 1986",
        "Dumb and Dumber by Peter Farrelly - 1994",
        "Blade Runner by Ridley Scott - 1982",
        "The Matrix by Lana Wachowski, Lilly Wachowski - 1999",
        "Inception by Christopher Nolan - 2010",
        "Interstellar by Christopher Nolan - 2014",
        "E.T. the Extra-Terrestrial by Steven Spielberg - 1982",
        "The Lord of the Rings: The Fellowship of the Ring by Peter Jackson - 2001",
        "Harry Potter and the Sorcerer's Stone by Chris Columbus - 2001",
        "The Princess Bride by Rob Reiner - 1987",
        "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe by Andrew Adamson - 2005",
        "Stardust by Matthew Vaughn - 2007",
        "Se7en by David Fincher - 1995",
        "The Silence of the Lambs by Jonathan Demme - 1991",
        "Gone Girl by David Fincher - 2014",
        "Shutter Island by Martin Scorsese - 2010",
        "Memento by Christopher Nolan - 2000",
        "Toy Story by John Lasseter - 1995",
        "Finding Nemo by Andrew Stanton, Lee Unkrich - 2003",
        "Spirited Away by Hayao Miyazaki - 2001",
        "The Incredibles by Brad Bird - 2004",
        "Zootopia by Byron Howard, Rich Moore - 2016",
        "The Notebook by Nick Cassavetes - 2004",
        "Pride and Prejudice by Joe Wright - 2005",
        "La La Land by Damien Chazelle - 2016",
        "Eternal Sunshine of the Spotless Mind by Michel Gondry - 2004",
        "Before Sunrise by Richard Linklater - 1995",
        "The Da Vinci Code by Ron Howard - 2006",
        "Knives Out by Rian Johnson - 2019",
        "Sherlock Holmes by Guy Ritchie - 2009",
        "Murder on the Orient Express by Kenneth Branagh - 2017",
        "Blackfish by Gabriela Cowperthwaite - 2013",
        "Planet Earth by Alastair Fothergill - 2006",
        "Won't You Be My Neighbor? by Morgan Neville - 2018"
        ])
        
        greet = "Giving you the movie recommandation..."
        async for _ in self.typeWriterEffect(greet,True,3):
            yield
        self.prompt = ""
        main_movie = f"{movies_recommendations}"
        async for _ in self.typeWriterEffect(main_movie,True,3):
            yield

    async def getTime(self):
        self.prompt = ""
        time = datetime.today().strftime("%I:%M:%S - %p")
        current_time = f"Current time: {time}"
        async for _ in self.typeWriterEffect(current_time,True,3):
            yield

    async def greetOnLoad(self):
        self.prompt = ""
        sent: str = "Get started by clicking a box..."
        async for _ in self.typeWriterEffect(sent,True,3):
            yield

    async def typeWriterEffect(self,string,erase,pause=2):
        for char in list(string):
            await asyncio.sleep(0.05),
            self.prompt += char
            yield

        if erase:
            await asyncio.sleep(pause)
            for char in list(string):
                await asyncio.sleep(0.05)
                self.prompt = self.prompt[:-1]
                yield