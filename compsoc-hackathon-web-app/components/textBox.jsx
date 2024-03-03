import React, { useState } from 'react';

const TextBox = ({ placeholderText, labelText, validation }) => {
  const [textValue, setTextValue] = useState('');
  const [error, setError] = useState('');

  const handleChange = (event) => {
    const value = event.target.value;
    setTextValue(value);
    if (validation && typeof validation === 'function') {
      const errorMessage = validation(value);
      setError(errorMessage);
    }
  };

  return (
    <div className="textbox-wrapper">
      <label className="textbox-label" htmlFor="textbox">{labelText}</label>
      <input className="textbox"
        type="text" 
        id="textbox"
        value={textValue} 
        onChange={handleChange} 
        placeholder={placeholderText} 
        placeholderText={placeholderText}
      />
      {error && <p className="textbox-error">{error}</p>}
    </div>
  );
};

export default TextBox;
