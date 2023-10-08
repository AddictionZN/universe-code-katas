// DigitPower class with a single responsibility: to find the value of k for given n and p.
class DigitPower {
  constructor(n, p) {
    this.n = n;
    this.p = p;
  }

  // Method to find and return the value of k
  findK() {
    // Convert the number to a string and then to an array of digits
    const digits = Array.from(String(this.n), Number);

    // Calculate the sum of the digits taken to the successive powers of p
    let sum = 0;
    for (let i = 0; i < digits.length; i++) {
      sum += Math.pow(digits[i], this.p + i);
    }

    // Find k such that sum = n * k
    const k = sum / this.n;

    // If k is an integer, return k. Otherwise, return -1.
    return Number.isInteger(k) ? k : -1;
  }
}

// Testing the DigitPower class
const dig_pow = (n, p) => {
  const digitPower = new DigitPower(n, p);
  return digitPower.findK();
};
