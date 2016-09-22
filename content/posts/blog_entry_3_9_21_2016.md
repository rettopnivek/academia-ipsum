Title: Setting column names in Rcpp
Date: 2016-09-21
Category: Rcpp
Tags: Rcpp, code
Slug: column-names-rcpp
Authors: Kevin Potter

Rcpp provides an easy way to set the column names of a matrix.  
```r
library(Rcpp)
cppFunction('
  NumericMatrix matEx( ) {
    NumericMatrix mat(2,2);
    mat(0,0) = 1; mat(0,1) = 2;
    mat(1,0) = 3; mat(1,1) = 4;
    
    colnames(mat) = Rcpp::CharacterVector::create("A", "B");
    
    return( mat );
  }
')
```
