import React, {Component} from 'react'
import ReactHighCharts from 'react-highcharts'
//import data from './assets/trace-route-analysis.json'
import sampleClientdata from './assets/oneClientDataSample.json'
import clientsVsTransitNetworks from './assets/Client_ISPs.json'
import isp_routers from './assets/ISP_Routers.json'
import client_isps from './assets/clientISPs.json'
import cloud_isps from './assets/cloudISPs.json'
import transit_isps from './assets/transitISPs.json'

const tmpSeries = [];
sampleClientdata.routes.forEach(function (el) {
  const cur_data = {};
  if(el.timeTaken != '*') {
    cur_data.name = el.server;
    cur_data.y = el.transit;
    cur_data.drilldown = el.server;
    tmpSeries.push(cur_data);
  }
});
console.log(tmpSeries);

const ISPvsClientsSeries = [];
clientsVsTransitNetworks.forEach(function (el) {
  const cur_data = {};
  cur_data.name = el.AS + ', ' + el.ISP;
  cur_data.y = el.numberOfClients;
  ISPvsClientsSeries.push(cur_data);
});
console.log(ISPvsClientsSeries);
ISPvsClientsSeries.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } );

const ClientISPvsRouters = [];
const CloudISPvsRouters = [];
const TransitISPvsRouters = [];

isp_routers.forEach(function (el) {
  const cur_data = {};
  cur_data.name = el.AS + ', ' + el.ISP;
  cur_data.y = el.routerCount;
  if( (client_isps.indexOf(el.AS)) > -1) {
    ClientISPvsRouters.push(cur_data);
  }
  if( (cloud_isps.indexOf(el.AS)) > -1) {
    CloudISPvsRouters.push(cur_data);
  }
  if( (transit_isps.indexOf(el.AS)) > -1) {
    TransitISPvsRouters.push(cur_data);
  }
});
ClientISPvsRouters.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } );
CloudISPvsRouters.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } );
TransitISPvsRouters.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } );

// Create the chart
const config1 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Transit Networks Per Session for Client ' + sampleClientdata.client
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
const config2 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Clients Per ISP'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of Clients using the ISP'
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
    name: 'ISPs',
    colorByPoint: true,
    data: ISPvsClientsSeries
  }]
};
const config3 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Routers Per Transit ISP'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of Routers'
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
    name: 'Transit ISPs',
    colorByPoint: true,
    data: TransitISPvsRouters
  }]
};
const config4 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Routers Per Cloud ISP'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of Routers'
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
    name: 'Cloud ISPs',
    colorByPoint: true,
    data: CloudISPvsRouters
  }]
};
const config5 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Routers Per Client ISP'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of Routers'
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
    name: 'Client ISPs',
    colorByPoint: true,
    data: ClientISPvsRouters
  }]
};

export default class RouteAnalysisPage extends Component {
  render() {
    return (
      <div>
        <h1>Route Analysis Page</h1>
        <div style={{width:'100%'}}>
          <ReactHighCharts config={config1}/>
          <ReactHighCharts config={config2}/>
          <ReactHighCharts config={config3}/>
          <ReactHighCharts config={config4}/>
          <ReactHighCharts config={config5}/>
        </div>
      </div>
    )
  }
}
