const display = document.getElementById('display');

function appendToDisplay(input) {
    display.value += input;
}

function clearDisplay() {
    display.value = "";
}

function calculate() {
    try {
        // eval() takes the string (e.g., "2+2") and does the math
        display.value = eval(display.value);
    } catch (error) {
        display.value = "Error";
    }
}