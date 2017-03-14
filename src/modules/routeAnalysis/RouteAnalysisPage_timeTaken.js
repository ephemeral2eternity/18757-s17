// import React, {Component} from 'react'
// import ReactHighCharts from 'react-highcharts'
// import data from './assets/trace-route-analysis.json'
//
// const tmpSeries = [];
// data.forEach(function (el) {
//   const cur_data = {};
//   if(el.timeTaken != '*') {
//     cur_data.name = el.id;
//     cur_data.y = el.timeTaken;
//     cur_data.drilldown = el.id;
//     tmpSeries.push(cur_data);
//   }
// });
// console.log(tmpSeries);
//
// // Create the chart
// const config = {
//   chart: {
//     type: 'column'
//   },
//   title: {
//     text: 'Time Taken To Reach Servers on a busy Internet Day'
//   },
//   subtitle: {
//     text: 'Feb 5th 2017'
//   },
//   xAxis: {
//     type: 'category'
//   },
//   yAxis: {
//     title: {
//       text: 'Time Taken for trace route to servers'
//     }
//
//   },
//   legend: {
//     enabled: true
//   },
//   plotOptions: {
//     series: {
//       borderWidth: 0,
//       dataLabels: {
//         enabled: true,
//         format: '{point.y:.1f}ms'
//       }
//     }
//   },
//
//   tooltip: {
//     headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
//     pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
//   },
//
//   series: [{
//     name: 'Servers',
//     colorByPoint: true,
//     data: tmpSeries
//   }]
// };
//
// export default class RouteAnalysisPage extends Component {
//   render() {
//     return (
//       <div>
//         <h1>Route Analysis Page</h1>
//         <div style={{width:'100%'}}>
//           <ReactHighCharts config={config}/>
//         </div>
//       </div>
//     )
//   }
// }
