# Rando Prompto - BuildVer: 1.5.2_RV1.0 - (By: EyeFly and ChatGTP)

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import Scrollbar
import random
import pyperclip
import time
import os
import sys
import re

from contents.lib.people import people
from contents.lib.animals import animals
from contents.lib.emotions import emotions
from contents.lib.eyes import eyes
from contents.lib.hair import hair
from contents.lib.skin import skin
from contents.lib.genitals import genitals
from contents.lib.sex import sex
from contents.lib.clothing import clothing
from contents.lib.accessories import accessories
from contents.lib.objects import objects
from contents.lib.actions import actions
from contents.lib.places import places
from contents.lib.time_periods import time_periods
from contents.lib.times_of_day import times_of_day
from contents.lib.professions import professions
from contents.lib.mystical_elements import mystical_elements
from contents.lib.weather import weather
from contents.lib.vehicles import vehicles
from contents.lib.food_drinks import food_drinks
from contents.lib.fantasy_creatures import fantasy_creatures
from contents.lib.nature_elements import nature_elements
from contents.lib.technology_tools import technology_tools
from contents.lib.hobbies_activities import hobbies_activities
from contents.lib.social_interactions import social_interactions
from contents.lib.legendary_places_realms import legendary_places_realms
from contents.lib.historical_events_moments import historical_events_moments
from contents.lib.body_language_gestures import body_language_gestures
from contents.lib.art_styles import art_styles
from contents.lib.wildcards import wildcards
from contents.lib.custom_1 import custom_1
from contents.lib.custom_2 import custom_2
from contents.lib.custom_3 import custom_3
from contents.lib.button_names import button_names

# Dictionary to map variable names to display names
var_to_display = {var_name: display_name for var_name, display_name in button_names}

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2 + 200)
    
    window.geometry(f"{width}x{height}+{x}+{y}")

# Initialize the main application window
app = tk.Tk()
app.title("Rando-Prompto 🪄 - Random Prompt Generator - BV1.5.2_RV1.0")
app.configure(bg='#0b0f19')  # Set background color of the main window

window_width = 560
window_height = 600
center_window(app, window_width, window_height)

# Load the image from file
icon_path = "contents/media/icon_1.png"
icon_image = PhotoImage(file=icon_path)
emoji_image = PhotoImage(file="contents/media/icon_3.png")

# Set the window icon
app.iconphoto(True, icon_image)

var_people = tk.BooleanVar()
var_eyes = tk.BooleanVar()
var_hair = tk.BooleanVar()
var_skin = tk.BooleanVar()
var_genitals = tk.BooleanVar()
var_sex = tk.BooleanVar()
var_objects = tk.BooleanVar()
var_animals = tk.BooleanVar()
var_emotions = tk.BooleanVar()
var_actions = tk.BooleanVar()
var_places = tk.BooleanVar()
var_time_periods = tk.BooleanVar()
var_times_of_day = tk.BooleanVar()
var_clothing = tk.BooleanVar()
var_accessories = tk.BooleanVar()
var_professions = tk.BooleanVar()
var_mystical = tk.BooleanVar()
var_weather = tk.BooleanVar()
var_vehicles = tk.BooleanVar()
var_food_drinks = tk.BooleanVar()
var_fantasy_creatures = tk.BooleanVar()
var_nature_elements = tk.BooleanVar()
var_technology_tools = tk.BooleanVar()
var_hobbies_activities = tk.BooleanVar()
var_social_interactions = tk.BooleanVar()
var_legendary_places_realms = tk.BooleanVar()
var_historical_events_moments = tk.BooleanVar()
var_body_language_gestures = tk.BooleanVar()
var_art_styles = tk.BooleanVar()
var_wildcards = tk.BooleanVar()
var_custom_1 = tk.BooleanVar()
var_custom_2 = tk.BooleanVar()
var_custom_3 = tk.BooleanVar()

# Add an entry widget for user input at the beginning of the prompt
beginning_prompt_label = tk.Label(app, text="(Optional) Past/Type the beginning of the prompt/Model trigger words:", bg='#0b0f19', fg='white')
beginning_prompt_label.pack(pady=(5, 0))

beginning_prompt_entry = tk.Entry(app, bg='#1f2937', fg='white', insertbackground='white')
beginning_prompt_entry.pack(fill=tk.X, padx=10, pady=(2, 10), expand=True)

# Add an entry widget for user input words to exclude from the prompt choices
excluseed_words_label = tk.Label(app, text="(Optional) Words to exclude from the prompt, separated by commas:", bg='#0b0f19', fg='white')
excluseed_words_label.pack(pady=(0, 0))

excluseed_words_entry = tk.Entry(app, bg='#1f2937', fg='white', insertbackground='white')
excluseed_words_entry.pack(fill=tk.X, padx=10, pady=(2, 10), expand=True)

