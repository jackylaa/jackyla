var ec_right2=echarts.init(document.getElementById('r2'),"dark");
var ec_right2_Option={
   title:{
      text:"湖北地区城市确诊TOP5",
      textStyle:{
         color:'white',
      },
      left:'left',
   },
     color:['#3398DB'],
       tooltip:{
          trigger:'axis',
          axisPointer:{
             type:'shadow',
         }
      },
   xAxis:{
      type:'category',
      data:[]
   },
   yAxis:{
      type:'value',
   },
   series:[{
      data:[],
      type:'bar',
      barMaxWidth:"50%"
   }]
};
ec_right2.setOption(ec_right2_Option)
function get_r2_data(){
   $.ajax({
      url:"/get_right2_data",
      success: function(data) {
         ec_right2_Option.xAxis.data=data.city;
         ec_right2_Option.series[0].data=data.comfirmed;
         ec_right2.setOption(ec_right2_Option);
      }
   })
}
get_r2_data()