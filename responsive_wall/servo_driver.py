#to do: add a scheduler

import serial

def servo_init(port_name):
	global com_port
	com_port = serial.Serial(port_name, 115200)
	
def servo_move_us(channel, value_us):
	if value_us < 1000 or  value_us > 2000:
		return
	
	temp_string = '#' + str(channel) + 'P' + str(value_us) + '\r'
	
	com_port.write(temp_string)
	
def servo_move_float(channel, value_float):
	if value_float < -1.0 or value_float > 1.0:
		return
	
	#map the float to the servo's pulse width
	value_us = (value_float+1) * 500 + 1000
	
	temp_string = '#' + str(channel) + 'P' + str(int(value_us)) + '\r'
	
	com_port.write(temp_string)
	

## not yet implemented
def servo_move_mm(channel, value_mm):
	return
