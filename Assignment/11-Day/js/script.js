let currentVehicle = "Polo";

function generateData() {
    return {
        temp: 80 + Math.floor(Math.random() * 25),
        voltage: (12 + Math.random()).toFixed(2),
        speed: 50 + Math.floor(Math.random() * 80)
    };
}

function updateDashboard() {
    let data = generateData();

    document.getElementById("temp").innerText = data.temp + " °C";
    document.getElementById("voltage").innerText = data.voltage + " V";
    document.getElementById("speed").innerText = data.speed + " km/h";

    if (data.temp > 100) {
        document.getElementById("status").innerText = "Overheating";
        document.getElementById("status").style.color = "red";
        console.log("Alert: Engine temperature crossed safe limit.");
    } else {
        document.getElementById("status").innerText = "Healthy";
        document.getElementById("status").style.color = "green";
    }

    console.log("Monitoring data refreshed for vehicle: " + currentVehicle);
}

function changeVehicle() {
    currentVehicle = document.getElementById("vehicleSelect").value;
    console.log("Vehicle switched to: " + currentVehicle);
    updateDashboard();
}

function manualRefresh() {
    console.log("Manual refresh executed by user.");
    updateDashboard();
}

function toggleTheme() {
    document.body.classList.toggle("dark");

    let btn = document.getElementById("themeBtn");

    if (document.body.classList.contains("dark")) {
        btn.innerText = "Light Mode";
        console.log("Dark mode enabled.");
    } else {
        btn.innerText = "Dark Mode";
        console.log("Light mode enabled.");
    }
}

window.onload = function() {
    updateDashboard();

    setInterval(updateDashboard, 5000);

    console.log("Vehicle monitoring panel loaded successfully.");
};