function filter_illegal_char(s) {
    var pattern = new RegExp("[%--`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——|{}【】‘；：”“'。，、？]");
    var rs = "";
    for (var i = 0; i < s.length; i++) {
        rs = rs + s.substr(i, 1).replace(pattern, '');
    }
    return rs;
}


function email_jundge(str) {
    const reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
    return reg.test(str)
}

function phone_jundge(str) {
    const reg = /^((0\d{2,3}-\d{7,8})|(1[3456789]\d{9}))$/
    return reg.test(str)
}

function staff_id_jundge(str) {
    const reg = /^((0\d{2,3}-\d{7,8})|(1[3456789]\d{9}))$/
    return reg.test(str)
}

// todo 测试
function CheckPassWord(password) {//必须为字母加数字且长度不小于8位
    var str = password;
    if (str == null || str.length < 8) {
        return false;
    }
    var reg1 = new RegExp(/^[0-9A-Za-z]+$/);
    if (!reg1.test(str)) {
        return false;
    }
    var reg = new RegExp(/[A-Za-z].*[0-9]|[0-9].*[A-Za-z]/);
    if (reg.test(str)) {
        return true;
    } else {
        return false;
    }
}

// todo 入职时间

// todo 等级


