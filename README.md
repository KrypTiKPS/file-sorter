First, a brief explanation. I made this out of pure boredom, and yes, I will be updating it. This means that there is code that may seem "unnecessary" such as "def sort(dir)" since the directory is static in this release. I could have just add the directory (cwd) into the function instead of making the function take parameters. I'll be adding an argv in the future for other directories (hence the parameter(dir)).

To get help you can type --h (for help, atm there is only 1 option so I'll cover it)

Using --sort will do all the same as using no options except it'll take all your files with a certain extension and move them to the appropriate directories.
For example, all .py files will be moved to py/, .txt to txt/, and so on.

If you use the file with no options it'll just show all the files in your cwd, count them, and show if they're a dir, file, unkown, or in the case of *nix, a backup file. Ex "sort.py sort.py~" where "sort.py~" is a backup file of "sort.py". I'll clean up this code in the near future. It's a tad bit sloppy but it works great.
