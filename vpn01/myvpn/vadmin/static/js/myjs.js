/**
 * Created by xiaoxin on 16/5/20.
 */

function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return decodeURI(r[2]); return null;
}
var ShowMsg = function(){
    var code = getUrlParam('code');
    if (code === '1')
    {
        $('#msg').modal("show")
    }

}
ShowMsg();