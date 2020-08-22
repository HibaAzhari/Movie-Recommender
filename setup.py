from PSmodel import Condition, ProductionSystem

light = Condition("Light-hearted", False)
intense = Condition("Action-packed", False)
before2010 = Condition("Released before 2010", False)
after2010 = Condition("Released after 2010", False)
over2hrs = Condition("Longer than 2 hours", False)
under2hrs = Condition("Shorter than 2 hours", False)
american = Condition("American", False)
intl = Condition("International", False)

movies = []
D_A_F = Condition("Death at a Funeral(2007)", True)
L_W_R = Condition("Love Wedding Repeat", True)
chungking = Condition("The Chungking Express", True)
nineteen17 = Condition("1917", True)
badboys = Condition("Bad Boys", True)
frozen2 = Condition("Frozen 2", True)
saw = Condition("Saw", True)
theGrudge = Condition("The Grudge", True)
heraPheri = Condition("Hera Pheri", True)
kingsman = Condition("Kingsman: The Secret Service", True)
theHost = Condition("The Host", True)
parasite = Condition("Parasite", True)
weddingCrash = Condition("The Wedding Crashers", True)
jumanji2 = Condition("Jumanji II", True)
titanic = Condition("Titanic", True)
twelveYrs = Condition("12 Years A Slave", True)

movies.append(weddingCrash)
movies.append(chungking)
movies.append(saw)
movies.append(jumanji2)
movies.append(heraPheri)
movies.append(nineteen17)
movies.append(badboys)
movies.append(frozen2)
movies.append(titanic)
movies.append(parasite)
movies.append(theGrudge)
movies.append(D_A_F)
movies.append(twelveYrs)
movies.append(kingsman)
movies.append(L_W_R)
movies.append(theHost)

class Setup:
    def __init__(self):

        conditions = [] # Initialize list of possible conditions (Knowledge-Base)

        # Conditions relevant to movie recommender:
        # Genre:
        
        conditions.append(light)
        
        conditions.append(intense)
        comedy = Condition("Comedy", False)
        conditions.append(comedy)
        animation = Condition("Animation", False)
        conditions.append(animation)
        drama = Condition("Drama", False)
        conditions.append(drama)
        action = Condition("Action", False)
        conditions.append(action)
        war = Condition("War", False)
        conditions.append(war)
        thriller = Condition("Thriller", False)
        conditions.append(thriller)
        history = Condition("History", False)
        conditions.append(history)
        romance = Condition("Romance", False)
        conditions.append(romance)
        # Age:
        
        conditions.append(before2010)
        
        conditions.append(after2010)
        old = Condition("Old", False)
        conditions.append(old)
        new = Condition("New", False)
        conditions.append(new)
        # Runtime:
        
        conditions.append(over2hrs)
        
        conditions.append(under2hrs)
        Long = Condition("Long", False)
        conditions.append(Long)
        short = Condition("Short", False)
        conditions.append(short)
        # Origin country:
        
        conditions.append(american)
        
        conditions.append(intl)
        british = Condition("British", False)
        conditions.append(british)
        korean = Condition("Korean", False)
        conditions.append(korean)
        bollywood = Condition("Bollywood", False)
        conditions.append(bollywood)
        # Movies:
        conditions.append(D_A_F)
        conditions.append(L_W_R)
        conditions.append(chungking)
        conditions.append(nineteen17)
        conditions.append(badboys)
        conditions.append(frozen2)
        conditions.append(saw)
        conditions.append(theGrudge)
        conditions.append(heraPheri)
        conditions.append(kingsman)
        conditions.append(theHost)
        conditions.append(parasite)
        conditions.append(weddingCrash)
        conditions.append(jumanji2)
        conditions.append(titanic)
        conditions.append(twelveYrs)

        movieRecommender = ProductionSystem(conditions) # Initialize movie recommender production system

        rules = [] # Initialize list of rules

        # For Genre:
        rules.append(ProductionSystem.Rule(movieRecommender, [light], [comedy, action, animation],"IF light movie PUT ON WM: Comedy, Drama"))
        rules.append(ProductionSystem.Rule(movieRecommender, [intense], [thriller, romance, drama, war, history],"IF intense movie PUT ON WM: Thriller, Romance, Drama, Action"))
        # For Age:
        rules.append(ProductionSystem.Rule(movieRecommender, [before2010], [old],"IF release date < 2010 PUT ON WM: OLD"))
        rules.append(ProductionSystem.Rule(movieRecommender, [after2010], [new],"IF release date > 2010 PUT ON WM: NEW"))
        # For Runtime:
        rules.append(ProductionSystem.Rule(movieRecommender, [under2hrs], [short],"IF viewing time < 2 hrs PUT ON WM: Short"))
        rules.append(ProductionSystem.Rule(movieRecommender, [over2hrs], [Long],"IF viewing time > 2 hrs PUT ON WM: Long"))
        # For Origin:
        rules.append(ProductionSystem.Rule(movieRecommender, [intl], [korean, british, bollywood],"IF international PUT ON WM: korean, british, bollywood"))
        # For movies:
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, old, short, american], [badboys],"IF comedy, old, short and american PUT ON WM: badboys"))
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, old, short, british], [D_A_F],"IF comedy, old, short and british PUT ON WM: Death at a Funeral"))
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, old, Long, american], [weddingCrash],"IF comedy, drama, old, long and american PUT ON WM: The wedding Crashers"))
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, old, Long, bollywood], [heraPheri],"IF comedy, old, long and bollywood PUT ON WM: Hera Pheri"))
        rules.append(ProductionSystem.Rule(movieRecommender, [animation, new, short, american], [frozen2],"IF drama, animation, new, short and american PUT ON WM: Frozen 2"))
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, new, short, british], [L_W_R],"IF drama, comedy, new, short and british PUT ON WM: Love Wedding Repeat"))
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, action, new, Long, american], [jumanji2],"IF comedy, action, new, long and american PUT ON WM: Jimanji II"))
        rules.append(ProductionSystem.Rule(movieRecommender, [comedy, action, new, Long, british], [kingsman],"IF comedy, action, new, long and british PUT ON WM: Kingsman"))
        rules.append(ProductionSystem.Rule(movieRecommender, [thriller, old, short, american], [saw],"IF thriller, old, short and american PUT ON WM: Saw"))
        rules.append(ProductionSystem.Rule(movieRecommender, [drama, romance, old, short, korean], [chungking],"IF drama, romance, short and korean PUT ON WM: The Chungking Express"))
        rules.append(ProductionSystem.Rule(movieRecommender, [romance, old, Long, american], [titanic],"IF romance, old, long and american PUT ON WM: Titanic"))
        rules.append(ProductionSystem.Rule(movieRecommender, [thriller, old, Long, korean], [theHost],"IF thriller, old, long and korean PUT ON WM: The Host"))
        rules.append(ProductionSystem.Rule(movieRecommender, [thriller, new, short, american], [theGrudge],"IF thriller, new, short and american PUT ON WM: The Grudge"))
        rules.append(ProductionSystem.Rule(movieRecommender, [drama, war, new, short, british], [nineteen17],"IF drama, war, new, short and british PUT ON WM: 1917"))
        rules.append(ProductionSystem.Rule(movieRecommender, [drama, history, new, Long, american], [twelveYrs],"IF drama, history, new, long and american PUT ON WM: Twelve Years A Slave"))
        rules.append(ProductionSystem.Rule(movieRecommender, [thriller, new, Long, korean], [parasite],"IF thriller, new, long and korean PUT ON WM: Parasite"))
        
        movieRecommender.setRules(rules)
        self.system = movieRecommender