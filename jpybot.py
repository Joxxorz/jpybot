import functions
def poseQuestion(botResponse, userResponse):
    botResponse = functions.findAnswer(botResponse, userResponse)
    return botResponse
botResponse = 'Hi, ask me things!'
while True:
    userResponse = str(raw_input(botResponse + '\n'));
    userResponse = userResponse.lower()

    if userResponse not in 'jpybotstopit':
        botResponse = poseQuestion(botResponse, userResponse)
    else:
        break
