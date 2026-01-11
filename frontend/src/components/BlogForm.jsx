import { useState } from "react";
import { generateBlog } from "../lib/api";

export default function BlogForm({ setLoading, setBlogData, settings, setSettings }) {
  const { title, tone, language } = settings;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setBlogData(null);

    try {
      console.log(settings);
      const data = await generateBlog(settings);
      setBlogData(data);
    } catch (err) {
      console.error(err);
      alert("Failed to generate blog");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-6 rounded-lg shadow space-y-4"
    >
      <div>
        <label className="block text-sm font-medium">Blog Title</label>
        <input
          value={title}
          onChange={(e) => setSettings({ ...settings, title: e.target.value })}
          required
          className="mt-1 w-full rounded border px-3 py-2"
        />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium">Tone</label>
          <select
            value={tone}
            onChange={(e) => setSettings({ ...settings, tone: e.target.value })}
            className="mt-1 w-full rounded border px-3 py-2"
          >
            <option>informative</option>
            <option>professional</option>
            <option>casual</option>
            <option>persuasive</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium">Language</label>
          <select
            value={language}
            onChange={(e) => setSettings({ ...settings, language: e.target.value })}
            className="mt-1 w-full rounded border px-3 py-2"
          >
            <option>English</option>
            <option>Hindi</option>
            <option>Spanish</option>
          </select>
        </div>
      </div>

      <button
        type="submit"
        className="w-full bg-black text-white py-2 rounded hover:bg-gray-800"
      >
        Generate Blog
      </button>
    </form>
  );
}
