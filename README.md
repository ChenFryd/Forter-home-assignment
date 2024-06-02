# Forter Home assignment
Counts the number of unique name.

## How to Run
you need to have [nicknames](https://pypi.org/project/nicknames/), [ntlk](https://pypi.org/project/nltk/) and [unittest](https://docs.python.org/3/library/unittest.html)
### Option 1: gui
run the gui.py file. <br>
unfortunately tkinter is hard to use in docker, so that's why there are two options.
You need in addition to have [tkinter](https://docs.python.org/3/library/tkinter.html) 
#### The options are:
![image](https://github.com/ChenFryd/Forter-home-assignment/assets/93209122/8a018afb-323d-41d7-b465-71ead6cfc0c8) <br>
1. you can set the maximum amount of typos allowed  <br>
![image](https://github.com/ChenFryd/Forter-home-assignment/assets/93209122/0a7a83c2-6417-4730-9925-12de0b553c5b) <br>
2. run all the automated tests <br>
it simply runs all the unittests
3. and run a manual test  <br>
![image](https://github.com/ChenFryd/Forter-home-assignment/assets/93209122/8277f3b3-080d-4560-b6aa-56129c813222) <br>
please enter at least one character on the first and last names, and the bill name on card at least two parts seperated by a space.
4. exit  <br>
 
### Option 2: cli
Run the cli.py file.<br>
If you are running this code with docker, please use the flag -it <br>
**docker run -it <IMAGE_NAME>**

![image](https://github.com/ChenFryd/Forter-home-assignment/assets/93209122/7fbcf146-aeae-4834-8504-1cf2db1df438)<br>
Enter the desired option.<br>

## How Does it Work
### Nicknames
The first names are checked with their cannonical. cannonical it's the opposite of nickname.
so here in the example Richard is the cannonical of the nickname dick.
it allows edge cases where the first name Richard -> dick<br>
and the other first name is Richard -> rich<br>
and it stiill allows the program to count the first names as they are the same.

### Typos
The program counts the typos by edit distance (or its other name levinstein distance)
this way if the user enter "Deborah" and in mistake put in "Deborha" it will count as one typo.

### middle names
If one name has middle name and other doesn't, it doesn't being counted for the amount of typos.
