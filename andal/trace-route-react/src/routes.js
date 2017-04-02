import React from 'react'
import { Route, IndexRoute } from 'react-router'

import App from './components/App'
import HomePage from './components/HomePage'
import AboutPage from './components/AboutPage'
import NotFoundPage from './components/NotFoundPage'
import StatsPage from './components/StatsPage'
import MapPage from './components/MapPage'
import RouteAnalysisPage from './modules/routeAnalysis/RouteAnalysisPage'
import PeerVisualizationPage from './modules/routeAnalysis/PeeringVisualizationPage'

export default (
  <Route path="/" component={App}>
    <IndexRoute component={HomePage}/>
    <Route path="about" component={AboutPage}/>
    <Route path="stats" component={StatsPage}/>
    <Route path="map" component={MapPage}/>
    <Route path="route-analysis" component={RouteAnalysisPage}/>
    <Route path="peering-visualization" component={PeerVisualizationPage}/>
    <Route path="*" component={NotFoundPage}/>
  </Route>
)
