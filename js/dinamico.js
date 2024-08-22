//Ocultar navbar

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

//libreria mapa leaflet

document.addEventListener('DOMContentLoaded', function () {
    var map = L.map('map').setView([4.740831, -73.304276], 8);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var marker = L.marker([4.547809686715518, -73.73339720573871]).addTo(map);
    marker.bindPopup("<b>Parque Nacional Natural Chingaza</b><br>Oso de Anteojos").openPopup();

    var circleMarker = L.circle([4.547809686715518, -73.73339720573871], {
        color: 'green',
        fillColor: '#f75',
        fillOpacity: 0.5,
        radius: 8000 // radio en metros
    }).addTo(map);
    
    var marker2 = L.marker([5.052368906844551, -73.50490346401537]).addTo(map);
    marker2.bindPopup("<b>Municipio de Tibirita</b><br>Puma Concolor").openPopup();

    var circleMarker = L.circle([5.052368906844551, -73.50490346401537], {
        color: 'green',
        fillColor: '#f75',
        fillOpacity: 0.5,
        radius: 5000 // radio en metros
    }).addTo(map);

    var marker3 = L.marker([4.638419, -73.796926]).addTo(map);
    marker3.bindPopup("<b>Parque Nacional Natural Chingaza</b><br>Venado de Cola Blanca").openPopup();

    var circleMarker = L.circle([4.638419, -73.796926], {
        color: 'green',
        fillColor: '#f75',
        fillOpacity: 0.5,
        radius: 1500 // radio en metros
    }).addTo(map);

    var marker4 = L.marker([3.818233980246738, -74.23545324121196]).addTo(map);
    marker4.bindPopup("<b>Parque Nacional Natural Sumapaz</b><br>Tapir Andino").openPopup();

    var circleMarker = L.circle([3.818233980246738, -74.23545324121196], {
        color: 'green',
        fillColor: '#f75',
        fillOpacity: 0.5,
        radius: 2500 // radio en metros
    }).addTo(map);



document.getElementById('animals').addEventListener('change',function(e){
  let coords = e.target.value.split(",");
  map.flyTo(coords,13);
})
});

//popover

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl, {
    trigger: 'hover'
  })
})    

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))


const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')
myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})