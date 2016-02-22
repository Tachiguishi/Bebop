## windows command
* `cd` display current directory. Short for "change directory".
* `cd ..` - move up the directory tree one level. Doing this from C:\Users\JohnSmith\Desktop will take you to C:\Users\JohnSmith, for example.
* `cd %userprofile%\Desktop` - takes you to the currently logged in users desktop on most versions of Windows
* `cd C:\Users\JohnSmith\Desktop` - takes you to the desktop on Win 7 and 8. Replace JohnSmith with your logon or profile name.
* `cd C:\Documents and Settings\JohnSmith\Desktop` - takes you to the desktop on Windows XP
* `cd \` - brings you back to the root of the current drive
* `X:` - takes you to the last used location on drive X (typically, use `C:` or `D:`). It defaults to the root directory if you have not previously cd'd to anywhere on that drive.
* `dir` - Display a list of files and folders, very fast.
* `dir /p` - Display´s long lists of files and folders per "pages". Slower.
* `dir /?` - Shows commands for folders and subfolders in the current folder/directory.
* `cls` - Clear the screen
* `Up arrow` - display previous commands within that session. Enter to select the command or Escape to get back to the prompt
* `Tab` - Toggles through existing files and folders in current directory, will auto complete the typing of a file or folder name once the first letters are typed.
* `dir > myfile` - creates a text file named myfile containing the directory listing. To open it with Notepad, just type "Notepad myfile" at the prompt.
* `exit` - Closes the command window. It has the same effect that closing the window with the "X" button (at the top right corner).
* `F3` - repeats previous command (i.e. if you typed `ping 10.10.10.10` and pressed Enter. It would show `ping 10.10.10.10` again without having to retype it.


## Python command
* `quit()` or `ctrl + Z` or `exit()` -ends Python on Windows.
* `quit()` or `ctrl + D` -Tells "End Of File" to Python on Mac and GNU/Linux.
* `quit()` or `ctrl + C` -Kills Python process on Mac and GNU/Linux.