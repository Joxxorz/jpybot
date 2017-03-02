import questions
import answers
import intent

def lookInQuestions(userResponse):
    questionsList = questions.botQuestions
    for e in questionsList:
        if e in userResponse:
            return searchAgainstAnswers(questionsList.index(e))

def searchAgainstAnswers(index):
    answersList = answers.botAnswers
    for e in answersList:
        return answersList[index]

def findIntent(userResponse):
    intentList = intent.intent
    for e in intentList:
        print(e)
        return intentList[index]

def findAnswer(botResponse, userResponse):
    botResponse = lookInQuestions(userResponse)

    if botResponse:
        answer = botResponse
    else:
        answer = 'I\'m sorry I don\'t have an answer for that.'

    return answer;
