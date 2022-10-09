let Temperature = 0
kitronik_air_quality.setTime(16, 19, 0)
kitronik_air_quality.setDate(9, 10, 2022)
kitronik_air_quality.setupGasSensor()
loops.everyInterval(60000, function () {
    kitronik_air_quality.measureData()
    kitronik_air_quality.clear()
    kitronik_air_quality.show("Environment" + kitronik_air_quality.readTime())
    kitronik_air_quality.show("Tmp:  " + ("" + kitronik_air_quality.readTemperature(kitronik_air_quality.TemperatureUnitList.C)) + "°C", 3)
    kitronik_air_quality.show("Press:" + ("" + kitronik_air_quality.readPressure(kitronik_air_quality.PressureUnitList.Pa)) + " Pa", 4)
    kitronik_air_quality.show("Hum:  " + ("" + kitronik_air_quality.readHumidity()) + "    %", 5)
    kitronik_air_quality.show("CO2:  " + ("" + kitronik_air_quality.readeCO2()) + "   ppm", 6)
    kitronik_air_quality.show("IAQ:  " + ("" + kitronik_air_quality.getAirQualityPercent()) + "    %", 7)
})
basic.forever(function () {
    Temperature = kitronik_air_quality.readTemperature(kitronik_air_quality.TemperatureUnitList.C)
    if (Temperature >= 16) {
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
    } else {
        basic.showLeds(`
            # . . . #
            . # # # .
            . # . # .
            . # # # .
            # . . . #
            `)
    }
})
