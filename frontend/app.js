const API_BASE_URL = "https://YOUR-RENDER-SERVICE.onrender.com";

const form = document.querySelector("#prediction-form");
const submitButton = document.querySelector("#submit-button");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.textContent = "";
  result.className = "result";

  if (API_BASE_URL.includes("YOUR-RENDER-SERVICE")) {
    result.textContent = "Set API_BASE_URL in frontend/app.js to your Render API URL.";
    result.classList.add("error");
    return;
  }

  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());
  for (const [name, value] of formData.entries()) {
    if (
      form.elements.namedItem(name).type === "number" ||
      ["holiday_period", "weekend_order", "peak_season"].includes(name)
    ) {
      payload[name] = Number(value);
    }
  }

  submitButton.disabled = true;
  submitButton.textContent = "Predicting…";

  try {
    const response = await fetch(`${API_BASE_URL.replace(/\/+$/, "")}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const details = await response.text();
      throw new Error(`API error ${response.status}: ${details}`);
    }

    const prediction = await response.json();
    result.textContent = prediction.result;
    result.classList.add(Number(prediction.prediction) === 1 ? "warning" : "success");
  } catch (error) {
    result.textContent = `Could not get a prediction. ${error.message}`;
    result.classList.add("error");
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = "Predict delivery";
  }
});
