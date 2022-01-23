#!/bin/sh
sudo python3 micha9.py --led-rows=32 --led-chain=2 --led-cols=64 --led-slowdown-gpio=4 --led-show-refresh --led-chain=2 --led-pwm-bits=11 --led-gpio-mapping=adafruit-hat-pwm --led-pixel-mapper="PiPong"
