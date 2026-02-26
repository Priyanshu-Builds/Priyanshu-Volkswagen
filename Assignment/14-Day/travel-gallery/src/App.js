import React, { useState } from "react";
import "./App.css";

import goa from "./images/goa.jpg";
import manali from "./images/manali.jpg";
import jaipur from "./images/jaipur.jpg";
import kerala from "./images/kerala.jpg";

function App() {
  const destinations = [
    { name: "Goa", image: goa, description: "Beaches & Nightlife" },
    { name: "Manali", image: manali, description: "Mountains & Snow" },
    { name: "Jaipur", image: jaipur, description: "Royal Palaces" },
    { name: "Kerala", image: kerala, description: "Backwaters & Nature" }
  ];

  const [selected, setSelected] = useState(destinations[0]);

  return (
    <div className="container">
      <h1>Travel Destination Gallery</h1>

      <div className="preview">
        <img
          key={selected.name}
          src={selected.image}
          alt={selected.name}
          className="main-image"
        />
        <h2>{selected.name}</h2>
        <p>{selected.description}</p>
      </div>

      <div className="thumbnails">
        {destinations.map((place, index) => (
          <img
            key={index}
            src={place.image}
            alt={place.name}
            className={selected.name === place.name ? "active" : ""}
            onClick={() => setSelected(place)}
          />
        ))}
      </div>
    </div>
  );
}

export default App;