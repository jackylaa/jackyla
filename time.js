
function get_time(){
   $.ajax({
      url:"/get_time_data",
      timeout:10000,
      success: function(data) {
         $("#time").html(data)
         },
         error:function(xhr,type,errorThrow){
         }
   });
}
get_time()