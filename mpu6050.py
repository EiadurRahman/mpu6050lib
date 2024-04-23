from machine import I2C, Pin
from time import sleep

class MPU6050:
    def __init__(self, i2c, addr=0x68,lsbg = 16384.0,lsbds = 131.0):
        self.i2c = i2c
        self.ADDR = addr
        self.PWR_MGMT_1 = 0x6B
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_XOUT_L = 0x3C
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_YOUT_L = 0x3E
        self.ACCEL_ZOUT_H = 0x3F
        self.ACCEL_ZOUT_L = 0x40
        self.GYRO_XOUT_H = 0x43
        self.GYRO_XOUT_L = 0x44
        self.GYRO_YOUT_H = 0x45
        self.GYRO_YOUT_L = 0x46
        self.GYRO_ZOUT_H = 0x47
        self.GYRO_ZOUT_L = 0x48
        self.LSBG = lsbg
        self.LSBDS = lsbds

    def init(self):
        self.i2c.writeto_mem(self.ADDR, self.PWR_MGMT_1, bytes([0]))

    def combine_register_values(self, h, l):
        if not h[0] & 0x80:
            return h[0] << 8 | l[0]
        return -((h[0] ^ 255) << 8) |  (l[0] ^ 255) + 1
    

    def get_accel(self):
        accel_x_h = self.i2c.readfrom_mem(self.ADDR, self.ACCEL_XOUT_H, 1)
        accel_x_l = self.i2c.readfrom_mem(self.ADDR, self.ACCEL_XOUT_L, 1)
        accel_y_h = self.i2c.readfrom_mem(self.ADDR, self.ACCEL_YOUT_H, 1)
        accel_y_l = self.i2c.readfrom_mem(self.ADDR, self.ACCEL_YOUT_L, 1)
        accel_z_h = self.i2c.readfrom_mem(self.ADDR, self.ACCEL_ZOUT_H, 1)
        accel_z_l = self.i2c.readfrom_mem(self.ADDR, self.ACCEL_ZOUT_L, 1)
        
        return [self.combine_register_values(accel_x_h, accel_x_l) / self.LSBG,
                self.combine_register_values(accel_y_h, accel_y_l) / self.LSBG,
                self.combine_register_values(accel_z_h, accel_z_l) / self.LSBG]

    def get_gyro(self):
        gyro_x_h = self.i2c.readfrom_mem(self.ADDR, self.GYRO_XOUT_H, 1)
        gyro_x_l = self.i2c.readfrom_mem(self.ADDR, self.GYRO_XOUT_L, 1)
        gyro_y_h = self.i2c.readfrom_mem(self.ADDR, self.GYRO_YOUT_H, 1)
        gyro_y_l = self.i2c.readfrom_mem(self.ADDR, self.GYRO_YOUT_L, 1)
        gyro_z_h = self.i2c.readfrom_mem(self.ADDR, self.GYRO_ZOUT_H, 1)
        gyro_z_l = self.i2c.readfrom_mem(self.ADDR, self.GYRO_ZOUT_L, 1)
        
        return [self.combine_register_values(gyro_x_h, gyro_x_l) / self.LSBDS,
                self.combine_register_values(gyro_y_h, gyro_y_l) / self.LSBDS,
                self.combine_register_values(gyro_z_h, gyro_z_l) / self.LSBDS]

# Example usage:
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# mpu = MPU6050(i2c)
# mpu.init()
# while True:
#     accel_data = mpu.get_accel()
#     gyro_data = mpu.get_gyro()
#     print("Accelerometer:", accel_data)
#     print("Gyroscope:", gyro_data)
#     sleep(1)

