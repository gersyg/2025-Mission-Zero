from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

sense.color.gain = 60 
sense.color.integration_cycles = 64 

m = (34, 139, 34)
n = (154, 205, 50)
d = (100, 149, 237)
s = (139, 69, 19)
q = (255, 255, 0)

for i in range(25):
  rgb = sense.color
  c = (rgb.red, rgb.green, rgb.blue)

  image = [
   d, d, d, d, d, d, q, q,
    d, d, d, d, d, d, d, q,
    d, d, d, d, d, m, d, d,
    d, m, d, d, m, m, m, d,
    m, m, m, d, d, s, d, d,
    d, s, d, d, d, s, d, d,
    d, s, d, d, d, s, d, d,
    n, n, n, n, n, n, n, n]

  sense.set_pixels(image)
  sleep(1)

x = (178, 34, 34) 
sense.clear(x)
