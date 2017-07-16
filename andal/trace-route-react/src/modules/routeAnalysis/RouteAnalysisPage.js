import React, {Component} from 'react'
import ReactHighCharts from 'react-highcharts'
import Palette from 'google-material-color-palette-json'
//import data from './assets/trace-route-analysis'
import sampleClientdata from './assets/oneClientDataSample'
import clientsVsTransitNetworks from './assets/Client_ISPs'
import isp_routers from './assets/ISP_Routers'
import client_isps from './assets/clientISPs'
import cloud_isps from './assets/cloudISPs'
import transit_isps from './assets/transitISPs'
import peer_freq from './assets/peeringFreq'
import cloud_peer from './assets/peering_cloud_CDN'
import client_peer from './assets/peering_transit_client'
import transit_peer from './assets/peering_transit_transit'

import pathLength_azure from './assets/peering/pathLength_azure.json'

const alternateChartBgColor = Palette.blueGrey.shade_50

const pathLengthSeries_1 = []
pathLength_azure.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.id
  cur_data.y = el.pathLength
  cur_data.drilldown = el.id
  pathLengthSeries_1.push(cur_data)
})

const tmpSeries = []
sampleClientdata.routes.forEach(function (el) {
  const cur_data = {}
  if(el.timeTaken != '*') {
    cur_data.name = el.server
    cur_data.y = el.transit
    cur_data.drilldown = el.server
    tmpSeries.push(cur_data)
  }
})

const ISPvsClientsSeries = []
clientsVsTransitNetworks.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.AS + ', ' + el.ISP
  cur_data.y = el.numberOfClients
  ISPvsClientsSeries.push(cur_data)
})
ISPvsClientsSeries.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )

const ClientISPvsRouters = []
const CloudISPvsRouters = []
const TransitISPvsRouters = []

isp_routers.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.AS + ', ' + el.ISP
  cur_data.y = el.routerCount
  if( (client_isps.indexOf(el.AS)) > -1) {
    ClientISPvsRouters.push(cur_data)
  }
  if( (cloud_isps.indexOf(el.AS)) > -1) {
    CloudISPvsRouters.push(cur_data)
  }
  if( (transit_isps.indexOf(el.AS)) > -1) {
    TransitISPvsRouters.push(cur_data)
  }
})
ClientISPvsRouters.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )
CloudISPvsRouters.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )
TransitISPvsRouters.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )

const PeeringvsNumber = []
peer_freq.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.neighborAS + ', ' + el.AS
  cur_data.y = el.number
  PeeringvsNumber.push(cur_data)
})
PeeringvsNumber.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )

const CloudPeeringvsNumber = []
cloud_peer.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.neighborAS + ', ' + el.AS
  cur_data.y = el.number
  CloudPeeringvsNumber.push(cur_data)
})
CloudPeeringvsNumber.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )

const ClientPeeringvsNumber = []
client_peer.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.neighborAS + ', ' + el.AS
  cur_data.y = el.number
  ClientPeeringvsNumber.push(cur_data)
})
ClientPeeringvsNumber.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )

const TransitPeeringvsNumber = []
transit_peer.forEach(function (el) {
  const cur_data = {}
  cur_data.name = el.neighborAS + ', ' + el.AS
  cur_data.y = el.number
  TransitPeeringvsNumber.push(cur_data)
})
TransitPeeringvsNumber.sort(function(a,b) { return parseFloat(b.y) - parseFloat(a.y) } )

// Create the chart
const config = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Path Length per session - Azure '
  },
  subtitle: {
    text: 'May 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Path Length per session'
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
    name: 'Path length of Sessions',
    colorByPoint: true,
    data: pathLengthSeries_1
  }]
}
const config0 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Sessions per Peering '
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of sessions using the peering'
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
    name: 'ISP Peerings',
    colorByPoint: true,
    data: PeeringvsNumber
  }]
}
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
}
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
}
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
}
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
}
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
}
const config6 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Sessions between Cloud and transit/CDN Peerings'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of sessions using the peering'
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
    name: 'Cloud & Transit/CDN Peerings',
    colorByPoint: true,
    data: CloudPeeringvsNumber
  }]
}
const config7 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Sessions between Client and Transit Peerings'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of sessions using the peering'
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
    name: 'Client & Transit Peerings',
    colorByPoint: true,
    data: ClientPeeringvsNumber
  }]
}
const config8 = {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Number of Sessions between Inter ISP transit Peerings'
  },
  subtitle: {
    text: 'Feb 5th 2017'
  },
  xAxis: {
    type: 'category'
  },
  yAxis: {
    title: {
      text: 'Number of sessions using the peering'
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
    name: 'Inter-ISP transit Peerings',
    colorByPoint: true,
    data: TransitPeeringvsNumber
  }]
}

export default class RouteAnalysisPage extends Component {
  render() {
    const configs = [config, config0, config6, config7, config8, config1, config2, config3, config4, config5]
    return (
      <div>
        <h1>Route Analysis Page</h1>
        <div style={{width:'100%'}}>
          {
            configs.map((c, idx) => {
              if(idx %2 === 1) {
                c.chart.backgroundColor = alternateChartBgColor
              }
              return (
                <ReactHighCharts config={c}/>
              )
            })
          }
        </div>
      </div>
    )
  }
}
