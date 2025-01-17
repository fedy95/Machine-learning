# KNN metric classifier
[Table of contents](https://github.com/fedy95/MachineLearning/blob/master/README.md)

## Used software:
- Python-IDE: PyCharm Community 2017.2;
- Project Interpreter: python 3.5.3 (amd64);
- Used python packeges:
	- matplotlib v2.1.0;
	- tabulate v0.8.1.

### Problem
1) Implement the metric classifier kNN;
2) Make cross-validation; justify the choice of the number of folds for it;
3) Perform data visualization;
4) Configure the classifier with 2-3 metrics and 2-3 spatial transformations;
5) To assess the quality, you can use the *Accuracy* metric, but better - *F1-measure*;

### Start dataset
[Dataset.txt](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/dataset.txt) - sample of objects: coordinates of the dot(x,y),class{0,1}.

### Program structure
- [Plot](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/Plot.py):
	- buildPlotWithAllDots;
	- buildPlotCentroid;
	- buildPlotCircle.
- [Statistic](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/Statistic.py):
	- compareClasses;
	- computingRecall;
	- computingSpecificity;
	- computingPrecision;
	- computingAccuracy;
	- computingF1_measure.
- [DatasetProcessing](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/DatasetProcessing.py):
	- getDataset;
	- getTrainTestDots;
	- getDotsByClass;
	- computingManhattanDistance2D;
	- computingManhattanDistance3D;
	- computingEuclideanDistance2D;
	- computingEuclideanDistance3D;
	- getCentroid;
	- classifyDotCentroid;
	- classifyDotCircle;
	- classifyKNNCentroid;
	- classifyKNNCircle;
	- getTrainTestDots.
- *presentation files*:
	- [output_mesh](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/output_mesh.py);
	- [output_table](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/output_table%20(all%20vars%20fixed).py) (all vars fixed);
	- [output_table](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/output_table%20(k_fold%20cycle).py) (k_fold cycle).
	
### Output table (one of the best result) 
#### *[presentation files -> output_table (all vars fixed)]*
| Training dots | Test dots | k_neighbors | k_fold | Kernel functions | Metrics for configuring kNN | Spatial coordinate transformations | F1-measure | Recall | Specificity | Precision | Accuracy |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|30|88|10|1| none | manhattan | none |0,76087|0,833333|0,666667|0,7|0,747126|
|30|88|10|2| none | manhattan | elliptic |0,833846|0,904255|0,6875|0,774081|0,804598|
|30|88|10|3| none | manhattan | elliptic |0,82012|0,875969|0,742424|0,773565|0,808429|
|30|88|10|4| none | euclidean | elliptic |0,843119|0,914634|0,76087|0,787364|0,833333|
|30|88|10|5| gaussian | manhattan | none |0,855745|0,904545|0,781395|0,812642|0,843678|
|30|88|10|6| none | euclidean | elliptic |0,856968|0,909091|0,782946|0,812181|0,846743|
|30|88|10|7| none | manhattan | elliptic |0,85414|0,904762|0,796825|0,811838|0,848933|
|30|88|10|8| gaussian | manhattan | elliptic |0,901953|0,925|0,863095|0,881464|0,895115|
|**30**|**88**|**10**|**9**|**none**|**manhattan**|**none**|**0,905819**|**0,953086**|**0,830688**|**0,865636**|**0,893997**|
|30|88|10|10| none | euclidean | elliptic |0,900326|0,940909|0,839535|0,866322|0,890805|

### FAQ
1) **Question:**
   What is [linear classifier](https://en.wikipedia.org/wiki/Linear_classifier)?
   
   **Answer:**
   It is a classification algorithm, which based on the construcion of a linear separating surface. In the case of two classes of separating force is a hyperplane that divides the feature space into two half-spaces. Metric classifier is based on the concept of similarity between objects. In this task, the similarity measure between objects is *distance*.

2) **Question:**
   What is [empirical risk](https://en.wikipedia.org/wiki/Empirical_risk_minimization) ([эмпирический риск](http://www.machinelearning.ru/wiki/index.php?title=%D0%AD%D0%BC%D0%BF%D0%B8%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B8%D1%81%D0%BA))?
   
   **Answer:**
   This is the average error value of the algorithm on the training sample.

3) **Question:**
   How to determine the optimal number of neighbors (k_neighbors)?
   
   **Answer:**
   As a rule, lt's processed  how: sqrt(datasetStartSample). In this problem datasetStartSample=118 => optimal k_neighbors≈10. You can check this experimentally.

4) **Question:**
   What cross-validation is used?
   
   **Answer:**
   Was implemented [k-fold cross validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)#k-fold_cross-validation).

5) **Question:**
   How to determine the optimal number of k-fold (k_fold)?
   
   **Answer:**
   Experimentally. I was get the best f1-measure (0,905819) when k_fold was equal 9 (of course, because of the random *shuffle* function, this number may vary slightly) . Think that 10 is the optimal k_fold value.

6) **Question:**
   What does your decision contain?

   **Answer:**
   Look at [Program structure](https://github.com/fedy95/MachineLearning/blob/master/1.%20KNN%20metric%20classifier/_readme_lab1.md#program-structure), also:
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
 
### Links
1) [RESULTS table](https://docs.google.com/spreadsheets/d/1IkHaIzaHMTVHIrxbvIXl9kbQINCencgx8dtkAhNKXRw/edit#gid=0);
2) [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification);
3) [Cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis);
4) [Info](https://github.com/flyingleafe/ML-Course-ITMO/blob/master/Homework.org).
