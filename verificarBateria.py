import psutil

# Captura sensor da bateria
battery = psutil.sensors_battery()

# Captura percentual da bateria
percent = str(battery.percent)

# Mostra resultado
print(f'No momento você tem {percent}% de bateria!')
