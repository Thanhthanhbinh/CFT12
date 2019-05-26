import urllib.request
import pyglet

urllib.request.urlretrieve('https://www.youtube.com/watch?v=K2b_Vk132_I', 'Call Me Devil (Lucifer Soundtrack) - Friends in Tokyo.mp3')
a= pyglet.media. load ('K.wav')
a.play()