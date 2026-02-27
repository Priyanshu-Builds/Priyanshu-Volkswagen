import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useUser } from '../context/UserContext';

function Registration() {
    const navigate = useNavigate();
    const { registerUser } = useUser();

    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        address: '',
        gender: '',
        dob: '',
    });

    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});

    const validate = (data) => {
        const newErrors = {};
        if (!data.name.trim()) newErrors.name = 'Name is required';
        if (!data.email.trim()) {
            newErrors.email = 'Email is required';
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
            newErrors.email = 'Enter a valid email address';
        }
        if (!data.phone.trim()) {
            newErrors.phone = 'Phone number is required';
        } else if (!/^\d{10}$/.test(data.phone)) {
            newErrors.phone = 'Enter a valid 10-digit phone number';
        }
        if (!data.address.trim()) newErrors.address = 'Address is required';
        if (!data.gender) newErrors.gender = 'Please select a gender';
        if (!data.dob) newErrors.dob = 'Date of birth is required';
        return newErrors;
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        const updated = { ...formData, [name]: value };
        setFormData(updated);
        if (touched[name]) {
            setErrors(validate(updated));
        }
    };

    const handleBlur = (e) => {
        const { name } = e.target;
        setTouched((prev) => ({ ...prev, [name]: true }));
        setErrors(validate(formData));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const validationErrors = validate(formData);
        setErrors(validationErrors);
        setTouched({
            name: true,
            email: true,
            phone: true,
            address: true,
            gender: true,
            dob: true,
        });

        if (Object.keys(validationErrors).length === 0) {
            registerUser(formData);
            navigate('/dashboard');
        }
    };

    return (
        <div className="page-container">
            <div className="form-card animate-in">
                <div className="card-header-custom">
                    <h2>Create Your Account</h2>
                    <p>Fill in your details to register</p>
                </div>

                <form onSubmit={handleSubmit} noValidate>
                    <div className="mb-3">
                        <label htmlFor="name" className="form-label">
                            Full Name
                        </label>
                        <input
                            type="text"
                            className={`form-control custom-input ${touched.name && errors.name ? 'is-invalid' : ''
                                } ${touched.name && !errors.name ? 'is-valid' : ''}`}
                            id="name"
                            name="name"
                            placeholder="Enter your full name"
                            value={formData.name}
                            onChange={handleChange}
                            onBlur={handleBlur}
                        />
                        {touched.name && errors.name && (
                            <div className="invalid-feedback">{errors.name}</div>
                        )}
                    </div>

                    <div className="mb-3">
                        <label htmlFor="email" className="form-label">
                            Email Address
                        </label>
                        <input
                            type="email"
                            className={`form-control custom-input ${touched.email && errors.email ? 'is-invalid' : ''
                                } ${touched.email && !errors.email ? 'is-valid' : ''}`}
                            id="email"
                            name="email"
                            placeholder="you@example.com"
                            value={formData.email}
                            onChange={handleChange}
                            onBlur={handleBlur}
                        />
                        {touched.email && errors.email && (
                            <div className="invalid-feedback">{errors.email}</div>
                        )}
                    </div>

                    <div className="row">
                        <div className="col-md-6 mb-3">
                            <label htmlFor="phone" className="form-label">
                                Phone Number
                            </label>
                            <input
                                type="tel"
                                className={`form-control custom-input ${touched.phone && errors.phone ? 'is-invalid' : ''
                                    } ${touched.phone && !errors.phone ? 'is-valid' : ''}`}
                                id="phone"
                                name="phone"
                                placeholder="10-digit number"
                                value={formData.phone}
                                onChange={handleChange}
                                onBlur={handleBlur}
                            />
                            {touched.phone && errors.phone && (
                                <div className="invalid-feedback">{errors.phone}</div>
                            )}
                        </div>

                        <div className="col-md-6 mb-3">
                            <label htmlFor="dob" className="form-label">
                                Date of Birth
                            </label>
                            <input
                                type="date"
                                className={`form-control custom-input ${touched.dob && errors.dob ? 'is-invalid' : ''
                                    } ${touched.dob && !errors.dob ? 'is-valid' : ''}`}
                                id="dob"
                                name="dob"
                                value={formData.dob}
                                onChange={handleChange}
                                onBlur={handleBlur}
                            />
                            {touched.dob && errors.dob && (
                                <div className="invalid-feedback">{errors.dob}</div>
                            )}
                        </div>
                    </div>

                    <div className="mb-3">
                        <label className="form-label">Gender</label>
                        <div className="d-flex gap-4">
                            {['Male', 'Female', 'Other'].map((g) => (
                                <div className="form-check" key={g}>
                                    <input
                                        className="form-check-input"
                                        type="radio"
                                        name="gender"
                                        id={`gender-${g}`}
                                        value={g}
                                        checked={formData.gender === g}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                    />
                                    <label className="form-check-label" htmlFor={`gender-${g}`}>
                                        {g}
                                    </label>
                                </div>
                            ))}
                        </div>
                        {touched.gender && errors.gender && (
                            <div className="text-danger small mt-1">{errors.gender}</div>
                        )}
                    </div>

                    <div className="mb-4">
                        <label htmlFor="address" className="form-label">
                            Address
                        </label>
                        <textarea
                            className={`form-control custom-input ${touched.address && errors.address ? 'is-invalid' : ''
                                } ${touched.address && !errors.address ? 'is-valid' : ''}`}
                            id="address"
                            name="address"
                            rows="3"
                            placeholder="Enter your full address"
                            value={formData.address}
                            onChange={handleChange}
                            onBlur={handleBlur}
                        ></textarea>
                        {touched.address && errors.address && (
                            <div className="invalid-feedback">{errors.address}</div>
                        )}
                    </div>

                    <button type="submit" className="btn btn-primary w-100 submit-btn">
                        Register
                    </button>
                </form>
            </div>
        </div>
    );
}

export default Registration;