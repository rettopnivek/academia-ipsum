Title: Printing to the console in Rcpp
Date: 2016-09-21
Category: Rcpp
Tags: Rcpp, code
Slug: console-printing-rcpp
Authors: Kevin Potter

Here's a simple example of how to print to the console window with a simple Rcpp function. This also provides an example of the versatile 'cppFunction'.  

```r
library(Rcpp)
cppFunction('
  void helloWorld( ) {
    Rcpp::Rcout << "Hello world!" << std::endl;
  }
')
```
