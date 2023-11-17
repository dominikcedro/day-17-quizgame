
class QuizBrain:

    def __int__(self, q_list, twojastara):
        self.q_number = 0
        self.q_list = q_list
        self.twojastara = twojastara

    def next_q(self):
        current_q = self.q_list[self.q_number]
        input(f"Q.{self.q_number}: {current_q.text} (True/False): ")
