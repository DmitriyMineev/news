import streamlit as st



st.title('Запрос без знаков препинания ухудшает точность нейросетей до 20%')
st.image('images/1.jpg')

st.write('Ученые из Института искусственного интеллекта AIRI выяснили, что отсутствие знаков препинания в запросах снижает точность работы языковых моделей до 20%. Исследование показало, что грамотное составление запросов существенно улучшает функционирование чат-ботов и виртуальных помощников. Такие элементы языка, как пунктуация и артикли, обычно считающиеся малозначимыми, критически важны для обработки информации нейросетями. Модели рассматривают текст как набор токенов, среди которых важно выделить ключевые для понимания контекста.')
st.write('В рамках эксперимента исследователи проверяли способность модели восстанавливать оригинальный текст на основе последовательности токенов, включая знаки препинания, артикли и стоп-слова, которые сами по себе могут быть несущественными. К стоп-словам относятся, например, служебные части речи: союзы, предлоги, частицы. Было установлено, что наибольший объем полезной информации о контексте содержится именно в стоп-словах. Аналогичные эксперименты проводились на тестах MMLU и BABILong, оценивающих возможности языковых моделей. При удалении элементов, которые считаются несущественными для восприятия текста, производительность системы заметно падала.')