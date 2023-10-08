function distancesFromAverage(arr) {
  // Calculate the total sum of the array
  const total = arr.reduce((sum, num) => sum + num, 0);

  // Calculate the average
  const avg = total / arr.length;

  // Create a new array that contains the rounded differences from the average
  const result = arr.map((num) => parseFloat((avg - num).toFixed(2)));

  return result;
}
