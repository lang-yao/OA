function check_serialize(serialize_arr) {
    for (var ele in serialize_arr) {
        if (serialize_arr[ele]['name'] != 'ruzhitime' && serialize_arr[ele]['name'] != 'email') {
            if (serialize_arr[ele]['value'] == "") {
                swal({
                    title: "不能为空!",
                    icon: "error",
                });
                return 0;//0 非法字符
            }
            if (!filter_illegal_char(serialize_arr[ele]['value'])) {
                swal({
                    title: "请勿使用非法字符!",
                    icon: "error",
                });
                return 0;//0 非法字符
            }
        }
    }
    for (var ele in serialize_arr) {
        if (serialize_arr[ele]['name'] == 'staff_id') {
            if (!staff_id_jundge(serialize_arr[ele]['value'])) {
                swal({
                    title: "工号格式错误!",
                    icon: "error",
                });
                return 0;//0 staff_id格式错误
            }
        } else if (serialize_arr[ele]['name'] == 'ruzhitime') {
            if (!offertime_jundge(serialize_arr[ele]['value'])) {
                swal({
                    title: "入职时间格式错误!",
                    icon: "error",
                });
                return 0;//2 入职时间错误
            }
        } else if (serialize_arr[ele]['name'] == 'dengji') {
            if (!level_jundge(serialize_arr[ele]['value'])) {
                swal({
                    title: "等级格式错误!",
                    icon: "error",
                });
                return 0;//3 等级错误
            }
        } else if (serialize_arr[ele]['name'] == 'iphone') {
            if (!phone_jundge(serialize_arr[ele]['value'])) {
                swal({
                    title: "电话格式错误!",
                    icon: "error",
                });
                return 0;//4 电话错误
            }
        } else if (serialize_arr[ele]['name'] == 'email') {
            if (!email_jundge(serialize_arr[ele]['value'])) {
                swal({
                    title: "邮箱格式错误!",
                    icon: "error",
                });
                return 0;//5 邮箱格式错误
            }
        } else if (serialize_arr[ele]['name'] == 'password') {
            if (!password_jundge(serialize_arr[ele]['value'])) {
                swal({
                    title: "密码格式错误!",
                    text: "包含大小写字母和数字，且长度大于8位",
                    icon: "error",
                });
                return 0;//6 密码格式错误
            }
        } else if (serialize_arr[ele]['name'] == 'diqu') {
            if (!filter_illegal_char(serialize_arr[ele]['value'])) {
                swal({
                    title: "地区格式错误!",
                    icon: "error",
                });
                return 0;//7 地区格式错误
            }
        }
    }
    return true;
}

function filter_illegal_char(s) {
    var pattern = new RegExp("[%--`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——|{}【】‘；：”“'。，、？]");
    var rs = "";
    for (var i = 0; i < s.length; i++) {
        rs = rs + s.substr(i, 1).replace(pattern, '');
    }
    if (s.length != rs.length) {
        return false;
    }
    return true;
}


function email_jundge(str) {
    var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    return reg.test(str)
}

function phone_jundge(str) {
    var reg = /^((0\d{2,3}-\d{7,8})|(1[3456789]\d{9}))$/;
    return reg.test(str)
}

function staff_id_jundge(str) {
    var reg = /^[aA]\d{6}$/;
    return reg.test(str)
}

function password_jundge(password) {//必须为字母加数字且长度不小于8位
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

function offertime_jundge(str) {
    var reg = /^\d{4}-\d{2}-\d{2}$/;
    return reg.test(str)
}

function level_jundge(str) {
    var reg = /^\d$/;
    return reg.test(str)
}
