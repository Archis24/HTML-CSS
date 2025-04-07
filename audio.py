import speech_recognition as sr
def speech():
    # Inicializamos el reconocedor de voz
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        print("Por favor, hable")
        
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        
        return recog.recognize_google(audio, language="es-ES")