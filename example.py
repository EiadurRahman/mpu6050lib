from mpu6050 import MPU6050
from machine import I2C,Pin
import time

if __name__ == "__main__":
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    mpu = MPU6050(i2c)
    while True:
        x = round(mpu.get_gyro()[0],1)
        y = round(mpu.get_gyro()[1],1)
        z = round(mpu.get_gyro()[2],1)
        print("X : {} | Y : {} | Z : {}".format(x,y,z))
        time.sleep(.1)
