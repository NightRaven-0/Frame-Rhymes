export async function handleUpload(form, captionSpan, poemArea, moodDisplay, output) {
  const formData = new FormData(form);
  const moodInput = form.querySelector("input[name='mood']");

  try {
    const res = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData,
    });

    if (!res.ok) {
      throw new Error(`Server error: ${res.status} ${res.statusText}`);
    }

    const data = await res.json();
    captionSpan.textContent = data.caption || "No caption generated";
    poemArea.value = data.poem || "No poem generated";
    moodDisplay.textContent = moodInput.value || "None";
    output.style.display = "block";
  } catch (err) {
    alert("Error generating poem: " + err.message);
  }
}

export function showUploadedImage(input, previewImg) {
  const file = input.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      previewImg.src = reader.result;
      previewImg.style.display = "block";
    };
    reader.readAsDataURL(file);
  }
}
