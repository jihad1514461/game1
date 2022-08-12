import random
import os,sys

clear = lambda: os.system('cls')


stra, dex, inte, char, vit, wis= 5,5,5,5,5,5

def total(clss,stra, dex, inte):
    if clss == "warrior" or clss == "1" or clss == "Warrior":
        total = stra*3 + dex*2.5 + inte*2
    elif clss == "mage" or clss == "2" or clss == "Mage":
        total = stra*2 + dex*2.5 + inte*3
    elif clss == "hunter" or clss == "3" or clss == "Hunter":
        total = stra*2.5 + dex*3 + inte*2
    elif clss == "allround" or clss == "4" or clss == "Allround":
        total = stra*2.56667 + dex*2.56667 + inte*2.56667
    else:
        total = stra*random.randint(1,3) + dex*random.randint(1,3) + inte*random.randint(1,3)
        
    total=int(total)
    return total

class player:
    def playerinfo(self,clss, name, stra, dex, inte, char, vit, wis,exp,ap,lv,expfull,defe):
        self.clss   = clss
        self.name   = name 
        self.stra   = stra
        self.dex    = dex
        self.inte   = inte
        self.cher   = char
        self.vit    = vit
        self.wis    = wis
        self.hp     = self.vit*10
        self.mp     = int(self.wis/3)
        tota        = total(self.clss,self.stra, self.dex, self.inte)
        self.tota   = tota
        self.exp    = exp
        self.expfull= expfull
        self.ap     = ap
        self.lv     = lv
        self.defe   = defe
        
    def stat(self):
        print(f'''
            Name  = {self.name}    
            class = {self.clss}     
            level = {self.lv:<15}  str   = {self.stra:<15}
            hp    = {self.hp:<15}  dex   = {self.dex:<15}
            mp    = {self.mp:<15}  int   = {self.inte:<15} 
            exp   = {self.exp:<4}/{self.expfull:<10}  char  = {self.cher:<15}
            ap    = {self.ap:<15}  vit   = {self.vit:<15}
            total = {self.tota:<15}  wis   = {self.wis:<15}
          
            
            ''')
        
    def statupdater(self,uap,stra, dex, inte, char, vit, wis):
        self.ap     -= uap
        self.stra   += stra
        self.dex    += dex
        self.inte   += inte
        self.cher   += char
        self.vit    += vit
        self.wis    += wis
        self.hp      = 2+int(self.vit/3)
        self.mp      = 2+int(self.wis/3)
        tota         = total(self.clss,self.stra, self.dex, self.inte)
        self.tota    = tota
     
    def levelup(self,exp):
        self.exp += exp
        f=0
        if  self.expfull == self.exp:
            self.exp = 0
            self.lv += 1
            self.ap += 4
            self.expfull =self.lv*10
            f=1
        elif self.expfull < self.exp:
            while self.expfull < self.exp:
                self.exp = self.exp-self.expfull 
                self.lv += 1
                self.ap += 4
                self.expfull =self.lv*10
                f=1
            
        return f
                  
def chos():
    ap = player1.ap
    
    s  = int(input("enter sta : "))
    d  = int(input("enter dex : "))
    i  = int(input("enter int : "))
    c  = int(input("enter char: "))
    v  = int(input("enter vit : "))
    w  = int(input("enter wis : "))
    uap = s+d+i+c+v+w 
    if uap > ap:
        print('not enough ap')
        chos()
        print("1")
    else:
        reset= input("reset?:")
        if reset =='y': 
            chos()
        else:
            print("updating")      
            player1.statupdater(uap,s,d,i,c,v,w)
    
def lvup(exp):
    a = player1.levelup(exp)
    if a == 1:
        player1.stat()
        chos()
    
player1 = player()
player2 = player()
head    = player()
weapon  = player()
body    = player() 
lring   = player() 
rring   = player() 
pant    = player()
shoe    = player()
s,d,i,c,v,w,e,ap,lv,epfull,df=3,3,3,3,3,3,0,10,1,10,2
player1.playerinfo("mage","jihad",s,4,i,c,v,w,e,ap,lv,epfull,df)
player2.playerinfo("warrior","dipu",s,d,i,c,v,w,5,ap,lv,epfull,df)
head.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1)
weapon.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1)
body.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1)
lring.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1) 
rring.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1)
pant.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1)
shoe.playerinfo("mage","robe",0,0,0,0,0,0,0,0,1,1,1)

