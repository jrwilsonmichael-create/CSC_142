import tkinter as tk
from tkinter import messagebox

class TriviaGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Albright College Trivia Game")
        self.root.geometry("600x500")
        self.root.config(bg="Royal Blue")
        
        self.questions = [
            {
                "question": "When did Albright college trace their roots to union seminary?",
                "choices": ["1817", "1856", "1920", "1945"],
                "answer": "1856"
            },
            {
                "question": "What is Albright college mostly named after?",
                "choices": ["A founder", "Jacob Albright", "A state", "A president"],
                "answer": "Jacob Albright"
            },
            {
                "question": "Who did Albright merge with in 1928?",
                "choices": ["Pennsylvania College", "Reading College", "Schuylkill College", "Central College"],
                "answer": "Pennsylvania College"
            },
            {
                "question": "Is it true that Albright merged 19th-century church-founded schools?",
                "choices": ["True", "False"],
                "answer": "True"
            },
            {
                "question": "What is Albright recognized for academically?",
                "choices": ["Engineering", "Liberal Arts", "Medicine", "Law"],
                "answer": "Liberal Arts"
            },
            {
                "question": "What is the origin of the Albright surname?",
                "choices": ["English", "German", "French", "Welsh"],
                "answer": "German"
            }
        ]
        
        self.score = 0
        self.current_question = 0
        self.selected_answer = tk.StringVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Albright College Trivia", 
                               font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue")
        title_label.pack(pady=10)
        
        # Score label
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}/{len(self.questions)}", 
                                    font=("Arial", 14), bg="lightblue")
        self.score_label.pack(pady=5)
        
        # Question label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), 
                                       bg="lightblue", wraplength=500, justify=tk.LEFT)
        self.question_label.pack(pady=15)
        
        # Button frame
        self.button_frame = tk.Frame(self.root, bg="lightblue")
        self.button_frame.pack(pady=15)
        
        self.option_buttons = []
        
        # Submit button
        submit_btn = tk.Button(self.root, text="Submit Answer", font=("Arial", 12),
                              command=self.check_answer, bg="green", fg="white", width=20)
        submit_btn.pack(pady=10)
        
        # Restart button (hidden initially)
        self.restart_btn = tk.Button(self.root, text="Restart Game", font=("Arial", 12),
                                     command=self.restart_game, bg="orange", fg="white", width=20)
        
        self.load_question()
        
    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=f"Question {self.current_question + 1}: {question['question']}")
            
            # Clear previous buttons
            for btn in self.option_buttons:
                btn.destroy()
            self.option_buttons.clear()
            
            # Create new buttons for choices
            self.selected_answer.set("")
            for choice in question['choices']:
                btn = tk.Radiobutton(self.button_frame, text=choice, variable=self.selected_answer,
                                    value=choice, font=("Arial", 11), bg="Royal Blue", fg="white",
                                    activebackground="Royal Blue", padx=15)
                btn.pack(anchor=tk.W, padx=20)
                self.option_buttons.append(btn)
        
    def check_answer(self):
        if self.selected_answer.get() == "":
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        question = self.questions[self.current_question]
        if self.selected_answer.get() == question['answer']:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Wrong!", f"Wrong! The correct answer is: {question['answer']}")
        
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
        
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.end_game()
    
    def end_game(self):
        # Hide question and buttons
        self.question_label.config(text="")
        for btn in self.option_buttons:
            btn.destroy()
        self.option_buttons.clear()
        
        # Show result
        percentage = (self.score / len(self.questions)) * 100
        result_text = f"Game Over!\n\nFinal Score: {self.score}/{len(self.questions)}\nPercentage: {percentage:.1f}%"
        
        if self.score == len(self.questions):
            result_text += "\n\n✓ You passed all questions!"
            messagebox.showinfo("Game Over", result_text)
        else:
            result_text += "\n\n✗ You failed some questions."
            messagebox.showerror("Game Over", result_text)
        
        # Show restart button
        self.restart_btn.pack(pady=10)
    
    def restart_game(self):
        self.score = 0
        self.current_question = 0
        self.selected_answer.set("")
        self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
        self.restart_btn.pack_forget()
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    game = TriviaGameGUI(root)
    root.mainloop()