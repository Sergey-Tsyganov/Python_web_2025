// комментарий для всех c подобных языков
/*
Скрипт js тоже какие то комментарии
https://learn.javascript.com
*/

//Функция
/*
function sayHello(name){
document.writeln("Вас зовут" + name);
}
// Переменные (var или let
let name = prompt("Ваше имя");
sayHello(name)
*/
let colors=["Красный","Синий","Голубой"];
document.writeln("<h1>Цвета<h1><ul>");
for(let i=0; i<colors.length;i++){
    document.writeln("<li>" + colors[i] +"</li>");
}
document.writeln("</ul>");