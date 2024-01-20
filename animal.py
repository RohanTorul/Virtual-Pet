import random as rand
import time
chooseindex = lambda arr: rand.randrange(0,len(arr),1)
calc_int_average = lambda n: sum(n)//len(n)
def gameMsg(s:str):
    print("-"*len(s))
    print()
    print("-"*len(s))


class animal:
    health : float = 0.0
    name : str = ""
    hunger : float = 0.0
    happiness : float = 0.0
    boredom: float = 0.0
    difficulty: float = 0.0
    favourite_food: str = {}
    hated_food: str = {}
    born_time : float = 0.0
    current_time : float = 0.0
    MAX:int = 100

    happy_faces=["ヾ(＠⌒▽⌒＠)ﾉ",
                 "(°∀°)",
                 "┏(＾0＾)┛┗(＾0＾) ┓",
                 "ヽ(‘ ∇‘ )ノ",
                 "!⑈ˆ~ˆ!⑈",
                 "●ᴥ●",
                 "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
                 "(づ｡◕‿‿◕｡)づ",
                 "(〃^∇^)ﾉ",
                 "ヾ(＠＾▽＾＠)ﾉ"
                 ]
    not_happy_faces=["ಥ_ಥ",
                     "o(╥﹏╥)o",
                     "(ㄒoㄒ)",
                     "(✖╭╮✖)",
                     "(x_x☆",
                     "(◕﹏◕✿)",
                     "v(ಥ ̯ ಥ)v",
                     "(╥_╥)",
                     "٩(× ×)۶"
                     ]
    
    def __init__(self,name:str, difficulty:float):
        self.name = name
        self.difficulty = difficulty
        self.born_time = time.time()
        self.current_time = self.born_time
        
    def increaseHunger(self, food:str):
        self.hunger -= self.favourite_food[food] * 1/self.difficulty
        self.happiness += self.favourite_food[food]/self.difficulty
    def decreaseHunger(self, food:str):
        pass
    def increaseBoredom(self):
        pass
    def decreaseBoredom(self):
        pass
    def increaseBoredom(self):
        pass
        
    def feed(self,food:str, amount:int):
        eatingSounds = ["nom","nyam","nyom","nam"]
        
        print(eatingSounds[chooseindex(eatingSounds)],
              eatingSounds[chooseindex(eatingSounds)],
              eatingSounds[chooseindex(eatingSounds)],"...")
        gameMsg(self.name + " ate " + food)

        if(food in self.favourite_food): 
            
            self.hunger -= self.favourite_food[food] * 1/self.difficulty

        elif(food in self.hated_food):
            
             self.hunger += self.hated_food[food] * self.difficulty
             self.happiness -= self.hated_food[food]/(100*self.difficulty)

        else: 

            food_like_level = round(rand.uniform(0, 20), 3)

            if food_like_level > 5 + (self.difficulty*5) :
                 
                 self.favourite_food[food] = food_like_level
                 self.hunger -= self.favourite_food[food] * 1/self.difficulty

            else: 
                self.hated_food[food] = food_like_level
                self.hunger += self.hated_food[food] * self.difficulty
                self.happiness -= self.hated_food[food]/(100*self.difficulty)
            

    def Update(self):
        time_now = time.time()
        time_passed = time_now - self.current_time

        
    def showFace(self, state:float):
        return((self.happy_faces[chooseindex(self.happy_faces)]*(state >= self.MAX/2)) +
                (self.not_happy_faces[chooseindex] * (state < self.MAX/2)) )

    def CheckStatus(self):
        self.Update(self)
        gameMsg(self.name+" is "+ str((self.current_time -  self.born_time)))
        gameMsg(self.name+" 's health: "+("▄"*(self.health/10)))
        gameMsg(self.name+" 's hunger: "+("▄"*(self.hunger/10)))
        gameMsg(self.name+" 's happiness: "+("▄"*(self.happiness/10)))
        self.showFace(calc_int_average([self.health ,self.happiness]))
    
