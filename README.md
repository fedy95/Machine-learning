Discipline "Intellectual systems and technologies"
---------------------------------------------------
Used software:
- Python-IDE: PyCharm Community 2017.2;
- Project Interpreter: python 3.5.3 (amd64);
- Used python packeges: matplotlib v2.1.0.
--------------------------------------------------- 
1. KNN metric classifier.
  Dataset.txt - set of objects: coordinates of the dot(x,y),class{0,1}.
  ---
Program structure:
- Main: started point.
- Plot:
	- buildPlotWithAllDots;
	- buildPlotCentroid;
	- buildPlotCircle.
- Statistic:
	- compareClasses;
	- computingRecall;
	- computingSpecificity;
	- computingPrecision;
	- computingAccuracy;
	- computingF1_measure.
- DatasetProcessing:
	- getDataset;
	- getDotsByClass;
	- getManhattanDistance;
	- getEuclideanDistance;
	- getCentroid;
	- classifyDotCentroid;
	- classifyDotCircle;
	- classifyKNNCentroid;
	- classifyKNNCircle.
 ---

Число фолдов для кросс-валидации определите и обоснуйте сами исходя из числа объектов в датасете.
Можно попробовать несколько способов выбора k.
- Рандомный выбор для тестирования
Хотелось бы увидеть некоторую визуализацию данных.
- Разделение и раскраска границ точек
- 2 Spatial coordinate transformations:
	- [elliptic paraboloid](https://en.wikipedia.org/wiki/Paraboloid#Elliptic_paraboloid);
	- [hyperbolic paraboloid](https://en.wikipedia.org/wiki/Paraboloid#Hyperbolic_paraboloid).
- 2 [Kernel fuctions](https://en.wikipedia.org/wiki/Kernel_(statistics)):
	- [Gaussian](https://en.wikipedia.org/wiki/Normal_distribution);
	- [Logistic](https://en.wikipedia.org/wiki/Logistic_distribution).
	
>=2 метрики для настройки kNN (https://ru.wikipedia.org/wiki/%D0%95%D0%B2%D0%BA%D0%BB%D0%B8%D0%B4%D0%BE%D0%B2%D0%B0_%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B0 + https://en.wikipedia.org/wiki/Taxicab_geometry).
- (евклидово расстояние[p=2] + Manhattan[p=1])
Для настройки классификатора пока можно использовать метрику "accuracy". Очень хорошо, если вы сразу разберетесь с "F1-measure" и попробуете использовать её.
- Sensitivity or Recall + Specificity + Precision + Accuracy + 𝐹1-measure

писать какие-нибудь формулы и рисовать примеры при обосновании выборов.

- (+-)разбиение по файлам
- дерево

