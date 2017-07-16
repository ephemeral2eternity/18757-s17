import React from 'react'
import ispPeers from './assets/peering/cloud_direct_peers.json'

function ExpandButton(props) {
  return (
    <button className="btn btn-link">
      {
        props.isExpanded
          ? (
            <i className="fa fa-minus"/>
          ) : (
            <i className="fa fa-plus"/>
          )
      }
    </button>
  )
}
export default function IspDirectPeersPage() {
  return (
    <div>

      <h2>IspDirectPeersPage</h2>
      <ul className="list-inline">
        {
          ispPeers.map((isp) => (
            <li key={isp.ispName}>
              <h3>
                <ExpandButton/>
                {' '}
                {isp.ispName}</h3>
              <ul>
                {
                  Object.keys(isp.cloud_peer_map).map(as => (
                    <li key={as}>
                      {as}
                      <ul className="list-inline">
                        {
                          isp.cloud_peer_map[as].peers.map((peer) => (
                            <li key={peer.AS} >
                              <button className="btn btn-default btn-xs" style={{marginBottom: 5}}>
                              {peer.AS} - <em>{peer.ispName}</em>
                              </button>
                            </li>
                          ))
                        }
                      </ul>
                    </li>
                  ))
                }
              </ul>
            </li>
          ))
        }
      </ul>

    </div>
  )
}
