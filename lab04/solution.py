def winner(name, scores):
    mx = -123492874
    for i in range(len(scores)):
        if score[i] > mx:
            mx = score[i]
            uns = i
    return name[uns]

def average(scores):
    sm = 0.0
    for i in scores:
        sm += i
    if len(score) > 0:
        return round(sm / len(score), 2)
    return 0.0
