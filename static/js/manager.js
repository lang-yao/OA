function submit_add_demand() {
    $.ajax({
        type: "POST",
        url: "/manager/manager_xqadd/",
        data: $('#add').serialize(),// 序列化表单值
        async: false,
        success: function (data) {
            if (data['status'] == 'success') {
                swal({
                    title: "添加成功!",
                    icon: "success",
                }).then((clc) => {
                    window.location.href = "/manager/manager_xqadd/"
                });
            }
        }
    });
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
        url: "/manager/query_demand_person/",
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
                var new_tr = '<tr><td>' + staff_id + "</td><td>" + data[staff_id]['name'] + "</td><td><div class='fivestar'></div></td></tr>"
                tab.innerHTML = tab.innerHTML + new_tr;
            }
        }
    });
    var stars = document.getElementsByClassName("fivestar");
    $(stars).each(function (index, star) {
        var id = star.parentElement.parentElement.firstElementChild.innerText;
        $(star).markingSystem({
            num: 5,
            unit: '星',
            grade: dirc[id]['access'],
            height: 20,
            width: 20,
        });
    });
}

function access_staff() {
    var csrfcookies = $.cookie('csrftoken');
    var demand_id = document.getElementById("access_tab").lastElementChild.value;
    var trs = document.getElementById("access_tab").firstElementChild.nextElementSibling;
    var access_of_all = {};
    $(trs.children).each(function (index, element) {
        var staff_id = element.firstElementChild.innerText;
        var access_num = element.lastElementChild.firstElementChild.firstElementChild.lastElementChild.childElementCount;
        access_of_all[staff_id] = access_num
    });
    for (var i in access_of_all) {
        console.log(i, access_of_all[i])
        if (access_of_all[i] == 0) {
            swal({
                title: "未评完成价!",
                text: "请确认所有人员已评价。",
                icon: "error",
            });
            return;
        }
    }
    $.ajax({
        type: "POST",
        headers: {
            'X-CSRFtoken': csrfcookies,
        },
        dataType: "json",
        url: "/manager/deman_access/",
        data: JSON.stringify({
            id: demand_id,
            access_data: access_of_all,
        }),
        async: false,   //异步等待
        success: function (data) {
            if (data['status'] == 'success') {
                swal({
                    title: "评价成功!",
                    icon: "success",
                }).then((clc) => {
                    window.location.href = "/manager/manager_xqhistory"
                });
            }
        }
    });
}