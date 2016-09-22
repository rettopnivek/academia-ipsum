Title: Progress bar in R
Date: 2016-09-21
Category: R
Tags: R, code
Slug: progress-bar
Authors: Kevin Potter

Here is an example of creating a simple text progress bar in R to track the progress of a loop:  

```r
# Set the maximum number of iterations
total = 10
# Create a progress bar using a base R function
pb = txtProgressBar( min = 0, max = total, style = 3 )
for (i in 1:total) {
	# Update the progress bar
	setTxtProgressBar(pb,i)
}
close(pb)
```

The third style is nice because it also shows the percentage and indicates both the start and end of the progress bar.
