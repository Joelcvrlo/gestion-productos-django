(function(){
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

btnEliminacion.forEach(btn => {
    btn.addEventListener("click", (e) => {
        const confirmacion = confirm('¿Estás seguro que deseas eliminar este item?');
        if(!confirmacion) {
            e.preventDefault();
        }
    });
});
})();