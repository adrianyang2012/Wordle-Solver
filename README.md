# Wordle-Solver

## What is this
This is a wordle solver that can solve "wordle" on either the following websites:
- https://wordlegame.org/ (default)
- https://www.nytimes.com/games/wordle/index.html

This Python program can automatically type the answer and see the answer on its own. I also made it to automatically go to the next wordle game when you are using the [unlimited wordle](https://wordlegame.org). 

This is how it looks like ([Youtube video](https://www.youtube.com/watch?v=KjCDkzm17Qo)):

[![A video](https://img.youtube.com/vi/KjCDkzm17Qo/0.jpg)](https://www.youtube.com/watch?v=KjCDkzm17Qo)

## How I made it
-  I made this by using [**nltk**](https://www.nltk.org/) to store all the words
-  I used [**pyautogui**](https://pyautogui.readthedocs.io/en/latest/) to automatically use the keyboard and mouse to type the answers. 
### nltk
-  For nltk, I used the word and wordnet corpuses
-  If the word nltk thinks is a word but wordle does not, it goes on to the next possible word.
### pyautogui
-  I also used pyautogui for screenshooting the screen and see the colors of each box. I took the corners of each box and measuared its color to see what it was. 
-  To see what words were possible after that, I removed the words that did not match the letters that were green. I also removed the words that contained letters that were supposed to be grey.
-  For the yellow ones, I made it so it detected if a letter is on a different box and those that did not were removed. Then, the program chooses the first possible word.

## How to use it
To use this, you first need to install an ad blocker. Then, you need to split the code and the wordle window in half like this:

![Wordle screen on one half and code on the other](Wordle_solver.png?raw=true)


## Timelapse on running a lot of game automatically
- ([Youtube video](https://www.youtube.com/watch?v=WJ9y50yJzP8))

[![A video](https://img.youtube.com/vi/WJ9y50yJzP8/0.jpg)](https://www.youtube.com/watch?v=WJ9y50yJzP8)

