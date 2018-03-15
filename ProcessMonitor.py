import psutil

# This script is intended to profile memory consumption of the process till process is alive.

# Process name to monitor.
procName = input("Please set process name: ")

# Base loop here we look for the process.
sleepTime = 0.1
isProcStarted = False
isProcFinished = False
memoryMeasurements = []
while True:
    # Get existing processes list
    pids= psutil.pids()
    isProcFoundOnCurrentIteration = False
    # Check existence of the target process
    for pid in pids:
        try:
            # Here we use try approach since process can be closed after collecting pids
            if (procName == psutil.Process(pid).name()):
                # Process is found.
                isProcFoundOnCurrentIteration = True
                if not isProcStarted:
                    print("Process is found. Collecting started")
                    isProcStarted = True

                currentMemory = psutil.Process(pid).memory_info().rss / (1024 * 1024)
                memoryMeasurements.append(currentMemory)
                print("The current memory consumption (MB): ", memoryMeasurements[-1])
        except:
            pass
    # Check stop criterion: counting is started and target process is not found.
    if (isProcStarted and not isProcFoundOnCurrentIteration):
        isProcFinished = True

    if (isProcFinished):
        print("Collecting is stopped")
        minimalConsumption = 1.0e100
        middleMemoryConsuption = 0.0
        maximalMemoryConstumption = 0.0
        for value in memoryMeasurements:
            if (value > maximalMemoryConstumption):
                maximalMemoryConstumption = value
            if (value < minimalConsumption):
                minimalConsumption = value
            middleMemoryConsuption += value
        middleMemoryConsuption /= len(memoryMeasurements)
        print("=========================================================")
        print("The minimal memory consumption (MB): ", minimalConsumption)
        print("The middle  memory consumption (MB): ", middleMemoryConsuption)
        print("The maximal memory consumption (MB): ", maximalMemoryConstumption)
        break
