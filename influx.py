from influxdb import InfluxDBClient

client = InfluxDBClient(host = '167.71.158.245', port = 8086, username = 'shiny', password = 'metrics', database = "temperature")

print(client.query("SHOW MEASUREMENTS"))

