"""
This script runs the Speech_to_Braille application using a development server.
"""

from os import environ
from Speech_to_Braille import TextToBraille

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
