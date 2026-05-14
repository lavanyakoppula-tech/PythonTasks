Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/pythonTasks/Scikit_Learn/Car_price_prediction/car_price_prediction.py
  Car_Name  Year  Selling_Price  ...  Seller_Type  Transmission Owner
0     Take  2018          23.21  ...   Individual     Automatic     3
1       As  2005          17.64  ...   Individual     Automatic     1
2    Final  2012          24.24  ...   Individual     Automatic     3
3   Effect  2007          22.53  ...       Dealer     Automatic     3
4      Way  2019          17.17  ...   Individual     Automatic     2

[5 rows x 9 columns]
--------------------------------------------------------------------------------
Checking Null Values
Car_Name         0
Year             0
Selling_Price    0
Present_Price    0
Kms_Driven       0
Fuel_Type        0
Seller_Type      0
Transmission     0
Owner            0
dtype: int64
--------------------------------------------------------------------------------
  Car_Name  Selling_Price  Present_Price  ...  Transmission  Owner  Car_Age
0     Take          23.21           5.22  ...             0      3        7
1       As          17.64          12.61  ...             0      1       20
2    Final          24.24          22.41  ...             0      3       13
3   Effect          22.53          10.97  ...             0      3       18
4      Way          17.17           3.02  ...             0      2        6

