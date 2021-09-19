from influxdb import InfluxDBClient

client = InfluxDBClient(host = 'localhost', port = 8086, database = 'temperature')

res = client.query(query = "select * from room_temperature_humidity;", database = "temperature")

print(res)

