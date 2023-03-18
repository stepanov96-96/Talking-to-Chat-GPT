import speech_recognition as sr
import pyttsx3
import openai


openai.api_key = ""


engine = pyttsx3.init()  # Используем русский голосовой движок

# Создание объекта Recognizer
r = sr.Recognizer()

# Определение источника звука (например, микрофона)
with sr.Microphone() as source:
    print("Скажите что-нибудь...")
    audio = r.listen(source)

# Распознавание речи
try:
    text = r.recognize_google(audio, language="ru-RU")
    print("Вы сказали: " + text)
except sr.UnknownValueError:
    print("Не удалось распознать речь")
except sr.RequestError as e:
    print("Ошибка запроса к сервису распознавания речи: {0}".format(e))


response = openai.Completion.create(
    model="text-davinci-003", # имя модели, которую вы хотите использовать
    prompt=text, # ваш запрос или вопрос
    temperature=0.5,
    max_tokens=1000, # максимальное количество токенов в ответе
    top_p=1.0,
    frequency_penalty = 0.5,
    presence_penalty = 0.0,

)


engine.say(response['choices'][0]['text'])
engine.runAndWait()
print("abesalom")