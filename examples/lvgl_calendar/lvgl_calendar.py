import lvgl as lv
import lv_utils
from st7789_lv import ST7789_lv
from machine import Pin, SPI

if not lv.is_initialized(): lv.init()
if not lv_utils.event_loop.is_running(): event_loop=lv_utils.event_loop()

lcd_spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
lcd_dc = Pin(11, Pin.OUT)
lcd_cs = Pin(12, Pin.OUT)
lcd_rst = Pin(10, Pin.OUT)
lcd_bl = Pin(13, Pin.OUT)

disp_drv = ST7789_lv(lcd_spi, lcd_rst, lcd_cs, lcd_dc, lcd_bl)

scr = lv.obj()

lv.screen_load(scr)

cal = lv.calendar(scr)
cal.align(lv.ALIGN.CENTER,0,0)
cal.set_size(180,180)

d = lv.calendar.add_header_dropdown(cal)