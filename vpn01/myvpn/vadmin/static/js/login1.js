/**
 * Created by xiaoxin on 16/5/23.
 */
$(document).ready(function () {

    window.onload = function () {
        $(".userspan1").hide();
        $(".userspan2").hide();
        $(".passspan1").hide();
        $(".passspan2").hide();
    }

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

    }
    function show_message(message) {
        $("#message").text(message);
        $("#msg").show();
    }
    $("#username").bind('input propertychange', function () {
        form_check('.user', '#username', '.userspan1', '.userspan2');
    })
    $("#password").bind('input propertychange', function () {
        form_check('.pass', '#password', '.passspan1', '.passspan1');

    });
    $(".submit").click(function () {
        show_message('用户或密码不能为空!');
        var user = form_check('.user', '#username', '.userspan1', '.userspan2');
        var pass = form_check('.pass', '#password', '.passspan1', '.passspan1');
        if (! user || ! pass){
            show_message('用户或密码不能为空!');
            $("p").hide(1000);
            //return false;
        }
    });
    function loginform() {
        $.post("login", {'username':'aaa', "password":"xiaoxin"}, function (data) {
            if (data == "ok"){
                alert("ok");
            }else{
                alert("fail");
            }
        });
    };
});

// window.load.href 登陆成功后需要用的函数跳转到页面
/*$(function () {
 $("#login").click(function () {
 var name = $("#userName").val();
 var pwd = $("#userPwd").val();

 $.post("Login.ashx", { n: name, p: pwd }, function (data) {
 if (data == 'ok') {
 alert("登录成功");
 $(function () {
 window.location.href = "/Default.aspx";
 })

 } else {
 alert("登录失败");
 }
 });
 });

 });
 */