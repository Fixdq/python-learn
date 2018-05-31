function getDate() {
    let date = new Date();
    let year = date.getFullYear();
    let month = date.getMonth();
    let day = date.getDate();
    let hours = date.getHours();
    let min = date.getMinutes();
    let mins = min < 10 ? "0"+min: min;
    let week = date.getDay();


    function getWeek(week) {
        switch (week) {
        case 1:
            return '星期一'
        case 2:
            return '星期二'
        case 3:
            return '星期三'
        case 4:
            return '星期四'
        case 5:
            return '星期五'
        case 6:
            return '星期六'
        case 0:
            return '星期日'
        }
    }
    return (year+'-'+(month+1)+"-"+day+" " + hours+":"+mins +" "+ getWeek(week))
}

// json 相关
let str1 = '{"name":"fixd","age":89}'
let obj1 = {"name":"fixd","age":18}
// json字符串转换成对象
var obj  = JSON.parse(str1)
// 对象转换成json字符串
var str = JSON.stringify(obj1)




var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9]{5,11}$")
reg1.test('kajsdhf2355')



var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/;

reg2.test(s1);  // true


// String对象与正则结合的4个方法
var s2 = "hello world";

s2.match(/o/g);         // ["o", "o"]             查找字符串中 符合正则 的内容
s2.search(/h/g);        // 0                      查找字符串中符合正则表达式的内容位置
s2.split(/o/g);         // ["hell", " w", "rld"]  按照正则表达式对字符串进行切割
s2.replace(/o/g, "s");  // "hells wsrld"          对字符串按照正则进行替换

// 关于匹配模式：g和i的简单示例
var s1 = "name:Alex age:18";

s1.replace(/a/, "哈哈哈");      // "n哈哈哈me:Alex age:18"
s1.replace(/a/g, "哈哈哈");     // "n哈哈哈me:Alex 哈哈哈ge:18"      全局匹配
s1.replace(/a/gi, "哈哈哈");    // "n哈哈哈me:哈哈哈lex 哈哈哈ge:18"  不区分大小写


// 注意事项1：
// 如果regExpObject带有全局标志g，test()函数不是从字符串的开头开始查找，而是从属性regExpObject.lastIndex所指定的索引处开始查找。
// 该属性值默认为0，所以第一次仍然是从字符串的开头查找。
// 当找到一个匹配时，test()函数会将regExpObject.lastIndex的值改为字符串中本次匹配内容的最后一个字符的下一个索引位置。
// 当再次执行test()函数时，将会从该索引位置处开始查找，从而找到下一个匹配。
// 因此，当我们使用test()函数执行了一次匹配之后，如果想要重新使用test()函数从头开始查找，则需要手动将regExpObject.lastIndex的值重置为 0。
// 如果test()函数再也找不到可以匹配的文本时，该函数会自动把regExpObject.lastIndex属性重置为 0。

var reg3 = /foo/g;
// 此时 regex.lastIndex=0
reg3.test('foo'); // 返回true
// 此时 regex.lastIndex=3
reg3.test('xxxfoo'); // 还是返回true
// 所以我们在使用test()方法校验一个字符串是否完全匹配时，一定要加上^和$符号。

// 注意事项2(说出来你可能不信系列)：
// 当我们不加参数调用RegExpObj.test()方法时, 相当于执行RegExpObj.test("undefined"), 并且/undefined/.test()默认返回true。
var reg4 = /^undefined$/;
reg4.test(); // 返回true
reg4.test(undefined); // 返回true
reg4.test("undefined"); // 返回true