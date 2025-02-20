from enum import Enum

class CONST(Enum):
    MANIFESTO_LINK = "https://www.washingtonpost.com/wp-srv/national/longterm/unabomber/manifesto.text.htm"
    PROMPT = f'''
        This is being fed into another automated program so don't include intros or outros such as "Certainly, here is..." or "Let me know if there is anything else", etc.

        You're goal is to summarize sections of the Unibomber's Manifesto into "Gen Z Brain rot" slang. I will tell you in subsequent API calls which section you are currently summarizing.

        You're text will be fed into another AI to be turned into audio clips. The goal is for these to be read aloud by another AI and put on Tiktok & Instagram Reels. So try to make your responses as close to what you feel would be 60 seconds of audio when read aloud.
        
        The hyperlink for the text can be found here: {MANIFESTO_LINK}

        As you can see the sections are:
            1) INTRODUCTION: Verses 1 - 5
            2) THE PYSCHOLOGY OF MODERN LEFTISM: Verses 6 - 9
            3) FEELINGS OF INFERIORITY: Verses 10 - 23
            4) OVERSOCIALIZATION: Verses 24 - 32
            5) THE POWER PROCESS: Verses 33 - 37
            6) SURROGATE ACTIVITIES: Verses 38 - 41
            7) AUTONOMY: Verses 42 - 44
            8) SOURCES OF SOCIAL PROBLEMS: Verses 45 - 58
            9) DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY: Verses 59 - 76
            10) HOW SOME PEOPLE ADJUST: Verses 77 - 86
            11) THE MOTIVES OF SCIENTISTS: 


    '''