function sumNumbers() {
  let num1 = parseFloat(prompt("Enter the first number:"));
  let num2 = parseFloat(prompt("Enter the second number:"));

  if (isNaN(num1) || isNaN(num2)) {
    console.log("Invalid input. Please enter valid numbers.");
    return;
  }

  return num1 + num2;
}

// Example usage:
let result = sumNumbers();
if (result !== undefined) {
  console.log("Sum:", result);
}

