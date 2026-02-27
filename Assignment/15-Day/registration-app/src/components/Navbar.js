import React from 'react';
import { useUser } from '../context/UserContext';
import { useNavigate } from 'react-router-dom';

function Navbar() {
    const { user, logoutUser } = useUser();
    const navigate = useNavigate();

    const handleLogout = () => {
        logoutUser();
        navigate('/');
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-dark custom-navbar">
            <div className="container-fluid">
                <span className="navbar-brand fw-bold">
                    <i className="bi bi-person-plus-fill me-2"></i>
                    Registration Portal
                </span>

                {user && (
                    <div className="d-flex align-items-center ms-auto">
                        <span className="welcome-text me-3">
                            Welcome, <strong>{user.name}</strong>
                        </span>
                        <button
                            className="btn btn-outline-light btn-sm logout-btn"
                            onClick={handleLogout}
                        >
                            <i className="bi bi-box-arrow-right me-1"></i>
                            Logout
                        </button>
                    </div>
                )}
            </div>
        </nav>
    );
}

export default Navbar;