# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    #opponent_history.append(prev_play)

    #guess = "R"
    #if len(opponent_history) > 2:
    #    guess = opponent_history[-2]

    #return guess

    opponent_history.append(prev_play)
    guess = 'S'
    if not prev_play: opponent_history.clear()
    if prev_play:
        rockCount = 0
        paperCount = 0
        scissorsCount = 0
        for i in range(len(opponent_history) - 1):
            if opponent_history[i] == prev_play:
                next = opponent_history[i + 1] 
                if next == 'R':
                    rockCount += 1
                if next == 'P':
                    paperCount += 1
                if next == 'S':
                    scissorsCount += 1

        rockGuess = scissorsCount
        paperGuess = rockCount
        scissorsGuess = paperCount

        maxGuess = max(rockGuess, paperGuess, scissorsGuess)
        if maxGuess == rockGuess: guess = 'R'
        if maxGuess == paperGuess:  guess = 'P'
        if maxGuess == scissorsGuess: guess = 'S'

        bigBrain = {'P':'R', 'R':'S', 'S':'P'}
        if len(opponent_history) > 2:
            if opponent_history[-1] == opponent_history[-2] != opponent_history[-3] : guess = bigBrain[prev_play]

        if (rockCount == paperCount == scissorsCount == 0): guess = prev_play
    
    return guess
