# EmpiricalDistribution
This is a simple class that you can use for computing the empirical cdf and the inverse of the empirical cdf.

After importing a dataframe, and selecting the column, you need to initialize the class, and fit them to the selected columns:

```
ecdf = EmpiricalDistribution()
ecdf.fit_transform(data, columns)
```

Then if you want to go back to the original data, or for example you have used the empirical probabilities for modelling, and you have newer ones, you can use the instantied class to go back to the values:

```
ecdf.inverse_transform(data)
```

