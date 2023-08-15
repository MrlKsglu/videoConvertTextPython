import moviepy.editor as mp #bir video üzerinde temel işlemleri gerçekleştirmek için kullanılır . Video düzenleme sürecinde kesme, metin ekleme, videoları birleştirme ve daha pek çok işlevi
import speech_recognition as sr #  konuşma tanıma modülü, konuşma ve ses dosyalarıyla etkileşim kurmanın kolay bir yolunu sağlar.


video = mp.VideoFileClip("C://Users//mkoseoglu//Desktop//hikaye.mp4") #video yükleme
audio_file = video.audio #audio özniteliğini kullanarak videodan sesi çıkarın
audio_file.write_audiofile("geeksforgeeks.wav") #'.mp4' dosyasını '.wav' dosyasına yazın.
# Initialize recognizer
r = sr.Recognizer()
file=sr.AudioFile("geeksforgeeks.wav")
# ses dosyasını döngü şeklinde al
with file as source:
    data = r.record(source)
    text = r.recognize_google(data,language='tr')
    print(text)

# sesi metne dönüştür
#text = r.recognize_google(data)

