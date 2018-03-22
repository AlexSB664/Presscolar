function tutores(e){
    if(e.keyCode == 13){
        var filtro = document.getElementById('inputFiltroTutor').value
        $.ajax({
            url = 'tutores/busqueda',
            type:'GET',
            contentType:'application/json charset=utf-8',
            dataType:'json',
            data:{"nombre": filtro},
            success.function(response){
            console.log(response)   
           }});   
    }
}