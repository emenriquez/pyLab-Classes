# Python Lab - Quiz Game (Classes)

For this lab, you will be constructing a simple quiz game using classes. You will need to complete the following:

## Part 1 - Question Class
Create a class that has the following attributes:
1. `question`
2. `answer`

For example, your question can be something like the following
 - question: `Is 7 a prime number?`
 - answer: `yes`

To keep it simple for now, we can create open-ended answers, but a good version of this game might utilize multiple choice questions!
 - question: `Which of these is a prime number?`
    * A. 4    
    * B. 7    
    * C. 9
    * D. 10
 - answer: `B`

 **Constructor**: Your `Question` class should also contain a constructor (init function) to set the Question and Correct Answer attributes (not using console input)

 ## Part 2 - Quiz Class (Attributes)
 Define a class `Quiz` that has the following attributes:
 1. `quizQuestions`
    - A list of quiz Question objects
 2. `currentScore`
    - should keep track of the player's score, and will start at zero with each game
 3. `topScores`
    - this should be a dictionary of player names and their scores who have played this quiz
4. `currentPlayerName`
    - this will hold the name of the player currently playing your game

## Part 3 - Quiz Class (Methods)
Your class should have the following methods:
 1. \_\_init\_\_() [*constructor*]
    - inputs: self, (optional) list of quiz question objects
    - use this method to set the attributes to their initial values

 2. playQuestion()
    - inputs: self, Question object
    - this method should display the current `question` to the user
    - this function will then take *console input* from the user for the answer
    - next, this method will check if the answer submitted matches the correct answer
    - if the answer is correct, increase the `currentScore` by 1

 3. displayScore()
    - inputs: self
    - this method should display the user's score (will be run once the quiz is done)
    - this should also add the user's top score entry to `topScores`

4. addQuestion()
    - inputs: self, question object
    - this method should take in a `question` object and add it to the quiz question list

5. startGame()
    - inputs: self
    - this method should ask for the player's name (console input) and store it in `currentPlayerName`
    - the score will also be reset to zero here
    - Next, the method should play each question using `playQuestion()` for each question in the `quizQuestions` attribute
    - Once the questions are complete, the game should use `displayScore()` to show the user's final score and save it to the `topScores` attribute