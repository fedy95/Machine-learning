Discipline "Intellectual systems and technologies"
---------------------------------------------------
Used software:
- Python-IDE: PyCharm Community 2017.2;
- Project Interpreter: python 3.5.3 (amd64);
- Used python packeges:
	- matplotlib v2.1.0;
	- tabulate v0.8.1.
--------------------------------------------------- 
1. KNN metric classifier.
  Dataset.txt - set of objects: coordinates of the dot(x,y),class{0,1}.
  ---
Program structure:
- Main: started point.
- OutputMethods:
	- outputTable.
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
	- computingManhattanDistance2D;
	- computingManhattanDistance3D;
	- computingEuclideanDistance2D;
	- computingEuclideanDistance3D;
	- getCentroid;
	- classifyDotCentroid;
	- classifyDotCircle;
	- classifyKNNCentroid;
	- classifyKNNCircle.
 ---
Output table
 ---
| Group number | Training dots | Test dots | k (neighbors) | Kernel functions | Metrics for configuring kNN | Spatial coordinate transformations | F1-measure | Recall | Specificity | Precision | Accuracy |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | | |5| none | manhattan | none | | | | | |
| | | |5| gaussian | manhattan | none | | | | | |
| | | |5| logistic | manhattan | none | | | | | |
| | | |5| none | euclidean | none | | | | | |
| | | |5| gaussian | euclidean | none | | | | | |
| | | |5| logistic | euclidean | none | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|-|
| | | |5| none | manhattan | elliptic | | | | | |
| | | |5| gaussian | manhattan | elliptic | | | | | |
| | | |5| logistic | manhattan | elliptic | | | | | |
| | | |5| none | euclidean | elliptic | | | | | |
| | | |5| gaussian | euclidean | elliptic | | | | | |
| | | |5| logistic | euclidean | elliptic | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|-|
| | | |5| none | manhattan | hyperbolic | | | | | |
| | | |5| gaussian | manhattan | hyperbolic | | | | | |
| | | |5| logistic | manhattan | hyperbolic | | | | | |
| | | |5| none | euclidean | hyperbolic | | | | | |
| | | |5| gaussian | euclidean | hyperbolic | | | | | |
| | | |5| logistic | euclidean | hyperbolic | | | | | |

- 2 [Spatial coordinate transformations](https://en.wikipedia.org/wiki/Paraboloid):
	- [elliptic paraboloid](https://en.wikipedia.org/wiki/Paraboloid#Elliptic_paraboloid);
	- [hyperbolic paraboloid](https://en.wikipedia.org/wiki/Paraboloid#Hyperbolic_paraboloid).
- 2 [Kernel functions](https://en.wikipedia.org/wiki/Kernel_(statistics)):
	- [gaussian](https://en.wikipedia.org/wiki/Normal_distribution);
	- [logistic](https://en.wikipedia.org/wiki/Logistic_distribution).
- 2 Metrics for configuring kNN:
	- [manhattan distance (p=1)](https://en.wikipedia.org/wiki/Taxicab_geometry);
	- [euclidean distance (p=2)](https://en.wikipedia.org/wiki/Euclidean_distance).
- Quality assessment:
	- [Sensitivity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity#Sensitivity) or [Recall](https://en.wikipedia.org/wiki/Precision_and_recall#Recall);
	- [Specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity#Specificity);
	- [Precision](https://en.wikipedia.org/wiki/Precision_and_recall#Precision);
	- [Accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision);
	- [F1-measure](https://en.wikipedia.org/wiki/F1_score).


Tasks:
- добавить пространственные преобразования
- Число фолдов для кросс-валидации определите и обоснуйте сами исходя из числа объектов в датасете.
- Можно попробовать несколько способов выбора k.
	- Рандомный выбор для тестирования
- Хотелось бы увидеть некоторую визуализацию данных.
	- Разделение и раскраска границ точек
- дерево

писать какие-нибудь формулы и рисовать примеры при обосновании выборов.

[Info](https://github.com/flyingleafe/ML-Course-ITMO/blob/master/Homework.org):

