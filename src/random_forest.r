library("randomForest")

aggregated = read.csv("../data/aggregated_by_customer_train_cat.csv")
training_history = read.csv("../data/offersAndTrainJoined.csv")

# Joining the offers+train data and the transaction aggregation data
total_joined_train = merge(aggregated, training_history, by = "id")

# Remove the extra offer column
total_joined_train$offer.1 <- NULL

# Set certain variables as factors
total_joined_train$id <- factor(total_joined_train$id)
total_joined_train$chain <- factor(total_joined_train$chain)
total_joined_train$offer <- factor(total_joined_train$offer)
total_joined_train$market <- factor(total_joined_train$market)
total_joined_train$category <- factor(total_joined_train$category)
total_joined_train$quantity <- factor(total_joined_train$quantity)
total_joined_train$company <- factor(total_joined_train$company)
total_joined_train$brand <- factor(total_joined_train$brand)

# Train the random forest
drops <- c("repeattrips", "repeater")
variables <- total_joined_train[,!(colnames(total_joined_train) %in% drops)]
rf <- randomForest(total_joined_train$repeater, data = total_joined_train)
