/*function mostravalor() {
    var els = document.getElementsByClassName("valor");
    var valorcalculado = 0.00;
    [].forEach.call(els, function (el)
    {
        valorcalculado += parseFloat((el.innerHTML));
    });

    document.getElementById("total").innerHTML = valorcalculado.toFixed(2);
}
*/

function mostravalor() {
    const els = document.getElementsByClassName("valor");
    let valorcalculado = 0;

    [].forEach.call(els, function (element){
        let intergerElement = parseInt(element.innerHTML.replace(/,/g, "") // remove qualquer vírgula que exista.
        .replace(/\./g, "") // remove qualquer ponto que exista.
    );

    valorcalculado += intergerElement;
});

/* Dividimos o valor por 100 para adicionar as casas decimais
e depois convertemos para o valor pt-BR */

let total = (valorcalculado / 100).toLocaleString("pt-BR");
document.getElementById("total").innerHTML = total;
}