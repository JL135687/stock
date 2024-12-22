async function fetchComponent() {
  const companyName = document.getElementById("company-name").value;
  const response = await fetch(`http://127.0.0.1:5000/company?name=${companyName}`);
  const data = await response.json();
  console.log(data);  // Log the response data for debugging

  const display = document.getElementById("component-details");
  display.innerHTML = ''; // Clear previous details

  if (data.error) {
      display.innerHTML = `<p style="color: red;">${data.error}</p>`;
  } else {
      display.innerHTML = `
          <h3>${data[0]['Company name']}</h3>
          <p><strong>Component:</strong> ${data[0]['Components']}</p>
          <p><strong>Value:</strong> ${data[0]['Values']}</p>
          <p><strong>Packets:</strong> ${data[0]['Packets']}</p>
      `;
  }
}
