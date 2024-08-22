document.addEventListener("DOMContentLoaded", function(){
    
    async function cargarAves(){
        try {
            const respuesta= await fetch("http://127.0.0.1:5000/aves/")

            if(!respuesta.ok){
                console.error("Error al cargar aves: ", respuesta.statusText)
                return
            }

            const aves = await respuesta.json()
            // console.log(aves)

            const tbody = document.getElementById("i-table-aves").querySelector("tbody")
            tbody.innerHTML= ""
  
            aves.forEach(ave => {
                const row= tbody.insertRow()
                row.insertCell(0).textContent= ave.id
                row.insertCell(1).textContent= ave.nombre
                row.insertCell(2).textContent= ave.ubicacion
                row.insertCell(3).textContent= ave.caracteristica
                row.insertCell(4).textContent= ave.datoCurioso
                row.insertCell(5).textContent= ave.nombreCientifico
            });

        } catch (error) {
            console.error("Error: ", error)
        }
    }

    cargarAves()
})