def playereqp():
    p1n  = player1.name 
    p1hp = player1.hp   + head.hp   + weapon.hp   + body.hp   + lring.hp   + rring.hp   + pant.hp +shoe.hp
    p1mp = player1.mp   + head.mp   + weapon.mp   + body.mp   + lring.mp   + rring.mp   + pant.mp +shoe.mp
    p1s  = player1.stra + head.stra + weapon.stra + body.stra + lring.stra + rring.stra + pant.stra +shoe.stra
    p1d  = player1.dex  + head.dex  + weapon.dex  + body.dex  + lring.dex  + rring.dex  + pant.dex +shoe.dex
    p1i  = player1.inte + head.inte + weapon.inte + body.inte + lring.inte + rring.inte + pant.inte +shoe.inte
    p1t  = player1.tota + head.tota + weapon.tota + body.tota + lring.tota + rring.tota + pant.tota +shoe.tota 
    p1v  = player1.vit  + head.vit  + weapon.vit  + body.vit  + lring.vit  + rring.vit  + pant.vit +shoe.vit 
    p1w  = player1.wis  + head.wis  + weapon.wis  + body.wis  + lring.wis  + rring.wis  + pant.wis +shoe.wis 
    p1c  = player1.cher + head.cher + weapon.cher + body.cher + lring.cher + rring.cher + pant.cher +shoe.cher 
    p1df =                head.defe + weapon.defe + body.defe + lring.defe + rring.defe + pant.defe +shoe.defe
    return p1hp,p1mp,p1s,p1d,p1i,p1t,p1n,p1v,p1w,p1c,p1df

def estat():
    p1hp,p1mp,p1s,p1d,p1i,p1t,p1n,p1v,p1w,p1c,p1df  = playereqp()
    print(f'''
            Name  = {p1n}    
            class = {player1.clss}     
            level = {player1.lv:<15}  str   = {p1s:<15}
            hp    = {p1hp:<15}  dex   = {p1d:<15}
            mp    = {p1mp:<15}  int   = {p1i:<15} 
            exp   = {player1.exp:<4}/{player1.expfull:<10}  char  = {p1c:<15}
            ap    = {player1.ap:<15}  vit   = {p1v:<15}
            total = {p1t:<15}  wis   = {p1w:<15}
      

        ''')

 

#clear() 
i=0

#lvup(99)    
#enemy()

def fight():
    p1hp,p1mp,p1s,p1d,p1i,p1t,p1n,p1v,p1w,p1c,p1df  = playereqp()
    p2hp,p2mp,p2s,p2d,p2i,p2t,p2n,p2e,p2df = player2.hp, player2.mp, player2.stra, player2.dex, player2.inte, player2.tota, player2.name, player2.exp, player2.defe
    estat()
    player2.stat()
    if p1d>p2d: turn = p1n
    else: turn = p2n
    p1en,p2en= 0,0
    p1r  = (1-p1df/100)
    p2r  = (1-p2df/100)
    p1es = int(p1t/4 - p1i/9 )
    p1eh = int(p1t/5 - p1i/15)
    p1st = (p1t*1.5 + p1s)
    p1hl = p1i*4
    p1nt = int(p1t*p2r)
    p1st = int(p1st*p2r)
    
    
    p2es = int(p2t/4 - p2i/9 )
    p2eh = int(p2t/5 - p2i/15)
    p2st = p2t*1.5  + p2s
    p2hl = p2i*4 
    p2t *= p1r
    p2nt = int(p2t*p1r)
    p2st = int(p2st*p1r)
    
    while p1hp>=0 or p2hp>=0:
        p1nt=random.randint(p1nt-5,p1nt)
        p1st=random.randint(p1st-9,p1st)
        p2nt=random.randint(p2nt-5,p2nt)
        p2st=random.randint(p2st-9,p2st)
        
        print(f'''
          turn = {turn:<13}
          player hp  = {p1hp:<12}      enemy hp {p2hp:<12}
          player mp  = {p1en:<12}      enemy mp {p2en:<12}          
          ''')
        if p1hp<=0 or p2hp<=0: break
        if turn == p1n:
            a = int(input(f'\n1. normal atk {p1nt} and +{p1mp} \n2. special atk {p1st} and -{p1es} \n3. heal +{p1hl} and -{p1eh} \nchoose an action: '))
            if a == 1:
                p2hp -= p1nt
                p1en += p1mp
                turn  = p2n
                print(f'player attack {p1nt}' )
            elif a == 2 and p1en >= p1es:
                p2hp -= p1st
                p1en -= p1es
                turn  = p2n
            elif a == 3 and p1en >= p1eh:
                p1hp += p1hl
                p1en -= p1eh
                turn  = p2n
            else :
                print('not enough mp or wrong number')
                turn = p1n
        else: 
            if p1hp <= p2st and p2en >= p2es:
                p1hp -= p2st
                p2en -= p2es
                turn  = p1n
            elif p2hp< player2.hp/4 and p2en >= p2eh:
                p2hp += p2hl
                p2en -= p2eh
                turn  = p1n
            elif p2en >= p2es:
                p1hp -= p2st
                p2en -= p2es
                turn  = p1n
            else:
                p1hp -= p2nt
                p2en += p2mp
                turn  = p1n
                print(f'enemy attack {p2nt}' )
    
    
    if  p1hp<=0 and p2hp<=0:
        print("draw")
    elif p2hp<=0:
        print('player win')
        lvup(p2e)
    else: print('enemy win')
    
fight()


