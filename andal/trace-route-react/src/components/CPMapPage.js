import React, {Component} from 'react'
import data from './mapData/cloudProvider.json'
import H from 'highcharts/highmaps'
import ReactHighmaps from 'react-highcharts/ReactHighmaps.src'
import map from './mapData/world'
import Palette from 'google-material-color-palette-json'

function getData() {
// Add series with state capital bubbles
  var server_data = data.server; //Google
  var agent_data = data.agent;  //Azure
  var network_data = data.network; //Amazon
  // var clients_amazon = data.clientsAmazon;
  // var clients_azure = data.clientsAzure;
  // var clients_google = data.clientsGoogle;
  var best_performers = data.bestPerformers;
  var cur_net_data = [];
  var cur_server_data = [];
  var cur_agent_data =[];
  var cur_clients_to_amazon_data = [];
  var cur_clients_to_azure_data = [];
  var cur_clients_to_google_data = [];
  var planetLabLocations = [];


  // best_performers.forEach( (n) => {
  //   n.z = n.QoE;
  //   if(n.provider == "Amazon") {
  //     cur_clients_to_amazon_data.push(n);
  //   }
  //   if(n.provider == "Azure") {
  //     cur_clients_to_azure_data.push(n);
  //   }
  //
  //   if(n.provider == "Google") {
  //     cur_clients_to_google_data.push(n);
  //   }
  // })

  best_performers.forEach( (n) => {
    n.z = n.QoE;
    if(n.provider == "Amazon") {
      planetLabLocations.push(n);
    }
    if(n.provider == "Azure") {
      planetLabLocations.push(n);
    }

    if(n.provider == "Google") {
      planetLabLocations.push(n);
    }
  })

  const seriesData = [{
    name: 'Basemap',
    mapData: map,
    borderColor: 'rgba(200, 200, 200, 0.9)',
    nullColor: 'rgba(200, 200, 200, 0.4)',
    showInLegend: false
  }];

  seriesData.push({
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.asn}'
    },
    marker: {
          "fillColor": "white",
          "lineColor": "black",
          "lineWidth": 2,
          "radius": 3
    },
    name: "Planet Lab Locations",
    data: planetLabLocations,
    minSize: 0.10,
    maxSize: '150%',
    enableMouseTracking: true,
    color: Palette.grey.shade_200,
    tooltip: {
      pointFormat: '{point.asn}<br>' +
      'ID: {point.netID}<br>' +
      'Lat: {point.lat}<br>' +
      'Lon: {point.lon}<br>' +
      'QoE: {point.QoE}'
    }
  });

  // seriesData.push({
  //   type: 'mappoint',
  //   dataLabels: {
  //     enabled: true,
  //     format: '{point.asn}'
  //   },
  //   name: "Azure dominant PL location",
  //   data: cur_clients_to_azure_data,
  //   minSize: 0.10,
  //   maxSize: '150%',
  //   enableMouseTracking: true,
  //   color: Palette.grey.shade_700,
  //   tooltip: {
  //     pointFormat: '{point.asn}<br>' +
  //     'ID: {point.netID}<br>' +
  //     'Lat: {point.lat}<br>' +
  //     'Lon: {point.lon}<br>' +
  //     'QoE: {point.QoE}'
  //   }
  // });
  //
  // seriesData.push({
  //   type: 'mappoint',
  //   dataLabels: {
  //     enabled: true,
  //     format: '{point.asn}'
  //   },
  //   marker: {
  //     "fillColor": "white",
  //     "lineColor": "black",
  //     "lineWidth": 2,
  //     "radius": 3
  //   },
  //   name: "GCP dominant PL location",
  //   data: cur_clients_to_google_data,
  //   minSize: 0.10,
  //   maxSize: '150%',
  //   enableMouseTracking: true,
  //   color: Palette.grey.shade_900,
  //   tooltip: {
  //     pointFormat: '{point.asn}<br>' +
  //     'ID: {point.netID}<br>' +
  //     'Lat: {point.lat}<br>' +
  //     'Lon: {point.lon}<br>' +
  //     'QoE: {point.QoE}'
  //   }
  // });

  // seriesData.push({
  //   type: 'mappoint',
  //   dataLabels: {
  //     enabled: true,
  //     format: '{point.asn}'
  //   },
  //   name: "Google Experience for PlanetLab Clients",
  //   data: clients_google,
  //   minSize: 0.20,
  //   maxSize: '150%',
  //   enableMouseTracking: true,
  //   color: Palette.cyan.shade_500,
  //   tooltip: {
  //     pointFormat: '{point.asn}<br>' +
  //     'ID: {point.netID}<br>' +
  //     'Lat: {point.lat}<br>' +
  //     'Lon: {point.lon}<br>' +
  //     'QoE: {point.QoE}'
  //   }
  // });
  //
  // seriesData.push({
  //   type: 'mappoint',
  //   dataLabels: {
  //     enabled: true,
  //     format: '{point.asn}'
  //   },
  //   name: "Amazon Experience for PlanetLab Clients",
  //   data: clients_amazon,
  //   minSize: 0.50,
  //   maxSize: '20%',
  //   enableMouseTracking: true,
  //   color: Palette.pink.shade_500,
  //   tooltip: {
  //     pointFormat: '{point.asn}<br>' +
  //     'ID: {point.netID}<br>' +
  //     'Lat: {point.lat}<br>' +
  //     'Lon: {point.lon}<br>' +
  //     'QoE: {point.QoE}'
  //   }
  // });
  //
  // seriesData.push({
  //   type: 'mappoint',
  //   dataLabels: {
  //     enabled: true,
  //     format: '{point.asn}'
  //   },
  //   name: "Azure Experience for PlanetLab Clients",
  //   data: clients_azure,
  //   minSize: 0.50,
  //   maxSize: '20%',
  //   enableMouseTracking: true,
  //   color: Palette.amber.shade_900,
  //   tooltip: {
  //     pointFormat: '{point.asn}<br>' +
  //     'ID: {point.netID}<br>' +
  //     'Lat: {point.lat}<br>' +
  //     'Lon: {point.lon}<br>' +
  //     'QoE: {point.QoE}'
  //   }
  // });

  seriesData.push({
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.asn}'
    },
    name: "AWS Cloud",
    data: network_data,
    minSize: 0.10,
    maxSize: '10%',
    enableMouseTracking: true,
    color: Palette.grey.shade_600,
    tooltip: {
      pointFormat: '{point.asn}<br>' +
      'ID: {point.netID}<br>' +
      'Lat: {point.lat}<br>' +
      'Lon: {point.lon}<br>' +
      'QoE: {point.QoE}'
    }
  });

  seriesData.push({
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.asn}'
    },
    name: "Google Cloud",
    data: server_data,
    minSize: 0.10,
    maxSize: '10%',
    enableMouseTracking: true,
    color: Palette.grey.shade_600,
    tooltip: {
      pointFormat: '{point.asn}<br>' +
      'ID: {point.netID}<br>' +
      'Lat: {point.lat}<br>' +
      'Lon: {point.lon}<br>' +
      'QoE: {point.QoE}'
    }
  });

  seriesData.push({
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.asn}'
    },
    marker: {
      "fillColor": "white",
      "lineColor": "black",
      "lineWidth": 2,
      "radius": 3
    },
    name: "Azure Cloud",
    data: agent_data,
    minSize: 0.10,
    maxSize: '10%',
    enableMouseTracking: true,
    color: Palette.grey.shade_600,
    tooltip: {
      pointFormat: '{point.asn}<br>' +
      'ID: {point.netID}<br>' +
      'Lat: {point.lat}<br>' +
      'Lon: {point.lon}<br>' +
      'QoE: {point.QoE}'
    }
  });

  /*seriesData.push({
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.name}'
    },
    name: "Google",
    data: server_data,
    enableMouseTracking: true,
    color: H.getOptions().colors[1],
    tooltip: {
      pointFormat: '{point.ip}<br>' +
      'Name: {point.name}<br>' +
      'Lat: {point.lat}<br>' +
      'Lon: {point.lon}<br>'
    }
  });

  seriesData.push({
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.name}'
    },
    name: "Azure",
    data: agent_data,
    enableMouseTracking: true,
    color: H.getOptions().colors[2],
    tooltip: {
      pointFormat: '{point.ip}<br>' +
      'Name: {point.name}<br>' +
      'Lat: {point.lat}<br>' +
      'Lon: {point.lon}<br>'
    }
  }); */

  return seriesData;
}

const seriesData = getData();

const config1 = {
  chart: {
    spacingBottom: 20
  },

  title: {
    text: 'Cloud Providers\' locations'
  },


  xAxis: {
    crosshair: {
      zIndex: 5,
      dashStyle: 'dot',
      snap: false,
      color: 'gray'
    }
  },

  yAxis: {
    crosshair: {
      zIndex: 5,
      dashStyle: 'dot',
      snap: false,
      color: 'gray'
    }
  },

  legend: {
    enabled: true
  },

  mapNavigation: {
    enabled: true,
    buttonOptions: {
      verticalAlign: 'bottom'
    }
  },

  series: seriesData
}

export default class CPMapPage extends Component {
  render() {
    return (
      <div>
        <h1>
          Cloud Providers Across the World
        </h1>
        <div>
          <ReactHighmaps config={config1}/>
        </div>
      </div>
    )
  }
}
