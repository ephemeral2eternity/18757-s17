import React, {Component} from 'react'
import d3 from 'd3';
import _ from 'lodash';
import RAW_DATA from './assets/sample.json'
import './peeringVisualization.css'

function prepareMatrix(uniqueKeys, data) {
  const matrix = []
  keys.forEach((row) => {
    const rowSet = []
    keys.forEach(col => {
      let colValue = 0
      if (row !== col) {
        // const combinationsRowToCol = data.filter(r => (r.key === row && (r.imports_1 === col || r.imports_2 === col)))
        const combinationsRowToCol = []
        const combinationsColToRow = data.filter(r => (r.AS === col && (r.upperBoundAS === row || r.lowerBoundAS === row)))
        colValue = combinationsColToRow.length + combinationsColToRow.length
      }
      rowSet.push(colValue)
    })
    matrix.push(rowSet)
  })
  return matrix
}

const COLORS = ["#E41A1C","#FFFF33","#FF7F00","#FF7F00","#FF7F00","#FF7F00","#FF7F00","#FF7F00","#999999","#984EA3","#984EA3","#984EA3","#984EA3","#984EA3","#984EA3","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#377EB8","#4DAF4A","#4DAF4A","#4DAF4A","#4DAF4A","#4DAF4A","#F781BF","#F781BF","#F781BF","#A65628",""]

let keys = RAW_DATA.map(e => [e.AS, e.imports_1 || e.AS, e.imports_2 || e.AS])
keys = _.uniq([].concat.apply([], keys))
keys.sort((a, b) => a - b)
const matrix = prepareMatrix(keys, RAW_DATA);
// console.log(matrix)

const groups = keys.map((e, idx) => {
  return {
    name: e,
    //ISP: _.uniq(RAW_DATA.filter(el => (el.AS === e && el.ISP)).map(el => el.ISP? el.ISP: "")).join(", ").trim(),
    population: RAW_DATA.filter(el => (el.AS === e || el.imports_1 === e || el.imports_2 === e)).length,
    // color: COLORS[idx % COLORS.length - 1]
    color: COLORS[idx * 2]
  }
})


export default class PeeringVisualization extends Component {
  renderGraph(container){
    var width = 720,
      height = 720,
      outerRadius = Math.min(width, height) / 2 - 10,
      innerRadius = outerRadius - 44;

    var formatPercent = d3.format(".1%");

    var arc = d3.svg.arc()
      .innerRadius(innerRadius)
      .outerRadius(outerRadius);

    var layout = d3.layout.chord()
      .padding(.04)
      .sortSubgroups(d3.descending)
      .sortChords(d3.ascending);

    var path = d3.svg.chord()
      .radius(innerRadius);

    var svg = d3.select(container).append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("id", "circle")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    svg.append("circle")
      .attr("r", outerRadius);

    function ready(groups, matrix) {

      // Compute the chord layout.
      layout.matrix(matrix);

      // Add a group per neighborhood.
      var group = svg.selectAll(".group")
        .data(layout.groups)
        .enter().append("g")
        .attr("class", "group")
        .on("mouseover", mouseover);

      // Add a mouseover title.
      group.append("title").text(function (d, i) {
        return groups[i].name + ": " + (d.value) + " connections, ISP: " + (groups[i].ISP) ;
      });

      // Add the group arc.
      var groupPath = group.append("path")
        .attr("id", function (d, i) { return "group" + i; })
        .attr("d", arc)
        .style("fill", function (d, i) { return groups[i].color; });

      // Add a text label.
      var groupText = group.append("text")
        .attr("x", 6)
        .attr("dy", 15);

      groupText.append("textPath")
        .attr("xlink:href", function (d, i) { return "#group" + i; })
        .text(function (d, i) { return groups[i].name; });

      // Remove the labels that don't fit. :(
      groupText.filter(function (d, i) { return groupPath[0][i].getTotalLength() / 2 - 16 < this.getComputedTextLength(); })
        .remove();

      // Add the chords.
      var chord = svg.selectAll(".chord")
        .data(layout.chords)
        .enter().append("path")
        .attr("class", "chord")
        .style("fill", function (d) { return groups[d.source.index].color; })
        .attr("d", path);

      // Add an elaborate mouseover title for each chord.
      chord.append("title").text(function (d) {
        return groups[d.source.index].name
          + " → " + groups[d.target.index].name
          + ": " + d.source.value + 'Connections'
          + "\n" + groups[d.target.index].name
          + " → " + groups[d.source.index].name
          + ": " + d.target.value + 'Connections';
      });

      function mouseover(d, i) {
        chord.classed("fade", function (p) {
          return p.source.index != i
            && p.target.index != i;
        });
      }
    }

    ready(groups, matrix)
  }

  componentDidMount() {
    this.renderGraph(this.refs.container)
  }

  render() {
    return (
      <div>
        <h1>Peering Visualization Page</h1>
        <div ref="container"></div>

      </div>
    )
  }
}

