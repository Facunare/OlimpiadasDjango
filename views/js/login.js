

$(".inputs").on("focus", function (e) {
  $(`label[for='${e.currentTarget.id}']`).addClass("labelActive");
});
$(".inputs").on("blur", function (e) {
  if (e.currentTarget.value == "") {
    $(`label[for='${e.currentTarget.id}']`).removeClass("labelActive");
  }
});
$(".togglePassword").on("click",e=>{
    console.log()

    $(e.currentTarget.offsetParent.children[0]).attr("type",$(e.currentTarget.offsetParent.children[0]).attr("type") == "text" ? "password" : "text")
    if($(e.currentTarget.offsetParent.children[0]).attr("type") != "password"){
        e.currentTarget.src = "./imgs/eye-slash.svg"
    }else{
        e.currentTarget.src = "./imgs/eye.svg"

    }
})
