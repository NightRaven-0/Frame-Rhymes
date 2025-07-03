import { handleUpload } from "./poemdisplay.js";
import { showUploadedImage } from "./poemdisplay.js";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("uploadForm");
  const imageInput = document.getElementById("imageInput");
  const previewImg = document.getElementById("uploadedImage");
  const captionSpan = document.getElementById("caption");
  const poemArea = document.getElementById("poemArea");
  const moodDisplay = document.getElementById("moodDisplay");
  const output = document.getElementById("output");
  const downloadBtn = document.getElementById("downloadBtn");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    handleUpload(form, captionSpan, poemArea, moodDisplay, output);
  });

  imageInput.addEventListener("change", () => {
    showUploadedImage(imageInput, previewImg);
  });

  downloadBtn.addEventListener("click", () => {
    if (!poemArea.value) return alert("No poem to download!");

    const blob = new Blob([poemArea.value], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "poem.txt";
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  });
});
