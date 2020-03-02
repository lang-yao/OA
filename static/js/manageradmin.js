function add_input_id(self) {
    ele_id = self.previousElementSibling.value;
    ele = document.createElement('input');
    ele.setAttribute('value', ele_id);
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'id');
    par = document.getElementsByClassName('modal-body')[0].firstElementChild;
    par.append(ele);
}

function xuqiu_add_hidden(hid_id) {
    var lab_diqu = document.getElementsByClassName("modal-body")[0].children[0].children[2];
    var sel_diqu = document.getElementsByClassName("modal-body")[0].children[0].children[3].children[0];
    if (hid_id == '2') {
        lab_diqu.style.display = 'none';
        sel_diqu.style.display = 'none';
    } else if (hid_id == '1') {
        lab_diqu.style.display = 'block';
        sel_diqu.style.display = 'block';
    }
}

function add_input_id(self) {
    ele_id = self.previousElementSibling.value;
    ele = document.createElement('input');
    ele.setAttribute('value', ele_id);
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'id');
    par = document.getElementsByClassName('modal-body')[0].firstElementChild;
    par.append(ele);
}

function xuqiu_his_hidden(hid_id) {
    var lab_diqu = document.getElementsByClassName("modal-body")[0].children[0].children[2];
    if (hid_id == '3') {
        lab_diqu.style.display = 'none';
    } else if (hid_id == '1') {
        lab_diqu.style.display = 'block';
    }
}

function access_data(self) {
    var csrfcookies = $.cookie('csrftoken');
    var demand_id = self.parentElement.firstElementChild.value;
    var dirc = {};
    $.ajax({
        type: "POST",
        headers: {
            'X-CSRFtoken': csrfcookies,
        },
        url: "/manageradmin/query_demand_person/",
        data: {
            id: demand_id,
        },
        async: false,   //异步等待
        success: function (data) {
            dirc = data;
            var tab = document.getElementById("access_tab").children[1];
            tab.innerHTML = "";
            if (document.getElementsByName('xmxqd_id').length == 0) {
                var ele = document.createElement('input');
                ele.setAttribute('value', demand_id);
                ele.setAttribute('type', 'hidden');
                ele.setAttribute('name', 'xmxqd_id');
                document.getElementById("access_tab").append(ele);
            }
            for (var staff_id in data) {
                if (data[staff_id]['access'] == '') {
                    var new_tr = '<tr><td>' + staff_id + "</td><td>" + data[staff_id]['name'] + "</td><td><div class='fivestar'>未评价</div></td></tr>"
                } else {
                    var new_tr = '<tr><td>' + staff_id + "</td><td>" + data[staff_id]['name'] + "</td><td><div class='fivestar'></div></td></tr>"
                }
                tab.innerHTML = tab.innerHTML + new_tr;
            }
        }
    });
    var stars = document.getElementsByClassName("fivestar");
    $(stars).each(function (index, star) {
        var id = star.parentElement.parentElement.firstElementChild.innerText;
        if (dirc[id]['access'] != '') {
            $(star).markingSystem({
                num: 5,
                unit: '星',
                grade: dirc[id]['access'],
                height: 20,
                width: 20,
            });
        }
    });
}

function submit_add_person() {
    $.ajax({
        type: "POST",
        url: "/manageradmin/tjd_add/",
        data: $('#add').serialize(),// 序列化表单值
        async: false,
        success: function (data) {
            if (data['status'] == 'success') {
                swal({
                    title: "人员添加成功!",
                    icon: "success",
                }).then((clc) => {
                    window.location.href = "/manageradmin/tjd_list/"
                });
            } else {
                if (data['err'] == 'staff_id') {
                    swal({
                        title: "工号不能重复",
                        icon: "error",
                    })
                }
            }
        }
    });
}

function modify_person() {
    $.ajax({
        type: "POST",
        url: "/manageradmin/tjd_update/",
        data: $('#modify').serialize(),// 序列化表单值
        async: false,
        success: function (data) {
            if (data['status'] == 'success') {
                swal({
                    title: "信息修改成功!",
                    icon: "success",
                }).then((clc) => {
                    window.location.href = "/manageradmin/tjd_list/"
                });
            } else {
                if (data['err'] == 'staff_id') {
                    swal({
                        title: "工号不能重复",
                        icon: "error",
                    })
                }
            }
        }
    });
}

function get_modify_msg(self) {
    var per_id = self.previousElementSibling.value;
    var first_name = self.innerText;
    var staff_id = self.nextElementSibling.innerText;
    var offer_time = self.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
    var area = self.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
    var level = self.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
    offer_time = offer_time.replace(/\//g, '-');
    document.getElementById('input-0').value = per_id;
    document.getElementById('input-1').value = first_name;
    document.getElementById('input-2').value = staff_id;
    document.getElementById('autoclose-datepicker').value = offer_time;
    document.getElementById('input-5').value = area;
    document.getElementById('input-6').value = level;
}

function submit_add_person() {
    $.ajax({
        type: "POST",
        url: "/manageradmin/manager_user_add/",
        data: $('#add').serialize(),// 序列化表单值
        async: false,
        success: function (data) {
            if (data['status'] == 'success') {
                swal({
                    title: "人员添加成功!",
                    icon: "success",
                }).then((clc) => {
                    window.location.href = "/manageradmin/manager_user_list/"
                });
            } else {
                if (data['err'] == 'username') {
                    swal({
                        title: "用户名不能重复",
                        icon: "error",
                    })
                } else if (data['err'] == 'staff_id') {
                    swal({
                        title: "工号不能重复",
                        icon: "error",
                    })
                } else if (data['err'] == 'iphone') {
                    swal({
                        title: "电话不能重复",
                        icon: "error",
                    })
                } else if (data['err'] == 'email') {
                    swal({
                        title: "邮箱不能重复",
                        icon: "error",
                    })
                }
            }
        }
    });
}


function modify_clerk_staff() {
    $.ajax({
        type: "POST",
        url: "/manageradmin/modify_staff/",
        data: $('#modify').serialize(),// 序列化表单值
        async: false,
        success: function (data) {
            if (data['status'] == 'success') {
                swal({
                    title: "信息修改成功!",
                    icon: "success",
                }).then((clc) => {
                    window.location.href = "/manageradmin/manager_user_list/"
                });
            } else {
                if (data['err'] == 'username') {
                    swal({
                        title: "用户名不能重复",
                        icon: "error",
                    })
                } else if (data['err'] == 'staff_id') {
                    swal({
                        title: "工号不能重复",
                        icon: "error",
                    })
                } else if (data['err'] == 'iphone') {
                    swal({
                        title: "电话不能重复",
                        icon: "error",
                    })
                } else if (data['err'] == 'email') {
                    swal({
                        title: "邮箱不能重复",
                        icon: "error",
                    })
                }
            }
        }
    });
}