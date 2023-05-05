import json
import random
import textwrap
from time import time, sleep
import itertools
from rich.console import Console
from rich.text import Text
import os
console = Console()

# Load jokes from JSON file


data_file_path = os.path.join(os.path.dirname(__file__), "jokesdata.json")
with open(data_file_path, "r") as file:

    jokes_data = json.load(file)

# Convert JSON object to list of tuples and get unique categories
jokes_list = [(joke["joke"], joke["punchline"], joke["category"]) for joke in jokes_data]
categories = set([joke[2] for joke in jokes_list])

# Shuffle the jokes to ensure they are not told in the same order every time
random.shuffle(jokes_list)

def tell_joke(joke):
    max_width = 80 # adjust as needed
    
    # Generate random color for the joke and punchline
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    joke_color = random.choice(colors)
    punchline_color = random.choice(colors)
    
    # Add emojis to the joke and punchline
    joke_emoji = itertools.cycle(["😄", "😃", "😁", "😆"])
    punchline_emoji = itertools.cycle(["😆", "😂", "🤣"])
    
    joke_lines = textwrap.wrap(joke[0], max_width)
    for line in joke_lines:
        console.print(Text("\r" + next(joke_emoji) + " " + line, style=joke_color), end="")
        sleep(0.05) # add delay between lines
        
    sleep(1) # add delay before punchline
    
    console.print(Text("\r" + next(punchline_emoji) + " " + joke[1], style=punchline_color), end="")
    sleep(0.3)
    console.print()  # move to the next line


emoji_sequence = ["😃", "😄", "😁", "😆", "😂", "🤣", "😜", "😝", "🤪", "😎"]

told_jokes = [] # keep track of told jokes
start_time = time()
while True:
    # Choose a random category
    category = random.choice(list(categories))
    category_jokes = [j for j in jokes_list if j[2] == category and j not in told_jokes]
    if category_jokes:
        joke = random.choice(category_jokes)
        tell_joke(joke)
        told_jokes.append(joke)
    
    # Choose an emoji to display
    elapsed_time = time() - start_time
    emoji = emoji_sequence[int(elapsed_time / 10) % len(emoji_sequence)]
    
    # Print the emoji and elapsed time
    console.print(emoji, end="")
    console.print(Text(f" {int(elapsed_time)} seconds", style="bold"), end="")
    
    # Check if 10 seconds have elapsed since the start of the loop
    if time() - start_time >= 10:
        break
    
    # Add a small delay between iterations to make the animation smoother
    sleep(0.05)

console.print(f"\nFinished! 🎉🎆🎇 Total jokes told: {len(told_jokes)}")
