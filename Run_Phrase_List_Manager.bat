@echo off
echo  [92m. . . App Running . . .[0m
echo.
echo  [36m* Rando-Prompto - Phrase List Manager - BuildVer: 1.1.6_RV1.0 - (Coded By: [92mEyeFly [36mand [31mChatGPT[36m)[0m
echo. 
echo  [31m- Example Phrase List Setup For The List Manager and Auto Formatter:[33m
echo.
echo.
echo  ([31mNote about the following puctuation examples:[33m Most of these are removed during the adding proccess
echo   anyway, but apostrophes and commas are added back to the phrases as part of the string list formatting
echo   to separate the phrases.
echo. 
echo   The ONLY punctuation that is kept is dashes and underscores, besides the commas and apostrophes that
echo   separate the phrases.
echo. 
echo   Some of these examples are just in case you manually edit the files in a text editor,
echo   since the list manager takes care of them when you add the phrases.)
echo.
echo.
echo. 
echo  [31mExample[92m - Vertical List:[33m
echo  car
echo  a truck
echo  a green boat
echo  keep
echo  adding
echo  lines like
echo  this
echo. 
echo. 
echo  [31mExample[92m - Horizontal List:[33m
echo  car, a truck, a green boat, keep, adding, lines like, this
echo. 
echo. 
echo  [31mExample[92m - Mixed List Types:[33m
echo  car
echo  a truck
echo  a green boat
echo  car, a truck, a green boat, keep, adding, lines like, this
echo  keep
echo  adding
echo  lines like
echo  this
echo. 
echo.
echo  [31mExample[92m - Acceptable Punctuation In Phrases:[33m
echo.
echo  car
echo  a_truck
echo  a-green boat
echo  'apple'
echo  "a_painting-of"
echo. 
echo  'this', 'is', 'also ok', 'to do', 'in', 'the list before', 'adding' (Note: This is the app's internal string formatting)
echo. 
echo  "this", "is", "also", "also ok", "to do", "in", "the list before", "adding"
echo. 
echo. 
echo  [31mExample[92m - Not Recomended Punctuation In Phrases:[33m
echo  jake's (it will likely break the file due to the apostrophe. So make it "Jakes" or just Jake instead.)
echo. 
echo  (this), ((is not)), (OK to do:1.24), (((if you plan on))), (using the random weights:0.673)
echo   (Note: The random weights function removes all existing weights before adding new ones.)
echo.  
echo. 
echo  [31mBasically[36m, do not bracket your phrases with any symbols except for the ones I showed to be OK.
echo  Follow my examples and look at the way the pre-poppulated lists are laid out for more examples.[92m
echo. 
echo. 
echo  [31mThe basic internal category list file structure is:[92m
echo  category_name = ['your', 'lists will', 'be formatted like', 'this', 'in the category list files', 'in the app']
echo.
echo.
echo  [31mMaking your own categories/phrase lists:[92m
echo  I used ChatGPT to make most of the lists, along with a chat AI on Huggingface.co to list the X-Rated categories.
echo  I recomend asking ChatGPT to make a list of whatever you want. A vertical list is totally OK.
echo  Take the lists that chatgpt makes for you and paste them into the Phrase List Manager's input field and click
echo  the add button. The list will be formatted correctly and added to the list box. 
echo. 
echo  Avoiding APOSTROPHES is absolutely needed because they break the string list file. The app can have errors. 
echo  Try to avoid getting the punctuation I mentioned, by telling chatgpt to make sure not to use any special
echo  characters or accent marks. Telling chatgpt to make a python string can get you what you want too (pre-formatted),
echo  when the AI is feeling generous. LOL.
echo.
echo.
echo  [31mFixing a broken category list file:[92m
echo  If you do break the list files, and get errors loading the app, and you can't fix it, I have provided a backup of
echo  all the original category files. (Checkthe app folder for: [31mBackups.zip[92m)
echo. 
echo.  
echo  [36mNow, Go Make Some Cool Stuff![0m
echo. 
echo  :EyeFly:[92m
echo. 
echo  . . . . . . . . . . . . . . . . . . . . . [31m!SCROLL UP FOR LIST FORMAT EXAMPLES![92m . . . . . . . . . . . . . . . . . . . .
echo. 
python phrase_list_manager.py
pause