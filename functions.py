import questions
import answers

def lookInQuestions(userResponse):
    questionsList = questions.botQuestions
    for e in questionsList:
        if e in userResponse:
            return searchAgainstAnswers(questionsList.index(e))

def searchAgainstAnswers(index):
    answersList = answers.botAnswers
    for e in answersList:
        return answersList[index]

def findAnswer(botResponse, userResponse):
    botResponse = lookInQuestions(userResponse)

    if botResponse:
        answer = botResponse
    else:
        answer = 'I\'m sorry I don\'t have an answer for that.'

    return answer;
