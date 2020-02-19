// sloth：
function person_del(self) {
    var csrfcookies = $.cookie('csrftoken');
    var path = window.location.pathname.split('/');
    var choice = (new Date()).valueOf();
    if (path[2] == 'tjd_list') {
        choice = choice | 1;
    } else {
        choice = choice << 1;
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
                url: '/manageradmin/del/',
                headers: {
                    'X-CSRFtoken': csrfcookies,
                    'del-path': window.location.pathname,
                },
                data: {
                    "id": self_id,
                    'choice': choice,
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