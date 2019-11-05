function mostravalor() {
    var els = document.getElementsByClassName("valor");
    var valorcalculado = 0.00;
    [].forEach.call(els, function (el)
    {
        valorcalculado += parseFloat((el.innerHTML));
    });

    document.getElementById("total").innerHTML = valorcalculado.toFixed(2);
}

