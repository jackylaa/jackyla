var ec_right1=echarts.init(document.getElementById('r1'),"dark");
var ec_right1_Option={
   title:{
      text:"非湖北地区城市确诊TOP5",
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
ec_right1.setOption(ec_right1_Option)
function get_r1_data(){
   $.ajax({
      url:"/get_right1_data",
      success: function(data) {
         ec_right1_Option.xAxis.data=data.city;
         ec_right1_Option.series[0].data=data.comfirmed;
         ec_right1.setOption(ec_right1_Option);
      }
   })
}
get_r1_data()