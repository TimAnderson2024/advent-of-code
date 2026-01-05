import sys

def calculateFinalPos(x1, y1, deltaX, deltaY, elapsedTime, height, width):
    x2 = x1 + (deltaX * elapsedTime)
    y2 = y1 + (deltaY * elapsedTime)
    x2 = x2 % width
    y2 = y2 % height
    
    print(x2, y2)
    return (x2, int(y2))
        
def processFile(filename):
    time = 100
    height = 103
    width = 101
    q1, q2, q3, q4 = 0, 0, 0, 0
    with open(filename, 'r') as file:
        lines = file.readlines()

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

            # Print the results for each line
            print(f"x1 = {x1}, y1 = {y1}, deltaX = {deltaX}, deltaY = {deltaY}")
        
            x2, y2 = calculateFinalPos(x1, y1, deltaX, deltaY, time, height, width)
            xBound = width // 2
            yBound = height // 2
            if x2 < xBound and y2 < yBound:
                q1 += 1
            elif x2 > xBound and y2 < yBound:
                q2 += 1
            elif x2 < xBound and y2 > yBound:
                q3 += 1
            elif x2 > xBound and y2 > yBound:
                q4 += 1
        print(q1 * q2 * q3 * q4)
                

def main():
    processFile(sys.argv[1])
    

if __name__ == "__main__":
    main()