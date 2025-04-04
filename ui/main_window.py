import tkinter as tk
from tkinter import messagebox, scrolledtext
from ui.styles import Styles
from api.recycling_api import RecyclingAPI
from data.user_data import UserData
import random

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.user_data = UserData()
        self.api = RecyclingAPI()  # Assumes Gemini API key is set in recycling_api.py
        Styles.configure_root(root)
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Label(self.root, text="AI Recycling Guide", font=Styles.FONT_BOLD, fg=Styles.TEXT_COLOR, bg=Styles.BACKGROUND_COLOR)
        header.pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(self.root, bg=Styles.BACKGROUND_COLOR)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Item:", font=Styles.FONT, bg=Styles.BACKGROUND_COLOR).grid(row=0, column=0, padx=5)
        self.item_entry = tk.Entry(input_frame, width=30, font=Styles.FONT)
        self.item_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Custom Instruction (optional):", font=Styles.FONT, bg=Styles.BACKGROUND_COLOR).grid(row=1, column=0, padx=5)
        self.instruction_entry = tk.Entry(input_frame, width=30, font=Styles.FONT)
        self.instruction_entry.grid(row=1, column=1, padx=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg=Styles.BACKGROUND_COLOR)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Get Info", command=self.get_info, bg=Styles.BUTTON_COLOR, fg="white", font=Styles.FONT).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Save Instruction", command=self.save_instruction, bg=Styles.BUTTON_COLOR, fg="white", font=Styles.FONT).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Show History", command=self.show_history, bg=Styles.BUTTON_COLOR, fg="white", font=Styles.FONT).grid(row=0, column=2, padx=5)

        # Output Area
        self.output_text = scrolledtext.ScrolledText(self.root, width=60, height=10, font=Styles.FONT, wrap=tk.WORD)
        self.output_text.pack(pady=10)

        # Tips Section
        self.tips = [
            "Rinse containers before recycling to avoid contamination.",
            "Check local rules—some areas don’t accept plastic bags in curbside bins.",
            "Compost food scraps to reduce landfill waste."
        ]
        self.tip_label = tk.Label(self.root, text="Tip: " + random.choice(self.tips), font=Styles.FONT, bg=Styles.BACKGROUND_COLOR, fg=Styles.TEXT_COLOR)
        self.tip_label.pack(pady=5)

        # Registration Number
        self.reg_no_label = tk.Label(self.root, text="Registration No: 12306100 \n Name: Sandeep Kumar", font=Styles.FONT, bg=Styles.BACKGROUND_COLOR, fg=Styles.TEXT_COLOR)
        self.reg_no_label.pack(pady=5)

    def get_info(self):
        item = self.item_entry.get().strip()
        custom_instruction = self.instruction_entry.get().strip()  # Optional hint
        
        if not item:
            messagebox.showwarning("Input Error", "Please enter an item.")
            return
        
        # Check user-saved data first
        saved_instruction = self.user_data.get_instruction(item)
        if saved_instruction:
            result = f"User Instruction: {saved_instruction}"
        else:
            # Use custom instruction as a hint for Gemini if provided
            if custom_instruction:
                api_result = self.api.get_recycling_info(item + f" (user hint: {custom_instruction})")
            else:
                api_result = self.api.get_recycling_info(item)
            result = api_result
        
        # Display result
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)
        self.update_tip()

    def save_instruction(self):
        item = self.item_entry.get().strip()
        instruction = self.instruction_entry.get().strip()
        if not item or not instruction:
            messagebox.showwarning("Input Error", "Please enter both item and instruction.")
            return
        
        self.user_data.add_instruction(item, instruction)
        messagebox.showinfo("Success", f"Saved instruction for '{item}'.")
        self.item_entry.delete(0, tk.END)
        self.instruction_entry.delete(0, tk.END)
        self.update_tip()

    def show_history(self):
        history = self.user_data.get_history()
        self.output_text.delete(1.0, tk.END)
        if history:
            self.output_text.insert(tk.END, "History:\n" + "\n".join(history))
        else:
            self.output_text.insert(tk.END, "No history yet.")
        self.update_tip()

    def update_tip(self):
        self.tip_label.config(text="Tip: " + random.choice(self.tips))
