data <- read.csv("final_data.csv")
summary(data)
model1 <- glm(data$pcthmlsofciv ~ data$Rent + data$gini + data$pctcrime + data$pctinv +data$Housing_Supply, data = data)
model2 <- lm(data$pcthmlsofciv ~ data$Rent + data$gini + data$pctcrime + data$pctinv +data$Housing_Supply, data = data)

plot(data$pcthmlsofciv ~ data$Rent)
model_rent <- lm(data$pcthmlsofciv ~ data$Rent)
abline(model_rent, col="blue")

plot(data$pcthmlsofciv ~ data$gini)
model_gini <- lm(data$pcthmlsofciv ~ data$gini, data = data)
abline(model_gini, col="blue")

model_crime <- lm(data$pcthmlsofciv ~ data$pctcrime, data = data)
plot(data$pcthmlsofciv ~ data$pctcrime)
abline(model_crime, col="blue")

summary(model1)

