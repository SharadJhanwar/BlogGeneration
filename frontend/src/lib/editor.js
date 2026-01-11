import axios from "axios";

const API_BASE = "http://localhost:8000/api/v1";

export async function exportBlog(content, title, format) {
  try {
    const response = await axios.post(`${API_BASE}/export`, {
      content,
      title: title || "blog_post",
      format: format.toLowerCase()
    }, {
      responseType: format.toLowerCase() === "pdf" || format.toLowerCase() === "docx" ? "blob" : "text"
    });

    const blob = format.toLowerCase() === "pdf" || format.toLowerCase() === "docx" 
      ? response.data 
      : new Blob([response.data], { type: response.headers["content-type"] });

    const url = window.URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", `${title || "blog_post"}.${format.toLowerCase() === "docx" ? "docx" : format.toLowerCase()}`);
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
    
    return { success: true };
  } catch (error) {
    console.error(`Export failed:`, error);
    throw error;
  }
}

export async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    return { success: true };
  } catch (err) {
    console.error('Copy failed: ', err);
    throw err;
  }
}
