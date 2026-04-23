import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
import sys

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium Age Calculator")
        self.root.geometry("450x550")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.header_label = tk.Label(
            root, text="Age Calculator", font=("Helvetica", 24, "bold"),
            bg="#1a1a2e", fg="#e94560", pady=30
        )
        self.header_label.pack()

        self.input_frame = tk.Frame(root, bg="#1a1a2e")
        self.input_frame.pack(pady=10)

        lbl_config = {"bg": "#1a1a2e", "fg": "#ffffff", "font": ("Helvetica", 12)}
        entry_config = {
            "font": ("Helvetica", 14), 
            "bg": "#16213e", 
            "fg": "#ffffff", 
            "insertbackground": "white",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#533483"
        }

        tk.Label(self.input_frame, text="Day (DD)", **lbl_config).grid(row=0, column=0, padx=10, pady=5)
        self.day_entry = tk.Entry(self.input_frame, width=10, justify='center', **entry_config)
        self.day_entry.grid(row=1, column=0, padx=10, pady=5)

        tk.Label(self.input_frame, text="Month (MM)", **lbl_config).grid(row=0, column=1, padx=10, pady=5)
        self.month_entry = tk.Entry(self.input_frame, width=10, justify='center', **entry_config)
        self.month_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.input_frame, text="Year (YYYY)", **lbl_config).grid(row=0, column=2, padx=10, pady=5)
        self.year_entry = tk.Entry(self.input_frame, width=12, justify='center', **entry_config)
        self.year_entry.grid(row=1, column=2, padx=10, pady=5)

        self.calc_button = tk.Button(
            root, text="Calculate Age", command=self.calculate_age,
            font=("Helvetica", 14, "bold"), bg="#e94560", fg="#ffffff",
            activebackground="#c62a48", activeforeground="#ffffff",
            bd=0, padx=40, pady=10, cursor="hand2"
        )
        self.calc_button.pack(pady=40)

        self.result_container = tk.Frame(root, bg="#1a1a2e")
        self.result_container.pack(fill="x", padx=40)

        self.year_result = tk.Label(
            self.result_container, text="", font=("Helvetica", 18),
            bg="#1a1a2e", fg="#00d2ff"
        )
        self.year_result.pack()

        self.day_result = tk.Label(
            self.result_container, text="", font=("Helvetica", 14),
            bg="#1a1a2e", fg="#95a5a6"
        )
        self.day_result.pack(pady=5)

    def calculate_age(self):
        try:
            day_str = self.day_entry.get().strip()
            month_str = self.month_entry.get().strip()
            year_str = self.year_entry.get().strip()

            if not (day_str and month_str and year_str):
                raise ValueError("All fields are required!")

            day = int(day_str)
            month = int(month_str)
            year = int(year_str)

            birth_date = date(year, month, day)
            today = date.today()

            if birth_date > today:
                raise ValueError("Date of birth cannot be in the future!")

            years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            try:
                last_birthday = birth_date.replace(year=today.year)
            except ValueError:
                last_birthday = birth_date.replace(year=today.year, day=28)
                
            if last_birthday > today:
                try:
                    last_birthday = birth_date.replace(year=today.year - 1)
                except ValueError:
                    last_birthday = birth_date.replace(year=today.year - 1, day=28)

            days_remaining = (today - last_birthday).days

            self.year_result.config(text=f"{years} Years Old")
            self.day_result.config(text=f"and {days_remaining} days")
            
        except ValueError as e:
            error_msg = str(e)
            if "invalid literal" in error_msg:
                messagebox.showerror("Input Error", "Please enter valid numeric values for day, month, and year.")
            elif "month must be" in error_msg or "day is out of range" in error_msg:
                messagebox.showerror("Invalid Date", "The date you entered does not exist. Please check your input.")
            else:
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            messagebox.showerror("Calculation Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()
