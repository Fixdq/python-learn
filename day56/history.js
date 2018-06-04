// 找到本页面中id是i1的标签
$('#j1')
// 找到本页面中所有的h2标签
$('h2')
// 找到本页面中所有的input标签
$('input')
// 找到本页面所有样式类中有c1的标签
$('.c1')
// 找到本页面所有样式类中有btn-default的标签
$('.btn-default')
// 找到本页面所有样式类中有c1的标签和所有h2标签
$('.c1, h2')
// 找到本页面所有样式类中有c1的标签和id是p3的标签
$('.c1, #p3')
// 找到本页面所有样式类中有c1的标签和所有样式类中有btn的标签
$('.c1, .btn')
// 找到本页面中form标签中的所有input标签
$('from input')
// 找到本页面中被包裹在label标签内的input标签
$('label>input')
// 找到本页面中紧挨在label标签后面的input标签
$('label+input')
// 找到本页面中id为p2的标签后面所有和它同级的li标签
$('#p2~li')
// 找到id值为f1的标签内部的第一个input标签
$('#f1 input:first')
$('#f1 input').first()
// 找到id值为my-checkbox的标签内部最后一个input标签
$('#my-checkbox input:last')
$('#my-checkbox input').last()
// 找到id值为my-checkbox的标签内部没有被选中的那个input标签
$('#my-checkbox input:not(:checked)')
$('#my-checkbox input').not(':checked')
// 找到所有含有input标签的label标签
$('label:has(input)')
