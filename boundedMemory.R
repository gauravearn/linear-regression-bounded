boundedMemoryLinearRegression <- function(file_csv){
    # an R funtion to Bounded memory linear regression on 
    # interpreting the height to phenotype bolting measures
    read_phenotype <- read.csv(file_csv, stringsAsFactors = FALSE)
    readnew <- na.omit(read_phenotype)
    colnames(readfinal) <- c("height", "bolting")
    linear_formula <- bolting ~ height
    model <- bigglm(linear_formula, data = readfinal, chunksize = 10, sandwich = TRUE)
    return(summary(model))
}

