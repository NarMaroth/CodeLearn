// See https://aka.ms/new-console-template for more information

string text = "asdkjhdsjañlv,dsmclkdsaov{s,salñ;F";

// entregar todo lo de text, en esta consulta se le asigna el alias de c a text y devuelve c (text)
var query = from c in text select c;

// entrega solamente los items que concidan con la condicion
var queryv2 = from c in text where c == 'a' select c;


// entrega solamente los items que concidan con la condicion
var method = text.Where(c => c == 'a');

// entregar objetos anonimos como respuesta por cada coincidencia
var methodv3 = text.Where(c => c == 'a').Select(o => new {letra=o});


// devolver los char de mayor valor
// query
var queryv3 = from c in text where c == text.Max() select c;
// method
var methodv4 = text.Where(c => c==text.Max());

//deovlver odernado por valor
// query
var queryv4 = from c in text orderby c select c;
// method
var methodv5 = text.OrderBy(c => c).Select(c => c);

Console.WriteLine("");
