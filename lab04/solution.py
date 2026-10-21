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

def ranking(name, scores):
    results = [(x,y) for x,y in zip(name, scores)]
    results = sorted(results, reverse = true)
    uns = [i[0] for i in results]
    return uns

def above_average(name, scores):
    sr = aversge(scores)
    uns = []
    results = [(x,y) for x,y in zip(name, scores)]
    for i in results:
        if i[1] > sr:
            uns.append(i[0])
    return uns


if __name__ == '__main__':
    print(winner(names,scores))
    print(average(scores))
    print(ranking(names, scores))
    print(above_average(names, scores))
