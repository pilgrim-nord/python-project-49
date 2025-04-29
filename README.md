# Brain Games

[![Actions Status][image-1]][1] [![Maintainability][image-2]][2]





Brain Games is a set of five console games based on the principle of popular mobile applications for brain training. Each game asks questions that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end the game and offer to complete it again. 

**Games:** 

- Brain Calculator: Arithmetic expressions that need to be calculated 
- Brain Even: Determining an even number 
- Brain GCD: Determining the greatest common divisor 
- Brain Progression: Searching for missing numbers in a sequence of numbers 
- Brain Prime: Definition of a prime number

You can call them with simple commands:

brain-even
brain-calc
brain-gcd
brain-progression
brain-prime

Game example:

```
brain-progression
Welcome to the Brain Game!
What number is missing in this progression?
May I have your name? Roman
Hello, Roman!
Question: 14 .. 18 20 22 24 26 28
Your answer: 16 # Пользователь вводит ответ
Correct!
Question: 5 6 7 8 9 .. 11 12
Your answer: 10 # Пользователь вводит ответ
Correct!
Question: 12 15 18 21 .. 27 30 33
Your answer: 24 # Пользователь вводит ответ
Correct!
Congratulations, Roman!
```

#### **Installation**

#### **Project package**

To work with the package, you need to clone the repository to your computer. This is done using the git clone command. 

Clone the project on the command line:

Clone via HTTPS:
git clone [https://github.com/pilgrim-nord/python-project-49.git][3]

Before installing the package, you need to make sure that you have Python version 3.13 or higher installed

#### Install using uv:

```
uv sync brain-games
uv build brain-games
uv tool install dist/*.whl
```

## Usage

#### Brain Even

A random number is shown to the user. And he needs to answer yes if the number is even, or no if it is odd.

##### Brain-even demo:

[![asciicast][image-3]][4]



#### Brain Calculator

The user is shown a random mathematical expression, for example, 35 + 16, which needs to be calculated and the correct answer written down.

##### Brain-calc demo:

[![asciicast][image-4]][5]



#### Brain GCD

The user is shown two random numbers, for example, 25 50. The user must calculate and enter the largest common divisor of these numbers.

##### Brain-gcd demo:

[![asciicast][image-5]][6]



#### Brain progression

The player is shown a series of numbers that forms an arithmetic progression by replacing any of the numbers with two dots. The player must determine this number.

##### Brain-progression demo:

[![asciicast][image-6]][7]



#### Brain prime

The player is shown a series of numbers that forms an arithmetic progression by replacing any of the numbers with two dots. The player must determine this number.

##### Brain-prime demo:

[![asciicast][image-7]][8]

[1]:	https://github.com/pilgrim-nord/python-project-49/actions
[2]:	https://codeclimate.com/github/pilgrim-nord/python-project-49/maintainability
[3]:	https://github.com/pilgrim-nord/python-project-49.git
[4]:	https://asciinema.org/a/CMk3tEDgZzJQbcY9m1gy8yanj
[5]:	https://asciinema.org/a/FRZ4e2s0UYpSFmo1tQXLcLu9E
[6]:	https://asciinema.org/a/kQ84u1Pgh15LC3e4bmvj5GSJy
[7]:	https://asciinema.org/a/bO5cjIkI9wRqUgYiGfGxxNwL1
[8]:	https://asciinema.org/a/ZgFIDxhV3lGx3NaUNvx1dmTmV

[image-1]:	https://github.com/pilgrim-nord/python-project-49/actions/workflows/hexlet-check.yml/badge.svg
[image-2]:	https://api.codeclimate.com/v1/badges/4f012ef14d09f68b0c08/maintainability
[image-3]:	https://asciinema.org/a/CMk3tEDgZzJQbcY9m1gy8yanj.svg
[image-4]:	https://asciinema.org/a/FRZ4e2s0UYpSFmo1tQXLcLu9E.svg
[image-5]:	https://asciinema.org/a/kQ84u1Pgh15LC3e4bmvj5GSJy.svg
[image-6]:	https://asciinema.org/a/bO5cjIkI9wRqUgYiGfGxxNwL1.svg
[image-7]:	https://asciinema.org/a/ZgFIDxhV3lGx3NaUNvx1dmTmV.svg