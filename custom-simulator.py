from time import sleep
from clint.textui import colored
from yamcs.client import YamcsClient
import csv

yamcs_address = "localhost:8090"
plant_name = "roverlocation"
plant_str = "/" + plant_name + "/"
client = YamcsClient(yamcs_address)
processor = client.get_processor(instance=plant_name, processor='realtime')

telemetry_file_path = 'rover_mock_path.csv'
sleep_duration = 3

def initializeParameters(latitude, longitude):
    try:
        print(colored.cyan("\n* * Attempting to set parameters * *\n"))
        print('Latitude: ' + latitude)
        print('Longitude: ' + longitude)
        processor.set_parameter_value(plant_str + "Rover_Latitude", float(latitude))
        processor.set_parameter_value(plant_str + "Rover_Longitude", float(longitude))
        print(colored.green("\n* * Latitude and Logitude have been set. * *\n"))
    except:
        print(colored.magenta("\nError: Failed to set parameters.\n\n\n"))

def read_from_file(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        num_rows = len(list(csv_reader))
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            if line_count == 1:
                line_count += 1
            elif line_count == num_rows:
                initializeParameters(row[0], row[1])
                sleep(sleep_duration)
                print(colored.magenta("\n* * Reading file from start. * *\n"))
                read_from_file(path)
            else:
                line_count += 1
                initializeParameters(row[0], row[1])
                sleep(sleep_duration)

if __name__ == "__main__":
    print(colored.magenta("\n* * Starting Program... * *\n"))
    read_from_file(telemetry_file_path)
