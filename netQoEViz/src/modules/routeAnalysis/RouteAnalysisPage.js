import React, {Component} from 'react'
import ReactHighCharts from 'react-highcharts'
//import data from './assets/trace-route-analysis.json'
import data from './assets/clientVsServers.json'

const tmpSeries = [];
data.routes.forEach(function (el) {
  const cur_data = {};
  if(el.timeTaken != '*') {
    cur_data.name = el.server;
    cur_data.y = el.transit;
    cur_data.drilldown = el.server;
    tmpSeries.push(cur_data);
  }
});
console.log(tmpSeries);

// Create the chart
const config = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Transit Networks Per Session for Client ' + data.client
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of Transit Networks Per session'
    }

  },
  legend: {
    enabled: true
  },
  plotOptions: {
    series: {
      borderWidth: 0,
      dataLabels: {
        enabled: true,
        format: '{point.y}'
      }
    }
  },

  tooltip: {
    headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
    pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}%</b> of total<br/>'
  },

  series: [{
    name: 'Servers',
    colorByPoint: true,
    data: tmpSeries
  }]
};

export default class RouteAnalysisPage extends Component {
  render() {
    return (
      <div>
        <h1>Route Analysis Page</h1>
        <div style={{width:'100%'}}>
          <ReactHighCharts config={config}/>
        </div>
      </div>
    )
  }
}
