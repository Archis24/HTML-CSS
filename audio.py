import speech_recognition as sr

mic = sr.Microphone()
recog = sr.Recognizer()

with mic as audio_file:
    print("Por favor, hable")
    
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    
    print("Conversión de voz a texto...")
    print("Usted dijo: " + recog.recognize_google(audio, language="es-ES"))