# used to periodically truncate the log file being created
# Writes the file with 0 bytes
# This does not interfere with continuous writing values to the file
truncate -s 0 temperature.log