import React, {Component} from 'react'
import proj4 from 'proj4'
window.proj4 = proj4
import HighCharts from 'highcharts/highmaps'
import ReactHighmaps from 'react-highcharts/ReactHighmaps.src'
import maps from './mapData/world'
import Palette from 'google-material-color-palette-json'
import dataSet from '../modules/routeAnalysis/assets/nodes_links_data_initial_viz'
import darkTheme from 'highcharts/themes/dark-unica'
darkTheme(HighCharts)

// Add series with state capital bubbles
const impNodes = []
const data = []
dataSet.nodes.forEach(function (e) {
  //delete e.name;
  e.z = e.number
  if (e.number > 6) {
    //e.color = '#' + Math.floor(Math.random() * 16777215).toString(16);
    e.color = Palette.deepOrange.shade_500
    //e.legend = e.name;
    impNodes.push(e)
  } else {
    data.push(e)
  }
})

const tmpSeries = []
dataSet.links.forEach(function (el) {
  const cur_data = [data[el.source], data[el.target]]
  const cur_series_point = {        // Specify points using lat/lon
    type: 'mappoint',
    id: 'connected-points',
    name: 'Connection',
    cursor: 'move',
    //color: '#' + Math.floor(Math.random() * 16777215).toString(16),
    color: '#333',
    lineWidth: 2,
    showInLegend: false,
    data: cur_data
  }
  tmpSeries.push(cur_series_point)
})

const config2 = {
  chart: {
    spacingBottom: 20
  },

  title: {
    text: 'ISP-s around the World!'
  },

  legend: {
    enabled: true
  },

  mapNavigation: {
    enabled: true,
    enableDoubleClickZoomTo: true
  },

  tooltip: {
    pointFormat: '{point.AS}, {point.name}<br>' +
    'Lat: {point.lat}<br>' +
    'Lon: {point.lon}<br>' +
    'number: {point.number}'
  },

  xAxis: {
    crosshair: {
      zIndex: 5,
      dashStyle: 'dot',
      snap: false,
      //color: 'gray'
    }
  },

  yAxis: {
    crosshair: {
      zIndex: 5,
      dashStyle: 'dot',
      snap: false,
      //color: 'gray'
    }
  },
  /*
   plotOptions: {
   map: {
   allAreas: true,
   joinBy: ['iso-a2', 'code'],
   dataLabels: {
   enabled: true,
   color: 'white',
   style: {
   fontWeight: 'bold'
   }
   }
   ,
   mapData: maps,
   tooltip: {
   headerFormat: '',
   pointFormat: '{point.AS}, {point.name}<br>' +
   //pointFormat: '{point.AS}<br>' +
   'Lat: {point.lat}<br>' +
   'Lon: {point.lon}<br>' +
   'number: {point.number}'
   }

   }
   },
   */

  series: [{
    name: 'Basemap',
    mapData: maps,
    borderColor: '#606060',
    nullColor: 'rgba(200, 200, 200, 0.2)',
    showInLegend: false
  }, {
    name: 'Separators',
    type: 'mapline',
    data: HighCharts.geojson(maps, 'mapline'),
    color: '#101010',
    enableMouseTracking: false,
    showInLegend: false
  }, {

    type: 'mapbubble',
    dataLabels: {
      enabled: true,
      format: '{point.AS}'
    },
    name: 'ISPs',
    data: impNodes,
    maxSize: '12%',
    color: HighCharts.getOptions().colors[0]
    //color: data.color
  }, {
    type: 'mappoint',
    dataLabels: {
      enabled: true,
      format: '{point.AS}'
    },
    name: 'ISPs',
    data: data,
    maxSize: '12%',
    color: Palette.green.shade_500
  }].concat(tmpSeries)
}

export default class MapPage extends Component {
  render() {
    return (
      <div>
        <h1>
          Map Page
        </h1>
        <div>
          <ReactHighmaps config={config2}/>
        </div>
      </div>
    )
  }
}
