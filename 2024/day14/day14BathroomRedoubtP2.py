import sys

HEIGHT = 103
WIDTH = 101
OUTPUT_FILE = "output.txt"

def checkSymmetrical(robots, robotMap):
    middle = (HEIGHT - 1) / 2
    for robot in robots:
        x2 = 2 * middle - robot["x1"]
        if robotMap.get((x2, robot["y1"]), 0) == 0:
            print("NotSym")
            return False
    return True
            

def printMap(robotMap):
    for i in range(0, HEIGHT):
        row = ""
        for j in range(0, WIDTH):
            numRobot = robotMap.get((j, i), ".")
            row += str(numRobot)
        print(row)
    print("")
    print("")
    
def saveMapToFile(robotMap, timeElapsed):
    with open(OUTPUT_FILE, "a") as file:  # Open the file in append mode
        for i in range(0, HEIGHT):
            row = ""
            for j in range(0, WIDTH):
                numRobot = robotMap.get((j, i), ".")
                row += str(numRobot)
            file.write(row + "\n")
        file.write("Seconds Elapsed: " + str(timeElapsed))
        file.write("\n\n")
    

def calculateFinalPos(x1, y1, deltaX, deltaY, elapsedTime):
    x2 = x1 + (deltaX * elapsedTime)
    y2 = y1 + (deltaY * elapsedTime)
    x2 = x2 % WIDTH
    y2 = y2 % HEIGHT
    
    return (x2, y2)
        
def processFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        robots = []
        robotMap = {}
        for line in lines:
            line = line.strip()
            
            # Split the line into components
            parts = line.split()
            
            # Extract and parse values for p
            p_values = parts[0].split('=')[1]  # Get the value after 'p='
            x1, y1 = map(int, p_values.split(','))  # Split into x1 and y1
            
            # Extract and parse values for v
            v_values = parts[1].split('=')[1]  # Get the value after 'v='
            deltaX, deltaY = map(int, v_values.split(','))  # Split into deltaX and deltaY

            robots.append({"x1":x1, "y1":y1, "deltaX":deltaX, "deltaY":deltaY}) 
            robotMap[(x1, y1)] = 1 + robotMap.get((x1, y1), 0)
    
    return robots, robotMap
        
def incrementTime(robots, numSeconds):
    robotMap = {}
    for robot in robots:
        x2, y2 = calculateFinalPos(robot["x1"], robot["y1"], robot["deltaX"], robot["deltaY"], numSeconds)
        # print(x2, y2)
        robot["x1"] = x2
        robot["y1"] = y2
        robotMap[(x2, y2)] = 1 + robotMap.get((x2, y2), 0)
    
    return robots, robotMap


def main():
    robots, robotMap = processFile(sys.argv[1])
    maxTime, h_pattern, v_pattern, lastCalculated = 10000, 33, 84, 0

    for second in range(0, maxTime):
        if second == h_pattern:
            robots, robotMap = incrementTime(robots, second - lastCalculated)
            saveMapToFile(robotMap, second)
            lastCalculated = second
            h_pattern += 103
        elif second == v_pattern:
            robots, robotMap = incrementTime(robots, second - lastCalculated)
            saveMapToFile(robotMap, second)
            lastCalculated = second
            v_pattern += 101
    
    
    # for second in range(0, totalTime):
    #     robots, robotMap = incrementTime(robots, 1)
    #     saveMapToFile(robotMap, second)
    #     # checkSymmetrical(robots, robotMap)
    

if __name__ == "__main__":
    main()