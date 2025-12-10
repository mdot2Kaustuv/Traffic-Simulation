import random
from queue import Vehicle
import time

data_file = "Traffic.data"
LANES = ["A","B","C","D"]

def record (Vehicle) :
    with open(data_file, "a") as file:
        file.write(f"{Vehicle.lane},{Vehicle.id},{Vehicle.time}\n")

def generate_vehicle (delay = 2.0):
    while True :
        road = random.choice(LANES)
        vehicle_id = random.randint(1,10000)
        interval = random.expovariate(1.0 / delay)
        time.sleep(interval)
        return Vehicle(vehicle_id, road,interval)

def generator():
    while True:
        v=generate_vehicle()
        record(v)


generator()





