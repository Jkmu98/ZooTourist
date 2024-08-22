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
var map = L.map('map').setView([4.740831, -73.304276], 7);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var marker = L.marker([6.995325042985385, -72.74336420436748]).addTo(map);
marker.bindPopup("<b>Paramo del Almorzadero Santander</b><br>Condor Andino").openPopup();

var circleMarker = L.circle([6.995325042985385, -72.74336420436748], {
    color: 'yellow',
    fillColor: '#f75',
    fillOpacity: 0.5,
    radius: 8000 // radio en metros
}).addTo(map);

circleMarker.bindPopup("<b>Paramo del Almorzadero Santander</b><br>Condor Andinoe");
//marcador y circulo rojo
var marker2 = L.marker([5.017219328050363, -74.29674561924905]).addTo(map);
marker2.bindPopup("<b>Jardin Encantado San Francisco, Cundinamarca</b><br>Colibris").openPopup();

var circleMarker = L.circle([5.017219328050363, -74.29674561924905], {
    color: 'red',
    fillColor: '#f75',
    fillOpacity: 0.5,
    radius: 500 // radio en metros
}).addTo(map);

var marker3 = L.marker([5.397056350810991, -73.23763851932951]).addTo(map);
marker3.bindPopup("<b>Páramo Mamapacha Bijagua</b><br>Aguila Real de Montaña").openPopup();

var circleMarker = L.circle([5.397056350810991, -73.23763851932951], {
    color: 'blue',
    fillColor: '#f75',
    fillOpacity: 0.5,
    radius: 2000 // radio en metros
}).addTo(map);

var marker4 = L.marker([6.221404426693992, -73.45073807864507]).addTo(map);
marker4.bindPopup("<b>Cascada de Los Caballeros</b><br>Carpintero Dorado").openPopup();

var circleMarker = L.circle([6.221404426693992, -73.45073807864507], {
    color: 'green',
    fillColor: '#f75',
    fillOpacity: 0.5,
    radius: 1000 // radio en metros
}).addTo(map);


//Funcion flyTo para lograr acercar el punto
document.getElementById('animals2').addEventListener('change',function(e){
let coords = e.target.value.split(",");
map.flyTo(coords,13);
})
});