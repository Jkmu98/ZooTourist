//Funcion para ocultar menu
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (currentScrollPos == 0) {
        document.querySelector(".navbar").style.top = "0";
    } else {
        document.querySelector(".navbar").style.top = "-80px";
    }
    prevScrollpos = currentScrollPos;
}


//Mapa leaflet se llama funcion
document.addEventListener('DOMContentLoaded', function () {
var map = L.map('map').setView([5.54174682681746, -73.36269949853047], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
//marcador y circulo rojo
var marker = L.marker([5.54174682681746, -73.36269949853047]).addTo(map);
marker.bindPopup("<b>Tunja Boyaca</b><br>Sitio Oficial").openPopup();

var circleMarker = L.circle([5.54174682681746, -73.36269949853047], {
    color: 'Blue',
    fillColor: '#f75',
    fillOpacity: 0.3,
    radius: 300 // radio en metros
}).addTo(map);

});