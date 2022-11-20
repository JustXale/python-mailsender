from vosk import Model, KaldiRecognizer
import sys
import queue
import pyttsx3

model = Model('models/en-us')
q = queue.Queue()


def callback(in_data, frames, time, status):
    if status:
        print(status, file=sys.std.error)

    q.put(bytes(in_data))



def init():
    while True:
        pass


if __name__ == "__main__":
    init()
