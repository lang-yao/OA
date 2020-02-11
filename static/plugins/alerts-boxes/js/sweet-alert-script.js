$(document).ready(function () {

    $("#alert-basic").click(function () {
        swal("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis");
    });

    $("#alert-title").click(function () {
        swal("Here's the title!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis");
    });

    $("#alert-success").click(function () {
        swal("Good job!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis", "success");
    });

    $("#alert-error").click(function () {
        swal("Somthing Wrong!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis,", "error");
    });

    $("#alert-info").click(function () {
        swal("Information!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis,", "info");
    });

    $("#alert-warning").click(function () {
        swal("Warning!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis,", "warning");
    });


    // $("#confirm-btn-alert").click(function () {

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
                url: "/manageradmin/tjd_del/",
                headers: {'X-CSRFtoken': csrfcookies},
                data: {
                    "id": self_id,
                },
                success: function (data, status) {
                    if (status == 'success') {
                        swal("噗 , 删除成功 ! ", {
                            icon: "success",
                        });
                    }
                }
                ,
            });
        } else {
            swal("已经取消删除啦 ! ");
        }
    });

    // });

});

// sloth：
function alert_del_someb(self) {
    var csrfcookies = $.cookie('csrftoken');
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
                url: "/manageradmin/tjd_del/",
                headers: {'X-CSRFtoken': csrfcookies},
                data: {
                    "id": self_id,
                },
                success: function (data, status) {
                    if (status == 'success') {
                        swal("噗 , 删除成功 ! ", {
                            icon: "success",
                        });
                    }
                }
                ,
            });
        } else {
            swal("已经取消删除啦 ! ");
        }
    });

    // swal({
    //     title: "您确定删除吗?",
    //     text: "数据删除后 , 您将无法恢复 !",
    //     icon: "warning",
    //     buttons: true,
    //     dangerMode: true,
    // }).then(function () {
    //     $.ajax({
    //         type: "post",
    //         url: "/manageradmin/tjd_del/",
    //         headers: {'X-CSRFtoken': csrfcookies},
    //         data: {
    //             "id": self_id,
    //         },
    //         success: function (data, status) {
    //             if (status == 'success') {
    //                 swal("噗 , 删除成功 ! ", {
    //                     icon: "success",
    //                 });
    //             }
    //         }
    //         ,
    //     })
    //     ;
    // }
    // );
}