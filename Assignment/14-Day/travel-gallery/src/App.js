import React, { useState, useEffect } from "react";
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

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const nextImage = () => {
    setCurrentIndex((prev) =>
      prev === destinations.length - 1 ? 0 : prev + 1
    );
  };

  const prevImage = () => {
    setCurrentIndex((prev) =>
      prev === 0 ? destinations.length - 1 : prev - 1
    );
  };

  useEffect(() => {
    if (isModalOpen) return;

    const interval = setInterval(() => {
      nextImage();
    }, 3500);

    return () => clearInterval(interval);
  }, [currentIndex, isModalOpen]);

  const selected = destinations[currentIndex];

  return (
    <div className="container">
      <h1>Travel Destination Gallery</h1>

      <div className="preview-container">
        <button className="arrow left" onClick={prevImage}>❮</button>

        <div className="preview">
          <img
            src={selected.image}
            alt={selected.name}
            className="main-image"
            onClick={() => setIsModalOpen(true)}
          />
          <h2>{selected.name}</h2>
          <p>{selected.description}</p>
        </div>

        <button className="arrow right" onClick={nextImage}>❯</button>
      </div>

      <div className="thumbnails">
        {destinations.map((place, index) => (
          <img
            key={index}
            src={place.image}
            alt={place.name}
            className={currentIndex === index ? "active" : ""}
            onClick={() => setCurrentIndex(index)}
          />
        ))}
      </div>

      {isModalOpen && (
        <div className="modal">
          <span className="close" onClick={() => setIsModalOpen(false)}>✖</span>

          <button className="modal-arrow left" onClick={prevImage}>❮</button>

          <img
            src={selected.image}
            alt={selected.name}
            className="modal-image"
          />

          <button className="modal-arrow right" onClick={nextImage}>❯</button>
        </div>
      )}
    </div>
  );
}

export default App;