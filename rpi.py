import time

def export_gpio(gpio):
    open('/sys/class/gpio/export', 'w').write(str(gpio)).close()

def unexport_gpio(gpio):
    open('/sys/class/gpio/unexport', 'w').write(str(gpio)).close()

def init_gpio(gpio):
    unexport(gpio)
    export(gpio)

def set_gpio_to(gpio, mode):
    path = '/sys/class/gpio/gpio' + gpio + '/direction'
    f = open(path, 'w')
    f.write(mode)
    f.close()

def set_gpio_to_out(gpio):
    set_gpio_to(gpio, 'out')

def set_gpio_to_in(gpio):
    set_gpio_to(gpio, 'in')

gpios = [17, 27, 22]
for gpio in gpios:
    init_gpio(gpio)
init_gpio(20)

for gpio in gpios:
    set_gpio_to_out(gpio)
set_gpio_to_in(20)

# Loop through LED 'ON' and 'OFF' for the number of times specified
i = 0
prev_state = 0
current_state = 0
while True:
    path = '/sys/class/gpio/gpio' + gpios[i] + '/value'
    prev_state = current_state
    f = open(path, 'r')
    current_state = f.read(1) - '0'
    f.close()
    # OnButtonPressed
    if current_state == 1 and current_state != prev_state:
        open('/sys/class/gpio/gpio' + i + '/value', 'w').write('0').close()
        i = (i + 1) % 3
    open('/sys/class/gpio/gpio20/value', 'w').write('1').close()
    time.sleep(0.005)

for gpio in gpios:
    unexport_gpio(gpio)
unexport_gpio(20)

