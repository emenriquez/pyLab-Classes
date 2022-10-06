## Used for tests - do not code here!
from question import Question
from quiz import Quiz

def test_Question():
    try:
        myQuestion = Question("How are you?", "Great!")

        assert myQuestion.question == "How are you?"
        assert myQuestion.answer == "Great!"
    except:
        assert False, f"Question class is invalid!"

def test_Quiz():
    try:
        myQuiz = Quiz()
    except:
        assert False, f"Quiz class is invalid!"

def test_addQuestion():
    myQuiz = Quiz()
    myQuestion = Question("How are you?", "Great!")
    otherQ = Question("What's 1 + 1", "two")
    myQuiz.addQuestion(myQuestion)
    myQuiz.addQuestion(myQuestion)
    myQuiz.addQuestion(otherQ)

    assert len(myQuiz.quizQuestions) == 3

def test_playQuestion(monkeypatch):
    myQuiz = Quiz()
    myQuestion = Question("How are you?", "Great!")
    otherQ = Question("What's 1 + 1", "two") 



    monkeypatch.setattr('builtins.input', lambda _: "two")
    myQuiz.playQuestion(myQuestion)
    assert myQuiz.currentScore == 0

    myQuiz.playQuestion(otherQ)
    assert myQuiz.currentScore > 0

def test_displayScore():
    try:
        myQuiz = Quiz()
        myQuiz.currentPlayerName = "Hank"
        myQuiz.currentScore = 99
        myQuiz.displayScore()
    except:
        assert False, f"displayScore() function error!"
    
    assert myQuiz.topScores['Hank'] == 99

def test_startGame(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Carolinha")
    try:
        myQuiz = Quiz()
        otherQ = Question("What's 1 + 1", "two")
        myQuiz.addQuestion(otherQ)
        myQuiz.startGame()
    except:
        assert False, f"startGame() function error!"

    assert myQuiz.topScores['Carolinha'] >= 0
        