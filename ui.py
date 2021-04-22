from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # add question
        self.question_box = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_box.create_text(
            150,
            125,
            text="Text",
            width=290,
            font=(FONT_NAME, 20, "italic"),
            fill=THEME_COLOR)
        self.question_box.grid(column=0, row=1, columnspan=2, pady=50)
        # add buttons
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.select_true, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.select_false, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        # add score
        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=(FONT_NAME, 14, "normal"))
        self.score_text.grid(column=1, row=0)
        # initialize first question
        self.show_next_question()
        # hold window
        while self.quiz.still_has_questions():
            self.window.mainloop()

    def show_next_question(self):
        self.question_box.config(bg="white")
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            question_text = self.quiz.current_question.text
            self.question_box.itemconfig(self.question_text, text=f"Q{self.quiz.question_number}: {question_text}")
            self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number-1}")
        else:
            self.question_box.itemconfig(self.question_text, text="You've finished the quiz.")
            self.score_text.config(text=f"Total score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def select_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)
        self.window.after(1000, self.show_next_question)

    def select_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
        self.window.after(1000, self.show_next_question)

    def give_feedback(self, is_correct):
        if is_correct:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")

