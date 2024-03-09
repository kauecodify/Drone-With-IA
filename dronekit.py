#pip install dronekit
#pip install pymavlink

def connect_to_drone();
    connect_to_drone
    connection_string = 'udp:127.0.0.1:14550'
    vehicle = conect(connection_string, wait_ready=True)
    return vehicle

#ship 
def enviar_para_local(vehicle, lat, lon, alt):
    location = LocationGlobalRelative(lat, lon, alt)
    vehicle.simple_goto(location)
    while True:

#verify ship
    atual = vehicle.location.global_relative_frame
    distancia = get_distance_metres(atual.lat, atual.lon, lat, lon)
    if distancia <1.000: # 1 metro de distância da proxima entrega
        break
    time.sleep(1)

#pegar obj
    def pegar_objeto(vehicle, altitude):
#altitude desejada
    vehicle.simple_takeoff(altitude)
    while True:
#verify alt
        if vehicle.location.global_relative_frame.alt >= altitude * 0.75:
            break
        time.sleep(1)

#connect
        def main()
            drone = connect_to_drone()
            
            destino_lat = 37.0
            desstino_lon = -122.0
            destino_alt = 1.000 #alt in meters

#ship
enviar_para_local(drone, destino_lat, destino_lon, destino_alt)

#pegar obj
altura_objeto = 0.25 #in meters
pegar_objeto(drone, altura_objeto)

#return
if __modeldrone__ == "__main__":
    main()