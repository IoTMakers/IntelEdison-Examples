import pyupm_i2clcd as lcd
import pyupm_grove
import time

lcd_display = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcd_display.setColor(0, 0,255)
lcd_display.setCursor(0, 0)
lcd_display.write ('#IntelMaker 2015 ')

lcd_display.setCursor(1, 0)
lcd_display.write ('IoT Green')

temperature = pyupm_grove.GroveTemp(0)
print(temperature)

