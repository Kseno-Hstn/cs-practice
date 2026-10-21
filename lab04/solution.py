def winner(name, scores):
    mx = -123492874
    for i in range(len(scores)):
        if score[i] > mx:
            mx = score[i]
            uns = i
    return name[uns]
