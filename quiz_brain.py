class QuizBrain:
    def __init__(self , q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
    def next_question(self):

        inp1= input(f"Q.{self.q_number+1}: {self.q_list[self.q_number].text} (True / False): ")
        inp1 = inp1.lower()
        c_a = self.q_list[self.q_number].answer.lower()
        self.check_answer(inp1 , c_a )
        self.q_number += 1
    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score+=1
            print("You got it right!!")
            print("Your Score is" , self.score , "/" , self.q_number+1)
        else:
            print("You got it Incorrect!!")
            print("The Correct Answer was" , correct_answer)
