//var carro = {
//marca: "fiat",
//modelo: "uno",
//ano: 2001
//}
//var texto = JSON.stringify(carro)
//document.getElementById("area").innerHTML = texto;
//alert(carro.marca)
function BuscarCEP(){
    var end = document.getElementById('cep').value;
    const ajax = new XMLHttpRequest
    ajax.open ('GET','https://viacep.com.br/ws/'+ end +'/json/');
    ajax.send();
    ajax.onload = function(){
        var obj = JSON.parse(this.responseText);
        var logradouro = obj.logradouro;
        var cidade = obj.localidade;
        var estado = obj.uf;
    document.getElementById('texto').innerHTML = "Logradouro: " + logradouro
    + "<br>Cidade: " + cidade + "<br>Estado: " + estado;
    }
}
