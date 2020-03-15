var text = document.getElementsByClassName('js-text')[0]
// setTimeout(function () {
//     console.log('Hello world')
// }, 5000)
var classes = ['red', 'green', 'blue']
var index = 0
setInterval(function () {
    var className = classes[index]
    index += 1
    if (index > 2) {
        index = 0
    }
    text.className = className
    text.style['margin-left'] = index * 100 + 'px'
}, 1000)
console.log('Text=', text)
function lock() {
    while (true) {}
}
var variable = 3
let a = 1
a = "asdasdas"
const b = 2
// alert("ALERT")
// let value = confirm("Pokinut stranicu?")
// console.log(value)

var myList = [1, 2, 3, 4, 5]
var myObject = {
    "key": 123,
    "value": [1, 2, 3]
}
// var b = 1 + ++a
let i = 1;
for (;;) {
    console.log(i)
    i += 2
    if (i > 100) {
        break
    }
}
console.log('J')
let j = 3
while (j > 0) {
    console.log(j--)
    continue
}

let value = prompt('Text? ')
// if (value === 'text1') {
//     console.log('111')
// } else if (value === 'text2') {
//     console.log('222')
// } else if (value === 'text3'){
//     console.log('333')
// } else {
//     console.log('444')
// }

switch (value) {
    case "text1":
        console.log('111')
        break
    case "text2":
        console.log('222')
        break
    default:
        console.log('default')
        break
}

function foo(a, b, c) {
    return a + b + c
}

var storage = localStorage
storage.setItem('key', '1111111')
storage.getItem('key')

function getData() {
    var username = document.getElementById('username')
    var password = document.getElementById('password')
    var color = document.getElementById('color')
    console.warn(username.value, password.value, color.value)
    console.error('ERROR')
}