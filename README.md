### Итоговый проект курса "Машинное обучение в бизнесе"

Стек:
1. ML: sklearn, pandas, numpy
2. API: flask

Данные: Статистика боев UFC, данные с kaggle - https://www.kaggle.com/rajeevw/ufcdata

Назначение сервиса: по данным по конкретному бою предсказать его результат.

Тип запроса: POST

Используемые признаки и пример передавемых в запросе данных:
{
    'index': [466],  # int 
    'B_current_win_streak': [0.0],  # float
    'B_draw': [0.0],  # float
    'B_avg_BODY_att': [5.8],  # float
    'B_avg_BODY_landed': [3.2],  # float
    'B_avg_CLINCH_att': [2.6],  # float
    'B_avg_CLINCH_landed': [2.4],  # float
    'B_avg_DISTANCE_att': [47.4]  # float
}

Модель: Random Forest (sklearn)
