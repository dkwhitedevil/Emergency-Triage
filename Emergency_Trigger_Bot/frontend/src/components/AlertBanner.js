import React, { useEffect } from "react";

const AlertBanner = () => {
  useEffect(() => {
  const audio = new Audio("/alert.mp3");
  audio.play().catch((err) => {
    console.error("Failed to play alert sound:", err);
  });
}, []);

  return (
    <div className="alert-banner">
      🚨 Critical Alert: Seek immediate medical attention! 🚨
    </div>
  );
};

export default AlertBanner;