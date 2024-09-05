class quizz_brain:
    
    
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_li = q_list
    

      
    def validate_answer(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
            print ("Má pravdu Předseda")
            self.score+=1

        else:
            print("To není pravda")
            print(f"Správná odpověď je {answer}" )

        print(f"Vaše score je: {self.score} z {self.question_number}")
         
    def next_question(self):
        current_question = self.question_li[self.question_number]
        self.question_number +=1
        user_answer = input(f"Otázka č. {self.question_number}: {current_question.text} (True / False)\n")
        self.validate_answer(user_answer,current_question.answer)
        
    def has_question(self):     
        if self.question_number<len(self.question_li):
            print("Další otázka")
            return True
        else:
            print("další otázky došly")
            return False
        
        
 

        