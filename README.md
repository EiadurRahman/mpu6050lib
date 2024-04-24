# MicroPython Library: MPU6050

This library facilitates communication with the MPU6050 sensor, which combines an accelerometer and a gyroscope. It enables easy initialization of the sensor, reading accelerometer and gyroscope data, and performing various tasks on MicroPython-based microcontroller boards.

## Installation
1. Ensure your MicroPython environment is set up on your microcontroller board.
2. Copy the `mpu6050.py` file to your project directory.
   or,
run this script,(Internet required)

```python
import mip
mip.install('https://raw.githubusercontent.com/EiadurRahman/mpu6050lib/main/mpu6050.py')
```

## Usage

```python
from machine import I2C, Pin
from mpu6050 import MPU6050

# Initialize I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))

# Create an instance of MPU6050
mpu = MPU6050(i2c)

# Initialize the MPU6050 sensor
mpu.init()

# Read accelerometer data
accel_data = mpu.get_accel()

# Read gyroscope data
gyro_data = mpu.get_gyro()

print("Accelerometer data:", accel_data)
print("Gyroscope data:", gyro_data)
```

## API Reference

### `MPU6050(i2c, addr=0x68, lsbg=16384.0, lsbds=131.0)`

- `i2c`: An instance of the `machine.I2C` class representing the I2C bus.
- `addr`: The I2C address of the MPU6050 sensor (default is `0x68`).
- `lsbg`: The LSB (Least Significant Bit) sensitivity for the accelerometer (default is `16384.0`).
- `lsbds`: The LSB sensitivity for the gyroscope (default is `131.0`).

### `init()`

Initialize the MPU6050 sensor.

### `get_accel()`

Read and return accelerometer data as a list `[x, y, z]` where `x`, `y`, and `z` are the acceleration values in G-force.

### `get_gyro()`

Read and return gyroscope data as a list `[x, y, z]` where `x`, `y`, and `z` are the angular velocity values in degrees per second.

## Contributions

Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or create a pull request on GitHub.
