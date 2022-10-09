Temperature = 0
kitronik_air_quality.set_time(16, 19, 0)
kitronik_air_quality.set_date(9, 10, 2022)
kitronik_air_quality.setup_gas_sensor()
kitronik_air_quality.calc_baselines()

def on_every_interval():
    kitronik_air_quality.measure_data()
    kitronik_air_quality.clear()
    kitronik_air_quality.show("Environment at: " + kitronik_air_quality.read_time())
    kitronik_air_quality.show("Temperature:  " + ("" + str(kitronik_air_quality.read_temperature(kitronik_air_quality.TemperatureUnitList.C))) + "°C",
        3)
    kitronik_air_quality.show("Pressure:     " + ("" + str(kitronik_air_quality.read_pressure(kitronik_air_quality.PressureUnitList.PA))) + " Pa",
        4)
    kitronik_air_quality.show("Humidity:     " + ("" + str(kitronik_air_quality.read_humidity())) + "    %",
        5)
    kitronik_air_quality.show("CO2:          " + ("" + str(kitronik_air_quality.reade_co2())) + "   ppm",
        6)
    kitronik_air_quality.show("IAQ:          " + ("" + str(kitronik_air_quality.get_air_quality_score())) + "    /500",
        7)
    kitronik_air_quality.show("IAQ:          " + ("" + str(kitronik_air_quality.get_air_quality_percent())) + "    %",
        8)
loops.every_interval(60000, on_every_interval)

def on_forever():
    global Temperature
    Temperature = kitronik_air_quality.read_temperature(kitronik_air_quality.TemperatureUnitList.C)
    if Temperature < 16:
        basic.show_leds("""
            # . # . #
                        . # # # .
                        # # # # #
                        . # # # .
                        # . # . #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . # # # .
                        . # . # .
                        . # # # .
                        # . . . #
        """)
basic.forever(on_forever)
