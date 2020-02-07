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

    //     swal({
    //         title: "您确定删除吗?",
    //         text: "数据删除后 , 您将无法恢复 !",
    //         icon: "warning",
    //         buttons: true,
    //         dangerMode: true,
    //     }).then((willDelete) => {
    //             if (willDelete) {
    //                 swal("噗 , 删除成功 ! ", {
    //                     icon: "success",
    //                 });
    //             } else {
    //                 swal("已经取消删除啦 ! ");
    //             }
    //         });

    // });

});

// sloth：
function alert_del_someb() {
    swal({
        title: "您确定删除吗?",
        text: "数据删除后 , 您将无法恢复 !",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(function () {
        $.ajax({
            type: "post",
            url: "/manageradmin/tjd_del/",
            data: {
                "id": 1
            },
            success: function (data, status) {
                if (status == "success") {
                    alert(1);
                }
            },
        });
    });
}