[5 rows x 9 columns]
--------------------------------------------------------------------------------
Shape of X : (100, 8)
Shape of y : (100,)
--------------------------------------------------------------------------------
X_train Length : 80
X_test Length : 20
Traceback (most recent call last):
  File "C:/pythonTasks/Scikit_Learn/Car_price_prediction/car_price_prediction.py", line 102, in <module>
    X_train = scaler.fit_transform(X_train)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_set_output.py", line 316, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 907, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\preprocessing\_data.py", line 924, in fit
    return self.partial_fit(X, y, sample_weight)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 1336, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\preprocessing\_data.py", line 961, in partial_fit
    X = validate_data(
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 2902, in validate_data
    out = check_array(X, input_name="X", **check_params)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py", line 1022, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_array_api.py", line 878, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\Windows\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 2153, in __array__
    arr = np.asarray(values, dtype=dtype)
ValueError: could not convert string to float: 'I'

= RESTART: C:/pythonTasks/Scikit_Learn/Car_price_prediction/car_price_prediction.py
================================================================================
Dataset Preview
  Car_Name  Year  Selling_Price  ...  Seller_Type  Transmission Owner
0     Take  2018          23.21  ...   Individual     Automatic     3
1       As  2005          17.64  ...   Individual     Automatic     1
2    Final  2012          24.24  ...   Individual     Automatic     3
3   Effect  2007          22.53  ...       Dealer     Automatic     3
4      Way  2019          17.17  ...   Individual     Automatic     2

[5 rows x 9 columns]
================================================================================
Dataset Shape
(100, 9)
================================================================================
Null Values
Car_Name         0
Year             0
Selling_Price    0
Present_Price    0
Kms_Driven       0
Fuel_Type        0
Seller_Type      0
Transmission     0
Owner            0
dtype: int64
================================================================================
Processed Dataset
   Selling_Price  Present_Price  Kms_Driven  ...  Transmission  Owner  Car_Age
0          23.21           5.22       46953  ...             0      3        7
1          17.64          12.61       53330  ...             0      1       20
2          24.24          22.41      106180  ...             0      3       13
3          22.53          10.97       13672  ...             0      3       18
4          17.17           3.02      133694  ...             0      2        6

[5 rows x 8 columns]
================================================================================
X Shape : (100, 7)
y Shape : (100,)
================================================================================
Training and Testing Data
X_train : (80, 7)
X_test : (20, 7)
y_train : (80,)
y_test : (20,)
================================================================================
Linear Regression Results
R2 Score : -0.178
Accuracy Percentage : -17.78%
Mean Absolute Error : 6.770
Root Mean Squared Error : 7.533
================================================================================
Decision Tree Regressor Results
R2 Score : -1.372
Accuracy Percentage : -137.25%
Mean Absolute Error : 8.864
Root Mean Squared Error : 10.691
================================================================================
Random Forest Regressor Results
R2 Score : -0.620
Accuracy Percentage : -61.98%
Mean Absolute Error : 7.635
Root Mean Squared Error : 8.834
================================================================================
Gradient Boosting Regressor Results
R2 Score : -1.652
Accuracy Percentage : -165.22%
Mean Absolute Error : 9.225
Root Mean Squared Error : 11.304
================================================================================
KNN Regressor Results
R2 Score : -0.487
Accuracy Percentage : -48.68%
Mean Absolute Error : 7.719
Root Mean Squared Error : 8.464
================================================================================
Sample Predictions using Random Forest
[12.6684 13.1394  9.4902  9.2655  8.1837 12.0145 14.6545 12.1196  6.9204
 10.6304]

=================================== RESTART: C:/pythonTasks/Scikit_Learn/Car_price_prediction/car_price_prediction.py ===================================
================================================================================
  Car_Name  Year  Selling_Price  ...  Seller_Type  Transmission Owner
0     Take  2018          23.21  ...   Individual     Automatic     3
1       As  2005          17.64  ...   Individual     Automatic     1
2    Final  2012          24.24  ...   Individual     Automatic     3
3   Effect  2007          22.53  ...       Dealer     Automatic     3
4      Way  2019          17.17  ...   Individual     Automatic     2

[5 rows x 9 columns]
================================================================================
Linear Regression Results
R2 Score : -0.178
Accuracy Percentage : -17.78%
MAE : 6.770
RMSE : 7.533
================================================================================
Decision Tree Regressor Results
R2 Score : -1.372
Accuracy Percentage : -137.25%
MAE : 8.864
RMSE : 10.691
================================================================================
Random Forest Regressor Results
R2 Score : -0.620
Accuracy Percentage : -61.98%
MAE : 7.635
RMSE : 8.834
================================================================================
Gradient Boosting Regressor Results
R2 Score : -1.639
Accuracy Percentage : -163.91%
MAE : 9.229
RMSE : 11.276
================================================================================
KNN Regressor Results
R2 Score : -0.487
Accuracy Percentage : -48.68%
MAE : 7.719
RMSE : 8.464

========================================= RESTART: C:/pythonTasks/Scikit_Learn/Car_price_prediction/carprice.py =========================================
================================================================================
DATASET PREVIEW
  Car_Name  Year  Selling_Price  ...  Seller_Type  Transmission Owner
0     Take  2018          23.21  ...   Individual     Automatic     3
1       As  2005          17.64  ...   Individual     Automatic     1
2    Final  2012          24.24  ...   Individual     Automatic     3
3   Effect  2007          22.53  ...       Dealer     Automatic     3
4      Way  2019          17.17  ...   Individual     Automatic     2

[5 rows x 9 columns]
================================================================================
DATASET INFO
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 9 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Car_Name       100 non-null    object 
 1   Year           100 non-null    int64  
 2   Selling_Price  100 non-null    float64
 3   Present_Price  100 non-null    float64
 4   Kms_Driven     100 non-null    int64  
 5   Fuel_Type      100 non-null    object 
 6   Seller_Type    100 non-null    object 
 7   Transmission   100 non-null    object 
 8   Owner          100 non-null    int64  
dtypes: float64(2), int64(3), object(4)
memory usage: 7.2+ KB
None
================================================================================
NULL VALUES
Car_Name         0
Year             0
Selling_Price    0
Present_Price    0
Kms_Driven       0
Fuel_Type        0
Seller_Type      0
Transmission     0
Owner            0
dtype: int64
================================================================================
PROCESSED DATASET
   Selling_Price  Present_Price  Kms_Driven  ...  Transmission  Owner  Car_Age
0          23.21           5.22       46953  ...             0      3        7
1          17.64          12.61       53330  ...             0      1       20
2          24.24          22.41      106180  ...             0      3       13
3          22.53          10.97       13672  ...             0      3       18
4          17.17           3.02      133694  ...             0      2        6

[5 rows x 8 columns]
