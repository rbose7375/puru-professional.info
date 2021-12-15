// var alert = bootbox.alert('Massage')
// alert.show();
// setTimeout(function() { alert.modal('hide'); }, 4000);

// let warn = document.getElementById('warn');
// // console.log(warn.innerText);
// let data = document.getElementsByID('msg')
// data = Array(data);

function myFunction() {
    var myobj = document.getElementById("msg");
    myobj.remove();
}


function myFunctions() {
    setTimeout(function() {
        var myobj = document.getElementById("msg");
        myobj.remove();
    }, 500);
}