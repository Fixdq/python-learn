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

