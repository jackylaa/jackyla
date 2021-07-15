var china_map = echarts.init(document.getElementById('c2','dark'));

var my_data=[{'name':'上海','value':318}]

var china_map_option={
   title:{
      text: '中国疫情图',
      subtext: '',
      x: 'left'
   },
   tooltip:{
      trigger:'item'
   },
   //左侧小导航图标
   visualMap:{
      show:true,
      x:'left',
      y:'bottom',
      textStyle:{
         fontSize:8,
      },
      splitList: [{start:1,end:9},
          {start:10,end:99},
         {start:100,end:999},
         {start:1000,end:9999},
         {start:10000}],
      color:['#8A3310','#C64918','#E55B25','#F2AD92','#F9DCD1']
   },
   series:[{
      name:'累计确诊人数',
      type:'map',
      mapType:'china',
      roam:false,
      itemStyle:{
         normal:{
            borderWidth:.5,//区域边框宽度
            borderColor:'#009fe8',//区域边框颜色
            areaColor:'#ffefd5',//区域颜色
         },
         emphasis:{//鼠标划过地图高亮
            borderWidth:.5,
            borderColor:'#4b0082',
            areaColor:"#fff",
         }
      },
      label:{
         normal:{
            show:true,
            fontSize:8,
         },
         emphasis:{
            show:true,
            fontSize:8,
         }
      },
      data: my_data//数据
   }]
};
china_map.setOption(china_map_option)

function get_c2_data(){
   $.ajax({
      url:"/get_china_map_data",
      success: function(data) {
         china_map_option.series[0].data=data.data
         china_map.setOption(china_map_option)
      },
      error:function(xhr,type,errorThrow){
      }
   })
}
get_c2_data()