$("#somar").click(function(){
    var soma = 0;
    var totallanches = document.getElementById('totallanche');
    var totalbebidas = document.getElementById('totalbebidas');

    soma = totallanches + totalbebidas;

    $(".resultado").html(soma.toFixed(2));
});