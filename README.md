# ScattaFoto_withButton_Rpi
Scattare una foto premendo un bottone con la Pi Camera

FASE PRELIMINARE

Aggiorniamo Raspberry Pi OS con i comandi

`sudo apt-get update
sudo apt-get upgrade`

INSTALLAZIONE RASPBERRY PI CAMERA

Ho scritto una guida approfondito a riguardo, per leggerla potete utilizzare il seguente link: Come installare e configurare la Raspberry Pi Camera

DIAGRAMMA DI COLLEGAMENTO

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2021/08/Fritzing-screenshot-of-button-connected-to-gpio-4-and-gnd-of-Rpi-3.gif?resize=793%2C610)

clicca [QUI](https://github.com/SimoneMoreWare/ScattaFoto_withButton_Rpi/blob/main/buttonPhoto.py) per il codice

SPIEGAZIONE CODICE

Importiamo le varie librerie

`from gpiozero import Button 
from picamera import PiCamera 
from signal import pause
 
import time`

Inizializziamo la Raspberry Pi Camera

`camera = PiCamera()`

Definiamo la funzione take_picture_with_camera() che permetterà di acquisire le immagini e salvarle nella cartella “image”

`def take_picture_with_camera(): 
   image_path = '/home/pi/images/image_%s.jpg' % int(round(time.time() * 1000)) 
   camera.capture(image_path) 
   print('Took photo')`
   
nella variabile button inseriamo lo stato del bottone inserito nell’ingresso GPIO numero 4

`button = Button(4)`

Quando premo il bottone viene chiamata la funzione take_picture_with_camera()

`button.when_pressed = take_picture_with_camera`

TEST

Esegui il codice, premi il bottone, vai nella cartella ‘image’ e vedrai le tue fotografie scattate.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2021/08/connect-camera.jpg?w=1000&ssl=1)
