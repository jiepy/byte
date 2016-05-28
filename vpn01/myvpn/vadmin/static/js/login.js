/**
 * Created by xiaoxin on 16/5/23.
 */
$(document).ready(function () {

    window.onload = function () {
        $(".userspan1").hide();
        $(".userspan2").hide();
        $(".passspan1").hide();
        $(".passspan2").hide();
        $("#username").focus();
    };
    function form_check(divclass, idname, spanclass1, spanclass2) {
        if (!$(idname).val())
        {
            $(divclass).removeClass('has-success has-feedback');
            $(divclass).addClass('has-error has-feedback');
            $(spanclass1).removeClass('glyphicon-ok').addClass('glyphicon-remove')
            $(spanclass1).show();
            $(spanclass2).show();
            return false;
        }else
        {
            $(divclass).removeClass('has-error has-feedback')
            $(divclass).addClass('has-success has-feedback');
            $(spanclass1).removeClass('glyphicon-remove').addClass('glyphicon-ok')
            $(spanclass1).show();
            $(spanclass2).show();
            return true;
        };

    };
    function loginform() {

        $.post("vpn/check/", {'username':$('#username').val(), "password":$('#password').val()}, function (data) {
            if (data == "1"){
                window.location.href = "mod";
            }else{
                show_message('用户或密码错误!');
            }
        });
    };
    function show_message(message) {
        $("#message").text(message);
        $("#msg").show()
    };
    $("#username").bind('input propertychange', function () {
        form_check('.user', '#username', '.userspan1', '.userspan2');
    });
    $("#password").bind('input propertychange', function () {
        form_check('.pass', '#password', '.passspan1', '.passspan1');
    });
    $(".close").click(function () {
        $("#msg").hide();
    });
    $("#username").focus(function () {
        $(window).keydown(function(event){
            if (event.keyCode == "13" ){
                $("#loginsub").focus();
            };
        });
    });
    $("#loginsub").click(function(){
        var user = form_check('.user', '#username', '.userspan1', '.userspan2');
        var pass = form_check('.pass', '#password', '.passspan1', '.passspan1');
        if (! user || ! pass) {
            show_message('用户或密码不能为空!');
            return false;
        } else {
            loginform();
        };
    });
});