from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizBrain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR, justify="center",
                                                     width=280,
                                                     font=("Courier", 12, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1, pady=20)

        self.score_label = Label(text="Score: 0", font=("Courier", 10), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, sticky="e")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg=THEME_COLOR)
            self.canvas.itemconfig(self.question_text, fill="white",
                                   text=f"You reached the end of "f"QuizBrain!\nYour final score is: {self.quiz.score}/"
                                        f"{len(self.quiz.question_list)}")
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
