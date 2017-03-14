import React from 'react';
import {Link} from 'react-router';

const HomePage = () => {
  return (
    <div>
      <h1>Network Characterization based on QoE Measurement</h1>
      <p>
        Spring 2017
        <br/>
        18757 - Network Management and Control
        <br/>
        Andal Jayaseelan
        <br/>
      </p>
      <p>
        <Link className="btn btn-lg btn-primary" to="/route-analysis"> View Route Analysis Charts</Link>
      </p>
    </div>
  );
};

export default HomePage;
