import re

def parse_line(inputline):
    sensor, beacon = inputline.split(':')
    sensor_x, sensor_y = re.findall(r'\d+', sensor)
    sensor_position = (int(sensor_x), int(sensor_y))
    beacon_x, beacon_y = re.findall(r'\d+', beacon)
    beacon_position = (int(beacon_x), int(beacon_y))

    return sensor_position, beacon_position

def solution(inputarray, y_value):

    beacons_in_y = set()
    x_in_sensor_range = set()

    # for each line - measure the Manhattan distance between the sensor and the beacon
    # for a given y, check if the x is within the range of the sensor

    for line in inputarray:
        sensor_position, beacon_position = parse_line(line)
        print(sensor_position, beacon_position)
        if beacon_position[1] == y_value:
            beacons_in_y.add(beacon_position[0])
        manhattan_distance = abs(sensor_position[0] - beacon_position[0]) + abs(sensor_position[1] - beacon_position[1])
        y_delta = abs(sensor_position[1] - y_value)
        x_range = (manhattan_distance - y_delta)
        # print(sensor_position, beacon_position, manhattan_distance, y_delta, x_range)
        if x_range >= 0:
            for x in range(sensor_position[0] - x_range, sensor_position[0] + x_range + 1):
                x_in_sensor_range.add(x)
        #         print(x, end=', ')
        #     print('')
        # print('')

    all_x = x_in_sensor_range - beacons_in_y

    # print(beacons_in_y)
    return len(all_x)




def solution2(inputarray):
    pass


if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()

    print(solution(inputarray, 2000000))
    print(solution2(inputarray))
