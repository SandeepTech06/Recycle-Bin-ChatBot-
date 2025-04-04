# UI styles and configurations
# ui/styles.py
import tkinter as tk

class Styles:
    BACKGROUND_COLOR = "#E8F5E9"  # Light green
    BUTTON_COLOR = "#4CAF50"      # Green
    TEXT_COLOR = "#212121"        # Dark gray
    FONT = ("Helvetica", 12)
    FONT_BOLD = ("Helvetica", 12, "bold")

    @staticmethod
    def configure_root(root):
        root.configure(bg=Styles.BACKGROUND_COLOR)
        root.geometry("600x500")
        root.title("AI Recycling Guide")
        # Optional: root.iconbitmap("assets/icon.ico")