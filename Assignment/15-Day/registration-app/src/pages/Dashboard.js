import React from 'react';
import { Navigate } from 'react-router-dom';
import { useUser } from '../context/UserContext';

function Dashboard() {
    const { user } = useUser();

    if (!user) {
        return <Navigate to="/" replace />;
    }

    const details = [
        { label: 'Full Name', value: user.name, icon: '👤' },
        { label: 'Email Address', value: user.email, icon: '📧' },
        { label: 'Phone Number', value: user.phone, icon: '📱' },
        { label: 'Date of Birth', value: user.dob, icon: '🎂' },
        { label: 'Gender', value: user.gender, icon: '⚧' },
        { label: 'Address', value: user.address, icon: '📍' },
    ];

    return (
        <div className="page-container">
            <div className="dashboard-card animate-in">
                <div className="card-header-custom">
                    <h2>Registration Successful!</h2>
                    <p>Here are your submitted details</p>
                </div>

                <div className="details-grid">
                    {details.map((item, index) => (
                        <div
                            className="detail-item"
                            key={item.label}
                            style={{ animationDelay: `${index * 0.1}s` }}
                        >
                            <div className="detail-icon">{item.icon}</div>
                            <div className="detail-content">
                                <span className="detail-label">{item.label}</span>
                                <span className="detail-value">{item.value}</span>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Dashboard;