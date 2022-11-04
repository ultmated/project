// Clear the value on the display
function Reset() {
    document.getElementById("result").value = "";
}
 
// Display the value
function display(value) {
    document.getElementById("result").value += value;
}
 
// Calculate the result using default method by javascript
function calculate() {
    var p = document.getElementById("result").value;
    // eval() == evaluates the javascript and executes it 
    var q = eval(p);
    document.getElementById("result").value = q;
}