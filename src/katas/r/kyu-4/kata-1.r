find_prime_factors <- function(n) {
  factors <- c()
  i <- 2
  while(i * i <= n) {
    if (n %% i) {
      i <- i + 1
    } else {
      n <- n / i
      factors <- c(factors, i)
    }
  }
  if (n > 1) {
    factors <- c(factors, n)
  }
  return(unique(factors))
}

sumOfDivided <- function(I) {
  if (length(I) == 0 || is.null(I)) {
    return(list())
  }

  all_factors <- unique(unlist(lapply(I, find_prime_factors)))

  if (length(all_factors) == 0 || is.null(all_factors)) {
    return(list())
  }

  result <- lapply(sort(all_factors), function(p) {
    sum_vals <- sum(I[I %% p == 0])
    return(c(p, sum_vals))
  })

  return(result)
}
