# Phrase List Manager - BuildVer: 1.1.6_RV1.0 - (By: EyeFly and ChatGTP)

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import ast
import re
import random
import unicodedata
import time
import os

class Phrase_List_Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Rando-Promto - Phrase List Manager - BV1.1.6_RV1.0")
        self.root.configure(bg="#0b0f19")  # Set background color to #333333
        
        self.current_file_path = None
        
        icon_path = "contents/media/icon_2.png"
        icon_image = PhotoImage(file=icon_path)
        # Set the window icon
        root.iconphoto(True, icon_image)
        
        # Calculate the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Calculate the dimensions of the Tk root window
        window_width = 579  # Adjust based on your window size
        window_height = 714  # Adjust based on your window size
        
        # Calculate the x and y positions for the Tk root window
        x_position = int(screen_width / 2 - window_width / 2)
        y_position = int(screen_height / 2 - window_height / 2)
        
        # Set the window to open in the middle of the screen
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        # Input field for new items (multiline)
        self.placeholder_text = "...Enter phrase(s) here...(Vertical Lists or Separated By Commas)..."
        
        self.placeholder_filter = "...Enter filter keyword(s) here..."

        self.loaded_items = []  # Temporary copy of loaded items
        
        self.filtered_items = []  # Filtered items based on keyword search
        
        self.label0 = tk.Label(root, text="Enter your listed phrases or words in either a vertical list, or a horizontal list, seperated by commas.", font=("Helvetica", 8), bg="#0b0f19", fg="white")
        self.label0.pack(pady=(3, 0))
        
        self.label1 = tk.Label(root, text="(Example: car, a blue boat, a rusty truck, OR stacked in a list like these instructions you're reading.", font=("Helvetica", 8), bg="#0b0f19", fg="white")
        self.label1.pack(pady=0)
        
        self.label2 = tk.Label(root, text="Note: Dashes and Underscores are the ONLY punctuation that will be kept in added phrases. Any", font=("Helvetica", 8), bg="#0b0f19", fg="white")
        self.label2.pack(pady=0)
        
        text = 'others and accent marks will get removed. Make your words like "Ben\'s" to "Bens" or "Ben" first.'

        self.label3 = tk.Label(root, text=text, font=("Helvetica", 8), bg="#0b0f19", fg="white")
        self.label3.pack(pady=0)
        
        # Separator
        separator_below = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
        separator_below.pack(fill=tk.X, padx=5, pady=(4, 0))

        # Create the Listbox widget with a dark background and white text
        self.listbox = tk.Listbox(root, bd=0, width=90, height=20, bg="#1f2937", fg="white", selectmode=tk.MULTIPLE)
        self.listbox.pack(pady=(10, 0), padx=10)
        self.listbox.configure(highlightbackground="grey", highlightcolor="darkgrey")
        
        self.input_frame = tk.Frame(root, bg="#0b0f19")
        self.input_frame.pack(pady=5, padx=10, fill=tk.X)
        
        # Frame to hold the buttons, centered horizontally
        button_frame1 = tk.Frame(self.input_frame, bg="#0b0f19")
        button_frame1.pack(pady=(5, 3))
        
        # Button to add items from input
        self.add_button = tk.Button(button_frame1, text="🡩 Add New Phrase(s) 🡩", command=self.add_items, bg="#424c5b", fg="white", width=19)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.load_selected_button = tk.Button(button_frame1, text="🡫 Edit Selected 🡫", command=self.load_selected_item, bg="#424c5b", fg="white", width=14)
        self.load_selected_button.pack(side=tk.LEFT, padx=5)
        
        self.replace_button = tk.Button(button_frame1, text="🡫 Replace Selected 🡩", command=self.replace_selected_item, bg="#424c5b", fg="white", width=17)
        self.replace_button.pack(side=tk.LEFT, padx=5)
        
        self.remove_button = tk.Button(button_frame1, text="✕ Remove Selected ✕", command=self.remove_selected_items, bg="#424c5b", fg="white", width=18)
        self.remove_button.pack(side=tk.LEFT, padx=(5, 5), pady=1)

        # Create the Text widget
        self.input_entry = tk.Text(self.input_frame, width=68, height=10, bg="#1f2937", fg="white", insertbackground="white")
        self.input_entry.pack(padx=(0, 0), pady=(6, 5))

        # Add placeholder functionality
        self.input_entry.insert("1.0", self.placeholder_text)
        self.input_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.input_entry.bind("<FocusOut>", self.on_entry_focus_out)
        
        # Create a frame for filter input and buttons with dark background
        self.filter_frame = tk.Frame(root, bg="#0b0f19")
        self.filter_frame.pack(side=tk.TOP, pady=(0, 5), padx=10, fill=tk.X)
        
        # Input field for filter keyword
        self.filter_entry = tk.Text(self.filter_frame, width=44, height=1, bg="#1f2937", fg="white", insertbackground="white")
        self.filter_entry.grid(row=0, column=0, padx=5, pady=0)
        
        self.filter_entry.insert("1.0", self.placeholder_filter)
        self.filter_entry.bind("<FocusIn>", self.on_filter_focus_in)
        self.filter_entry.bind("<FocusOut>", self.on_filter_focus_out)
        
        # Buttons for filter actions
        self.filter_button = tk.Button(self.filter_frame, text="Filter For Keyword", command=self.apply_filter, bg="#424c5b", fg="white")
        self.filter_button.grid(row=0, column=1, padx=5, pady=0, sticky="w")
        
        self.clear_filter_button = tk.Button(self.filter_frame, text="Clear Filter", command=self.clear_filter, bg="#424c5b", fg="white")
        self.clear_filter_button.grid(row=0, column=2, padx=5, pady=0, sticky="w")
        
        # Create a frame for action buttons with dark background
        self.button_frame = tk.Frame(root, bg="#0b0f19")
        self.button_frame.pack(pady=5, padx=10, fill=tk.X)
        
        # Action buttons with dark background and white text
        self.load_button = tk.Button(self.button_frame, text="Load A File", command=self.load_file, bg="#008080", fg="white")
        self.load_button.pack(side=tk.LEFT, padx=(2, 5), pady=0)
        
        self.save_button = tk.Button(self.button_frame, text="Save To File", command=self.save_file, bg="#D32F2F", fg="white")
        self.save_button.pack(side=tk.LEFT, padx=(5, 5), pady=0)
        
        self.reload_button = tk.Button(self.button_frame, text="Reload File", command=self.reload_file, bg="#424c5b", fg="white")
        self.reload_button.pack(side=tk.LEFT, padx=(5, 5), pady=0)
        
        self.find_duplicates_button = tk.Button(self.button_frame, text="Find Duplicates", command=self.find_duplicates, bg="#424c5b", fg="white")
        self.find_duplicates_button.pack(side=tk.LEFT, padx=(5, 5), pady=0)
        
        self.remove_duplicates_button = tk.Button(self.button_frame, text="Remove Duplicates", command=self.remove_duplicates, bg="#424c5b", fg="white")
        self.remove_duplicates_button.pack(side=tk.LEFT, padx=(5, 5), pady=0)
        
        self.shuffle_button = tk.Button(self.button_frame, text="Shuffle The List", command=self.shuffle_items, bg="#424c5b", fg="white")
        self.shuffle_button.pack(side=tk.LEFT, padx=(5, 0), pady=0)
        
        # Create a context menu
        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(label="Paste", command=self.paste_from_clipboard)

        # Bind right-click to show the context menu
        self.input_entry.bind("<Button-3>", self.show_context_menu)
        self.filter_entry.bind("<Button-3>", self.show_context_menu)
        
    print("Launching Phrase List Manager, Now 🚀 . . . ")
        
    time.sleep(0.2)

    def load_file(self):
        # Open a file dialog to select the file
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                content = file.read()

                # Find the first list in the file
                parsed = ast.parse(content)
                list_found = None

                for node in ast.walk(parsed):
                    if isinstance(node, ast.Assign):
                        if isinstance(node.value, ast.List):
                            list_found = node.value
                            break

                if list_found is None:
                    raise ValueError("No list found in the file.")

                # Extract elements from the list, removing numbers before hyphens
                self.loaded_items = [re.sub(r'^\d+\s*-\s*', '', ast.literal_eval(element)) for element in list_found.elts]

                 # Set the current file path
                self.current_file_path = file_path
                
                # Extract and store the file name without the extension
                base_name = os.path.basename(file_path)
                self.current_file_name = os.path.splitext(base_name)[0]
                
                # Clear the listbox and insert the loaded items
                self.refresh_listbox()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def add_items(self):
        # Get input from entry field
        input_text = self.input_entry.get("1.0", tk.END).strip()

        if not input_text:
            return

        try:
            # Function to remove punctuation and accents, except dashes
            def clean_text(text):
                # Remove accents
                text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
                # Remove punctuation except dashes and underscores
                return re.sub(r'[^\w\s-]', '', text)

            # Split input by lines and commas to handle different formats
            items = re.split(r'[,\n]', input_text)
            new_items = [clean_text(item.strip().strip("'\"")) for item in items if item.strip()]

            # Add new items to the loaded items and listbox
            for item in new_items:
                if item:
                    self.loaded_items.append(item)

            # Clear the input field after adding items
            self.input_entry.delete("1.0", tk.END)
            self.refresh_listbox()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add items: {e}")
            
    def load_selected_item(self):
        # Get the selected item from the listbox
        selected_indices = self.listbox.curselection()

        if not selected_indices:
            messagebox.showerror("Error", "No item selected.")
            return

        # Get the first selected item
        selected_item = self.listbox.get(selected_indices[0])

        # Remove the index number from the beginning of the selected item
        item_text = re.sub(r'^\d+\s*-\s*', '', selected_item)

        # Insert the selected item text into the input field
        self.input_entry.delete("1.0", tk.END)
        self.input_entry.insert(tk.END, item_text)

    def replace_selected_item(self):
        # Get the input text
        input_text = self.input_entry.get("1.0", tk.END).strip()
    
        if not input_text:
            messagebox.showerror("Error", "Input field is empty.")
            return
    
        # Get the selected item index from the listbox
        selected_indices = self.listbox.curselection()
    
        if not selected_indices:
            messagebox.showerror("Error", "No item selected.")
            return
    
        # Clean the input text
        def clean_text(text):
            # Remove accents
            text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
            # Remove punctuation except dashes
            return re.sub(r'[^\w\s-]', '', text)
    
        clean_input_text = clean_text(input_text)
    
        # Replace the selected item with the new text
        if self.filtered_items:
            # If a filter is applied, replace the item in the filtered list and update loaded_items
            for index in selected_indices:
                if 0 <= index < len(self.filtered_items):
                    original_item = self.filtered_items[index]
                    original_index = self.loaded_items.index(original_item)
                    self.loaded_items[original_index] = clean_input_text
                    self.filtered_items[index] = clean_input_text
        else:
            # Otherwise, directly replace the item in loaded_items
            for index in selected_indices:
                if 0 <= index < len(self.loaded_items):
                    self.loaded_items[index] = clean_input_text
    
        # Refresh the listbox to reflect the change
        self.refresh_listbox()
        self.input_entry.delete("1.0", tk.END)

    def save_file(self):
        # Open a file dialog to select the save location
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if not file_path:
            return

        try:
            with open(file_path, "w") as file:
                file.write(f"{self.current_file_name} = [\n")
                for item in self.loaded_items:
                    file.write(f"    '{item}',\n")
                file.write("]\n")

                print("Success!...", f"File saved to: {file_path}")

        except Exception as e:
            messagebox.showerror("Error - Failed to save file:", f"You MUST load a file first or file will be empty: {e}")

    def remove_selected_items(self):
        # Get selected indices from listbox
        selected_indices = self.listbox.curselection()

        # Remove items from loaded_items based on selected indices
        if self.filtered_items:
            # If a filter is applied, remove items from filtered list and update loaded_items
            for index in sorted(selected_indices, reverse=True):
                if 0 <= index < len(self.filtered_items):
                    item_to_remove = self.filtered_items[index]
                    self.loaded_items.remove(item_to_remove)
                    self.filtered_items.remove(item_to_remove)
        else:
            # Otherwise, directly remove items from loaded_items
            for index in sorted(selected_indices, reverse=True):
                if 0 <= index < len(self.loaded_items):
                    del self.loaded_items[index]

        # Refresh the listbox after removal
        self.refresh_listbox()

    def shuffle_items(self):
        # Define the number of shuffles
        num_shuffles = 25
        
        for _ in range(num_shuffles):
            # Shuffle the items
            random.shuffle(self.loaded_items)
            
            self.refresh_listbox()
            
            # Update the GUI
            self.root.update()
            
            # Delay to allow seeing the shuffle effect
            time.sleep(0.005)

    def find_duplicates(self):
        # Create a set to track seen items and another list for duplicate items
        seen_items = set()
        duplicate_items = []

        for item in self.loaded_items:
            if item in seen_items:
                duplicate_items.append(item)
            seen_items.add(item)

        # Check if duplicates were found
        if duplicate_items:
            # Display only duplicates in the listbox
            self.listbox.delete(0, tk.END)
            for index, item in enumerate(duplicate_items, start=1):
                self.listbox.insert(tk.END, f"{index}- {item}")
        else:
            # If no duplicates found, refresh the listbox with all items
            self.refresh_listbox()

    def remove_duplicates(self):
        # Create a set to track seen items and a list for items without duplicates
        seen_items = set()
        unique_items = []

        for item in self.loaded_items:
            if item not in seen_items:
                unique_items.append(item)
                seen_items.add(item)

        # Update loaded_items with unique items and refresh listbox
        self.loaded_items = unique_items
        self.refresh_listbox()

    def apply_filter(self):
        # Get the filter keyword from the Text widget
        keyword = self.filter_entry.get("1.0", "end-1c").strip().lower()

        if not keyword:
            return

        # Filter items that contain the keyword (case insensitive)
        self.filtered_items = [item for item in self.loaded_items if keyword in item.lower()]

        # Display filtered items in the listbox
        self.display_filtered_items()

    def clear_filter(self):
        # Clear the filter and refresh the listbox with all items
        self.filtered_items = []
        self.refresh_listbox()
        self.filter_entry.delete("1.0", "end")

    def display_filtered_items(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Insert filtered items into the listbox
        for index, item in enumerate(self.filtered_items, start=1):
            self.listbox.insert(tk.END, f"{index}- {item}")

    def refresh_listbox(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Determine which items to display based on filter status
        items_to_display = self.filtered_items if self.filtered_items else self.loaded_items

        # Insert items into the listbox
        for index, item in enumerate(items_to_display, start=1):
            self.listbox.insert(tk.END, f"{index}- {item}")
            
    def on_entry_focus_in(self, event):
        if self.input_entry.get("1.0", "end-1c") == self.placeholder_text:
            self.input_entry.delete("1.0", "end-1c")
            self.input_entry.config(fg="white")

    def on_entry_focus_out(self, event):
        if not self.input_entry.get("1.0", "end-1c"):
            self.input_entry.insert("1.0", self.placeholder_text)
            self.input_entry.config(fg="grey")
            
    def on_filter_focus_in(self, event):
        if self.filter_entry.get("1.0", "end-1c") == self.placeholder_filter:
            self.filter_entry.delete("1.0", "end-1c")
            self.filter_entry.config(fg="white")

    def on_filter_focus_out(self, event):
        if not self.filter_entry.get("1.0", "end-1c"):
            self.filter_entry.insert("1.0", self.placeholder_filter)
            self.filter_entry.config(fg="grey")
            
    def show_context_menu(self, event):
        # Determine which widget triggered the event
        widget = event.widget
        if widget == self.input_entry:
            self.context_menu.post(event.x_root, event.y_root)
        elif widget == self.filter_entry:
            self.context_menu.post(event.x_root, event.y_root)

    def paste_from_clipboard(self):
        clipboard_content = self.root.clipboard_get()
        # Determine which widget has focus and paste into it
        widget = self.root.focus_get()
        if widget == self.input_entry:
            current_position = self.input_entry.index(tk.INSERT)
            self.input_entry.insert(current_position, clipboard_content)
        elif widget == self.filter_entry:
            current_position = self.filter_entry.index(tk.INSERT)
            self.filter_entry.insert(current_position, clipboard_content)
            
    def reload_file(self):
        if not self.current_file_path:
            messagebox.showerror("Error", "No file has been loaded yet.")
            return

        try:
            with open(self.current_file_path, "r") as file:
                content = file.read()

                # Find the first list in the file
                parsed = ast.parse(content)
                list_found = None

                for node in ast.walk(parsed):
                    if isinstance(node, ast.Assign):
                        if isinstance(node.value, ast.List):
                            list_found = node.value
                            break

                if list_found is None:
                    raise ValueError("No list found in the file.")

                # Extract elements from the list, removing numbers before hyphens
                self.loaded_items = [re.sub(r'^\d+\s*-\s*', '', ast.literal_eval(element)) for element in list_found.elts]

                # Clear the listbox and insert the reloaded items
                self.refresh_listbox()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to reload file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Phrase_List_Manager(root)
    root.mainloop()