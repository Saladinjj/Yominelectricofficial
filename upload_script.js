(async () => {
  const b64 = `...`; // I will replace this in the next step
  const res = await fetch(`data:image/png;base64,${b64}`);
  const blob = await res.blob();
  const file = new File([blob], "ym-0002.png", { type: "image/png" });
  const input = document.getElementById("storyboard-upload-input");
  const dataTransfer = new DataTransfer();
  dataTransfer.items.add(file);
  input.files = dataTransfer.files;
  input.dispatchEvent(new Event('change', { bubbles: true }));
})()