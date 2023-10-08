get_participants <- function(handshakes){
  if (handshakes == 0) {
    return(0)
  }
  
  discriminant <- sqrt(1 + 8 * handshakes)
  
  n <- (-(-1) + discriminant) / 2
  
  return(ceiling(n))
}