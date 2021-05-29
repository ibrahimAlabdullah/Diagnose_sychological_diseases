from experta import *
 
def cf_calculation(cf1, cf2):
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    if cf1 < 0 or cf2 < 0:
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))
    return cf1 + cf2 * (1 + cf1)
#data={'Difficulty_sleeping':0.3,'Fatigue':0.3,'Difficulty_focusing':0.2,'Fear':0,'Suicidal_thoughts':0.1,'Nervous':0.1}
    


difucaltSymptoms=["1 :Suicidal thoughts or suicide attempts",
                        "2 :illusions",
                        "3 :Feeling important and creative",
                        "4 :He seems to like to play alone, expecting his own person in his world",
                        "5 :The need for arrangement and symmetry",
                        "6 :Feeling of muscle tension",
                        "7 :Heart beat or acceleration",
                        "8 :Frequent errors and accidents" 
                 ]
 



class DepressionEngine(KnowledgeEngine):
    SymptomsList = ["Loss of desire to practice regular daily activities ",
                    "Feeling nervous and depressed",
                    "Feeling of hopelessness",
                    "Bouts of crying for no apparent reason",
                    "Sleep disturbances", "Difficulty focusing",
                    "Difficulties and Inability to making decisions",
                    "Difficulty focusing",
                    "Nervousness",
                    "Feeling tired or weak",
                    "Feeling undervalued",
                    "Accidentally gain or lose weight",
                    "Worried and restless", 
                    " Exessive sensitivity",
                    "Suicidal thoughts or suicide attempts",
                    "Unexplained physical problems, such as back or head pain."
                  ]
    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Depression', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        engine1.declare(Fact(work=True))
        #print(self.facts)
    @Rule(Fact(work=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)
        
         
engine1=DepressionEngine()
engine1.reset()
 


class SacehinoprzEngine(KnowledgeEngine):
    SymptomsList = [
            "illusions",
            "Hallucinations",
            "Confusion",
            "Syntax illogical",
            "Jump from one topic to another",
            "Slow moving",
            "Difficulties and Inability to making decisions",
            "Excessive preoccupation with meaningless writing",
            "A tendency to forget certain things or lose (waste) things",
            "Difficulties thinking logically and understanding everyday phenomena",
            "Decreased of feeling or expressing feelings, thoughts and moods that do not fit with the status quo (e.g., frustration crying instead of laughing when hearing a joke)",
            "Repeated movements or gestures, such as walking back and forth or walking in a circle",
            "Withdrawal from family life, community life and social activities",
            "Decreased physical energy",
            "Loss of desire to practice regular daily activities "]
    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Sacehinoprz', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work2=True))
        #print(self.facts)
    @Rule(Fact(work2=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)
        
         
engine2=SacehinoprzEngine()
engine2.reset()
 


class BipolarDisorderEngine(KnowledgeEngine):
    SymptomsList = [
            "Feeling of exhilaration, good psychic, irritable and sensitive",
             "strange",
             "Irritable",
            "Feeling that you don't need to sleep",
            "Loss of appetite to eat",
            "Speak quickly about different things at the same time",
            "Many ideas are mixed",
            "Feeling the ability to do more than one thing at the same time",
            "Doing too much",
            "Feeling important and creative",
            "Loss of desire to practice regular daily activities",
            "Feeling of increased appetite and weight gain",
            "Difficulty focusing to make any decisions",
            "Not feeling comfortable or calm",
            "Feeling of sadness",
            "Felling of anxiety", 
            "Felling of emptinessfor",
            "Feeling of hopelessness",
            "Difficulty going to sleep at night",
             ]
    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'depression', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work3=True))
        #print(self.facts)
    @Rule(Fact(work3=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)
   
         
engine3=BipolarDisorderEngine()
engine3.reset()
 

class AutismEngine(KnowledgeEngine):
    SymptomsList = [
            "not responding to his name",
            "No more direct eye contact",
            "Often he does not hear his interlocutor",
            "He refuses to hug or shrinks on himself",
            "play alone, expecting his own person in his world",
            "Speech begins at a later age",
            "It loses the ability to say specific words or phrases that it previously knew",
            "speaks with a strange voice or with different tones and rhythms",
            "cannot initiate a conversation or continue an existing conversation",
            "may repeat words, phrases or terms, but he does not know how to use them",
            "Perform frequent movements like vibrating, circling or waving",
            "It develops habits and rituals that it always repeats",
            "Always moving",
            "stunned and dazzled by certain parts of items, such as turning a wheel in a toy car",
            "Excessively sensitive to light, sound or touch, but unable to feel pain.",
             ]
    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Autism', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work4=True))
        #print(self.facts)
    @Rule(Fact(work4=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)

engine4=AutismEngine()
engine4.reset()
 
 
 
class ObsessiveCompulsiveDisorderEngine(KnowledgeEngine):
    SymptomsList = [
            "Fear of dirt or pollution",
            "The need for arrangement and symmetry",
            "Passive aggressive desires",
            "Fear of infection",
            "Doubts about locking the door, or turning off the oven",
            "Thoughts of hurting others in a road accident",
            "Severe distress when things are not arranged",
            "Fantasies about harming children",
            "Desire to scream in inappropriate situations",
            "Refrain from situations that can provoke obsessive thoughts, such as shaking hands, for example",
            "Inflammation of the skin from washing hands frequently",
            "Skin scars as a result of excessive treatment of it",
            "Hair loss, or local alopecia, as a result of trichotillomania."
             ]
    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Obsessive Compulsive Disorder', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work5=True))
        #print(self.facts)
    @Rule(Fact(work5=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)

engine5=ObsessiveCompulsiveDisorderEngine()
engine5.reset()
 
 

class AnxietyEngine(KnowledgeEngine):
    SymptomsList = [
            "Headache",
            "Nervousness",
            "tension",
            "Feeling of sore throat",
            "Difficulty focusing",
            "Tired",
            "Irritable",
            "lack of patience",
            "Confusion",
            "Insomnia",
            "Hyperhidrosis",
            "Difficulty breathing",
            "diarrhea",
            "stomach ache"
            
             ]
    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Anxiety', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work6=True))
        #print(self.facts)
    @Rule(Fact(work6=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)

engine6=AnxietyEngine()
engine6.reset()
 


 

class PanicEngine(KnowledgeEngine):
    SymptomsList = [
            "Difficulty breathing",
            "Heart beat or acceleration.",
            "Chills",
            "Hyperhidrosis",
            "Dizziness and dizziness",
            "Feeling of suffocation",
            "Nausea",
            "Chest pain and tightness",
            "Fear of death",
            "Numbness and numbness of the extremities",
            "feeling of separation from the body"
            "Hallucinations",
             ]

    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Panic', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact( Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work7=True))
        #print(self.facts)
    @Rule(Fact(work7=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)

engine7=PanicEngine()
engine7.reset()
 


class InsomniaEngine(KnowledgeEngine):
    SymptomsList = [
            "Difficulty going to sleep at night",
            "Waking up at night",
            "Waking up early",
            "Feeling uncomfortable after sleeping at night",
            "Fatigue or drowsiness during the day",
            "Nervousness",
            "depression",
            "anxiety",
            "Difficulty focusing",
            "Difficulty concentrating on tasks",
            "Frequent errors and accidents",
            "Symptoms of the digestive system",
            "Headache",
            "Constant anxiety about sleep"
             ]

    counter=0
    temp=0
    @DefFacts()
    def init(self):
        yield Fact(name = 'Insomnia', done='False')
        yield Fact( Cf=0)
        yield Fact(start='yes')
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact(  Cf=0))
    def calCF(self,fact1):
 
        for ds in self.SymptomsList:
            print( ds+"?\n")
            self.temp=input("Y or N")
            if(self.temp=="y" or self.temp=="Y" ):
                self.counter+=1
                #print(self.counter)
                self.declare(Fact(Symptoms=ds,value=True))
            else:
                self.counter-=1
        self.temp=float(self.counter/len(self.SymptomsList))
        
        self.declare(Fact(work8=True))
        #print(self.facts)
    @Rule(Fact(work8=True))
    def work(self):
        self.modify(self.facts[2], Cf=self.temp)

engine8=InsomniaEngine()
engine8.reset()
 
class MainEngine(KnowledgeEngine):
    @DefFacts()
    def init(self):
        yield Fact(name = 'MainEngine', done='True')
        yield Fact(start='yes')
        yield Fact(canContinue=True)
    @Rule(NOT(Fact(strat='no')),AS.fact1 << Fact(canContinue=True))
    def calCF(self,fact1):
        liste=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,]
        cf=0
        tempCounter=0
        while(cf<0.8):
            for tempCounter in range(len(difucaltSymptoms)) :
                
                if(liste[tempCounter] is 0 ):
                        print(difucaltSymptoms[tempCounter])
            temp=input("Enter chooice")
            if(temp=="1"):
                engine1.run()
                 
                if(engine1.facts[len(engine1.facts)]['Cf'] >0.8):
                    cf=1
                    print('Depression')
                    
            if(temp=="2"):
                 engine2.run()
                 if(engine2.facts[len(engine2.facts)]['Cf'] >0.8):
                    cf=1
                    
                    
                    print(" Sacehinoprz")
                 else:
                    liste[int(temp)-1]= int(temp)
                    engine2.reset()
                     
                
            if(temp=="3"):
                engine3.run()
                if(engine3.facts[len(engine3.facts)]['Cf'] >0.8):
                    cf=1
                    print('Bipolar Disorder')
                       
                else:
                    liste[int(temp)-1]= int(temp)
                    engine3.reset()
                    #print(liste)
                
            if(temp=="4"):
                
                engine4.run()
                if(engine4.facts[len(engine4.facts)]['Cf'] >0.8):
                    cf=1
                    print('Autism')
                       
                else:
                    liste[int(temp)-1]= int(temp)
                    engine4.reset()
                
            if(temp=="5"): 
                engine5.run()
                if(engine5.facts[len(engine5.facts)]['Cf'] >0.8):
                    cf=1
                    print('Obsessive Compulsive Disorder')   
                else:
                    liste[int(temp)-1]= int(temp)
                    engine5.reset()
                
            if(temp=="6"):
                engine6.run()
                if(engine6.facts[len(engine6.facts)]['Cf'] >0.8):
                    cf=1
                    print('Anxiety')
                      
                else:
                    liste[int(temp)-1]= int(temp)
                    engine6.reset()
                
            if(temp=="7"):  
                engine7.run()
                if(engine7.facts[len(engine7.facts)]['Cf'] >0.8):
                    cf=1
                    print('Panic')
                       
                else:
                    liste[int(temp)-1]= int(temp)
                    engine6.reset()
            if(temp=="8"):
                engine8.run()
                if(engine8.facts[len(engine8.facts)]['Cf'] >0.8):
                    cf=1
                    print('Insomnia')
                      
                else:
                    liste[int(temp)-1]= int(temp)
                    engine6.reset()
            if(temp=="0"):
                exit(-1)
engine=MainEngine()
engine.reset()
engine.run()