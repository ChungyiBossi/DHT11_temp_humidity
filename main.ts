basic.forever(function () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    true,
    true
    )
    led.plotBarGraph(
    dht11_dht22.readData(dataType.humidity),
    100
    )
    led.plotBarGraph(
    dht11_dht22.readData(dataType.temperature),
    100
    )
})
