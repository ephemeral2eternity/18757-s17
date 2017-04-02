import React, {Component} from 'react'
import {Link, IndexLink} from 'react-router'
import AppBar from 'material-ui/AppBar'
import FlatButton from 'material-ui/FlatButton'
import Palette from 'google-material-color-palette-json'

function handleTouchTap() {
  alert('onTouchTap triggered on the title component')
}

const styles = {
  title: {
    cursor: 'pointer',
  }, button: {
    color: Palette.white
  }
}

export class AppMenu extends Component {
  render() {
    return (
      <div>
        <FlatButton style={styles.button}>
          <Link style={{color: Palette.white}} to="/stats">Stats</Link>
        </FlatButton>
        <FlatButton style={styles.button}>
          <Link style={{color: Palette.white}} to="/map">Map</Link>
        </FlatButton>
        <FlatButton style={styles.button}>
          <Link style={{color: Palette.white}} to="/route-analysis">Route Analysis</Link>
        </FlatButton>
        <FlatButton style={styles.button}>
          <Link style={{color: Palette.white}} to="/peering-visualization">Peering Viz</Link>
        </FlatButton>
      </div>
    )

  }
}

export default class HeaderBar extends Component {
  renderTitle(){
    return(
      <FlatButton>
        <IndexLink style={{color: 'white'}} to="/">ISP Visualization</IndexLink>
      </FlatButton>
    )
  }
  render() {
    return (
      <AppBar
        style={{backgroundColor:'dimgrey', minHeight:50}}
        title={this.renderTitle()}
        onTitleTouchTap={handleTouchTap}
        iconElementLeft={<span/>}
        iconElementRight={<AppMenu/>}
      />
    )
  }
}