# Add a separator line above the checkboxes
separator_above = tk.Frame(app, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
separator_above.pack(fill=tk.X, padx=5, pady=(0, 5))

# Variable to track the checkbutton checked order
checked_order = []
# Variable to track the toggle state
toggle_var = tk.IntVar(value=0)

# Function to generate prompt
def generate_prompt():
    components = []
    
    # Get the excluded words from the entry widget
    excluded_words_input = excluseed_words_entry.get()
    if excluded_words_input:
        excluded_words = excluded_words_input.split(',')
        excluded_words = [word.strip().lower() for word in excluded_words]
    else:
        excluded_words = []
    
    beginning_prompt = beginning_prompt_entry.get()
    if beginning_prompt:
        components.append(beginning_prompt)
    
    def get_filtered_choice(lst):
        """Helper function to get a random choice from a list, excluding choices with certain words."""
        if excluded_words:
            filtered_lst = [item for item in lst if not any(ex_word in item.lower() for ex_word in excluded_words)]
            if filtered_lst:
                return random.choice(filtered_lst)
            return None
        else:
            return random.choice(lst)

    if toggle_var.get() == 0:
        # Use default order
        var_lists = [
            (var_people.get(), people),
            (var_animals.get(), animals),
            (var_fantasy_creatures.get(), fantasy_creatures),
            (var_skin.get(), skin),
            (var_genitals.get(), genitals),
            (var_sex.get(), sex),
            (var_emotions.get(), emotions),
            (var_eyes.get(), eyes),
            (var_hair.get(), hair),
            (var_clothing.get(), clothing),
            (var_accessories.get(), accessories),
            (var_objects.get(), objects),
            (var_actions.get(), actions),
            (var_places.get(), places),
            (var_time_periods.get(), time_periods),
            (var_times_of_day.get(), times_of_day),
            (var_mystical.get(), mystical_elements),
            (var_professions.get(), professions),
            (var_weather.get(), weather),
            (var_vehicles.get(), vehicles),
            (var_food_drinks.get(), food_drinks),
            (var_nature_elements.get(), nature_elements),
            (var_technology_tools.get(), technology_tools),
            (var_hobbies_activities.get(), hobbies_activities),
            (var_social_interactions.get(), social_interactions),
            (var_legendary_places_realms.get(), legendary_places_realms),
            (var_historical_events_moments.get(), historical_events_moments),
            (var_body_language_gestures.get(), body_language_gestures),
            (var_art_styles.get(), art_styles),
            (var_wildcards.get(), wildcards),
            (var_custom_1.get(), custom_1),
            (var_custom_2.get(), custom_2),
            (var_custom_3.get(), custom_3)
        ]
        
        for var, lst in var_lists:
            if var:
                choice = get_filtered_choice(lst)
                if choice:
                    components.append(choice)
    
    elif toggle_var.get() == 1:
        # Use checked_order
        for order in checked_order:
            order_num = int(order)
            if order_num == 1 and var_people.get():
                choice = get_filtered_choice(people)
            elif order_num == 2 and var_animals.get():
                choice = get_filtered_choice(animals)
            elif order_num == 3 and var_fantasy_creatures.get():
                choice = get_filtered_choice(fantasy_creatures)
            elif order_num == 4 and var_skin.get():
                choice = get_filtered_choice(skin)
            elif order_num == 5 and var_genitals.get():
                choice = get_filtered_choice(genitals)
            elif order_num == 6 and var_sex.get():
                choice = get_filtered_choice(sex)
            elif order_num == 7 and var_emotions.get():
                choice = get_filtered_choice(emotions)
            elif order_num == 8 and var_eyes.get():
                choice = get_filtered_choice(eyes)
            elif order_num == 9 and var_hair.get():
                choice = get_filtered_choice(hair)
            elif order_num == 10 and var_clothing.get():
                choice = get_filtered_choice(clothing)
            elif order_num == 11 and var_accessories.get():
                choice = get_filtered_choice(accessories)
            elif order_num == 12 and var_objects.get():
                choice = get_filtered_choice(objects)
            elif order_num == 13 and var_actions.get():
                choice = get_filtered_choice(actions)
            elif order_num == 14 and var_places.get():
                choice = get_filtered_choice(places)
            elif order_num == 15 and var_time_periods.get():
                choice = get_filtered_choice(time_periods)
            elif order_num == 16 and var_times_of_day.get():
                choice = get_filtered_choice(times_of_day)
            elif order_num == 17 and var_mystical.get():
                choice = get_filtered_choice(mystical_elements)
            elif order_num == 18 and var_professions.get():
                choice = get_filtered_choice(professions)
            elif order_num == 19 and var_weather.get():
                choice = get_filtered_choice(weather)
            elif order_num == 20 and var_vehicles.get():
                choice = get_filtered_choice(vehicles)
            elif order_num == 21 and var_food_drinks.get():
                choice = get_filtered_choice(food_drinks)
            elif order_num == 22 and var_nature_elements.get():
                choice = get_filtered_choice(nature_elements)
            elif order_num == 23 and var_technology_tools.get():
                choice = get_filtered_choice(technology_tools)
            elif order_num == 24 and var_hobbies_activities.get():
                choice = get_filtered_choice(hobbies_activities)
            elif order_num == 25 and var_social_interactions.get():
                choice = get_filtered_choice(social_interactions)
            elif order_num == 26 and var_legendary_places_realms.get():
                choice = get_filtered_choice(legendary_places_realms)
            elif order_num == 27 and var_historical_events_moments.get():
                choice = get_filtered_choice(historical_events_moments)
            elif order_num == 28 and var_body_language_gestures.get():
                choice = get_filtered_choice(body_language_gestures)
            elif order_num == 29 and var_art_styles.get():
                choice = get_filtered_choice(art_styles)
            elif order_num == 30 and var_wildcards.get():
                choice = get_filtered_choice(wildcards)
            elif order_num == 31 and var_custom_1.get():
                choice = get_filtered_choice(custom_1)
            elif order_num == 32 and var_custom_2.get():
                choice = get_filtered_choice(custom_2)
            elif order_num == 33 and var_custom_3.get():
                choice = get_filtered_choice(custom_3)
            
            if choice:
                components.append(choice)
    
    if components:
        prompt = ", ".join(components)
        result_label.config(text=prompt, bg='#1f2937', fg='white')
        add_weights_button.pack(pady=10)
        randomize_button.pack(pady=10)
        copy_button.pack(pady=10)
        save_button.pack(pady=10)
        print("✨ Generated Prompt =", prompt, "✨")
    else:
        # Create a new top-level window
        custom_warning = tk.Toplevel(app)
        custom_warning.title("Alert/Error!")
        
        # Customize the size and appearance of the window
        custom_warning.geometry("390x60")
        custom_warning.configure(bg='#0b0f19')
        
        # Add a label with the warning message
        label = tk.Label(custom_warning, text="⚠️ Select At Least One Category To Begin! ⚠️", bg='#0b0f19', fg='yellow', font=("Helvetica", 12, "bold"))
        label.pack(pady=20)
        
        # Center the window
        custom_warning.update_idletasks()
        width = custom_warning.winfo_width()
        height = custom_warning.winfo_height()
        x = (custom_warning.winfo_screenwidth() // 2) - (width // 2)
        y = (custom_warning.winfo_screenheight() // 2) - (height // 2)
        custom_warning.geometry(f'{width}x{height}+{x}+{y}')
        
        # Close the window after 1500 milliseconds
        custom_warning.after(1500, custom_warning.destroy)
    
    app.update_idletasks()
    app.geometry(f"{app.winfo_width()}x{app.winfo_reqheight()}")

# Function to copy prompt to clipboard
def copy_to_clipboard():
    prompt = result_label.cget("text")
    if prompt:
        pyperclip.copy(prompt)
        # Get current window position
        x = app.winfo_x() + (app.winfo_width() // 2) - 100  # Calculate x position for popup
        y = app.winfo_y() + (app.winfo_height() // 2) - 50  # Calculate y position for popup
        
        # Create popup window
        info_popup = tk.Toplevel()
        info_popup.title("Info")
        info_popup.geometry("200x60")
        info_popup.configure(bg='#0b0f19')  # Set popup background color
        info_popup.geometry(f"+{x}+{y}")  # Set position relative to main window
        tk.Label(info_popup, text="Prompt Copied To Clipboard!", bg='#0b0f19', fg='white').pack(pady=20)  # Set label colors
        # print("Prompt Copied To Clipboard =", prompt)
        # Schedule popup to destroy after 1000 ms (1 second)
        info_popup.after(1500, info_popup.destroy)
    else:
        messagebox.showwarning("Warning", "No Prompt To Copy!")
        
# Function to add random weights to the prompt
def add_weights():
    prompt = result_label.cget("text")
    
    if prompt:
        # Split the prompt into components
        components = prompt.split(", ")
        
        # First, remove all existing weights and brackets
        cleaned_components = []
        for component in components:
            if ':' in component:
                component = component.split(':')[0]  # Remove existing weight
            component = component.replace('(', '').replace(')', '')  # Remove any existing brackets
            cleaned_components.append(component)
        
        # Track the number of weights added
        weights_added = 0
        
        # Process each cleaned component
        for i in range(len(cleaned_components)):
            # Decide on the weight format
            weight_format = random.choice(["(segment)", "(segment:weight)", "((segment))", "(((segment)))", "(segment:weight)"])
            
            # Randomly decide to add a weight to this segment
            if random.random() < 0.15 and weights_added < 3:  # Adjust probability as needed
                if weight_format == "(segment)":
                    cleaned_components[i] = f"({cleaned_components[i]})"
                elif weight_format == "((segment))":
                    cleaned_components[i] = f"(({cleaned_components[i]}))"
                elif weight_format == "(((segment)))":
                    cleaned_components[i] = f"((({cleaned_components[i]})))"
                elif weight_format == "(segment:weight)":
                    weight = round(random.uniform(0.1, 1.6), 2)  # Random weight
                    cleaned_components[i] = f"({cleaned_components[i]}:{weight})"
                
                weights_added += 1  # Increment the count of added weights
            
            # Stop adding weights once 3 segments have been processed
            if weights_added == 3:
                break
        
        # Ensure at least one weight is added if none were added randomly
        if weights_added == 0:
            random_index = random.randint(0, len(cleaned_components) - 1)
            weight_format = random.choice(["(segment)", "(segment:weight)", "((segment))", "(((segment)))", "(segment:weight)"])
            if weight_format == "(segment)":
                cleaned_components[random_index] = f"({cleaned_components[random_index]})"
            elif weight_format == "((segment))":
                cleaned_components[random_index] = f"(({cleaned_components[random_index]}))"
            elif weight_format == "(((segment)))":
                cleaned_components[random_index] = f"((({cleaned_components[random_index]})))"
            elif weight_format == "(segment:weight)":
                weight = round(random.uniform(0.1, 1.6), 2)  # Random weight
                cleaned_components[random_index] = f"({cleaned_components[random_index]}:{weight})"
        
        # Update the prompt
        updated_prompt = ", ".join(cleaned_components)
        result_label.config(text=updated_prompt)
        print("💪 Weighted Prompt =", updated_prompt, "💪")
        
        app.update_idletasks()
        app.geometry(f"{app.winfo_width()}x{app.winfo_reqheight()}")

# Function to randomize prompt output
def randomize_output():
    prompt = result_label.cget("text")
    if prompt:
        components = prompt.split(", ")
        random.shuffle(components)
        randomized_prompt = ", ".join(components)
        result_label.config(text=randomized_prompt)
        print("🌀 Randomized Prompt =", randomized_prompt, "🌀")
        
        app.update_idletasks()
        app.geometry(f"{app.winfo_width()}x{app.winfo_reqheight()}")
        
def save_prompt():
    prompt = result_label.cget("text")
    if prompt:
        base_filename = "saved_prompt"
        file_extension = ".txt"
        counter = 1

        # Determine the initial suggested filename, starting from "saved_prompt_1.txt"
        suggested_filename = f"{base_filename}_{counter}{file_extension}"
        while os.path.exists(suggested_filename):
            counter += 1
            suggested_filename = f"{base_filename}_{counter}{file_extension}"

        # Open a file dialog to ask the user where to save the file
        file_path = filedialog.asksaveasfilename(
            initialfile=suggested_filename,
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            with open(file_path, "w") as file:
                file.write(prompt + "\n")

            # Get current window position
            x = app.winfo_x() + (app.winfo_width() // 2) - 100  # Calculate x position for popup
            y = app.winfo_y() + (app.winfo_height() // 2) - 50  # Calculate y position for popup

            # Create popup window
            info_popup = tk.Toplevel()
            info_popup.title("Save To File")
            info_popup.geometry("200x60")
            info_popup.configure(bg='#0b0f19')  # Set popup background color
            info_popup.geometry(f"+{x}+{y}")  # Set position relative to main window
            tk.Label(info_popup, text=f"Prompt Saved To File!", bg='#0b0f19', fg='white').pack(pady=20)  # Set label colors
            print("📄 Prompt File Saved To:", file_path)
            # Schedule popup to destroy after 1500 ms (1.5 second)
            info_popup.after(1500, info_popup.destroy)
    else:
        messagebox.showwarning("Warning", "No Prompt To Save!")
        
def count_category_items():
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    print("                                                                                     ")
    print(". . . Updating Category Phrase and Word Counts ⏳ . . . ")
    
    final_message_blank0 = ("")
    print(final_message_blank0)
    
    # Function to clean category names for display
    def clean_display_name(category_name):
        var_name = f"var_{category_name.lower().replace(' ', '_')}"
        display_name = next((name for var, name in button_names if var == var_name), category_name)
        return display_name
    
    categories = [
        ("People", people), ("Animals", animals), ("Fantasy Creatures", fantasy_creatures),
        ("Skin", skin), ("Genitals", genitals), ("Sex", sex), ("Emotions", emotions), ("Eyes", eyes), 
        ("Hair", hair), ("Clothing", clothing), ("Accessories", accessories), ("Objects", objects),
        ("Actions", actions), ("Places", places), ("Time Periods", time_periods),
        ("Times of Day", times_of_day), ("Mystical Elements", mystical_elements),
        ("Professions", professions), ("Weather", weather), ("Vehicles", vehicles),
        ("Food/Drinks", food_drinks), ("Nature Elements", nature_elements),
        ("Technology/Tools", technology_tools), ("Hobbies/Activities", hobbies_activities),
        ("Social Interactions", social_interactions), ("Legendary Places/Realms", legendary_places_realms),
        ("Historical Events/Moments", historical_events_moments), ("Body Language/Gestures", body_language_gestures),
        ("Art Styles", art_styles), ("Wildcards", wildcards), ("Custom 1", custom_1), ("Custom 2", custom_2),
        ("Custom 3", custom_3)
    ]
    
    # Calculate the total phrase count and total word count
    total_phrase_count = sum(len(category[1]) for category in categories)
    total_word_count = 0
    
    word_pattern = re.compile(r'\b\w+\b')  # regex pattern to match words
    
    # Calculate total word count across all categories
    for _, category_list in categories:
        for phrase in category_list:
            words = re.findall(word_pattern, phrase)
            total_word_count += len(words)
    
    # Determine number of columns for the grid
    num_columns = 3
    
    # Calculate number of rows needed
    num_rows = (len(categories) + num_columns - 1) // num_columns
    
    # Print categories one at a time with a delay
    for row in range(num_rows):
        for col in range(num_columns):
            index = row + col * num_rows
            if index < len(categories):
                category_name, category_list = categories[index]
                if category_list:  # If the category has a list associated with it
                    count = len(category_list)
                    display_name = clean_display_name(category_name)
                    print(f"* {display_name}: {count}".ljust(35), end="")
                else:  # If the category is the final message
                    display_name = clean_display_name(category_name)
                    print(display_name.ljust(35), end="")
                time.sleep(0.02997)
        print()  # Move to the next row after printing all columns
    
    time.sleep(0.15)  # 150ms delay
    
    final_message0 = ("")
    print(final_message0)     
    
    # Add the almost final message to the categories list
    almost_final_message = (f". . . Counted: {total_phrase_count:,} Total Phrases, with {total_word_count:,} Total Words! . . .")
    print(almost_final_message)
    
    time.sleep(0.25)  # 350ms delay
    
    final_message_blank1 = ("")
    print(final_message_blank1)
    
    final_message2 = (". . . Launching Rando-Prompto, Now 🚀 . . .")
    print(final_message2)

    time.sleep(0.5)  # 500ms delay
    
    final_message_blank2 = ("")
    print(final_message_blank2)
    
    print("➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➝ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➞ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜ ➜")
    
    final_message_blank4 = ("")
    print(final_message_blank4)

    # Update the tkinter window
    app.update_idletasks()
    app.geometry(f"{app.winfo_width()}x{app.winfo_reqheight()}")
        
# Create a label for Categories
categories_label = tk.Label(app, text="Select At Least One Category To Generate A Prompt From:", bg='#0b0f19', fg='white')
categories_label.pack(pady=(1, 0))  # Adjust the padding here

def edit_category(category_name, category_list):

    # Function to remove "and" from category names for saving
    def clean_category_name(category_name):
        return category_name.lower().replace(' ', '_').replace('and_', '')

    def shuffle_items():
        # Define the number of shuffles
        num_shuffles = 25
        
        for _ in range(num_shuffles):
            # Shuffle the items
            random.shuffle(original_category_list)
            
            # Update the listbox or GUI
            update_listbox()
            
            app.update()
            
            # Delay between shuffles
            time.sleep(0.005)

    def add_item():
        new_item = new_item_entry.get().strip()
        if new_item:
            original_category_list.append(new_item)
            update_listbox()
            new_item_entry.delete(0, tk.END)

    def remove_items():
        selected_indices = category_listbox.curselection()
        if selected_indices:
            selected_items = [category_listbox.get(i) for i in selected_indices]
            # Remove selected items from the original list
            for item in selected_items:
                if item in original_category_list:
                    original_category_list.remove(item)
            # Refresh the listbox to show the updated list
            update_listbox()
            # Clear the search filter
            search_entry.delete(0, tk.END)

    def save_changes():
        new_category_list = original_category_list.copy()
        try:
            # Clean the category_name before saving
            cleaned_category_name = clean_category_name(category_name)
            with open(f'contents/lib/{cleaned_category_name}.py', 'w') as file:
                file.write(f"{cleaned_category_name} = {new_category_list}")
                
                # Update the corresponding button name
            var_name = f"var_{cleaned_category_name}"
            if var_name in var_to_display:
                var_to_display[var_name] = category_name_entry.get()
                with open('contents/lib/button_names.py', 'w') as button_file:
                    button_file.write("button_names = [\n")
                    for var, display in var_to_display.items():
                        button_file.write(f'    ("{var}", "{display}"),\n')
                    button_file.write("]")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save changes to file: {e}")
            return
        
        # Close the current window
        edit_window.destroy()
        
        print("Reloading App...")
        
        final_message_blank_updating = ("")
        print(final_message_blank_updating)
        
        # Restart the application
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    def edit_item():
        selected_indices = category_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            selected_item = category_listbox.get(index)
            new_item_entry.delete(0, tk.END)
            new_item_entry.insert(0, selected_item)
            edit_button.config(state=tk.DISABLED)
            replace_button.config(state=tk.NORMAL)

    def replace_item():
        selected_indices = category_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            old_item = category_listbox.get(index)
            new_item = new_item_entry.get().strip()
            if new_item:
                # Replace item in the original list
                for i in range(len(original_category_list)):
                    if original_category_list[i] == old_item:
                        original_category_list[i] = new_item
                        break
                update_listbox()
                new_item_entry.delete(0, tk.END)
                edit_button.config(state=tk.NORMAL)
                replace_button.config(state=tk.DISABLED)
                # Clear the search filter
                search_entry.delete(0, tk.END)
        
    def search_items():
        keyword = search_entry.get().strip().lower()
        category_listbox.delete(0, tk.END)
        for item in original_category_list:
            if keyword in item.lower():
                category_listbox.insert(tk.END, item)
                
    def clear_filter():
        search_entry.delete(0, tk.END)
        update_listbox()

    def update_listbox():
        category_listbox.delete(0, tk.END)
        for item in original_category_list:
            category_listbox.insert(tk.END, item)
        
    # Entry for the category name
    cleaned_category_name = clean_category_name(category_name)
    var_name = f"var_{cleaned_category_name}"
    if var_name in var_to_display:
        display_name = var_to_display[var_name]
    else:
        display_name = category_name

    # Keep a copy of the original list
    original_category_list = category_list.copy()

    # Open a new window for editing the specified category
    edit_window = tk.Toplevel()
    edit_window.title(f"Edit {display_name} Category ✏️")
    edit_window.configure(bg='#0b0f19')
    
    def on_validate(P):
        if len(P) <= 28:  # Limiting to 30 characters
            return True
        else:
            return False
            
    # Label above the Name Entry widget
    label_text = "Edit Name (Max 28 Characters):"
    label = tk.Label(edit_window, text=label_text, bg='#0b0f19', fg='white')
    label.pack(pady=2)
    
    validate_cmd = edit_window.register(on_validate)
    
    category_name_entry = tk.Entry(edit_window, width=28, bg='#1f2937', fg='white', insertbackground='white', validate="key", validatecommand=(validate_cmd, '%P'))
    category_name_entry.insert(0, display_name)
    category_name_entry.pack(padx=10, pady=(0, 0))

    # Listbox to display current items
    category_listbox = tk.Listbox(edit_window, selectmode=tk.MULTIPLE, bd=0, width=68, height=23, bg='#1f2937', fg='white')
    category_listbox.pack(padx=10, pady=5)
    category_listbox.configure(highlightbackground="grey", highlightcolor="darkgrey")

    # Populate listbox with current items
    for item in category_list:
        category_listbox.insert(tk.END, item)
        
    # Buttons packed side by side
    button_frame = tk.Frame(edit_window, bg='#0b0f19')  # Create a frame for the buttons with a background color
    button_frame.pack(side=tk.TOP, pady=(3, 0))
    
    add_button = tk.Button(button_frame, text="Add Entry 🡩", command=add_item, bg='#424c5b', fg='white')
    add_button.pack(side=tk.LEFT, padx=(7, 4), pady=0)
    
    edit_button = tk.Button(button_frame, text="Edit Selected 🡫", command=edit_item, bg='#424c5b', fg='white')
    edit_button.pack(side=tk.LEFT, padx=4, pady=0)
    
    replace_button = tk.Button(button_frame, text="Replace Selected 🡙", command=replace_item, bg='#424c5b', fg='white', state=tk.DISABLED)
    replace_button.pack(side=tk.LEFT, padx=4, pady=0)
    
    remove_button = tk.Button(button_frame, text="Remove Selected ✕", command=remove_items, bg='#424c5b', fg='white')
    remove_button.pack(side=tk.LEFT, padx=(4, 5), pady=0)
    
    # Separator
    separator_below_buttons = tk.Frame(edit_window, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
    separator_below_buttons.pack(fill=tk.X, padx=5, pady=(5, 0))
        
    # Label above the Entry widget
    label_text = "Paste/Type new entries here (One Entry/Phrase, Per Add):"
    label = tk.Label(edit_window, text=label_text, bg='#0b0f19', fg='white')
    label.pack(pady=2)

    # Input field
    new_item_entry = tk.Entry(edit_window, width=69, bg='#1f2937', fg='white', insertbackground='white')
    new_item_entry.pack(padx=5, pady=(0, 7))
    
    # Separator
    separator_below = tk.Frame(edit_window, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
    separator_below.pack(fill=tk.X, padx=5, pady=(0, 2))
    
    # Label above search Entry widget
    label_text = "Filter for Keyword:"
    label = tk.Label(edit_window, text=label_text, bg='#0b0f19', fg='white')
    label.pack(pady=0)
    
    # Search entry and button
    search_frame = tk.Frame(edit_window, bg='#0b0f19')
    search_frame.pack(pady=0)

    search_entry = tk.Entry(search_frame, width=45, bg='#1f2937', fg='white', insertbackground='white')
    search_entry.pack(side=tk.LEFT, padx=5, pady=0)

    search_button = tk.Button(search_frame, text="Filter List", command=search_items, bg='#424c5b', fg='white')
    search_button.pack(side=tk.LEFT, padx=5, pady=0)
    
    clear_filter_button = tk.Button(search_frame, text="Clear Filter", command=clear_filter, bg='#424c5b', fg='white')
    clear_filter_button.pack(side=tk.LEFT, padx=5, pady=0)
    
    # Separator
    separator_below = tk.Frame(edit_window, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
    separator_below.pack(fill=tk.X, padx=5, pady=(5, 4))
    
    save_button_frame = tk.Frame(edit_window, bg='#0b0f19')  # Create a frame for the buttons with a background color
    save_button_frame.pack(side=tk.TOP, pady=0)
    
    shuffle_button = tk.Button(save_button_frame, text="Shuffle List", command=shuffle_items, bg='#424c5b', fg='white')
    shuffle_button.pack(side=tk.LEFT, padx=5, pady=(5, 5))
    
    save_button = tk.Button(save_button_frame, text="Save & Reload App", command=save_changes, bg='#424c5b', fg='white')
    save_button.pack(side=tk.LEFT, padx=5, pady=(5, 5))
    
    # Separator
    separator2_below = tk.Frame(edit_window, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
    separator2_below.pack(fill=tk.X, padx=5, pady=2)
    
    # Label at the bottom of the window
    label_text_top = "SCROLL DOWN TO SEE FULL LIST - Select entries and remove them or add"
    label_text_bottom = "more using the input field - Shuffle the list order/Mix in new additions"
    label = tk.Label(edit_window, text=label_text_top + "\n" + label_text_bottom, bg='#0b0f19', fg='white', justify=tk.CENTER, wraplength=420)
    label.pack(pady=5)
    
    update_listbox()

    center_window(edit_window, 430, 665)

# Create frame for checkboxes
checkbox_frame = tk.Frame(app, bg='#0b0f19')
checkbox_frame.pack(pady=5)

# Create two frames for checkboxes, one for each column
left_frame = tk.Frame(checkbox_frame, bg='#0b0f19')
left_frame.pack(side=tk.LEFT, padx=10)

center_frame = tk.Frame(checkbox_frame, bg='#0b0f19')
center_frame.pack(side=tk.LEFT, padx=10)

right_frame = tk.Frame(checkbox_frame, bg='#0b0f19')
right_frame.pack(side=tk.LEFT, padx=10)

# Define the font for the buttons
button_font = ("Helvetica", 8)  # Adjust the font size as needed
button_font2 = ("Helvetica", 12, "bold")

def open_edit_window():
    # Create a new Toplevel window for editing categories
    edit_categories_window = tk.Toplevel()
    edit_categories_window.title("Select A Category 📑")
    edit_categories_window.configure(bg='#0b0f19')
    
    # Label at the top of the window
    label_text = "Select A Category To Edit:"
    label = tk.Label(edit_categories_window, text=label_text, bg='#0b0f19', fg='white', font=('Helvetica', 12))
    label.pack(pady=5)
    
    # Define button texts and corresponding commands
    button_texts = [
        (var_to_display.get("var_people", "People"), lambda: edit_category("People", people)),
        (var_to_display.get("var_animals", "Animals"), lambda: edit_category("Animals", animals)),
        (var_to_display.get("var_fantasy_creatures", "Fantasy Creatures"), lambda: edit_category("Fantasy Creatures", fantasy_creatures)),
        (var_to_display.get("var_skin", "Skin"), lambda: edit_category("Skin", skin)),
        (var_to_display.get("var_genitals", "Genitals"), lambda: edit_category("Genitals", genitals)),
        (var_to_display.get("var_sex", "Sex"), lambda: edit_category("Sex", sex)),
        (var_to_display.get("var_emotions", "Emotions"), lambda: edit_category("Emotions", emotions)),
        (var_to_display.get("var_eyes", "Eyes"), lambda: edit_category("Eyes", eyes)),
        (var_to_display.get("var_hair", "Hair"), lambda: edit_category("Hair", hair)),
        (var_to_display.get("var_clothing", "Clothing"), lambda: edit_category("Clothing", clothing)),
        (var_to_display.get("var_accessories", "Accessories"), lambda: edit_category("Accessories", accessories)),
        (var_to_display.get("var_objects", "Objects"), lambda: edit_category("Objects", objects)),
        (var_to_display.get("var_actions", "Actions"), lambda: edit_category("Actions", actions)),
        (var_to_display.get("var_places", "Places"), lambda: edit_category("Places", places)),
        (var_to_display.get("var_time_periods", "Time Periods"), lambda: edit_category("Time Periods", time_periods)),
        (var_to_display.get("var_times_of_day", "Times of Day"), lambda: edit_category("Times of Day", times_of_day)),
        (var_to_display.get("var_mystical_elements", "Mystical Elements"), lambda: edit_category("Mystical Elements", mystical_elements)),
        (var_to_display.get("var_professions", "Professions"), lambda: edit_category("Professions", professions)),
        (var_to_display.get("var_weather", "Weather"), lambda: edit_category("Weather", weather)),
        (var_to_display.get("var_vehicles", "Vehicles"), lambda: edit_category("Vehicles", vehicles)),
        (var_to_display.get("var_food_drinks", "Food and Drinks"), lambda: edit_category("Food and Drinks", food_drinks)),
        (var_to_display.get("var_nature_elements", "Nature Elements"), lambda: edit_category("Nature Elements", nature_elements)),
        (var_to_display.get("var_technology_tools", "Technology and Tools"), lambda: edit_category("Technology Tools", technology_tools)),
        (var_to_display.get("var_hobbies_activities", "Hobbies and Activities"), lambda: edit_category("Hobbies and Activities", hobbies_activities)),
        (var_to_display.get("var_social_interactions", "Social Interactions"), lambda: edit_category("Social Interactions", social_interactions)),
        (var_to_display.get("var_legendary_places_realms", "Legendary Places and Realms"), lambda: edit_category("Legendary Places and Realms", legendary_places_realms)),
        (var_to_display.get("var_historical_events_moments", "Historical Events and Moments"), lambda: edit_category("Historical Events and Moments", historical_events_moments)),
        (var_to_display.get("var_body_language_gestures", "Body Language and Gestures"), lambda: edit_category("Body Language and Gestures", body_language_gestures)),
        (var_to_display.get("var_art_styles", "Art Styles"), lambda: edit_category("Art Styles", art_styles)),
        (var_to_display.get("var_wildcards", "Wildcards"), lambda: edit_category("Wildcards", wildcards)),
        (var_to_display.get("var_custom_1", "Custom 1"), lambda: edit_category("Custom 1", custom_1)),
        (var_to_display.get("var_custom_2", "Custom 2"), lambda: edit_category("Custom 2", custom_2)),
        (var_to_display.get("var_custom_3", "Custom 3"), lambda: edit_category("Custom 3", custom_3))
        ]

    # Calculate the midpoint to split buttons into three columns
    mid1 = len(button_texts) // 3
    mid2 = 2 * len(button_texts) // 3

    # Create left and right frames for buttons
    left_frame = tk.Frame(edit_categories_window, bg='#0b0f19')
    center_frame = tk.Frame(edit_categories_window, bg='#0b0f19')
    right_frame = tk.Frame(edit_categories_window, bg='#0b0f19')

    # Pack frames to the left and right sides of edit_categories_window
    left_frame.pack(side=tk.LEFT, padx=10, pady=0, fill=tk.BOTH, expand=True)
    center_frame.pack(side=tk.LEFT, padx=10, pady=0, fill=tk.BOTH, expand=True)
    right_frame.pack(side=tk.RIGHT, padx=10, pady=0, fill=tk.BOTH, expand=True)

    # Loop through button texts to create buttons in two columns
    for idx, (text, command) in enumerate(button_texts):
        # Determine in which frame to place the button
        if idx < mid1:
            frame = left_frame
        elif mid1 <= idx < mid2:
            frame = center_frame
        else:
            frame = right_frame
        
        # Create the button in the respective frame
        button = tk.Button(frame, text=text, command=command, borderwidth=1, relief=tk.SOLID, bg='#424c5b', fg='white', font=button_font)
        button.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X)
        
        center_window(edit_categories_window, 500, 409)

# Function to toggle the variable and update button color
def toggle_button():
    if toggle_var.get() == 0:
        toggle_var.set(1)
        use_select_order_button.config(bg='green', fg='white')  # Change button color to green
    else:
        toggle_var.set(0)
        use_select_order_button.config(bg='#333', fg='grey')  # Reset button color
        
def uncheck_all():
    var_people.set(0)
    var_animals.set(0)
    var_fantasy_creatures.set(0)
    var_skin.set(0)
    var_genitals.set(0)
    var_sex.set(0)
    var_emotions.set(0)
    var_eyes.set(0)
    var_hair.set(0)
    var_clothing.set(0)
    var_accessories.set(0)
    
    var_objects.set(0)
    var_actions.set(0)
    var_places.set(0)
    var_time_periods.set(0)
    var_times_of_day.set(0)
    var_mystical.set(0)
    var_professions.set(0)
    var_weather.set(0)
    var_vehicles.set(0)
    var_food_drinks.set(0)
    var_nature_elements.set(0)
    
    var_technology_tools.set(0)
    var_hobbies_activities.set(0)
    var_social_interactions.set(0)
    var_legendary_places_realms.set(0)
    var_historical_events_moments.set(0)
    var_body_language_gestures.set(0)
    var_art_styles.set(0)
    var_wildcards.set(0)
    var_custom_1.set(0)
    var_custom_2.set(0)
    var_custom_3.set(0)
    
    checked_order.clear()
    # print("Checked Order cleared:", checked_order)
       
buttonbox_frame = tk.Frame(app, bg='#0b0f19')
buttonbox_frame.pack(pady=0)

button_frame = tk.Frame(buttonbox_frame, bg='#0b0f19')
button_frame.pack(side=tk.LEFT, padx=10, pady=(5, 0))

use_select_order_button = tk.Button(button_frame, text="Use Selection Order", borderwidth=1, bg='#333', fg='grey', command=toggle_button)
use_select_order_button.pack(side=tk.LEFT, pady=(0, 0), padx=(0, 10))

uncheck_button = tk.Button(button_frame, text="UnCheck All", borderwidth=1, bg='#D32F2F', fg='white', command=uncheck_all)
uncheck_button.pack(side=tk.LEFT, pady=(0, 0), padx=(0, 10))

open_editor_button = tk.Button(button_frame, text="Edit Categories", borderwidth=1, bg='#008080', fg='white', command=open_edit_window)
open_editor_button.pack(side=tk.LEFT, pady=(0, 0))

# Function to track the order of checked items
def track_checkbutton_order(checkbutton_id):
    if checkbutton_id in checked_order:
        checked_order.remove(checkbutton_id)
    else:
        checked_order.append(checkbutton_id)
    
    # print("Checked Order:", checked_order)

# Left Frame
tk.Checkbutton(left_frame, text=var_to_display.get("var_people", "People"), variable=var_people, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("1")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_animals", "Animals"), variable=var_animals, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("2")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_fantasy_creatures", "Fantasy Creatures"), variable=var_fantasy_creatures, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("3")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_skin", "Skin"), variable=var_skin, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("4")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_genitals", "Genitals"), variable=var_genitals, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("5")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_sex", "Sex"), variable=var_sex, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("6")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_emotions", "Emotions"), variable=var_emotions, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("7")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_eyes", "Eyes"), variable=var_eyes, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("8")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_hair", "Hair"), variable=var_hair, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("9")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_clothing", "Clothing"), variable=var_clothing, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("10")).pack(anchor='w')
tk.Checkbutton(left_frame, text=var_to_display.get("var_accessories", "Accessories"), variable=var_accessories, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("11")).pack(anchor='w')

# Center Frame
tk.Checkbutton(center_frame, text=var_to_display.get("var_objects", "Objects"), variable=var_objects, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("12")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_actions", "Actions"), variable=var_actions, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("13")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_places", "Places"), variable=var_places, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("14")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_time_periods", "Time Periods"), variable=var_time_periods, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("15")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_times_of_day", "Times of Day"), variable=var_times_of_day, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("16")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_mystical_elements", "Mystical Elements"), variable=var_mystical, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("17")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_professions", "Professions"), variable=var_professions, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("18")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_weather", "Weather"), variable=var_weather, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("19")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_vehicles", "Vehicles"), variable=var_vehicles, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("20")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_food_drinks", "Food and Drinks"), variable=var_food_drinks, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("21")).pack(anchor='w')
tk.Checkbutton(center_frame, text=var_to_display.get("var_nature_elements", "Nature Elements"), variable=var_nature_elements, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("22")).pack(anchor='w')

# Right Frame
tk.Checkbutton(right_frame, text=var_to_display.get("var_technology_tools", "Technology and Tools"), variable=var_technology_tools, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("23")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_hobbies_activities", "Hobbies and Activities"), variable=var_hobbies_activities, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("24")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_social_interactions", "Social Interactions"), variable=var_social_interactions, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("25")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_legendary_places_realms", "Legendary Places and Realms"), variable=var_legendary_places_realms, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("26")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_historical_events_moments", "Historical Events and Moments"), variable=var_historical_events_moments, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("27")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_body_language_gestures", "Body Language and Gestures"), variable=var_body_language_gestures, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("28")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_art_styles", "Art Styles"), variable=var_art_styles, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("29")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_wildcards", "Wildcards"), variable=var_wildcards, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("30")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_custom_1", "Custom 1"), variable=var_custom_1, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("31")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_custom_2", "Custom 2"), variable=var_custom_2, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("32")).pack(anchor='w')
tk.Checkbutton(right_frame, text=var_to_display.get("var_custom_3", "Custom 3"), variable=var_custom_3, bg='#0b0f19', fg='white', selectcolor='#424c5b', command=lambda: track_checkbutton_order("33")).pack(anchor='w')

# Add a separator line below the checkboxes
separator_below = tk.Frame(app, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
separator_below.pack(fill=tk.X, padx=5, pady=10)

# Create button to generate prompt
generate_button = tk.Button(
    app,
    text="Generate Random Prompt ",
    image=emoji_image,
    compound=tk.RIGHT,  # Image to the left of the text
    command=generate_prompt,
    bg='#e56412',
    fg='white',
    height=30,
    width=240,
    font=button_font2
)
generate_button.pack(pady=10, padx=5)

# Label to display the generated prompt
result_label = tk.Label(app, text="", wraplength=500, bg='#1f2937', fg='white')
result_label.pack(pady=10, expand=True, fill='both')
result_label.config(text=". . . Generated Prompt Will Be Displayed Here and The Prompt History In The Terminal . . .")
result_label.pack(pady=10)

# Add a separator line below the checkboxes
separator_below = tk.Frame(app, height=2, bd=1, relief=tk.SUNKEN, bg='#424c5b')
separator_below.pack(fill=tk.X, padx=5, pady=(10, 0))

frame0 = tk.Frame(app, bg='#0b0f19')
frame0.pack(side=tk.TOP, padx=5)

frame1 = tk.Frame(frame0, bg='#0b0f19')
frame1.pack(side=tk.LEFT, padx=(7, 5), pady=5)

frame2 = tk.Frame(frame0, bg='#0b0f19')
frame2.pack(side=tk.LEFT, padx=5, pady=5)

frame3 = tk.Frame(frame0, bg='#0b0f19')
frame3.pack(side=tk.LEFT, padx=5, pady=5)

frame4 = tk.Frame(frame0, bg='#0b0f19')
frame4.pack(side=tk.LEFT, padx=5, pady=5)

# Create button to add random weights
add_weights_button = tk.Button(frame1, text="Add Random Weights", command=add_weights, bg='#424c5b', fg='white')
add_weights_button.pack(side=tk.LEFT, padx=10, pady=10)

# Hide randomize button initially
add_weights_button.pack_forget()

# Create button to randomize output
randomize_button = tk.Button(frame2, text="Randomize Prompt", command=randomize_output, bg='#424c5b', fg='white')
randomize_button.pack(side=tk.LEFT, padx=10, pady=10)

# Hide randomize button initially
randomize_button.pack_forget()

# Create button to copy prompt to clipboard
copy_button = tk.Button(frame3, text="Copy Prompt To Clipboard", command=copy_to_clipboard, bg='#424c5b', fg='white')
copy_button.pack(side=tk.LEFT, padx=10, pady=10)

# Hide copy button initially
copy_button.pack_forget()

# Create button to save prompt to file
save_button = tk.Button(frame4, text="Save Prompt To File", command=save_prompt, bg='#424c5b', fg='white')
save_button.pack(side=tk.RIGHT, padx=10, pady=10)

save_button.pack_forget()

count_category_items()

# Run the application
app.mainloop()
