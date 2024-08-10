from random import randint


def eventModel(generator, processor, countTasks, repeatProbability):
    tasksDone = 0
    curQueueLen = 0
    maxQueueLen = 0
    free = True
    processFlag = False
    events = [[generator.generate(), "g"]]

    while tasksDone < countTasks:
        event = events.pop(0)

        # Генератор
        if event[1] == "g":
            curQueueLen += 1

            if curQueueLen > maxQueueLen:
                maxQueueLen = curQueueLen

            addEvent(events, [event[0] + generator.generate(), "g"])

            if free:
                processFlag = True

        # Обработчик
        elif event[1] == "p":
            tasksDone += 1

            if randint(1, 100) <= repeatProbability:
                curQueueLen += 1

            processFlag = True

        if processFlag:
            if curQueueLen > 0:
                curQueueLen -= 1
                addEvent(events, [event[0] + processor.generate(), "p"])
                free = False
            else:
                free = True
                
            processFlag = False

    return maxQueueLen


def addEvent(events: list, event: list):
    i = 0
    while i < len(events) and events[i][0] < event[0]:
        i += 1

    if 0 < i < len(events):
        events.insert(i - 1, event)
    else:
        events.insert(i, event)
