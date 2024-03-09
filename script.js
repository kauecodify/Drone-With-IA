
function updateStatus(latitude, longitude, altitude) {
    const statusElement = document.getElementById('status');
    statusElement.innerHTML = `
        <p><strong>Latitude:</strong> ${latitude}</p>
        <p><strong>Longitude:</strong> ${longitude}</p>
        <p><strong>Altitude:</strong> ${altitude} meters</p>
    `;
}


function simulateDroneStatus() {
    const latitude = 37.0; // Exemplo
    const longitude = -122.0; // Exemplo
    const altitude = 10.0; // Exemplo
    updateStatus(latitude, longitude, altitude);
}


setInterval(simulateDroneStatus, 5000);

function initMap() {
    const droneLocation = { lat: -25.363, lng: 131.044 }; // Coordenadas do local do drone
    const mapOptions = {
        zoom: 8,
        center: droneLocation
    };
    // Criar o mapa
    const map = new google.maps.Map(document.getElementById('map'), mapOptions);
    // Definir marcador na posição do drone
    const marker = new google.maps.Marker({
        position: droneLocation,
        map: map,
        title: 'Local do Drone'
    });
}