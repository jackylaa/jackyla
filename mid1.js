function get_c1_data(){
   $.ajax({
      url:"/get_history",
      success: function(data) {
         $(".num h1").eq(0).text(data.comfirmed)
         $(".num h1").eq(1).text(data.crued)
         $(".num h1").eq(2).text(data.died)
      },
      error:function(xhr,type,errorThrow){
      }
   })
}

get_c1_data()
