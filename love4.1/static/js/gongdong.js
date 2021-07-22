 $(document).ready(function () {
            setInterval(function () {
                location.reload();
            }, 6000000);

        });

        var MyMarhq = '';
        clearInterval(MyMarhq);
        $('.tbl-body tbody').empty();
        $('.tbl-header tbody').empty();
        var str = '';
        var Items = "";

        $.ajax({
            type: "post",
            cache: false,
            async: false,
            url: "webtest.aspx?Oper=load_list&key=" + Math.random(),
            dataType: "json",
            success: function (data) {
                Items = data;
            }
        });



        $.each(Items, function (i, item) {
            str = '<tr>' +
        '<td>' + item.PRODUCT_NAME + '</td>' +
        '<td>' + item.QUANTITY + '</td>' +
        '<td>' + item.STEP_NAME + '</td>' +
        '</tr>'

            $('.tbl-body tbody').append(str);
            $('.tbl-header tbody').append(str);
        });

        if (Items.length > 10) {
            $('.tbl-body tbody').html($('.tbl-body tbody').html() + $('.tbl-body tbody').html());
            $('.tbl-body').css('top', '0');
            var tblTop = 0;
            var speedhq = 50; // 数值越大越慢
            var outerHeight = $('.tbl-body tbody').find("tr").outerHeight();
            function Marqueehq() {
                if (tblTop <= -outerHeight * Items.length) {
                    tblTop = 0;
                } else {
                    tblTop -= 1;
                }
                $('.tbl-body').css('top', tblTop + 'px');
            }

            MyMarhq = setInterval(Marqueehq, speedhq);

            // 鼠标移上去取消事件
            $(".tbl-header tbody").hover(function () {
                clearInterval(MyMarhq);
            }, function () {
                clearInterval(MyMarhq);
                MyMarhq = setInterval(Marqueehq, speedhq);
            })

        }