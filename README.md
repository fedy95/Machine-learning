Discipline "Intellectual systems and technologies".
---------------------------------------------------
1. KNN metric classifier.
  Dataset.txt - set of objects: coordinates of the dot(x,y),class{0,1}.
  
3). Число фолдов для кросс-валидации определите и обоснуйте сами исходя из числа объектов в датасете.
7). Можно попробовать несколько способов выбора k.
- Рандомный выбор для тестирования
4). Хотелось бы увидеть некоторую визуализацию данных.
- Разделение и раскраска границ точек
5). >= 2 пространственных преобразований,
- (рандомные, зависящие от x и y)
>= 2 Kernel fuctions (https://en.wikipedia.org/wiki/Kernel_(statistics))
- (Gaussian + Logistic)
>=2 метрики для настройки kNN (https://ru.wikipedia.org/wiki/%D0%95%D0%B2%D0%BA%D0%BB%D0%B8%D0%B4%D0%BE%D0%B2%D0%B0_%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B0 + https://en.wikipedia.org/wiki/Taxicab_geometry).
- (евклидово расстояние[p=2] + Manhattan[p=1])
6). Для настройки классификатора пока можно использовать метрику "accuracy". Очень хорошо, если вы сразу разберетесь с "F1-measure" и попробуете использовать её.
- Sensitivity or Recall + Specificity + Precision + Accuracy + 𝐹1-measure

8). писать какие-нибудь формулы и рисовать примеры при обосновании выборов.

разбиение по файлам
дерево

