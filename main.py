# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

import matplotlib.pyplot as plt
import wave,numpy as np

from googletrans import Translator

translator = Translator()

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def ToEnglish(audio2):
    # Using google to recognize audio
    translated_text = r.recognize_google(audio2, language="ar-EG").lower()

    detection = translator.detect(translated_text)

    print(detection.lang)

    translation = translator.translate(translated_text, dest="en")
    print(translation.text)

    print("You said: " + translated_text)

    SpeakText(translated_text)


def ToArabic(audio2):
    # Using google to recognize audio
    translated_text = r.recognize_google(audio2, language="en-US").lower()

    detection = translator.detect(translated_text)

    print(detection.lang)

    translation = translator.translate(translated_text, dest="ar")
    print(translation.text)

    print("You said: " + translated_text)

    SpeakText(translated_text)

# Loop infinitely for user to speak
def speech():
    while 1:
        print("Talk with which language?\n1.Arabic (translates English)\n2.English (translates Arabic)\n")
        choice = int(input())
        # Exception handling to handle
        # exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for 3 seconds to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=3)

                print("Talk.....")
                # listens for the user's input
                audio2 = r.listen(source2)

                with open('speech.wav', 'wb') as f:
                    f.write(audio2.get_wav_data())
                    f.close()

                # Using google to recognize audio

                if choice == 1:
                    ToEnglish(audio2)

                else:
                    ToArabic(audio2)
                # reading the audio file
                raw = wave.open('speech.wav')

                # reads all the frames
                # -1 indicates all or max frames
                signal = raw.readframes(-1)
                signal = np.frombuffer(signal, dtype="int16")

                # gets the frame rate
                f_rate = raw.getframerate()

                # to Plot the x-axis in seconds
                # you need get the frame rate
                # and divide by size of your signal
                # to create a Time Vector
                # spaced linearly with the size
                # of the audio file
                time = np.linspace(
                    0,  # start
                    len(signal) / f_rate,
                    num=len(signal)
                )

                # using matlplotlib to plot
                # creates a new figure
                plt.figure(1)

                # title of the plot
                plt.title("Sound Wave")

                # label of x-axis
                plt.xlabel("Time")

                # actual ploting
                plt.plot(time, signal)

                # shows the plot
                # in new window
                plt.show()

                # you can also save
                # the plot using
                plt.savefig('printed_signal')

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("No words spoken")


if __name__ == "__main__":
    speech()
