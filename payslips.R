set.seed(123)

genders <- c("male", "female")
workers <- list()

# Generate workers
for (i in 1:400) {
  workers[[i]] <- list(
    worker_id = i,
    gender = sample(genders, 1),
    salary = sample(6000:32000, 1)
  )
}

# Go through each worker and generate payslip
for (worker in workers) {
  tryCatch({
    level <- "Unassigned"
    
    if (worker$salary > 10000 && worker$salary < 20000) {
      level <- "A1"
    }
    
    if (worker$salary > 7500 && worker$salary < 30000 && worker$gender == "female") {
      level <- "A5-F"
    }
    
    cat("Payment Slip for worker with ID: ", worker$worker_id, "\n")
    cat("Gender: ", worker$gender, "\n")
    cat("Salary: $", worker$salary, "\n")
    cat("Employee Level: ", level, "\n")
    cat(rep("-", 100), "\n", sep = "")
    
  }, error = function(e) {
    cat("An error occurred while processing worker ", worker$worker_id, ": ", e$message, "\n", sep = "")
  })
}