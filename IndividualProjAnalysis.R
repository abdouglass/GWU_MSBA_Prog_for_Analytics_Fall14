#load data
wbAll <- read.csv("G:/ProgrammingForAnalytics/Assignments/IndividualProject/WB_All.csv")
#View(wbAll)
wb14 <- read.csv("G:/ProgrammingForAnalytics/Assignments/IndividualProject/WB_2014.csv")
#View(wb14)
wb04 <- read.csv("G:/ProgrammingForAnalytics/Assignments/IndividualProject/WB_2004.csv")
#View(wb04)
wb94 <- read.csv("G:/ProgrammingForAnalytics/Assignments/IndividualProject/WB_1994.csv")
#View(wb94)
wb84 <- read.csv("G:/ProgrammingForAnalytics/Assignments/IndividualProject/WB_1984.csv")
#View(wb84)

#Linear Regression on continuous variables
GiniAll <- lm(Gini ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + MF_Sec + MF_Prim, data = wbAll)
#summary(GiniAll)
Gini14 <- lm(Gini ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + MF_Sec + MF_Prim, data = wb14)
#summary(Gini14)
Gini04 <- lm(Gini ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + MF_Sec + MF_Prim, data = wb04)
#summary(Gini04)
Gini94 <- lm(Gini ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + MF_Sec + MF_Prim, data = wb94)
#summary(Gini94)
Gini84 <- lm(Gini ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + MF_Sec + MF_Prim, data = wb84)
#summary(Gini84)

PovertyAll <- lm(Poverty ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + FM_Sec + FM_Prim, data = wbAll)
#summary(PovertyAll)
Poverty14 <- lm(Poverty ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + FM_Sec + FM_Prim, data = wb14)
#summary(Poverty14)
Poverty04 <- lm(Poverty ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + FM_Sec + FM_Prim, data = wb04)
#summary(Poverty04)
Poverty94 <- lm(Poverty ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + FM_Sec + FM_Prim, data = wb94)
#summary(Poverty94)
Poverty84 <- lm(Poverty ~ Sec_M + Sec_F + Sec + Prim_M + Prim_F + Prim + FM_Sec + FM_Prim, data = wb84)
#summary(Poverty84)


#Logit on Income Equality Binary
logitAll <- glm(IncEqu ~ EdSecEqu + EdPrimEqu + Sec + Prim + Prim_M + Prim_F + Sec_M + Sec_F, data = wbAll, family = "binomial")
#summary(logitAll)
logit14 <- glm(IncEqu ~ EdSecEqu + EdPrimEqu + Sec + Prim + Prim_M + Prim_F + Sec_M + Sec_F, data = wb14, family = "binomial")
#summary(logit14)
logit04 <- glm(IncEqu ~ EdSecEqu + EdPrimEqu + Sec + Prim + Prim_M + Prim_F + Sec_M + Sec_F, data = wb04, family = "binomial")
#summary(logit04)
logit94 <- glm(IncEqu ~ EdSecEqu + EdPrimEqu + Sec + Prim + Prim_M + Prim_F + Sec_M + Sec_F, data = wb94, family = "binomial")
#summary(logit94)
logit84 <- glm(IncEqu ~ EdSecEqu + EdPrimEqu + Sec + Prim + Prim_M + Prim_F + Sec_M + Sec_F, data = wb84, family = "binomial")
#summary(logit84)

#graphs and charts
#histogram of Gini, Poverty, Primary & Secondary
hist(wbAll$Gini, freq=FALSE, main="Density plot", col="forestgreen", breaks = 20)
hist(wbAll$Prim, freq=FALSE, main="Density plot", col="forestgreen", breaks = 20)
hist(wbAll$Sec, freq=FALSE, main="Density plot", col="forestgreen", breaks = 20)
hist(wbAll$Poverty, freq = FALSE, main = "Density plot", col = "forestgreen", breaks = 20)

#scatter plots
#Gini
plot(WB_All$Prim_M, WB_All$Gini,col = 5, pch = 17, xlab="Education (%)",ylab="Gini Index",main="Gini Index vs Education")
points(WB_All$Prim_F,WB_All$Gini,col=6,pch=8)
points(WB_All$Sec_F,WB_All$Gini,col=2,pch=16)
points(WB_All$Sec_M, WB_All$Gini, col=4, pch=15)
legend(38.1,67.5,cex = 0.6, c("Primary- Male", "Primary- Female", "Secondary - Male", "Secondary - Female"),col=c(5,6,4,2),pch=c(17,8,15,16))
#Poverty
plot(WB_All$Prim_M, WB_All$Poverty,col = 5, pch = 17, xlab="Education (%)",ylab="Poverty (%)",main="Poverty vs Education")
points(WB_All$Prim_F,WB_All$Poverty,col=6,pch=8)
points(WB_All$Sec_F,WB_All$Poverty,col=2,pch=16)
points(WB_All$Sec_M, WB_All$Poverty, col=4, pch=15)
legend(38.1,47.1,cex = 0.6, c("Primary- Male", "Primary- Female", "Secondary - Male", "Secondary - Female"),col=c(5,6,4,2),pch=c(17,8,15,16))
