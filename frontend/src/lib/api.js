import axios from "axios";

const API_BASE = "http://localhost:8000";

export async function generateBlog(payload) {
  console.log("HELLO AXIOS");
  try {
    const response = await axios.post(`http://localhost:8000/api/v1/generateBlog3`, payload, {
      headers: { "Content-Type": "application/json" },
    });
    return response.data;
  } catch (error) {
    console.error("Error generating blog:", error);
    throw error;
  }
}

export async function generateImages(payload) {
  try {
    const response = await axios.post(`http://localhost:8000/api/v1/generateImages`, payload, {
      headers: { "Content-Type": "application/json" },
    });
    return response.data;
  } catch (error) {
    console.error("Error generating images:", error);
    throw error;
  }
}