from random import randint


def stepModel(generator, processor, countTasks, repeatProbability, step):
    tasksDone = 0
    timeCurrent = step
    timeGenerated = generator.generate()
    timeGeneratedPrev = 0
    timeProcessed = 0

    curQueueLen = 0
    maxQueueLen = 0
    free = True


    while tasksDone < countTasks:
        # Генератор
        if timeCurrent > timeGenerated:
            curQueueLen += 1

            if curQueueLen > maxQueueLen:
                maxQueueLen = curQueueLen
            
            timeGeneratedPrev = timeGenerated
            timeGenerated += generator.generate()

        # Обработчик
        if timeCurrent > timeProcessed:
            if curQueueLen > 0:
                wasFree = free

                if free:
                    free = False
                else:
                    tasksDone += 1
                    curQueueLen -= 1

                    if randint(1, 100) <= repeatProbability:
                        curQueueLen += 1

                if wasFree:
                    timeProcessed = timeGeneratedPrev + processor.generate()
                else:
                    timeProcessed += processor.generate()
            else:
                free = True

        timeCurrent += step

    return maxQueueLen
