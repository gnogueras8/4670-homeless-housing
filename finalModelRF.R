library(randomForest)
library(randomForestExplainer)

data <- read.csv("final_data.csv")
summary(data)

model <- glm(data$pcthmlsofciv ~ Rent +  gini + crime + Housing_Supply + pctmar , data = data)
summary(model)

forest <- randomForest(data$pcthmlsofciv ~ Rent +  gini + crime + Housing_Supply + pctmar , data = data, localImp = TRUE, ntree=1500)
forest
min_depth_frame <- min_depth_distribution(forest) 
head(min_depth_frame, n = 10)
plot_min_depth_distribution(min_depth_frame)
