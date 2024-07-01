# Instructions For Running App...
  
* PYTHON and PIP are REQUIRED to run this app!!! PYPERCLIP aslo required but, will be installed by the file below.

* Use the 'Run_Random_Prompt_Generator_This_File_Installs_or_Updates_Dependencies_Before_Running_App.bat' file if
  it is the first time running the app and you do not have pyperclip installed OR do not know if you have pyperclip
  installed. It will aslo update pip and pyperclip if they are already installed and there is an update availible.

* Use the 'Run_Random_Prompt_Generator.bat' file if the dependencies are installed and you do not want to check for
  updates when launching the app.
  
* After launching the app, see the terminal window for the 'How To Use' and 'Editing Categories' instructions. 
  (Instructions will be at the top of the terminal window. You will need to scroll up to see them).
  
  

# A WARNING to PAY ATTENTION to!!!

* When editing the category contents, it is IMPORTANT that you do not have apostrophes, commas or accent marks in the
  phrases, (example: "Jake's" or "Café" or "jake's eating a cake, at the Café"). Commas need to only be between the
  phrases in a (example: "car, a truck, a green boat")
  
* These will break the category list file when saving the changes. If this happens, you can go to the file
  directory (contents/lib/category_name.py) and open the file for the broken category in a text editor, and delete
  the offendong phrase. Or if you can't fix it for some reason, there is a backup folder with the original list files.
  There is also a backup of the category names. The file iscalled "button_names.py"
  
* You need to also delete the folder named "__pycache__" at the directory (contents/lib/__pycache__). As it may also
  contain a broken file. The folder and its contents will be re-generated the next time the app runs.
  
* See the default category contents (Phrases) for examples on acceptable phrase layout. Things like,
  (example: life-like or life_like or life like!) are OK.
  
* I have not tested other punctuation marks (other than: - and _ and !), because I do not see others use any other
  punctuation in their prompts.
  
* Do not add LoRA triggers to category lists. I have not tested that. It may break the lists or break the trigger format.
  Leave adding LoRAs for the Image Generator App.
  
* Do not add weights to the added phrases. Any existing weights are removed first if you use the 'Add Random Weights'
  button. Weights look like - example: ( ), (( )), ((( ))), or ( :0.8). And [ ], [[ ]], [[[ ]]], or [ :0.8].