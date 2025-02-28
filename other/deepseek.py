import requests
import json


def get_response(prompt, api_key):
    # Установите базовый URL и параметры запроса
    base_url = "https://api.deepseek.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Настройки запроса
    data = {
        "model": "deepseek-chat",  # Модель, которую вы хотите использовать
        "prompt": prompt,
        "max_tokens": 2048,  # Максимальное количество токенов в ответе
        "temperature": 0.7,  # Температура ответа (0.0 - 1.0)
        "top_p": 1,  # Вероятность ответа (0.0 - 1.0)
        "frequency_penalty": 0.0,  # Штраф за частоту повторов
        "presence_penalty": 0.0  # Штраф за присутствие повторов
    }

    # Отправка запроса
    response = requests.post(base_url, headers=headers, data=json.dumps(data))

    # Обработка ответа
    if response.status_code == 200:
        result = response.json()
        return result.get("choices", [{}])[0].get("text", "")
    else:
        return f"Ошибка: {response.status_code}"


def main():
    api_key = ""

    while True:
        prompt = input("Введите ваш вопрос или сообщение: ")
        if prompt.lower() == "exit":
            break

        response = get_response(prompt, api_key)
        print("Ответ:", response)


if __name__ == "__main__":
    main()
