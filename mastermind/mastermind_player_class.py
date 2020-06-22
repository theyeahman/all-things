
from mastermind_code_class import colour_choice, mastermind_code


class player:

    def __init__(self, code_size = 4, num_col_choice = 6, *args, **kwargs):
        self.guesses = []
        self.feedback_all = []
        self.round = 1
        self.num_col_choice = num_col_choice
        self.code_size = code_size
        self.SECRET_CODE = mastermind_code(
            col_selection_class = colour_choice,
            code_size = code_size,
            numcols = num_col_choice)


    def add_guess(self, code_input = None):
        guess = mastermind_code(
            col_selection_class = colour_choice,
            code_size = self.code_size,
            numcols = self.num_col_choice,
            code = code_input)
        self.guesses.append(guess)
        self.round += 1

    def check_score(self):
        feedback = [0] * self.code_size
        taken_1_point = []
        for i in range(self.code_size):
            if self.guesses[-1][i] == self.SECRET_CODE[i]:
                feedback[i] = 2
            else:
                for j in [num for num in range(self.code_size) if num != i ]:
                    if self.guesses[-1][i] == self.SECRET_CODE[j]:
                        if self.guesses[-1][j] != self.SECRET_CODE[j]:
                            if j not in taken_1_point:
                                feedback[i] =  1
                                taken_1_point.append(j)

        self.feedback_all.append(feedback)


if __name__ == "__main__":

    tom = player(code_size = 5, num_col_choice=2)
    print(tom.num_col_choice)
"""
    tom.add_guess()
    print(tom.guesses[-1])

    tom.check_score()
    print(tom.feedback_all)

    tom.add_guess(code_input = ["black","white","yellow","yellow","grunge"])
    print(tom.guesses[-1])

    tom.check_score()
    print(tom.feedback_all)

    tom.add_guess()
    print(tom.guesses[-1])

    tom.check_score()
    print(tom.feedback_all)

    print(tom.SECRET_CODE)
"""
