import RPi.GPIO as GPIO
import time
import socket

# Configuration des broches GPIO pour les moteurs
GPIO.setmode(GPIO.BCM)
pin_motor1_avancer = 17  # PWM pour la vitesse du moteur A
pin_motor1_reculer = 27  # Contrôle de direction du moteur A
pin_motor2_avancer = 18  # PWM pour la vitesse du moteur B
pin_motor2_reculer = 23  # Contrôle de direction du moteur B

# Configuration des broches pour les capteurs
ldr_pin = 5  # Capteur de lumière LDR
trigger_pin = 6  # Trigger du capteur ultrason
echo_pin = 13  # Echo du capteur ultrason
light_threshold = 700
sonar_threshold = 200

# Initialisation des GPIO
GPIO.setup(pin_motor1_avancer, GPIO.OUT)
GPIO.setup(pin_motor1_reculer, GPIO.OUT)
GPIO.setup(pin_motor2_avancer, GPIO.OUT)
GPIO.setup(pin_motor2_reculer, GPIO.OUT)
GPIO.setup(ldr_pin, GPIO.IN)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

# Initialisation des PWM pour les moteurs
pwm_motor1 = GPIO.PWM(pin_motor1_avancer, 100)
pwm_motor2 = GPIO.PWM(pin_motor2_avancer, 100)
pwm_motor1.start(0)
pwm_motor2.start(0)

def avancer(vitesse=100):
    GPIO.output(pin_motor1_reculer, GPIO.LOW)
    GPIO.output(pin_motor2_reculer, GPIO.LOW)
    pwm_motor1.ChangeDutyCycle(vitesse)
    pwm_motor2.ChangeDutyCycle(vitesse)
    print("Le robot avance")

def reculer(vitesse=100):
    GPIO.output(pin_motor1_avancer, GPIO.LOW)
    GPIO.output(pin_motor2_avancer, GPIO.LOW)
    pwm_motor1.ChangeDutyCycle(vitesse)
    pwm_motor2.ChangeDutyCycle(vitesse)
    print("Le robot recule")

def arreter():
    pwm_motor1.ChangeDutyCycle(0)
    pwm_motor2.ChangeDutyCycle(0)
    print("Le robot s'arrête")

def sonar_ping():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()
    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Vitesse du son en cm/s
    return distance

# Socket setup pour écouter les commandes
serveur
