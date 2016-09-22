Title: Clearing the workspace in R
Date: 2016-09-21
Category: R
Tags: R, code
Slug: clearing-the-workspace
Authors: Kevin Potter

It can be useful to wipe the workspace clean in R when you first start a script. Here's a small snippet of R code to do so:  

```r
# Clear workspace
rm(list = ls())
```