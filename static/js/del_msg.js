// sloth：
function person_del(self) {
    var csrfcookies = $.cookie('csrftoken');
    var path = window.location.pathname.split('/');
    if (path[2] == 'tjd_list') {
        path = '/' + path[1] + '/tjd_del/';
    } else {
        path = '/' + path[1] + '/manager_user_del/';
    }
    var self_id = self.parentElement.parentElement.children[0].value;
    swal({
        title: "您确定删除吗?",
        text: "数据删除后 , 您将无法恢复 !",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: "post",
                url: path,
                headers: {'X-CSRFtoken': csrfcookies},
                data: {
                    "id": self_id,
                },
                success: function (data, status) {
                    if (status == 'success') {
                        // swal("噗 , 删除成功 ! ", {
                        //     icon: "success",
                        // });
                        location.reload();
                    }
                }
                ,
            });
        } else {
            swal("已经取消删除啦 ! ");
        }
    });

}