#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
green_led = 17 #it will flash when there is a '.'
red_led = 27 #it will flash when there is a '-'
#Both will flash when there is an space ' '

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)


MORSE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

def toUpperCase(lowerString):
        upperString=''
        for i in lowerString:
                upperString = upperString + i.upper()
        return upperString

def characterToMorse(character):
        morseCharacter = ''
        for char in MORSE:
                if char == character:
                        return MORSE[char]

def toMorse(string):
        morseString = ''
        upperString = toUpperCase(string)
        for i in upperString:
                morseString = morseString + characterToMorse(i)
        return morseString

def morseToLight(string):
        morseString = toMorse(string)
        for character in morseString:
                if character == '.':
                        print '.'
                        GPIO.output(green_led, True)
                        sleep(1)
                        GPIO.output(green_led, False)
                        sleep(1)
                elif character == '-':
                        print '-'
                        GPIO.output(red_led, True)
                        sleep(1)
                        GPIO.output(red_led, False)
                        sleep(1)
                elif character == ' ':
                        print ' '
                        GPIO.output(red_led, True)
                        GPIO.output(green_led, True)
                        sleep(1)
                        GPIO.output(red_led, False)
                        GPIO.output(green_led, False)
                        sleep(1)

def clean():
	GPIO.cleanup()
