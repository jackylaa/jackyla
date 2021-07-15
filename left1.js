var ec_left1 = echarts.init(document.getElementById('l1'), "dark");
var ec_left1_Option = {
   title: {
      text: "全国累计趋势",
      textStyle: {
         //color:'white',
      },
      left: 'left',
   },
   tooltip: {
      trigger: 'axis',
      axisPointer: {
         type: 'line',
         lineStyle: {
            color: '#7171C6'
         }
      },
   },
   legend: {
      data: ["累计确诊", "累积治愈", "累计死亡"],
      left: "right"
   },
   //图形位置
   grid: {
      left: '4%',
      right: '6%',
      bottom: '4%',
      top: 50,
      containLabel: true
   },
   xAxis: [{
      type: 'category',
      data: []
   }],
   yAxis: [{
      type: 'value',
      axisLabel: {
         show: true,
         color: 'white',
         fontSize: 12,
         formatter: function(value) {
            if (value >= 1000) {
               value = value / 1000 + 'k';
            }
            return value;
         }
      },
      //y轴线设置显示
      axisLine: {
         show: true
      },
      //与x轴平行的线样式
      splitLine: {
         show: true,
         lineStyle: {
            color: '#17273B',
            width: 1,
            type: 'solid',
         }
      }
   }],
   series: [{
      name: "累计确诊",
      type: 'line',
      smooth: true,
      data: []
   }, {
      name: "累积治愈",
      type: 'line',
      smooth: true,
      data: []
   },{
      name: "累计死亡",
      type: 'line',
      smooth: true,
      data: []
   }]
};
ec_left1.setOption(ec_left1_Option)

function get_l1_data(){
   $.ajax({
      url:'/get_left1_data',
      success: function(data) {
         ec_left1_Option.xAxis[0].data=data.day
         ec_left1_Option.series[0].data=data.comfirmed
         ec_left1_Option.series[1].data=data.crued
         ec_left1_Option.series[2].data=data.died
         ec_left1.setOption(ec_left1_Option)
      },
      error:function(xhr,type,errorThrow){
      }
   })
}
get_l1_data()