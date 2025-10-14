document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario');

    formulario.addEventListener('submit', function(e) {
        let esValido = true;
        let camposVacios = [];
        
        // 1. OBTENER LAS REFERENCIAS DE TODOS LOS CAMPOS OBLIGATORIOS
        const nombreInput = document.getElementById('nombre');
        const emailInput = document.getElementById('email');
        const mensajeInput = document.getElementById('mensaje');
        

        // 2. CREAR UN ARRAY CON TODOS LOS CAMPOS OBLIGATORIOS PARA ITERAR
        const camposObligatorios = [
            { elemento: nombreInput, nombre: 'Nombre' },
            { elemento: emailInput, nombre: 'Email' },
            { elemento: mensajeInput, nombre: 'Mensaje' },
        ];

        // 3. ITERAR Y VERIFICAR SI ESTÁN VACÍOS
        camposObligatorios.forEach(campo => {
            if (campo.elemento.value.trim() === '') {
                esValido = false;
                camposVacios.push(campo.nombre);
            }
        });

        // 4. SI NO ES VÁLIDO, PREVENIR EL ENVÍO Y MOSTRAR ALERTA
        if (!esValido) {
            e.preventDefault(); // Detiene el envío del formulario

            let mensajeError = "Por favor, complete los campos ";
            mensajeError += camposVacios.join(', ');
            alert(mensajeError);
            
            const primerCampoVacio = camposObligatorios.find(campo => campo.elemento.value.trim() === '');
            if (primerCampoVacio) {
                primerCampoVacio.elemento.focus();
            }
        } else {
            e.preventDefault();
            alert("¡Tu mensaje fué enviados exitosamente, " + nombreInput.value + "!");
            formulario.reset();
            window.location.href = "../index/index.html";
        }
    });
});