function getSliderText() {
    var rangeInput = document.getElementById("rangeInput").value
    if (rangeInput == 0) {
        document.getElementById("slider").innerHTML = "Very easy";
    }
    else if (rangeInput == 25) {
        document.getElementById("slider").innerHTML = "Easy";
    }
    else if (rangeInput == 50) {
        document.getElementById("slider").innerHTML = "Moderate";
    }
    else if (rangeInput == 75) {
        document.getElementById("slider").innerHTML = "Difficult";
    }
    else {
        document.getElementById("slider").innerHTML = "Very difficult";
    }
}