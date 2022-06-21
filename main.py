溫濕度 = 0
Matrix.enable_interrupt(BaudRate.BAUD_RATE115200)

def on_forever():
    global 溫濕度
    溫濕度 += 1
    # Matrix.dread(0)
    basic.show_string("" + str(Matrix.read_adc(.0)))
    led.plot_bar_graph(溫濕度, 100)
    basic.pause(200)
basic.forever(on_forever)
Matrix.read_adc(.0)