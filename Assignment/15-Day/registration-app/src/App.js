import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { UserProvider } from './context/UserContext';
import Navbar from './components/Navbar';
import Registration from './pages/Registration';
import Dashboard from './pages/Dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <UserProvider>
      <Router>
        <div className="app-wrapper">
          <Navbar />
          <Routes>
            <Route path="/" element={<Registration />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </div>
      </Router>
    </UserProvider>
  );
}

export default App;
